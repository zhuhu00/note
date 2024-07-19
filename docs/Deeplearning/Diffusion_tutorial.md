# Diffusion Model的推导和学习

https://github.com/chunhuizhang/diffusion_models_tutorials

如何入坑 Diffusion 方向？ - cameron的回答 - 知乎
https://www.zhihu.com/question/658056360/answer/3526228476


# Diffusion 学习记录(2024)

> 更新 log: 
>
> - 2024.04: 针对 Diffusion 重新整理, 用 pytorch-lightning 重新实现. 
>
> - 2023.8 开始接触 Diffusion, 由于之前做的和DL 有一些差别, 基本属于传统视觉的内容, 但是公式推导还是挺多的, SLAM 就是数学很多. 

### 相关论文

1. *Diffusion-Original（2015）：[Deep Unsupervised Learning using Nonequilibrium Thermodynamics](https://arxiv.org/pdf/1503.03585v8.pdf)
2. NCSN（2019-Yang Song）：[Generative Modeling by Estimating Gradients of the Data Distribution](https://arxiv.org/pdf/1907.05600v3.pdf)
3. *DDPM（2020-6-UCB）：[Denoising Diffusion Probabilistic Models](https://arxiv.org/pdf/2006.11239v2.pdf)
4. SDE-Framework（2020-10-Yang Song）：[Score-Based Generative Modeling through Stochastic Differential Equations](https://arxiv.org/pdf/2011.13456v2.pdf)

【改进】详见单独章节

- 【6】DDIM（2020-10-Jiaming Song）：[Denoising Diffusion Implicit Models](http://arxiv.org/pdf/2010.02502.pdf)
- 【7】IDDPM（2021-2-OpenAI）：[Improved Denoising Diffusion Probabilistic Models](https://arxiv.org/pdf/2102.09672.pdf)
- 【8*】Diffusion-Beat-GANs（2021-5-OpenAI）：[Diffusion Models Beat GANs on Image Synthesis](https://arxiv.org/pdf/2105.05233.pdf)
- 

# DDPM

# DDIM

DDPM 的改进, DDPM 采样步数需要 1000 步, 属于是时间需要太久. 

