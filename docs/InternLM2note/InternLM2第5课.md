# Lecture 5 note & homework

# Note

大模型部署: 参数很冗余, 减少模型参数

![image-20240424223228114](https://raw.githubusercontent.com/zhuhu00/img/master/20240424223228.png)

![image-20240424223239694](https://raw.githubusercontent.com/zhuhu00/img/master/20240424223240.png)

![image-20240424223321968](https://raw.githubusercontent.com/zhuhu00/img/master/20240424223322.png)

## LMDeploy

![image-20240424223537694](https://raw.githubusercontent.com/zhuhu00/img/master/20240424223547.png)

![image-20240424223706608](https://raw.githubusercontent.com/zhuhu00/img/master/20240424223706.png)

```mermaid
flowchart LR
    subgraph Lagent
        tool[调用工具]
        subgraph AgentLego
            tool_support[工具功能支持]
        end
        tool_output(工具输出)
        tool --> tool_support --> tool_output
    end

    input(输入) --> LLM[大语言模型]
    LLM --> IF{是否需要调用工具}
    IF -->|否| output(一般输出)
    IF -->|是| tool
    tool_output -->|处理| agent_output(智能体输出)
```

# Homework

![image-20240425190218524](https://raw.githubusercontent.com/zhuhu00/img/master/20240425190218.png)

天气的例子, 试了下挺快的. 

![image-20240425191256976](https://raw.githubusercontent.com/zhuhu00/img/master/20240425191257.png)

第二部分的

![image-20240425192605030](https://raw.githubusercontent.com/zhuhu00/img/master/20240425192605.png)

![image-20240425192649068](https://raw.githubusercontent.com/zhuhu00/img/master/20240425192649.png)

![image-20240425194335704](https://raw.githubusercontent.com/zhuhu00/img/master/20240425194335.png)

![image-20240425210412106](https://raw.githubusercontent.com/zhuhu00/img/master/20240425210412.png)

![image-20240425210636349](https://raw.githubusercontent.com/zhuhu00/img/master/20240425210636.png)

检测物体上, 这种检测不出来. 

![image-20240425210700287](https://raw.githubusercontent.com/zhuhu00/img/master/20240425210700.png)

示例图倒是检测的不错. 
