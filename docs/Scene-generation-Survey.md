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

<br>

### CityDreamer: Compositional Generative Model of Unbounded 3D Cities

**Authors**: Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu

<details span>
<summary><b>Abstract</b></summary>
3D city generation is a desirable yet challenging task, since humans are more sensitive to structural distortions in urban environments. Additionally, generating 3D cities is more complex than 3D natural scenes since buildings, as objects of the same class, exhibit a wider range of appearances compared to the relatively consistent appearance of objects like trees in natural scenes. To address these challenges, we propose CityDreamer, a compositional generative model designed specifically for unbounded 3D cities. Our key insight is that 3D city generation should be a composition of different types of neural fields: 1) various building instances, and 2) background stuff, such as roads and green lands. Specifically, we adopt the bird’s eye view scene representation and employ a volumetric render for both instance-oriented and stuff-oriented neural fields. The generative hash grid and periodic positional embedding are tailored as scene parameterization to suit the distinct characteristics of building instances and background stuff. Furthermore, we contribute a suite of CityGen Datasets, including OSM and GoogleEarth, which comprises a vast amount of real-world city imagery to enhance the realism of the generated 3D cities both in their layouts and appearances. CityDreamer achieves state-of-the-art performance not only in generating realistic 3D cities but also in localized editing within the generated cities
</details>

  [📄 Paper](https://arxiv.org/pdf/2309.00610v2) | [🌐 Project Page](https://haozhexie.com/project/city-dreamer) | [💻 Code](https://github.com/hzxie/CityDreamer) | [🎥 Short Presentation](https://www.youtube.com/watch?v=te4zinLTYz0)

<br>

# 2023

[3D Scene Diffusion Guidance using Scene Graphs](https://arxiv.org/pdf/2308.04468.pdf)

https://github.com/zhao-yiqun/RoomDesigner

[![Paper](https://img.shields.io/badge/Paper-orange)](http://arxiv.org/abs/2212.00792) [![Project](https://img.shields.io/badge/Project-blue)](https://sparsefusion.github.io/) [![Code](https://img.shields.io/badge/Code-black)](https://github.com/zhizdev/sparsefusion)[![Video Links](https://img.shields.io/badge/video-blue)](https://www.youtube.com/watch?v=dSkw_fWU72k)

[![Paper](https://img.shields.io/badge/Paper-orange)](http://arxiv.org/abs/2212.00792) [![Project](https://img.shields.io/badge/Project-blue)](https://sparsefusion.github.io/) [![Code](https://img.shields.io/badge/Code-black)](https://github.com/zhizdev/sparsefusion) [![Video Links](https://img.shields.io/badge/video-blue)](https://www.youtube.com/watch?v=dSkw_fWU72k)


<div style="display: flex; justify-content: flex-start; align-items: center;">
    <a href="http://arxiv.org/abs/2212.00792"><img src="https://img.shields.io/badge/Paper-orange" alt="Paper"></a>
    <a href="https://sparsefusion.github.io/"><img src="https://img.shields.io/badge/Project-blue" alt="Project"></a>
    <a href="https://github.com/zhizdev/sparsefusion"><img src="https://img.shields.io/badge/Code-black" alt="Code"></a>
    <a href="https://www.youtube.com/watch?v=dSkw_fWU72k"><img src="https://img.shields.io/badge/video-blue" alt="Video Links"></a>
</div>

