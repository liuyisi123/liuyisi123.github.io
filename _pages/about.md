---
permalink: /
title: ""
excerpt: "Jian Liu is a Postdoctoral Fellow at The Chinese University of Hong Kong."
author_profile: true
redirect_from:
  - /main/
  - /main.html
---

# 👨‍🔬 About Me

<div class="about-summary" markdown="1">

I am a Postdoctoral Fellow at [The Chinese University of Hong Kong](https://www.cuhk.edu.hk/). I received my Ph.D. degree in Electronic Information from [Fudan University](https://www.fudan.edu.cn/) in 2025, advised by Prof. Cuiwei Yang. Before that, I received my M.S. degree from Southeast University in 2022 and my B.S. degree from Yanshan University in 2019.

My research focuses on **general medical AI**, **wearable physiological intelligence**, **multimodal physiological signal modeling**, **edge intelligence**, and **deployable healthcare systems**. I am especially interested in building robust, interpretable, and efficient AI methods that can move from curated datasets to real-world physiological monitoring, clinical decision support, and distributed healthcare IoT scenarios.

To date, I have published research papers as first author, co-first author, or co-author in venues and journals such as **ICML**, **Nature Communications**, **Information Fusion**, **Expert Systems with Applications**, **IEEE Journal of Biomedical and Health Informatics**, **IEEE Internet of Things Journal**, and **IEEE Transactions on Instrumentation and Measurement**. My recent work bridges foundation-model-style medical AI, physiological signal representation learning, and edge-deployable wearable healthcare systems.

</div>

<div class="scholar-profile" data-metrics-src="/assets/data/scholar-metrics.json">
  <a class="scholar-link" href="https://scholar.google.com/citations?user=IU9omVgAAAAJ&hl=en">Google Scholar Profile: <strong><span data-scholar-profile-citations>400+</span> citations</strong></a>
  <div class="scholar-badges" aria-label="Google Scholar metrics">
    <a class="scholar-badge scholar-badge--citations" href="https://scholar.google.com/citations?user=IU9omVgAAAAJ&hl=en" data-scholar-citations>Citations: 400+</a>
    <a class="scholar-badge scholar-badge--hindex" href="https://scholar.google.com/citations?user=IU9omVgAAAAJ&hl=en" data-scholar-hindex>h-index: 10</a>
    <a class="scholar-badge scholar-badge--i10" href="https://scholar.google.com/citations?user=IU9omVgAAAAJ&hl=en" data-scholar-i10 hidden>i10-index: </a>
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
        var profileCitations = container.querySelector('[data-scholar-profile-citations]');
        var hindex = container.querySelector('[data-scholar-hindex]');
        var i10 = container.querySelector('[data-scholar-i10]');
        if (profileCitations && metrics.citations) profileCitations.textContent = metrics.citations;
        if (citations && metrics.citations) citations.textContent = 'Citations: ' + metrics.citations;
        if (hindex && metrics.hIndex) hindex.textContent = 'h-index: ' + metrics.hIndex;
        if (i10 && metrics.i10Index) {
          i10.textContent = 'i10-index: ' + metrics.i10Index;
          i10.hidden = false;
        }
      })
      .catch(function () {});
  });
</script>

<nav class="home-anchor-nav" aria-label="Homepage sections">
  <a href="#education">Education</a>
  <a href="#research-interests">Research</a>
  <a href="#news">News</a>
  <a href="#awards--honors">Awards</a>
  <a href="#selected-publications">Publications</a>
  <a href="#resources">Resources</a>
  <a href="#contact-information">Contact</a>
</nav>

## 🎓 Education

<div class="education-timeline">
  <div>
    <time>2022 - 2025</time>
    <p><strong>Ph.D. in Electronic Information</strong>, Fudan University<br><span>Advisor: Prof. Cuiwei Yang</span></p>
  </div>
  <div>
    <time>2019 - 2022</time>
    <p><strong>M.S. in Instrumentation Science and Technology</strong>, Southeast University<br><span>Advisors: Prof. Chengyu Liu and Prof. Alan Murray</span></p>
  </div>
  <div>
    <time>2015 - 2019</time>
    <p><strong>B.S. in Measurement and Control Technology and Instrumentation</strong>, Yanshan University<br><span>Advisor: Prof. Yantao Zhao</span></p>
  </div>
</div>

## 🔬 Research Interests

<div class="interest-list">
  <span>General medical AI and interpretable healthcare systems</span>
  <span>Wearable physiological sensing and signal quality assessment</span>
  <span>Foundation models and representation learning for physiological signals</span>
  <span>Edge intelligence, model compression, and healthcare IoT deployment</span>
</div>

## 📰 News

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

## 🏅 Awards & Honors

