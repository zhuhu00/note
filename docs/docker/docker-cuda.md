# Docker cuda

构建任意版本的 docker 镜像, 包含 cuda. 需要主机安装 docker, docker-nvidia

- **Nvidia cuda docker镜像:** https://catalog.ngc.nvidia.com/orgs/nvidia/containers/cuda/tags

## 以root 用户创建(比较推荐, 但是后续会有一些权限问题)

> **使用 cuda11.8, ubuntu22.04 为例**

- `Dockerfile`如下

```docker
# Reference:
# https://github.com/cvpaperchallenge/Ascender
# https://github.com/nerfstudio-project/nerfstudio

FROM nvidia/cuda:11.8.0-devel-ubuntu22.04
# FROM nvidia/cuda:11.8.0-devel-ubuntu20.04
# FROM nvidia/cuda:11.7.1-devel-ubuntu20.04

ENV COMPOSE_PROJECT_NAME=ubuntu22
# 将sh改为bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# # Set compute capability for nerfacc and tiny-cuda-nn
# # See https://developer.nvidia.com/cuda-gpus and limit number to speed-up build
# ENV TORCH_CUDA_ARCH_LIST="6.0 6.1 7.0 7.5 8.0 8.6 8.9 9.0+PTX"
# ENV TCNN_CUDA_ARCHITECTURES=90;89;86;80;75;70;61;60
# # Speed-up build for RTX 30xx
ENV TORCH_CUDA_ARCH_LIST="8.6"
ENV TCNN_CUDA_ARCHITECTURES=86
# # Speed-up build for RTX 40xx
# # ENV TORCH_CUDA_ARCH_LIST="8.9"
# # ENV TCNN_CUDA_ARCHITECTURES=89

ENV CUDA_HOME=/usr/local/cuda
ENV PATH=${CUDA_HOME}/bin:/home/${USER_NAME}/.local/bin:${PATH}
ENV LD_LIBRARY_PATH=${CUDA_HOME}/lib64:${LD_LIBRARY_PATH}
ENV LIBRARY_PATH=${CUDA_HOME}/lib64/stubs:${LIBRARY_PATH}

# # apt install by root user
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

# conda by root user
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py310_23.11.0-2-Linux-x86_64.sh -O ~/miniconda.sh \
    && /bin/bash ~/miniconda.sh -b -p /opt/conda \
    && rm ~/miniconda.sh \
    && /opt/conda/bin/conda init bash
ENV PATH /opt/conda/bin:$PATH


# ssh
# The RSA key pub need to paste
RUN mkdir -p /root/.ssh && touch /root/.ssh/authorized_keys && echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCljSK/hqYOYv8Ed9ttRWFcHCESi4azhxOXPYP8O/x+RjnpJcUyrpgYIMxr6BShTeMVN2Wi9nwl7Ur6piJ6WnvHCk/1VSOjo93yd3/YPbiullX80qy00H8WgFdJxiv/P5f3qdflqAEDcI5pF758Sgt3t/c38tfh2mD479a5qOiHD/CJObmpbou89TTTLsGW4fbnREZsENZJGpbYpkTJc2d/x/fFCwVSkbzrZKzXsMQsGh5n5CyKFy7sk501EqBytFiIEU0hxgeZc/J7CdiVhDlqXVV0fdcQXsjuacUIowBZSJx/zMnZsX3f4+BuMkiFUOzqBZZZvEqsQwwKnLlm42qgTqa0mnPEVtydBAyohXTFcIRmIDb4dpH4YRi4a6LO6jAkQEOJFifFcFU/A3DwDpSGiIrCGW4wvqdc334dw87JXPM66JL7UrNi7dMe8TdSh1IDpMoWTm41hHS1ncstKc4sGcNN4JOtJPjzR8sd/ZfSmL7iBI0cdpZNNHboT+qvC1M= hu@Hus-MacBook-Pro.local" >> /root/.ssh/authorized_keys \
&& sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config

# change file permission
RUN mkdir -p /etc/periodic/daily \
    && echo "chown 1016:1016 /root/code/ /root/data/ -R" >> /etc/periodic/daily/change-permissions.sh \
    &&  chmod +x /etc/periodic/daily/change-permissions.sh \
    && (crontab -l 2>/dev/null; echo "*/2 * * * * /etc/periodic/daily/change-permissions.sh") | crontab -


# change color of bash prompt
RUN echo "PS1='\[\e[1;35m\]\u@${COMPOSE_PROJECT_NAME}\[\e[0m\]:\[\e[1;34m\]\w\[\e[0m\]\[\e[1;33m\]\$ \[\e[0m\]'" >> /etc/profile && echo "PS1='\[\e[1;35m\]\u@${COMPOSE_PROJECT_NAME}\[\e[0m\]:\[\e[1;34m\]\w\[\e[0m\]\[\e[1;33m\]\$ \[\e[0m\]'" >> ~/.bashrc

RUN printf '#!/bin/bash\n\nservice ssh start\nservice cron start\n\n \ntail -f /dev/null\n' > /start.sh && chmod +x /start.sh


# torch 环境，默认 2.0.0, cuda 11.8, python 3.10
# RUN conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia -y
RUN  pip install ninja ipdb

RUN mkdir -p /run/sshd
CMD ["/start.sh"]
# CMD ["/usr/sbin/sshd", "-D"]

WORKDIR /root/code
```

