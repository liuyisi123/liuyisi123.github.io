---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Profile
======
I am a Ph.D. candidate in Electronic Information at Fudan University. My research focuses on medical AI, wearable biosignals, medical IoT, cardiovascular diagnosis, and multimodal physiological signal analysis, with particular interest in cloud-edge collaborative systems and lightweight deep learning for personalized healthcare.

Education
======
* Ph.D. in Electronic Information, School of Information Science and Technology, Fudan University, Sep. 2022 - Dec. 2025
* M.S. in Instrumentation Science and Technology, School of Instrumentation Science and Engineering, Southeast University, Sep. 2019 - Jun. 2022
* B.S. in Measurement and Control Technology and Instrumentation, School of Electrical Engineering, Yanshan University, Sep. 2015 - Jun. 2019

Research interests
======
Medical AI, wearable biosignals, medical IoT, AI agents, cardiovascular disease diagnosis, multimodal physiological signal fusion, cloud-edge collaborative computing, and lightweight deep learning.

Skills
======
* Programming and modeling
  * Python, PyTorch, TensorFlow, Scikit-learn, MATLAB, C/C++, Linux Shell
  * Machine learning and deep learning for physiological time series
  * Signal processing, classification, prediction, and personalized modeling
* Wearable electronics and IoT systems
  * Physiological signal acquisition for ECG, PPG, and related biosignals
  * Embedded systems, PCB design, and peripheral circuit design
  * Online transmission, offline storage, and real-time visualization
* Cloud-edge collaborative computing
  * Edge deployment of lightweight models
  * LAN-based data transfer and monitoring interfaces
  * Multi-device physiological monitoring systems

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>

Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