<div class="awards-list">
  <div><time>2025</time><p>Fudan University Titled Scholarship, sole recipient in school.</p></div>
  <div><time>2025 / 2019</time><p>Outstanding Graduate, Fudan University / Hebei Province / Yanshan University.</p></div>
  <div><time>2024-2025</time><p>Academic Scholarship, 1st/2nd Class, Fudan University.</p></div>
  <div><time>2024</time><p>3rd Prize, China Postgraduate Artificial Intelligence Innovation Competition.</p></div>
  <div><time>2021 / 2023</time><p>1st/2nd Prize, National University Student BME Innovation Design Competition.</p></div>
  <div><time>2024 / 2019</time><p>Outstanding Youth League Member, Fudan University / Yanshan University.</p></div>
  <div><time>2022</time><p>Outstanding Communist Party Member, Southeast University.</p></div>
  <div><time>2019-2021</time><p>2nd Class Academic Scholarship, Southeast University, consecutive years.</p></div>
  <div><time>2016-2018</time><p>Outstanding Student / Class Leader, Yanshan University.</p></div>
</div>

## 📘 Selected Publications

<div class="publication-theme">
  <h3>General Medical AI and Interpretable Healthcare</h3>

  <div class="paper-box">
    <div class="paper-box-image">
      <a href="/publication/2026-07-01_icml-specialist-models">
        <span class="venue-badge">ICML 2026</span>
        <img src="/images/icml-specialist-models-fig1.png" alt="HetMedAgent heterogeneous multi-agent medical AI framework">
      </a>
    </div>
    <div class="paper-box-text" markdown="1">

[**Why Specialist Models Still Matter: A Heterogeneous Multi-Agent Paradigm for Medical Artificial Intelligence**](/publication/2026-07-01_icml-specialist-models)<br>
Yanan Wang, Shuaicong Hu, **Jian Liu**, Guohui Zhou, Aiguo Wang, and Cuiwei Yang.<br>
*International Conference on Machine Learning (ICML), 2026.*

- Studies a heterogeneous multi-agent paradigm for specialist medical AI.
</div>
  </div>

  <div class="paper-box">
    <div class="paper-box-image">
      <a href="/publication/2025-08-14_transparent-ai-sleep">
        <span class="venue-badge">Nat. Commun. 2025</span>
        <img src="/images/NN-1.jpg" alt="Transparent AI and multimodal sleep analysis framework">
      </a>
    </div>
    <div class="paper-box-text" markdown="1">

[**Transparent Artificial Intelligence-enabled Interpretable and Interactive Sleep Apnea Assessment across Flexible Monitoring Scenarios**](/publication/2025-08-14_transparent-ai-sleep)<br>
Shuaicong Hu, **Jian Liu**, Yanan Wang, Cong Fu, Jichu Zhu, Huan Yu, and Cuiwei Yang.<br>
*Nature Communications, 2025.*

- Develops transparent AI for flexible and interpretable sleep apnea assessment.
</div>
  </div>

  <div class="paper-box">
    <div class="paper-box-image">
      <a href="/publication/2025-2-21_articles">
        <span class="venue-badge">ESWA 2025</span>
        <img src="/images/ESWA.jpg" alt="LEAF-Net physiological signal quality assessment">
      </a>
    </div>
    <div class="paper-box-text" markdown="1">

[**LEAF-Net: A Real-Time Fine-Grained Quality Assessment System for Physiological Signals Using Lightweight Evolutionary Attention Fusion**](/publication/2025-2-21_articles)<br>
**Jian Liu**, Shuaicong Hu, Yanan Wang, Qihan Hu, Daomiao Wang, Wei Xiang, Xujian Feng, and Cuiwei Yang.<br>
*Expert Systems with Applications, 2025.*

- Builds a lightweight real-time system for fine-grained physiological signal quality assessment.
</div>
  </div>
</div>

<div class="publication-theme">
  <h3>Physiological Signal Representation and Multimodal Learning</h3>

  <div class="paper-box">
    <div class="paper-box-image">
      <a href="/publication/2026-05-01_bridging">
        <span class="venue-badge">Inf. Fusion 2026</span>
        <img src="/images/FACT-Net.png" alt="Bioelectrical signal analysis and representation learning architecture">
      </a>
    </div>
    <div class="paper-box-text" markdown="1">

[**Bridging the Gap Between Computer Vision and Bioelectrical Signal Analysis**](/publication/2026-05-01_bridging)<br>
Yanan Wang, Shuaicong Hu, **Jian Liu**, Aiguo Wang, Guohui Zhou, and Cuiwei Yang.<br>
*Information Fusion, 2026.*

- Connects visual representation learning with bioelectrical signal analysis.
</div>
  </div>

  <div class="paper-box">
    <div class="paper-box-image">
      <a href="/publication/2026-01-01_pretrained-transformer-physiology">
        <span class="venue-badge">JBHI 2026</span>
        <img src="/images/JBHI-1.jpg" alt="Pretrained transformer for physiological signals">
      </a>
    </div>
    <div class="paper-box-text" markdown="1">

[**Unleashing the Power of Pretrained Transformer for Dense Prediction in Physiological Signals**](/publication/2026-01-01_pretrained-transformer-physiology)<br>
Qihan Hu, Daomiao Wang, Hong Wu, **Jian Liu**, and Cuiwei Yang.<br>
*IEEE Journal of Biomedical and Health Informatics, 2026.*

