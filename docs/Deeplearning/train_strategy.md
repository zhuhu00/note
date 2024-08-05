# 有关 训练 的一些 tips

- 指定 cuda: `export CUDA_VISIBLE_DEVICES=1,2,3`

## DDP training strategy

The simple way is using lightning. 
分布式训练, 除了要改pytorch 的代码之外, 还可以用 Lightning, 以及 Lightning 的 Fabric