- `compose.yaml`

  ```yaml
  services:
    ubuntu22:
      # image: xx
      build:
        context: ../
        dockerfile: docker/Dockerfile
        # args:
        #   # you can set environment variables, otherwise default values will be used
        #   USER_NAME: ${HOST_USER_NAME:-gsplat}  # export HOST_USER_NAME=$USER
        #   GROUP_NAME: ${HOST_GROUP_NAME:-gsplats}
        #   UID: ${HOST_UID:-1000}  # export HOST_UID=$(id -u)
        #   GID: ${HOST_GID:-1000}  # export HOST_GID=$(id -g)
        shm_size: '40gb' # build memory
      shm_size: '40gb' # contrainer memory
      environment:
        NVIDIA_DISABLE_REQUIRE: 1  # avoid wrong `nvidia-container-cli: requirement error`
      tty: true
      volumes:
          # left: host, right: container
          - ../:/root/code
          - /mnt/data/:/root/data
      ports:
        - "10022:22" # ssh
        - "18888:8888" # jupyter
        - "16006:6006" # tensorboard
        - "16007:6007" # other viewers
        - "16008:6008" # other viewers
        - "16009:6009" # other viewers
        - "16010:6010" # other viewers
      deploy:
        resources:
          reservations:
            devices:
              - driver: nvidia
                capabilities: [gpu]
  ```

## 以普通用户创建(杜绝 root 权限)

> **使用 cuda11.8, ubuntu22.04 为例**, 这里创建的是 `dreamer` 用户, 并且其有 sudo 权限, 无密码, 或者密码是`password`, 

- `Dockerfile`

