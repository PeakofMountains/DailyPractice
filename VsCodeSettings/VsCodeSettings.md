Visual Studio Code是一款很好的编辑器，具备众多的插件支持，能在这款编辑器上进行代码的编写，调试和运行等操作，具有良好的代码补全功能
，极大地提高了程序代码书写效率，今天为了完成作业，在VsCode上准备编写C语言程序，需要进行一些相关的配置，在这里将我配置过程中遇到的问题
记录下来

安装过程感谢网上的相关教程和一位大佬舍友的指导！这篇[教程](https://www.bilibili.com/video/BV1sW411v7VZ?from=search&seid=7534839863080335944)很详细.


配置步骤：

1. 在VsCode中的插件库安装C/C++插件和Code Runner两款插件，这是在vscode上调试运行程序的必要插件。  
2. 安装MinGW提供C语言的编译环境和编译器  
3. 在电脑的环境变量里修改PATH路径，将MinGW文件中bin文件夹所在路径添加到PATH中，这样能在命令行中进行源程序的编译操作。  
4. 在vscode中修改两个文件：tasks.json文件和launch.json文件：  
先随便在工作路径下新建一个C语言程序，然后点击左边第四个debug图标，选择添加配置文件，然后系统会给创建一个launch.json文件，
将其中的内容用下列内容替换:  
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(gdb) Launch",    //链接执行preLaunchTask任务
            "preLaunchTask": "C/C++: gcc.exe build active file",    //链接到tasks.json文件中的对应内容label部分，执行其下的args部分
            "type": "cppdbg",
            "request": "launch",
            "program": "${fileDirname}/${fileBasenameNoExtension}.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,   //这里是选择是否采用外部控制台显示
            "internalConsoleOptions": "neverOpen",//选择运行后显示的是终端控制台还是Console控制台，这里设置的是先显示终端控制台
            "MIMode": "gdb",
            "miDebuggerPath": "D:\\VSCode\\MinGW\\bin\\gdb.exe", // 这里修改GDB路径为安装的mingw64的bin下的gdb.exe所在路径
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ]
        }]
}
```
这里的`"miDebuggerPath": "D:\\VSCode\\MinGW\\bin\\gdb.exe"`这一句需要根据自己的电脑MinGW安装所在位置进行修改，同时注意输入的时候
要保持和原来的格式相同，即文件目录之间用双反斜线相隔，否则会出现错误。  
如果想让程序直接在vscode中的控制台中执行显示，就把  
`"externalConsole": true,`这句的true改成false，注意后面的`,`不要漏掉，修改后保存。

点击launch.json就能看到下面有tasks.json文件，点击打开，将其中的内容用下面的内容替换:
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "build",
      "type": "shell",
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      },
      "windows": {
        "command": "g++",
        "args": [
          "-ggdb",
          "\"${file}\"",
          "--std=c++11",
          "-o",
          "\"${fileDirname}\\${fileBasenameNoExtension}.exe\""
        ]
      }
    },
    {
      "type": "shell",
      "label": "C/C++: gcc.exe build active file",
      "command": "D:/VSCode/MinGW/bin/gcc.exe",
      "args": [
        "-g",
        "${file}",
        "-o",
        "${fileDirname}\\${fileBasenameNoExtension}.exe"
      ],
      "options": {
        "cwd": "D:/VSCode/MinGW/bin"
      },
      "problemMatcher": [
        "$gcc"
      ],
      "group": "build"
    }
  ]
}
```
这个文件内容不用修改什么，照着复制就行。  
5. 试着编一个C语言的程序看能否正常运行和调试，如果出现乱码的情况，在右下角有选择编码方式，点击修改就能解决，如果修改后不能解决，重启vscode或者电脑使之生效。  
6. 如果发现不能在vscode的终端进行输入操作，就在CodeRunner插件上右键，选择扩展设background置，在里面将code-runner:Run in Terminal选项前打上勾。  
7. 配置完成，如果没有起作用就重启电脑试试。

碰到的其他问题:  
1. 由于 Exception.tostring()失败,因此无法打印异常字符串  
  解决办法：用管理员权限打开cmd，执行`chcp 936`命令，修改显示字符格式。  
2. Debug时出现`Unable to start debugging.Unable to establish a connection to GDB.`的错误，不能进行调试，解决办法就是把这里的`"externalConsole": true,`改成`"externalConsole": false`，vscode的终端应该和windows的不兼容，如果选择在内部终端运行就会报这个错误，所以目前不建议更改成内部终端执行，[详情解决办法](https://github.com/Microsoft/vscode-cpptools/issues/2889)  


### 我现在已经把我vscode的相关配置文件放在了此目录下,仅供参考,其中有些部分可能需要某些插件的支持,我也在下面列举了几个好用的插件,仅供参考:
1. bracket pair colorizer 2
2. background
3. code runner
