# ADB 常用命令速查

`adb` 是 Android Debug Bridge，用来连接电脑和 Android 设备，常用于调试、安装应用、传文件和抓日志。

## 1. 检查设备连接

```bash
adb devices
```

列出已连接的设备或模拟器。

```bash
adb devices -l
```

显示更详细的信息。

## 2. 进入设备命令行

```bash
adb shell
```

进入设备的 shell 环境后，可以执行很多 Android 命令。

常见的 shell 内命令：

```bash
getprop
pm list packages
dumpsys
logcat
```

## 3. 安装和卸载应用

```bash
adb install app.apk
```

安装 APK。

```bash
adb install -r app.apk
```

覆盖安装，保留应用数据。

```bash
adb uninstall com.example.app
```

卸载指定包名的应用。

## 4. 传输文件

```bash
adb push local.txt /sdcard/
```

把电脑上的文件传到设备。

```bash
adb pull /sdcard/remote.txt .
```

把设备上的文件拷回电脑当前目录。

## 5. 重启设备

```bash
adb reboot
```

重启到系统。

```bash
adb reboot recovery
adb reboot bootloader
```

分别重启到恢复模式和引导模式。

## 6. 查看日志

```bash
adb logcat
```

查看系统日志，是排查问题最常用的命令之一。

按关键字过滤日志：

```bash
adb logcat | grep ActivityManager
```

## 7. 端口转发

```bash
adb forward tcp:8080 tcp:8080
```

把电脑端口转发到设备端口。

```bash
adb reverse tcp:8080 tcp:8080
```

把设备端口反向映射到电脑。

## 8. 截图和录屏

```bash
adb shell screencap -p /sdcard/screen.png
adb pull /sdcard/screen.png
```

先在设备上截图，再拉回电脑。

```bash
adb shell screenrecord /sdcard/demo.mp4
adb pull /sdcard/demo.mp4
```

录屏并导出到电脑。

## 9. 启动应用或 Activity

```bash
adb shell am start -n com.example.app/.MainActivity
```

直接启动指定应用页面。

## 10. 查看包信息

```bash
adb shell pm list packages
```

列出设备中的所有应用包名。

```bash
adb shell pm list packages | grep music
```

按关键字筛选包名。

```bash
adb shell dumpsys package com.example.app
```

查看某个应用的详细信息。

## 11. 停止或清除应用

```bash
adb shell am force-stop com.example.app
```

强制停止应用。

```bash
adb shell pm clear com.example.app
```

清除应用数据，相当于恢复到初始状态。

## 12. 查看设备基本信息

```bash
adb shell getprop ro.build.version.release
adb shell getprop ro.product.model
```

查看 Android 版本和设备型号。

## 13. 常见排查命令

```bash
adb kill-server
adb start-server
```

重启 adb 服务，适合设备识别异常时使用。

```bash
adb usb
```

切换到 USB 连接模式。

```bash
adb tcpip 5555
```

让设备切换到 TCP/IP 调试模式。

## 14. 一个小流程示例

```bash
adb devices
adb install -r app.apk
adb shell am start -n com.example.app/.MainActivity
adb logcat
```

这是一个常见的调试流程：先确认设备连接，再安装应用，启动页面，最后看日志。

## 15. 常用提示

- 第一次连接手机时，记得在手机上允许 USB 调试授权。
- 如果 `adb devices` 显示 `unauthorized`，先看手机是否弹出授权提示。
- 如果设备没显示出来，可以尝试换 USB 线、换接口，或执行 `adb kill-server && adb start-server`。