```dockerfile
# Reference:
# https://github.com/cvpaperchallenge/Ascender
# https://github.com/nerfstudio-project/nerfstudio

FROM nvidia/cuda:11.8.0-devel-ubuntu22.04

ARG USER_NAME=dreamer
ARG USER_UID=1016
ARG USER_GID=1016
ENV COMPOSE_PROJECT_NAME=ubuntu22

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Set compute capability for nerfacc and tiny-cuda-nn
# See https://developer.nvidia.com/cuda-gpus and limit number to speed-up build
ENV TORCH_CUDA_ARCH_LIST="6.0 6.1 7.0 7.5 8.0 8.6 8.9 9.0+PTX"
ENV TCNN_CUDA_ARCHITECTURES=90;89;86;80;75;70;61;60
# Speed-up build for RTX 30xx
# ENV TORCH_CUDA_ARCH_LIST="8.6"
# ENV TCNN_CUDA_ARCHITECTURES=86
# Speed-up build for RTX 40xx
# ENV TORCH_CUDA_ARCH_LIST="8.9"
# ENV TCNN_CUDA_ARCHITECTURES=89

ENV CUDA_HOME=/usr/local/cuda
ENV PATH=${CUDA_HOME}/bin:/home/${USER_NAME}/.local/bin:${PATH}
ENV LD_LIBRARY_PATH=${CUDA_HOME}/lib64:${LD_LIBRARY_PATH}
ENV LIBRARY_PATH=${CUDA_HOME}/lib64/stubs:${LIBRARY_PATH}

# apt install by root user
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
    sudo \
    && rm -rf /var/lib/apt/lists/*


# Create a new user and grant sudo privileges
RUN groupadd --gid ${USER_GID} ${USER_NAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USER_NAME} \
    && echo "${USER_NAME}:password" | chpasswd \
    && usermod -aG sudo ${USER_NAME} \
    && echo "${USER_NAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/${USER_NAME} \
    && chmod 0440 /etc/sudoers.d/${USER_NAME}

# Change user to non-root user
USER ${USER_NAME}

# conda by non-root user
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py310_23.11.0-2-Linux-x86_64.sh -O ~/miniconda.sh \
    && /bin/bash ~/miniconda.sh -b -p ~/miniconda \
    && rm ~/miniconda.sh \
    && ~/miniconda/bin/conda init bash
ENV PATH ~/miniconda/bin:$PATH

# ssh
# The RSA key pub need to paste
RUN mkdir -p ~/.ssh && touch ~/.ssh/authorized_keys && echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCljSK/hqYOYv8Ed9ttRWFcHCESi4azhxOXPYP8O/x+RjnpJcUyrpgYIMxr6BShTeMVN2Wi9nwl7Ur6piJ6WnvHCk/1VSOjo93yd3/YPbiullX80qy00H8WgFdJxiv/P5f3qdflqAEDcI5pF758Sgt3t/c38tfh2mD479a5qOiHD/CJObmpbou89TTTLsGW4fbnREZsENZJGpbYpkTJc2d/x/fFCwVSkbzrZKzXsMQsGh5n5CyKFy7sk501EqBytFiIEU0hxgeZc/J7CdiVhDlqXVV0fdcQXsjuacUIowBZSJx/zMnZsX3f4+BuMkiFUOzqBZZZvEqsQwwKnLlm42qgTqa0mnPEVtydBAyohXTFcIRmIDb4dpH4YRi4a6LO6jAkQEOJFifFcFU/A3DwDpSGiIrCGW4wvqdc334dw87JXPM66JL7UrNi7dMe8TdSh1IDpMoWTm41hHS1ncstKc4sGcNN4JOtJPjzR8sd/ZfSmL7iBI0cdpZNNHboT+qvC1M= hu@Hus-MacBook-Pro.local" >> ~/.ssh/authorized_keys \
&& sudo sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config

# change color of bash prompt
RUN echo "PS1='\[\e[1;35m\]\u@${COMPOSE_PROJECT_NAME}\[\e[0m\]:\[\e[1;34m\]\w\[\e[0m\]\[\e[1;33m\]\$ \[\e[0m\]'" | sudo tee -a /etc/profile && echo "PS1='\[\e[1;35m\]\u@${COMPOSE_PROJECT_NAME}\[\e[0m\]:\[\e[1;34m\]\w\[\e[0m\]\[\e[1;33m\]\$ \[\e[0m\]'" >> ~/.bashrc

RUN printf '#!/bin/bash\n\nsudo service ssh start\n \ntail -f /dev/null\n\n' > ~/.start.sh && chmod +x ~/.start.sh

RUN sudo mkdir -p /run/sshd
CMD ["~/.start.sh"]
WORKDIR /home/${USER_NAME}/code
```

