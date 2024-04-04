# 轻松分钟玩转书生·浦语大模型趣味 Demo

- 创作一个小故事

  ![image-20240403110025453](https://raw.githubusercontent.com/zhuhu00/img/master/20240403110025.png)

## 部署**`八戒-Chat-1.8B`**

![image-20240403111918532](https://raw.githubusercontent.com/zhuhu00/img/master/20240403111918.png)

<img src="https://raw.githubusercontent.com/zhuhu00/img/master/20240403112126.png" alt="image-20240403112126726" style="zoom:50%;" />

感觉少了一点多样性, 很容易就是循环. 语料库可能还是比较少. 

## **实战：使用 `Lagent` 运行 `InternLM2-Chat-7B` 模型（开启 30% A100 权限后才可开启此章节）**

![image-20240403171632375](https://raw.githubusercontent.com/zhuhu00/img/master/20240403171633.png)

## **实战：实践部署 `浦语·灵笔2` 模型（开启 50% A100 权限后才可开启此章节）**

![image-20240403173803337](https://raw.githubusercontent.com/zhuhu00/img/master/20240403173803.png)

貌似有点问题, 还是需要设置好本地隐射, 端口隐射到本地后, 就可以显示正常的. 

![image-20240403181138195](https://raw.githubusercontent.com/zhuhu00/img/master/20240403181138.png)

不错不错, 这个文图并茂的方式. 

![image-20240403181216165](https://raw.githubusercontent.com/zhuhu00/img/master/20240403181216.png)

这个是预先定好的吗? 怎么感觉和教程中给的没啥区别.. 

### **图片理解实战（开启 50% A100 权限后才可开启此章节）**

![image-20240403181955515](https://raw.githubusercontent.com/zhuhu00/img/master/20240403181955.png)

效果不错, 

![image-20240403182134397](https://raw.githubusercontent.com/zhuhu00/img/master/20240403182134.png)

下载 huggingface 上的 model, 以及其他文件. 

![image-20240404133600593](https://raw.githubusercontent.com/zhuhu00/img/master/20240404133601.png)

通过 huggingface_hub 可以很方便下载. 

代码: 

```python
from huggingface_hub import hf_hub_download

model_name = "internlm/internlm2-chat-7b"
filename = "config.json"  # Specify the file you want to download
download_path = "./7b_config"

# Download the file
filepath = hf_hub_download(repo_id=model_name, filename=filename, cache_dir=download_path)

print(f"File downloaded at: {filepath}")

```

境内的话, 访问不了 huggingface, 还有 hf-mirror 可以使用, 也是不错的. 