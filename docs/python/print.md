# 打印带颜色的文本

```python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

```

使用方法:
```python
print(f"{bcolors.HEADER}===> Loading Street Gaussians config ==={bcolors.ENDC}")
```