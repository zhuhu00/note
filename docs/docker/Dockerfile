# EIAS
# 与非 GPU 版本区别一：
# 需要使用不同 cuda 版本，从 https://hub.docker.com/ 搜索对应版本，替换下面 FROM 的镜像
# FROM nvidia/cuda:11.8.0-devel-ubuntu22.04 # A800 可用
FROM registry.hub.com:5000/user-images/cuda11.8_lime123
USER root

# 设置编码
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# 设置时区
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone

# 设置默认 shell 为 bash
ENV SHELL=/bin/bash

# 配置 apt 源为北外镜像源
RUN sed -i "s@http://.*archive.ubuntu.com@http://mirrors.bfsu.edu.cn@g" /etc/apt/sources.list && \
    sed -i "s@http://.*security.ubuntu.com@http://mirrors.bfsu.edu.cn@g" /etc/apt/sources.list

# 安装系统依赖和常用工具
# 与非 GPU 版本区别二：
# 这里额外删除了 cuda.list 和 nvidia-ml.list，以免更新了 cuda 相关依赖，固定使用 FROM 镜像中的 cuda 即可
RUN rm -rf /var/lib/apt/lists/* \
        /etc/apt/sources.list.d/cuda.list \
        /etc/apt/sources.list.d/nvidia-ml.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        apt-utils build-essential ca-certificates software-properties-common \
        wget curl vim git openssh-server tmux htop iputils-ping iproute2 && \
    ldconfig && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* ~/*

# 用 miniconda 安装 Python 3.10
# 如果需要其他版本 python，从 https://mirrors.bfsu.edu.cn/anaconda/miniconda/ 替换下面的链接
# RUN wget --quiet -O ~/miniconda.sh https://mirrors.bfsu.edu.cn/anaconda/miniconda/Miniconda3-py310_23.11.0-2-Linux-x86_64.sh && \
#     /bin/bash ~/miniconda.sh -b -p /opt/conda && \
#     rm -f ~/miniconda.sh

# 将 conda/python 加入环境变量，以便能找到命令和依赖库
ENV PATH=/opt/conda/bin:$PATH
ENV LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH

# 配置 conda 北外镜像源
SHELL ["/bin/bash", "-c"]
RUN conda clean -i && echo -e "\
channels:\n\
  - defaults\n\
show_channel_urls: true\n\
default_channels:\n\
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/main\n\
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/r\n\
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/msys2\n\
custom_channels:\n\
  conda-forge: https://mirrors.bfsu.edu.cn/anaconda/cloud\n\
  msys2: https://mirrors.bfsu.edu.cn/anaconda/cloud\n\
  bioconda: https://mirrors.bfsu.edu.cn/anaconda/cloud\n\
  menpo: https://mirrors.bfsu.edu.cn/anaconda/cloud\n\
  pytorch: https://mirrors.bfsu.edu.cn/anaconda/cloud\n\
  pytorch-lts: https://mirrors.bfsu.edu.cn/anaconda/cloud\n\
  simpleitk: https://mirrors.bfsu.edu.cn/anaconda/cloud\n\
" > ~/.condarc

# 配置 pip 北外镜像源
RUN python -m pip install -i https://mirrors.bfsu.edu.cn/pypi/web/simple --upgrade pip && \
    pip config set global.index-url https://mirrors.bfsu.edu.cn/pypi/web/simple && \
    rm -rf /root/.cache/pip /tmp/*

################
# 额外需要安装的软件，写在这里
################
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    cron \
    git \
    libegl1-mesa-dev \
    libgl1-mesa-dev \
    libgles2-mesa-dev \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    wget \
    tmux \
    vim \
    zsh \ 
    openssh-server \
    unzip \
    && rm -rf /var/lib/apt/lists/*


# 解决 ssh 登录后 Dockerfile ENV 定义的环境变量在 shell 中无法读到
SHELL ["/bin/bash", "-c"]
RUN echo -e "\n\
export PATH=${PATH}\n\
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}\n\
" >> /etc/profile