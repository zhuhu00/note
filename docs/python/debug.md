# 如何调试代码

[TOC]

## 0. Debug 大法

- [ ] 待补充各个原则细节

书籍: 《调试九法》, 思想很重要, 精通了这本书的思想, **debug 能力和科研中解决问题的能力会非常强.** 

<details span>
<summary><b>网上读者对《调试九法》的评价</b></summary>
<br>
  > 如果每个CS学生和EE学生早点看看这本书，那么应该不会有那么多人因为抵触bug而神经奔溃最终放弃。

  > 拯救我于水火之中。

  > 非常不错的书籍，不管对于解决任何问题，不局限于软硬件问题，我觉得都能够给我帮助。

  > 简明扼要，很精彩。

  > 神书，看的酣畅淋漓，有种打通全身关节的感觉。

</details>


![image-20240409223537114](https://raw.githubusercontent.com/zhuhu00/img/master/20240409223537.png)

### **第一原则: 理解算法/ 代码(Debug 的基础)**

**Debug第一原则，理解算法/代码：“我们需要了解算法/代码的工作流程和原理。如果没有理解算法/代码中的某个部分，那么这通常就是出问题的地方。”**

### **第二原则: 复现 bug并观察运行细节(常用技巧 1)**

Debug第二原则，复现bug并观察运行细节：“复现bug有3个好处：可以观察bug的规律；可以准确知道bug在什么条件发生，从而集中精力查找原因；可以判断是否已修复bug。”

### **第三原则：以事实为依据来定位bug的根源**

**Debug第三原则，以事实为依据来定位bug的根源：“亲眼看到底层细节如何引发bug是非常重要的。如果只是猜测失败是如何发生的，那常常会修复一些根本不是bug的问题。这样的修复不仅不会解决问题，而且可能会破坏其他地方”**

### **第四原则：分而治之（常用技巧2）**

**Debug第四原则，分而治之：“分而治之是Debug的核心技巧，可以为我们节省大量的时间。具体做法是，反复地把问题分成好的一半和坏的一半，来缩小搜索范围，然后进一步研究有问题的那一半。”**

### **第五原则：Debug时要控制变量（常用技巧3）**

**Debug第五原则，Debug时要控制变量：“**控制变量，一次只改一个地方，以此充分确认该处改动的影响**”**

### **第六原则：做好实验记录（常用技巧4）**

**Debug第六原则，做好实验记录：“在检查某问题时，要记下你所做的事、做事的顺序，以及发生的结果。这样能帮助自己观察算法/代码的调试信息与运行细节，帮助自己发现bug在哪”**

### **第七原则：保持对假设的怀疑**

**Debug第七原则，保持对假设的怀疑：“保持对自己假设的怀疑，特别是当这些假设在一些无法解释的问题中是核心因素的时候。**

### **第八原则：询问他人的观点（常用技巧5）**

**Debug第八原则，询问他人的观点：“向别人寻求帮助至少有3个好处：获得全新观点、专业知识和对于算法/代码/debug的经验。”**

### **第九原则：从bug的源头解决bug**

**Debug第九原则，从bug的源头解决bug：“需要从bug的源头解决bug，否则bug会一直存在。比如，如果一个硬件设备失败了，不要以为它是无缘无故坏掉了。如果因为某些原因导致零件损坏，那么更换这个零件也只能带来短暂work的时间，然后新的零件也会损坏。你必须找到真正的失败之处。”**

### Reference

- 如何给算法和代码 debug: https://pengsida.notion.site/debug-1b69debf803a4c268fc8a09a9a748bbf
- 调试九法: 软硬件错误排查之道: https://brainku.github.io/2016/12/11/debugging-the-9-rules/

## 1. ipdb包
ipdb有两种方式, 一种要侵入式, 修改源码, 改动太多很麻烦, 另一种是命令行模式. 

```sh
pip install ipdb
```

### 命令行模式

```sh
python -m ipdb xxx.py
```

#### 常用命令: 

通过`h`可以查看所有命令, 或者使用`h command`查看该命令的具体用法. 

- **打印变量**: `p`或者`pp`. 

- **断点:** ` b linenumber`,  默认为当前文件的断点, 也可以设置成其他文件: `b file_name:line_number`, `filename`需要再`sys.path`中, 当前目录已经默认在`sys.path`中, 或者可以通过`..`引用上一层目录文件.

  - 使用`b linenumber`设置了断点的代码在重新运行(命令为`restart`或者`run`)后还会存在, 如果要忽略这些断点, 可以通过这两种做法

    1. 通过`disable`关闭这些断点, `enable`打开这些断点. 

    1. 通过`clear`清除这些断点. 

  - 还有**一次性的断点**, 命令为`tbreak`, 使用方法类似. 

  - 除了指定断点外, 还可以有**条件断点.** 在某个 condition 下, 断点才成立. 使用命令为`condition line_num bool_expression`, 只有当`bool_expression`为`True`时, 才会执行这个断点. 

  - 如果需要**列出已经设置的所有断点**，可以单独使用命令 `b`。

- **逐行执行**: 逐行执行主要有两个命令: `s`(Step)和`n`(Next). 两个命令主要区别是: 当运行到调用函数时, 则`s`会进入该函数, `n`则不会, 而是运行下一行. 所以可以用`s`进入函数, 在函数内部进行 debug. 

  - **进入函数之后**, 使用`a`(Argument) 可以列出当前函数的所有参数, `r`(Return)可以直接执行到 return 语句. 

- **忽略某段代码:** 使用`j line_number`可以忽略某段代码, 下一步直接从 line_number 开始执行

- **查看源码**: 通过`l`或者`ll`, `ll`是查看整个源码文件, `l`是查看当前断点处, `l`也可以指定查看的行数, 默认是前后 11 行. 例如`l 2,5`是查看第 2-5 行代码

- **重启或退出 Debugger**

  - 保留之前 debug 的断点, debug 的设置: `restart`或者`run`
  - 全新的 debugger: `q`, `quit`, `exit`退出 debugger 后重新进入. 

### Reference

- 官方文档: https://docs.python.org/3/library/pdb.html

## 2. vscode 自带的 debug

主要就是 `launch.json`文件, 填入规范的即可. 但是这种每次 debug 都是重新在一个终端下进行, 不是非常友好. 

需要添加 `args` 可以通过如下方式: 

```json
{
    "configurations": [
        {
            "name": "Python Debugger: Current File with Arguments",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "args": [
                "image_folder=xxx",
                "ckpt=xxx"
            ]
        }
    ]
}
```


## 3. debugpy 包
### 安装 debugpy
vscode 里面下载好 python 相关插件, 

```pip install debugpy -U```

### 配置

在要 debug 的代码中加入这个: 

``` python
import debugpy
try:
    # 5678 is the default attach port in the VS Code debug configurations. Unless a host and port are specified, host defaults to 127.0.0.1
    debugpy.listen(("localhost", 9501))
    print("Waiting for debugger attach")
    debugpy.wait_for_client()
except Exception as e:
    pass
```

在 vscode 中的 launch.json 的 configuration 中加入

```json
				{
            "name": "sh_file_debug", # 随意
            "type": "debugpy",
            "request": "attach",
            "connect": {
                "host": "localhost",
                "port": 9501
            }
        },
```

**可以写入多个**, 来回切换. 相比较直接 `launch.json`来进行配置更加方便一点. 

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Current File with Arguments",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "args": "${command:pickArgs}"
        },
        {
            "name": "sh_file_debug", // 任意
            "type": "debugpy",
            "request": "attach",
            "connect": {
                "host": "localhost",
                "port": 9501
            }
        }
    ]
}
```

### 启动

1. 就正常启动，直接`sh xxx.sh`, 或者 `python xx.py`
2. 在你需要debug的python文件，打上debug断点。
3. 你看打印出来的东西，是不是出现`Waiting for debugger attach`.一般来说，都很快，就出现了。
4. 再在vscode的debug页面，选择`sh_file_debug`进行debug。
5. 就基本上完成了。确实是很方便。
6. **debug结束之后，别忘记把代码里面的 添加的代码，注销掉**

