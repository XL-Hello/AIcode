@echo off
setlocal EnableExtensions EnableDelayedExpansion

rem Merge dre/audio logs from nested zips in chronological order.
rem Usage:
rem   merge_rtos_logs.bat [zip_path] [output_dir]

set "SCRIPT_DIR=%~dp0"
set "ZIP_PATH=%~1"
if not defined ZIP_PATH set "ZIP_PATH=%SCRIPT_DIR%log_rtos.zip"

set "OUT_DIR=%~2"
if not defined OUT_DIR set "OUT_DIR=%CD%"

set "AUDIO_OUTPUT=%OUT_DIR%\audio.log"
set "DRE_OUTPUT=%OUT_DIR%\dre.log"
set "SEVENZIP=C:\Program Files\7-Zip\7z.exe"

if not exist "%SEVENZIP%" (
  echo ERROR: 7-Zip not found: %SEVENZIP%>&2
  exit /b 1
)

if not exist "%ZIP_PATH%" (
  echo ERROR: zip file not found: %ZIP_PATH%>&2
  exit /b 1
)

if not exist "%OUT_DIR%" mkdir "%OUT_DIR%" >nul 2>&1
if errorlevel 1 (
  echo ERROR: failed to create output directory: %OUT_DIR%>&2
  exit /b 1
)

set "TMP_DIR=%TEMP%\merge_rtos_logs_%RANDOM%%RANDOM%%RANDOM%"
set "OUTER_DIR=%TMP_DIR%\outer"
set "MANIFEST=%TMP_DIR%\manifest.tsv"
set "MANIFEST_SORTED=%TMP_DIR%\manifest_sorted.tsv"
set "INNER_LIST=%TMP_DIR%\inner_zips.txt"

mkdir "%TMP_DIR%" >nul 2>&1
mkdir "%OUTER_DIR%" >nul 2>&1
if errorlevel 1 (
  echo ERROR: failed to create temp directory: %TMP_DIR%>&2
  exit /b 1
)

set "AUDIO_COUNT=0"
set "DRE_COUNT=0"
set "INNER_COUNT=0"

rem Step 1: extract the outer archive.
"%SEVENZIP%" x -y "-o%OUTER_DIR%" "%ZIP_PATH%" >nul
if errorlevel 1 (
  echo ERROR: failed to extract outer zip: %ZIP_PATH%>&2
  goto :fail
)

rem Step 2: collect and sort inner zip files.
dir /b /s /a-d "%OUTER_DIR%\*.zip" 2>nul | sort > "%INNER_LIST%"
for /f "usebackq delims=" %%I in ("%INNER_LIST%") do set /a INNER_COUNT+=1

if %INNER_COUNT% EQU 0 (
  echo ERROR: no inner zip files found in %ZIP_PATH%>&2
  goto :fail
)

type nul > "%MANIFEST%"

rem Step 3: build a sortable manifest of all log archives.
for /f "usebackq delims=" %%I in ("%INNER_LIST%") do (
  set "IN_FILE_LIST="
  for /f "usebackq delims=" %%L in (`"%SEVENZIP%" l -slt "%%~fI"`) do (
    set "LINE=%%L"
    if defined IN_FILE_LIST (
      if /I "!LINE:~0,7!"=="Path = " (
        set "MEMBER=!LINE:~7!"
        call :append_manifest "%%~fI" "!MEMBER!"
      )
    ) else if "!LINE!"=="----------" (
      set "IN_FILE_LIST=1"
    )
  )
)

sort "%MANIFEST%" /o "%MANIFEST_SORTED%"
if errorlevel 1 (
  echo ERROR: failed to sort manifest>&2
  goto :fail
)

type nul > "%AUDIO_OUTPUT%"
type nul > "%DRE_OUTPUT%"

rem Step 4: merge by chronological order per kind.
for /f "usebackq tokens=1,2,3,* delims=	" %%A in ("%MANIFEST_SORTED%") do (
  if /I "%%A"=="audio" (
    call :append_archive "%%C" "%%D" "audio"
    if errorlevel 1 goto :fail
    set /a AUDIO_COUNT+=1
  ) else if /I "%%A"=="dre" (
    call :append_archive "%%C" "%%D" "dre"
    if errorlevel 1 goto :fail
    set /a DRE_COUNT+=1
  )
)

