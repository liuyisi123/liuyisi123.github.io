---
permalink: /
title: "About Me"
excerpt: "Hello, I'm Jian Liu, a Postdoctoral Fellow at The Chinese University of Hong Kong. Welcome to my research space!"
author_profile: true
redirect_from:
  - /main/
  - /main.html
---

<div class="about-summary" markdown="1">

I am a Postdoctoral Fellow at [The Chinese University of Hong Kong](https://www.cuhk.edu.hk/). Before joining CUHK, I received my Ph.D. degree in Electronic Information from Fudan University in 2025, advised by Prof. Cuiwei Yang. I received my M.S. degree from Southeast University in 2022 and my B.S. degree from Yanshan University in 2019.

My research interests include general artificial intelligence, wearable electronics, large language model applications, model compression, edge computing, and intelligent physiological sensing. My recent work focuses on medical AI, wearable physiological monitoring, and efficient AI systems for healthcare and distributed IoT scenarios.

My papers have appeared in venues and journals such as ICML, Nature Communications, IEEE Journal of Biomedical and Health Informatics, IEEE Transactions on Instrumentation and Measurement, IEEE Internet of Things Journal, Information Fusion, and Expert Systems with Applications.

</div>

<div class="scholar-profile" data-metrics-src="/assets/data/scholar-metrics.json">
  <div class="scholar-badges" aria-label="Google Scholar metrics">
    <a class="scholar-badge scholar-badge--citations" href="https://scholar.google.com/citations?user=IU9omVgAAAAJ&hl=en" data-scholar-citations>Citations: 400+</a>
    <a class="scholar-badge scholar-badge--hindex" href="https://scholar.google.com/citations?user=IU9omVgAAAAJ&hl=en" data-scholar-hindex>h-index: 10</a>
  </div>
</div>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    var container = document.querySelector('.scholar-profile[data-metrics-src]');
    if (!container || !window.fetch) return;

    fetch(container.getAttribute('data-metrics-src'), { cache: 'no-store' })
      .then(function (response) { return response.ok ? response.json() : null; })
      .then(function (metrics) {
        if (!metrics) return;
        var citations = container.querySelector('[data-scholar-citations]');
        var hindex = container.querySelector('[data-scholar-hindex]');
        if (citations && metrics.citations) citations.textContent = 'Citations: ' + metrics.citations;
        if (hindex && metrics.hIndex) hindex.textContent = 'h-index: ' + metrics.hIndex;
      })
      .catch(function () {});
  });
</script>

## 🧑‍🎓 Education

- **Ph.D. in Electronic Information**, Fudan University, Sep. 2022 - Dec. 2025. Advisor: Prof. Cuiwei Yang.
- **M.S. in Instrumentation Science and Technology**, Southeast University, Sep. 2019 - Jun. 2022. Advisors: Prof. Chengyu Liu and Prof. Alan Murray.
- **B.S. in Measurement and Control Technology and Instrumentation**, Yanshan University, Sep. 2015 - Jun. 2019. Advisor: Prof. Yantao Zhao.

## 🔬 Research Interests

- Wearable physiological sensing and quality assessment for real-world healthcare monitoring.
- Cuffless blood pressure estimation, hemodynamic parameter analysis, and sleep-related physiological computing.
- Edge intelligence and model compression for deployable healthcare IoT systems.
- Medical AI, large language model applications, and interpretable decision-support systems.

## 📢 News

- **Jul. 2026**: 🎉🎉🎉 Our work *Why Specialist Models Still Matter: A Heterogeneous Multi-Agent Paradigm for Medical Artificial Intelligence* was accepted by *ICML 2026*.
- **Jun. 2026**: 🎉🎉🎉 *Thinking like Clinicians: Ranking-based Multi-instance Learning for PPG-based Hemodynamic Fluctuation Detection* was published in *Pattern Recognition*.
- **May 2026**: 🎉🎉🎉 Our paper *Edge-Intelligent Cross-Platform Architecture for Knowledge-Intensive Arterial Blood Pressure Inference in Distributed Healthcare IoT Networks* was published in *Expert Systems with Applications*.
- **May 2026**: *Bridging the Gap Between Computer Vision and Bioelectrical Signal Analysis* was published in *Information Fusion*.
- **Feb. 2026**: *An Ultra-Efficient Edge-Based Wearable System for Real-Time and Remote Blood Pressure Monitoring* was published in *Engineering Applications of Artificial Intelligence*.
- **Feb. 2026**: *Exploring an Adaptive Framework for Accurate Personalized Cuff-Less Blood Pressure Tracking* was published in *IEEE Transactions on Instrumentation and Measurement*.
- **Jan. 2026**: *Unleashing the Power of Pretrained Transformer for Dense Prediction in Physiological Signals* was published in *IEEE Journal of Biomedical and Health Informatics*.
- **2026**: I started as a Postdoctoral Fellow at *The Chinese University of Hong Kong*.

