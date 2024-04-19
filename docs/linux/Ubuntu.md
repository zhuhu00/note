# 显卡更新驱动
常规更新

```shell
sudo apt update
```


查询

```shell
ubuntu-drivers devices
```

> **不可`autoremove`, 不可`autoinstall`**

```shell
sudo apt-get update
sudo apt-get install nvidia-driver-530 #515对应上面查询到的推荐的版本号
```

等待安装完成, 之后重启即可.

```shell
sudo reboot
```

正常检查 `torch`, cuda, 版本能否使用. 

之后可以安装 cuda 什么的. 其实不装也可以. 


## 参考

- [为什么`nvidia-smi` 和 `nvcc -V` 的 `cuda` 版本不一样](https://www.zhihu.com/question/622711856/answer/3218272497)