- Explores pretrained transformer models for dense physiological signal prediction.
</div>
  </div>

  <div class="paper-box">
    <div class="paper-box-image">
      <a href="/publication/2024-10-23_articles">
        <span class="venue-badge">ASOC 2024</span>
        <img src="/images/ASOC.jpg" alt="Personalized multiview physiological signal fusion and transfer learning">
      </a>
    </div>
    <div class="paper-box-text" markdown="1">

[**Personalized Blood Pressure Estimation Using Multiview Fusion Information of Wearable Physiological Signals and Transfer Learning**](/publication/2024-10-23_articles)<br>
**Jian Liu**, Shuaicong Hu, Yanan Wang, Wei Xiang, Qihan Hu, and Cuiwei Yang.<br>
*Applied Soft Computing, 2024.*

- Studies personalized multiview physiological signal fusion and transfer learning for adaptive healthcare modeling.
</div>
  </div>
</div>

<div class="publication-theme">
  <h3>Edge Intelligence and Wearable Healthcare Systems</h3>

  <div class="paper-box">
    <div class="paper-box-image">
      <a href="/publication/2026-05-01_edge-intelligent-abp">
        <span class="venue-badge">ESWA 2026</span>
        <img src="/images/Fig.2.jpg" alt="Edge-intelligent arterial blood pressure inference">
      </a>
    </div>
    <div class="paper-box-text" markdown="1">

[**Edge-Intelligent Cross-Platform Architecture for Knowledge-Intensive Arterial Blood Pressure Inference in Distributed Healthcare IoT Networks**](/publication/2026-05-01_edge-intelligent-abp)<br>
**Jian Liu**, Shuaicong Hu, Yanan Wang, Wei Xiang, and Cuiwei Yang.<br>
*Expert Systems with Applications, 2026.*

- Designs a cross-platform edge architecture for distributed arterial blood pressure inference.
</div>
  </div>

  <div class="paper-box">
    <div class="paper-box-image">
      <a href="/publication/2025-06-01_dual-focus">
        <span class="venue-badge">IEEE IoT-J 2025</span>
        <img src="/images/JIOT.jpg" alt="Cloud-edge collaborative hemodynamic analysis">
      </a>
    </div>
    <div class="paper-box-text" markdown="1">

[**A Dual-Focus Cloud-Edge Collaborative Framework in Multitask Hemodynamic Parameter Cross-Scale Analysis**](/publication/2025-06-01_dual-focus)<br>
**Jian Liu**, Shuaicong Hu, Yanan Wang, Wei Xiang, and Cuiwei Yang.<br>
*IEEE Internet of Things Journal, 2025.*

- Balances clinical performance and computation efficiency for wearable hemodynamic analysis.
</div>
  </div>

  <div class="paper-box">
    <div class="paper-box-image">
      <a href="/publication/2024-10-14_articles">
        <span class="venue-badge">IEEE IoT-J 2025</span>
        <img src="/images/CPMP-IoT.png" alt="IoMT-driven precision cardiovascular assessment framework">
      </a>
    </div>
    <div class="paper-box-text" markdown="1">

[**An IoMT-Driven Framework for Precision Cardiovascular Assessment Incorporating Multiscale Perspectives and Microfiber Bragg Grating**](/publication/2024-10-14_articles)<br>
**Jian Liu**, Hengtian Zhu, Wei Xiang, Shuaicong Hu, Qihan Hu, Daomiao Wang, Huan Yang, Zhengyi Mao, Fei Xu, and Cuiwei Yang.<br>
*IEEE Internet of Things Journal, 2025.*

- Integrates wearable sensing, multiscale cardiovascular assessment, and IoMT deployment for precision monitoring.
</div>
  </div>
</div>

<p class="publication-cta"><a href="/publications/">Full publication list</a></p>

## 🔗 Resources

<div class="resource-grid">
  <a class="resource-card" href="https://github.com/liuyisi123/LSMOE"><strong>LSMOE</strong><span>Time-series multitask learning and personalized hemodynamic parameter estimation.</span></a>
  <a class="resource-card" href="https://github.com/liuyisi123/Leaf_Net"><strong>LEAF-Net</strong><span>Fine-grained quality assessment for physiological signals.</span></a>
  <a class="resource-card" href="https://github.com/liuyisi123/FACT-Net"><strong>FACT-Net</strong><span>ABP signal reconstruction with source code and circuit materials.</span></a>
</div>

## 📚 Teaching Experience

- **Autumn 2023**: Teaching assistant, *Medical Electronic Instrumentation*, chaired by Prof. Cuiwei Yang.

## 📫 Contact Information

- **Email**: [jianliu@cuhk.edu.hk](mailto:jianliu@cuhk.edu.hk)
- **Address**: The Chinese University of Hong Kong, Shatin, New Territories, Hong Kong SAR, China