<details class="simple-details">
  <summary>Earlier news</summary>
  <ul>
    <li><strong>Nov. 2025</strong>: <em>XSleepFusion</em> was published in <em>Information Fusion</em>.</li>
    <li><strong>Sep. 2025</strong>: Our dual-focus cloud-edge collaborative framework for multitask hemodynamic parameter analysis was published in <em>IEEE Internet of Things Journal</em>.</li>
    <li><strong>Aug. 2025</strong>: <em>Transparent artificial intelligence-enabled interpretable and interactive sleep apnea assessment across flexible monitoring scenarios</em> was published in <em>Nature Communications</em>.</li>
    <li><strong>Jul. 2025</strong>: I gave an oral presentation at <em>EMBC 2025</em> on VAM, a parallel cross-modal hybrid network for vascular age estimation from PPG.</li>
    <li><strong>Jun. 2025</strong>: <em>PULSE</em>, a personalized physiological signal analysis framework, was published in <em>Expert Systems with Applications</em>.</li>
    <li><strong>May 2025</strong>: <em>LEAF-Net</em> was published in <em>Expert Systems with Applications</em>.</li>
    <li><strong>2024</strong>: Our paper <em><a href="https://www.nature.com/articles/s41371-024-00978-3#citeas">Preventing Troublesome Variability in Clinical Blood Pressure Measurement</a></em> was published in <em>Journal of Human Hypertension</em>.</li>
    <li><strong>2024</strong>: <em><a href="https://www.sciencedirect.com/science/article/abs/pii/S1568494624011645?via%3Dihub">Personalized Blood Pressure Estimation Using Multiview Fusion Information of Wearable Physiological Signals and Transfer Learning</a></em> was published in <em>Applied Soft Computing</em>.</li>
    <li><strong>2021</strong>: I attended <em>Computing in Cardiology 2021</em> and gave an oral presentation on blood pressure regulation and variability.</li>
  </ul>
</details>

## ⭐ Selected Publications

<div class="paper-group">
  <h3>General Medical AI and Interpretable Healthcare</h3>
  <div class="paper-item">
    <p><a href="/publication/2026-07-01_icml-specialist-models"><strong>Why Specialist Models Still Matter: A Heterogeneous Multi-Agent Paradigm for Medical Artificial Intelligence</strong></a><br>
    Yanan Wang, Shuaicong Hu, <b>Jian Liu</b>, Guohui Zhou, Aiguo Wang, and Cuiwei Yang.<br>
    <em>International Conference on Machine Learning (ICML), 2026.</em></p>
  </div>
  <div class="paper-item">
    <p><a href="/publication/2025-08-14_transparent-ai-sleep"><strong>Transparent Artificial Intelligence-enabled Interpretable and Interactive Sleep Apnea Assessment across Flexible Monitoring Scenarios</strong></a><br>
    Shuaicong Hu, <b>Jian Liu</b>, Yanan Wang, Cong Fu, Jichu Zhu, Huan Yu, and Cuiwei Yang.<br>
    <em>Nature Communications, 2025.</em></p>
  </div>
  <div class="paper-item">
    <p><a href="/publication/2025-04-01_xsleepfusion"><strong>XSleepFusion: A Dual-stage Information Bottleneck Fusion Framework for Interpretable Multimodal Sleep Analysis</strong></a><br>
    Shuaicong Hu, Yanan Wang, <b>Jian Liu</b>, and Cuiwei Yang.<br>
    <em>Information Fusion, 2025.</em></p>
  </div>
</div>