- `compose.yaml`

  ```yaml
  services:
    threestudio: # image name
      build:
        context: ../
        dockerfile: docker/Dockerfile
        args:
          # you can set environment variables, otherwise default values will be used
          USER_NAME: ${HOST_USER_NAME:-dreamer}  # export HOST_USER_NAME=$USER
          UID: ${HOST_UID:-1016}  # export HOST_UID=$(id -u)
          GID: ${HOST_GID:-1016}  # export HOST_GID=$(id -g)
        shm_size: '40gb'
      shm_size: '40gb'
      environment:
        NVIDIA_DISABLE_REQUIRE: 1  # avoid wrong `nvidia-container-cli: requirement error`
      tty: true
      volumes:
          - ../:/home/${HOST_USER_NAME:-dreamer}/code
      ports:
        - "20022:22" # ssh
        - "28888:8888" # jupyter
        - "26006:6006" # tensorboard
        - "26007:6007" # other viewers
        - "26008:6008" # other viewers
        - "26009:6009" # other viewers
        - "26010:6010" # other viewers
      deploy:
        resources:
          reservations:
            devices:
              - driver: nvidia
                capabilities: [gpu]
  ```

**接下来的操作都是一样的.**


之后依次使用:

记得添加 ssh 的秘钥, 方便构建后使用 ssh 连接.

```shell
docker-compose build # 构建镜像
docker-compose up # 使用该镜像启动一个容器

# 或者使用
docker-compose up -d # 静默启动该容器, 通过 ssh 连接.

cd docker/
docker compose build  # build Docker image
docker compose up -d  # create and start a container in background
docker compose exec threestudio bash  # run bash in the container


exit  # or Ctrl+D
docker compose stop  # stop the container
docker compose start  # start the container
docker compose down  # stop and remove the container
```

## Docker push 一个镜像

```sh
docker ps
docker commit id zhuhu/ubuntu22:cu118
docker push zhuhu/ubuntu22:cu118
```

## Docker 删除

### 删除没有tag 的镜像

这些命令帮助你找到所有的`<none>`标签的镜像，这通常意味着它们没有被标记或者被临时使用过：

1. **列出所有没有标签的镜像：**
   ```bash
   docker images -f "dangling=true"
   ```

   这个命令会列出所有没有关联任何容器并且没有标签的镜像，也称为“悬挂镜像”。`-f "dangling=true"` 是过滤器的一部分，用来指定只显示悬挂镜像。

2. **删除这些没有标签的镜像：**
   ```bash
   docker rmi $(docker images -f "dangling=true" -q)
   ```

   这里，`docker rmi` 用于删除镜像，`$(docker images -f "dangling=true" -q)` 这部分命令会找出所有悬挂镜像的ID，然后传递给 `docker rmi` 命令来进行删除。

### 删除已经停止的容器

在Docker中查看所有当前未运行的容器，

```shell
docker ps -a -f "status=exited"
```

要删除所有已经退出的Docker容器，你可以使用以下命令：

```bash
docker container prune
```

这个命令会删除所有停止状态的容器，帮助清理未使用的Docker资源。在执行此命令时，Docker会提示你确认是否继续删除，你需要确认以继续。

或者，如果你想自动确认并删除所有已经退出的容器，可以使用下面的命令：

```bash
docker rm $(docker ps -a -q -f status=exited)
```


# Torch 安装

```shell
conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia -y
```

# Github unsafe

`````shell
fatal: detected dubious ownership in repository at '/root/code/xx'
To add an exception for this directory, call:

        git config --global --add safe.directory /root/code/xx
`````

解决办法是:

```shell
git config --system --add safe.directory '*'
# 注意这里是--system, 而不是--global, global 是当前用户下, 而 system 是系统级, 所有用户.
```

> 发生的原因是 docker 内是 root 用户, 但是经常需要修改文件所属, 所以可能有了这个问题.