echo Done.
echo   audio merged files: %AUDIO_COUNT% ^> %AUDIO_OUTPUT%
echo   dre merged files:   %DRE_COUNT% ^> %DRE_OUTPUT%
call :cleanup
exit /b 0

:append_manifest
set "INNER_ZIP=%~1"
set "MEMBER=%~2"
for %%F in ("%MEMBER%") do set "BASE=%%~nxF"

set "KIND="
set "TS_KEY="

if /I "!BASE:~-21!"==".audio_dre.log.tar.gz" (
  set "KIND=audio"
  set "PREFIX=!BASE:~0,-21!"
  set "TAIL16=!PREFIX:~-16!"
  if "!TAIL16:~0,1!"=="_" (
    call :is_digits "!TAIL16:~1!" 15
    if not errorlevel 1 set "TS_KEY=!TAIL16:~1!"
  )
  if not defined TS_KEY (
    set "HEAD14=!BASE:~0,14!"
    call :is_digits "!HEAD14!" 14
    if not errorlevel 1 set "TS_KEY=!HEAD14!"
  )
  if not defined TS_KEY set "TS_KEY=!BASE!"
) else if /I "!BASE:~-15!"==".dre.log.tar.gz" (
  set "KIND=dre"
  set "PREFIX=!BASE:~0,-15!"
  set "TAIL16=!PREFIX:~-16!"
  if "!TAIL16:~0,1!"=="_" (
    call :is_digits "!TAIL16:~1!" 15
    if not errorlevel 1 set "TS_KEY=!TAIL16:~1!"
  )
  if not defined TS_KEY (
    set "HEAD14=!BASE:~0,14!"
    call :is_digits "!HEAD14!" 14
    if not errorlevel 1 set "TS_KEY=!HEAD14!"
  )
  if not defined TS_KEY set "TS_KEY=!BASE!"
)

if defined KIND >> "%MANIFEST%" echo(!KIND!	!TS_KEY!	!INNER_ZIP!	!MEMBER!
exit /b 0

:append_archive
set "INNER_ZIP=%~1"
set "MEMBER=%~2"
set "KIND=%~3"
set "TEMP_GZ=%TMP_DIR%\payload_%RANDOM%%RANDOM%%RANDOM%.tar.gz"

"%SEVENZIP%" e -y -so "%INNER_ZIP%" "%MEMBER%" > "%TEMP_GZ%"
if errorlevel 1 (
  echo ERROR: failed to extract member "%MEMBER%" from "%INNER_ZIP%">&2
  if exist "%TEMP_GZ%" del /q "%TEMP_GZ%" >nul 2>&1
  exit /b 1
)

if /I "%KIND%"=="audio" (
  "%SEVENZIP%" x -y -so "%TEMP_GZ%" | "%SEVENZIP%" x -y -si -ttar -so >> "%AUDIO_OUTPUT%"
) else (
  "%SEVENZIP%" x -y -so "%TEMP_GZ%" | "%SEVENZIP%" x -y -si -ttar -so >> "%DRE_OUTPUT%"
)

if errorlevel 1 (
  echo ERROR: failed to unpack tar.gz payload "%MEMBER%">&2
  if exist "%TEMP_GZ%" del /q "%TEMP_GZ%" >nul 2>&1
  exit /b 1
)

if exist "%TEMP_GZ%" del /q "%TEMP_GZ%" >nul 2>&1
exit /b 0

:is_digits
setlocal
set "VALUE=%~1"
set "LEN=%~2"

if "%LEN%"=="15" (
  echo(%VALUE%| findstr /R "^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$" >nul
) else if "%LEN%"=="14" (
  echo(%VALUE%| findstr /R "^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$" >nul
) else (
  endlocal & exit /b 1
)

endlocal & exit /b %errorlevel%

:cleanup
if exist "%TMP_DIR%" rd /s /q "%TMP_DIR%" >nul 2>&1
exit /b 0

:fail
call :cleanup
exit /b 1