<div class="paper-group">
  <h3>Physiological Signal Foundation and Representation Learning</h3>
  <div class="paper-item">
    <p><a href="/publication/2026-05-01_bridging"><strong>Bridging the Gap Between Computer Vision and Bioelectrical Signal Analysis</strong></a><br>
    Yanan Wang, Shuaicong Hu, <b>Jian Liu</b>, Aiguo Wang, Guohui Zhou, and Cuiwei Yang.<br>
    <em>Information Fusion, 2026.</em></p>
  </div>
  <div class="paper-item">
    <p><a href="/publication/2026-01-01_pretrained-transformer-physiology"><strong>Unleashing the Power of Pretrained Transformer for Dense Prediction in Physiological Signals</strong></a><br>
    Qihan Hu, Daomiao Wang, Hong Wu, <b>Jian Liu</b>, and Cuiwei Yang.<br>
    <em>IEEE Journal of Biomedical and Health Informatics, 2026.</em></p>
  </div>
  <div class="paper-item">
    <p><a href="/publication/2025-2-21_articles"><strong>LEAF-Net: A Real-Time Fine-Grained Quality Assessment System for Physiological Signals Using Lightweight Evolutionary Attention Fusion</strong></a><br>
    <b>Jian Liu</b>, Shuaicong Hu, Yanan Wang, Qihan Hu, Daomiao Wang, Wei Xiang, Xujian Feng, and Cuiwei Yang.<br>
    <em>Expert Systems with Applications, 2025.</em></p>
  </div>
</div>

<div class="paper-group">
  <h3>Edge Intelligence and Wearable Healthcare Systems</h3>
  <div class="paper-item">
    <p><a href="/publication/2026-05-01_edge-intelligent-abp"><strong>Edge-Intelligent Cross-Platform Architecture for Knowledge-Intensive Arterial Blood Pressure Inference in Distributed Healthcare IoT Networks</strong></a><br>
    <b>Jian Liu</b>, Shuaicong Hu, Yanan Wang, Wei Xiang, and Cuiwei Yang.<br>
    <em>Expert Systems with Applications, 2026.</em></p>
  </div>
  <div class="paper-item">
    <p><a href="/publication/2025-06-01_dual-focus"><strong>A Dual-Focus Cloud-Edge Collaborative Framework in Multitask Hemodynamic Parameter Cross-Scale Analysis: The Equilibrium of Clinical Performance and Efficiency</strong></a><br>
    <b>Jian Liu</b>, Shuaicong Hu, Yanan Wang, Wei Xiang, and Cuiwei Yang.<br>
    <em>IEEE Internet of Things Journal, 2025.</em></p>
  </div>
  <div class="paper-item">
    <p><a href="/publication/2026-02-01_wearable-bp"><strong>An Ultra-Efficient Edge-Based Wearable System for Real-Time and Remote Blood Pressure Monitoring</strong></a><br>
    Wei Xiang, <b>Jian Liu</b>, Shuaicong Hu, HaiHui Zhang, Chao Huang, and Cuiwei Yang.<br>
    <em>Engineering Applications of Artificial Intelligence, 2026.</em></p>
  </div>
</div>

[Full publication list](/publications/)

## 🔗 Resources

- [LSMOE](https://github.com/liuyisi123/LSMOE): Time-series multitask learning and personalized hemodynamic parameter estimation.
- [LEAF-Net](https://github.com/liuyisi123/Leaf_Net): Fine-grained quality assessment for physiological signals.
- [FACT-Net](https://github.com/liuyisi123/FACT-Net): ABP signal reconstruction with source code and circuit materials.

## 📚 Teaching Experience

- **Autumn 2023**: Teaching assistant, *Medical Electronic Instrumentation*, chaired by Prof. Cuiwei Yang.

## Awards & Honors

- **2025**: Fudan University Titled Scholarship (sole recipient in school).
- **2025 / 2019**: Outstanding Graduate, Fudan University / Hebei Province / Yanshan University.
- **2024-2025**: Academic Scholarship (1st/2nd Class), Fudan University.
- **2024**: 3rd Prize, China Postgraduate Artificial Intelligence Innovation Competition.
- **2021 / 2023**: 1st/2nd Prize, National University Student BME Innovation Design Competition.
- **2024 / 2019**: Outstanding Youth League Member, Fudan University / Yanshan University.
- **2022**: Outstanding Communist Party Member, Southeast University.
- **2019-2021**: 2nd Class Academic Scholarship, Southeast University (consecutive years).
- **2016-2018**: Outstanding Student / Class Leader, Yanshan University.

## 📫 Contact Information

- **Email**: [jianliu@cuhk.edu.hk](mailto:jianliu@cuhk.edu.hk)
- **Address**: The Chinese University of Hong Kong, Shatin, New Territories, Hong Kong SAR, China
