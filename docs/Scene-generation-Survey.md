# Awesome-Scene-Generation

A curated list of papers and open-source resources focused on 3D Scene Generation, intended to keep pace with the anticipated surge of research in the coming months. If you have any additions or suggestions, feel free to contribute. Additional resources like blog posts, videos, etc. are also welcome.

<details span>
<summary><b>Update Log:</b></summary>
<br>
 **April 8, 2024** : Initial the repo!
</details>

<br>

### 3D Gaussian Splatting for Real-Time Radiance Field Rendering

**Authors**: Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis

<details span>
<summary><b>Abstract</b></summary>
Radiance Field methods have recently revolutionized novel-view synthesis
of scenes captured with multiple photos or videos. However, achieving high
visual quality still requires neural networks that are costly to train and render,
while recent faster methods inevitably trade off speed for quality. For
unbounded and complete scenes (rather than isolated objects) and 1080p
resolution rendering, no current method can achieve real-time display rates.
We introduce three key elements that allow us to achieve state-of-the-art
visual quality while maintaining competitive training times and importantly
allow high-quality real-time (≥ 30 fps) novel-view synthesis at 1080p resolution.
First, starting from sparse points produced during camera calibration,
we represent the scene with 3D Gaussians that preserve desirable properties
of continuous volumetric radiance fields for scene optimization while
avoiding unnecessary computation in empty space; Second, we perform
interleaved optimization/density control of the 3D Gaussians, notably optimizing
anisotropic covariance to achieve an accurate representation of the
scene; Third, we develop a fast visibility-aware rendering algorithm that
supports anisotropic splatting and both accelerates training and allows real-time
rendering. We demonstrate state-of-the-art visual quality and real-time
rendering on several established datasets.
</details>

  [📄 Paper (Low Resolution)](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_low.pdf) | [📄 Paper (High Resolution)](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_high.pdf) | [🌐 Project Page](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) | [💻 Code](https://github.com/graphdeco-inria/gaussian-splatting) | [🎥 Short Presentation](https://youtu.be/T_kXY43VZnk?si=DrkbDFxQAv5scQNT) | [🎥 Explanation Video](https://www.youtube.com/live/xgwvU7S0K-k?si=edF8NkYtsRbgTbKi)

<br>

# 2024

| Paper | Institute (first) | Keywords | Publication | Others |
| :---: | :---------------: | :------: | :---------: | :----: |
|[GALA3D: Towards Text-to-3D Complex Scene Generation via Layout-guided  Generative Gaussian Splatting](https://arxiv.org/pdf/2402.07207v1) |PKU|Scene Generation, layout|ICML 2024| [Project](https://gala3d.github.io/)  [Code](https://github.com/VDIGPKU/GALA3D)|
|[CityDreamer: Compositional Generative Model of Unbounded 3D Cities](https://arxiv.org/pdf/2309.00610.pdf) |NTU|Compositional Generation|CVPR 2024|[Project](https://haozhexie.com/project/city-dreamer)  [Code](https://github.com/hzxie/CityDreamer) |
| [Holodeck: Language Guided Generation of 3D Embodied AI Environments](https://arxiv.org/pdf/2312.09067.pdf) |UPenn, allenai, Stanford|Scene Generation, Embodied AI|CVPR 2024| [Project](https://yueyang1996.github.io/holodeck/)  [Code](https://github.com/allenai/Holodeck?tab=readme-ov-file)  |
| [CityGen: Infinite and Controllable 3D City Layout Generation](https://arxiv.org/pdf/2312.01508.pdf) |ZJU|Scene Generation, City generation|arXiv 2312|[Project](https://rese1f.github.io/CityGen/) [Code](https://github.com/rese1f/CityGen) |
| [CG3D: Compositional Generation for Text-to-3D via Gaussian Splatting](https://arxiv.org/pdf/2311.17907) |UCLA|Compositional Generation, 3DGS|arXiv 2311|[Project](https://asvilesov.github.io/CG3D/) [Code(Soon)](https://asvilesov.github.io/CG3D/) |
| [[2303.12218] Compositional 3D Scene Generation using Locally Conditioned Diffusion](https://arxiv.org/pdf/2303.12218) |Stanford University|Compositional Generation, VoxNeRF|arXiv 2303|[Project](https://ryanpo.com/comp3d/) [Code(Soon)](https://ryanpo.com/comp3d/) |
| [GraphDreamer: Compositional 3D Scene Synthesis from Scene Graphs](https://arxiv.org/pdf/2312.00093.pdf) |MPI, Tubingen|Compositional Generation, Scene graph|CVPR 2024|[Project](https://graphdreamer.github.io/)  [Code](https://github.com/GGGHSL/GraphDreamer) |
| [Dreamer XL: Towards High-Resolution Text-to-3D Generation via Trajectory  Score Matching](https://arxiv.org/pdf/2405.11252.pdf) |Durham U|3D Generation|arXiv 2405|[Project]()  [Code](https://github.com/xingy038/Dreamer-XL) |
| ||||[Project](https://yueyang1996.github.io/holodeck/)  [Code](https://github.com/allenai/Holodeck?tab=readme-ov-file) |

### CityDreamer: Compositional Generative Model of Unbounded 3D Cities

**Authors**: Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu

<details>
<summary><b>Abstract</b></summary>
3D city generation is a desirable yet challenging task, since humans are more sensitive to structural distortions in urban environments. Additionally, generating 3D cities is more complex than 3D natural scenes since buildings, as objects of the same class, exhibit a wider range of appearances compared to the relatively consistent appearance of objects like trees in natural scenes. To address these challenges, we propose CityDreamer, a compositional generative model designed specifically for unbounded 3D cities. Our key insight is that 3D city generation should be a composition of different types of neural fields: 1) various building instances, and 2) background stuff, such as roads and green lands. Specifically, we adopt the bird’s eye view scene representation and employ a volumetric render for both instance-oriented and stuff-oriented neural fields. The generative hash grid and periodic positional embedding are tailored as scene parameterization to suit the distinct characteristics of building instances and background stuff. Furthermore, we contribute a suite of CityGen Datasets, including OSM and GoogleEarth, which comprises a vast amount of real-world city imagery to enhance the realism of the generated 3D cities both in their layouts and appearances. CityDreamer achieves state-of-the-art performance not only in generating realistic 3D cities but also in localized editing within the generated cities
</details>

  [📄 Paper](https://arxiv.org/pdf/2309.00610v2) | [🌐 Project Page](https://haozhexie.com/project/city-dreamer) | [💻 Code](https://github.com/hzxie/CityDreamer) | [🎥 Short Presentation](https://www.youtube.com/watch?v=te4zinLTYz0)


- [BerfScene: Bev-conditioned Equivariant Radiance Fields for Infinite 3D  Scene Generation](https://arxiv.org/pdf/2312.02136.pdf) (CVPR 2024)
- [GALA3D: Towards Text-to-3D Complex Scene Generation via Layout-guided  Generative Gaussian Splatting](https://arxiv.org/pdf/2402.07207v1) | [![Project](https://img.shields.io/badge/Project-blue)](https://gala3d.github.io/) | [![Code](https://img.shields.io/badge/Code-black)](https://github.com/VDIGPKU/GALA3D) | (ICML 2024)
-

# 2023

- [3D Scene Diffusion Guidance using Scene Graphs (2023)](https://arxiv.org/pdf/2308.04468.pdf) | [![Paper](https://img.shields.io/badge/Paper-orange)](http://arxiv.org/abs/2212.00792) | [![Project](https://img.shields.io/badge/Project-blue)](https://sparsefusion.github.io/) | [![Code](https://img.shields.io/badge/Code-black)](https://github.com/zhizdev/sparsefusion) | [![Video Links](https://img.shields.io/badge/video-red)](https://www.youtube.com/watch?v=dSkw_fWU72k) | ()

https://github.com/zhao-yiqun/RoomDesigner

[GRM: Large Gaussian Reconstruction Model for Efficient 3D Reconstruction  and Generation](https://arxiv.org/pdf/2403.14621.pdf)

[3D Scene Diffusion Guidance using Scene Graphs (2023)](https://arxiv.org/pdf/2308.04468.pdf)

[Patch-based 3D Natural Scene Generation from a Single Example ( 2023)](https://arxiv.org/pdf/2304.12670.pdf)

[SceneDreamer: Unbounded 3D Scene Generation from 2D Image Collections (IEEE Transactions on Pattern Analysis and Machine Intelligence 2023)](https://arxiv.org/pdf/2302.01330.pdf)

[GraphDreamer: Compositional 3D Scene Synthesis from Scene Graphs (CVPR 2024)](https://arxiv.org/pdf/2312.00093.pdf)

https://github.com/cwchenwang/awesome-3d-diffusion

Set-the-scene: Global-local training for generating controllable nerf scenes

# Datasets
| Paper | Institute (first) | Keywords | Publication | Others |
| :---: | :---------------: | :------: | :---------: | :----: |
|[**Cap3D**: Scalable 3D Captioning with Pretrained Models](https://arxiv.org/pdf/2306.07279.pdf) |UMich|Descriptions of 3D objects by leveraging pretrained models in captioning, alignment, and LLM to consolidate multi-view information, from objaverse.|NeurIPS 2023| [Project](https://cap3d-um.github.io/)  [Code](https://github.com/crockwell/Cap3D) |
|Text2Shape ||||  |
|[[2401.09340] SceneVerse: Scaling 3D Vision-Language Learning for Grounded Scene Understanding](https://arxiv.org/pdf/2401.09340) |BIGAI|Large-scale, multi-purpose dataset of annotated scenes|arXiv 2401| [Project](https://scene-verse.github.io/)  [Code](https://github.com/scene-verse/sceneverse) |
|[[2312.14074] LiDAR-LLM: Exploring the Potential of Large Language Models for 3D LiDAR Understanding](https://arxiv.org/pdf/2312.14074) |PKU|Captioned version of 420k LiDAR scans from the nuScenes using GPT-4 and 2D MLLMs.|arXiv 2312| [Project](https://sites.google.com/view/lidar-llm)  [NoCode](https://sites.google.com/view/lidar-llm) |
| ||||  |
| ||||  |
| ||||  |
| ||||  |
-

# Text-2-3D object generation

| Paper |       Institute (first)       | Keywords   | Publication | Others |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------: | :--------------:  | :---------: | :---------:|
|Wonder3D |PKU|Scene Generation, layout|ICML 2024| [![Project](https://img.shields.io/badge/Project-blue)](https://gala3d.github.io/)  [![Code](https://img.shields.io/badge/Code-black)](https://github.com/VDIGPKU/GALA3D)|
|[CityDreamer: Compositional Generative Model of Unbounded 3D Cities](https://arxiv.org/pdf/2309.00610.pdf) |NTU|Compositional Generation|CVPR 2024|[![Project](https://img.shields.io/badge/Project-blue)](https://haozhexie.com/project/city-dreamer)  [![Code](https://img.shields.io/badge/Code-black)](https://github.com/hzxie/CityDreamer) |
| |||| |
| |||| |
| |||| |
| |||| |
| |||| |
| |||| |
| |||| |
