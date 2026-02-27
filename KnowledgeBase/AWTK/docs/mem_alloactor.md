# 内存分配器

## 1\. 介绍

![](images/mem_allocator.png)

  * mem_allocator 定义了内存分配器的基本接口


    
    
    /**
     * @method mem_allocator_alloc
     * 分配指定大小的内存。
     *
     * @param {mem_allocator_t*} allocator allocator 对象。
     * @param {uint32_t} size 内存的大小。
     * @param {const char*}  分配内存的函数（用于调试）。
     * @param {uint32_t} line 分配内存的行数（用于调试）。
     *
     * @return {void*} 成功返回内存块的地址，失败返回 NULL。
     */
    static inline void* mem_allocator_alloc(mem_allocator_t* allocator, uint32_t size, const char* func,
                                            uint32_t line) ;
    
    /**
     * @method mem_allocator_realloc
     * 重新分配指定大小的内存。
     *
     * @param {mem_allocator_t*} allocator allocator 对象。
     * @param {void*} ptr 原来内存的地址。
     * @param {uint32_t} size 内存的大小。
     * @param {const char*} 分配内存的函数（用于调试）。
     * @param {uint32_t} line 分配内存的行数（用于调试）。
     *
     * @return {void*} 成功返回内存块的地址，失败返回 NULL。
     */
    static inline void* mem_allocator_realloc(mem_allocator_t* allocator, void* ptr, uint32_t size,
                                              const char* func, uint32_t line) ;
    
    /**
     * @method mem_allocator_free
     * 释放内存。
     *
     * @param {mem_allocator_t*} allocator allocator 对象。
     * @param {void*} ptr 内存的地址。
     *
     * @return {void*} 成功返回内存块的地址，失败返回 NULL。
     */
    static inline void mem_allocator_free(mem_allocator_t* allocator, void* ptr) ;
    
    /**
     * @method mem_allocator_dump
     * 显示内存信息，用于调试。
     *
     * @param {mem_allocator_t*} allocator allocator 对象。
     *
     * @return {ret_t} 返回 RET_OK 表示成功，否则表示失败。
     */
    static inline ret_t mem_allocator_dump(mem_allocator_t* allocator);
    

## 2\. 基本内存分配器

  * mem_allocator_std 基于标准内存管理函数 malloc/free/realloc 实现的内存分配器。在系统提供了 malloc/free/realloc 函数时，请使用本分配器。

  * mem_allocator_simple AWTK 本身实现的一个简单内存分配器，在系统没有提供 malloc/free/realloc 函数时，请使用本分配器。




> 通过宏 HAS_STD_MALLOC 来选择是否使用标准的内存分配器。一般在 PC 上修改 awtk_config.py，在嵌入式系统一般修改 awtk_config.h。

## 3\. 装饰器-加锁

mem_allocator_lock 对现有的 allocator 进行包装，提供互斥功能。由于标准内存分配器使用的 malloc/free/realloc 本身有互斥功能，所以本装饰器主要用于 mem_allocator_simple 。

## 4\. 装饰器-防止碎片

mem_allocator_pool 对现有的 allocator 进行包装，预先分配一部分内存，用于分配小块内存，可以避免内存碎片。

经过测试，一般情况下，80%的情况，都是小块内存，在 pool 中分配，可以有效的防止内存碎片。

> 开发者可以跟踪 mem_allocator_pool 的使用情况，根据实际情况调整预先分配的块数。

## 5\. 装饰器-调试

mem_allocator_debug 对现有的 allocator 进行包装，记录分配的内存，用于帮助分析内存的使用和泄露。

> 由于 mem_allocator_debug 本身会占用一部分内存，一般在 PC 上使用。

一般按下指定快捷键时调用 tk_mem_dump 显示内存使用情况，如：

`c if (evt->key == TK_KEY_F9) { tk_mem_dump(); return RET_STOP; } else if (evt->key == TK_KEY_F10) { /*有时释放缓存数据后，再显示内存信息，可以排除一步部分干扰*/ font_manager_unload_all(font_manager()); image_manager_unload_all(image_manager()); assets_manager_clear_cache(assets_manager(), ASSET_TYPE_UI); tk_mem_dump(); return RET_STOP; }`

> 宏 ENABLE_MEM_LEAK_CHECK 决定是否开启调试功能。在 PC 上一般修改 awtk_config.py，在嵌入式系统一般修改 awtk_config.h。

一般长时间运行，才能得出真实数据。可以结合[输入事件记录与重放](https://github.com/zlgopen/awtk/blob/master/docs/event_recorder_player.html)来结合测试。

请参考 demos/demo_ui_app.c

## 6\. 装饰器-内存耗尽

mem_allocator_oom 对现有的 allocator 进行包装，如果分配内存失败，调用预先设置的回调函数释放内存，然后再重试。

给应用程序优雅退出的机会。
