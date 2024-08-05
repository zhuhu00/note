# Lecture 4 note & homework

# 笔记

微调

![image-20240424220455074](https://raw.githubusercontent.com/zhuhu00/img/master/20240424220456.png)

增量预训练还是比较多, 在深度学习上. 

不管是哪种微调方法, 还是很需要**数据**.

![image-20240424221033254](https://raw.githubusercontent.com/zhuhu00/img/master/20240424221033.png)

## XTuner 微调

运行原理如下: 

![image-20240425111138728](https://raw.githubusercontent.com/zhuhu00/img/master/20240425111138.png)

优点: 

- 傻瓜式, 以配置文件的形式(json)封装了大部分的微调场景, 一键开始微调
- 轻量级: 对于 7B 参数量的 LLM, 微调所需的最小显存为 8GB, 所以消费级显卡也可以. 

# Homework

![image-20240425134112949](https://raw.githubusercontent.com/zhuhu00/img/master/20240425134113.png)

与模型对话: 

![image-20240425141306870](https://raw.githubusercontent.com/zhuhu00/img/master/20240425141307.png)

比较奇怪, 这回复的. 也太拟合了. 

使用原本的模型就丝滑了很多. 

![image-20240425142223337](https://raw.githubusercontent.com/zhuhu00/img/master/20240425142223.png)

![image-20240425143418626](https://raw.githubusercontent.com/zhuhu00/img/master/20240425143418.png)

调整 adapter 参数进行对话, 也好一些. 

![image-20240425144245732](https://raw.githubusercontent.com/zhuhu00/img/master/20240425144246.png)

### 多模态训练微调

finetune 前:

![image-20240425175135040](https://raw.githubusercontent.com/zhuhu00/img/master/20240425175135.png)

finetune 后: 

![image-20240425181257359](https://raw.githubusercontent.com/zhuhu00/img/master/20240425181257.png)

有点东西, 但是我直接回车也输出这个内容描述. 

![image-20240425181408133](https://raw.githubusercontent.com/zhuhu00/img/master/20240425181408.png)

修改问题描述确实可以得到结果. 
