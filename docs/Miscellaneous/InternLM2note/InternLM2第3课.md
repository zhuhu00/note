# Lecture 3 note & homework

## Note

### RAG是什么

RAG（Retrieval Augmented Generation）技术, 结合外部知识库来生成更准确, 更丰富的回答. 解决例如: 幻觉, 知识过时, 缺乏透明, 可追溯的推理过程灯光. 提供更准确的回答, 降低推理成本, 实现外部记忆. 

![RAG overview](https://raw.githubusercontent.com/zhuhu00/img/master/20240412134041.png)

最基本的就是: 检索, 索引, 生成. 

最开始 RAG 是从问答系统, 信息检索出发. 之后出现的则是摘要生成, 内容推荐等. 

感觉之前没有那么发展则是因为没有生成, 总结? 所以其实和之前的siri 这些差不多. 

![image-20240412135342294](https://raw.githubusercontent.com/zhuhu00/img/master/20240412135342.png)

Fine-tuning 需要大量数据, 更新需要新的训练过程, 才能有效. 

![image-20240412141005503](https://raw.githubusercontent.com/zhuhu00/img/master/20240412141005.png)

工作流还是很符合 RAG 这个名字. 结合 text2vec 以及 LLM, 能够解决一些大模型相关的问题. 

## Homework

huixiangdou 的 web 端, 部署起来很方便, 也做了不同的测试, 发现解析 pdf 和其他能力非常 nice..

![image-20240412142515466](https://raw.githubusercontent.com/zhuhu00/img/master/20240412142515.png)

![image-20240412142701765](https://raw.githubusercontent.com/zhuhu00/img/master/20240412142701.png)

![image-20240412142946542](https://raw.githubusercontent.com/zhuhu00/img/master/20240412142946.png)

### 在 `InternLM Studio` 上部署茴香豆技术助手

![image-20240412173310541](https://raw.githubusercontent.com/zhuhu00/img/master/20240412173311.png)
