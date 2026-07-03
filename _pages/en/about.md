---
permalink: /en/about/
title: ""
excerpt: ""
author_profile: true
lang: en
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

# About Me
Yongchao Qiao, a PhD student (Class of 2026) at the School of Systems Science and Engineering, Sun Yat-sen University. My research interests focus on **computer vision** and **multimodal learning**, covering semantic segmentation, pedestrian trajectory prediction, embodied intelligence models, and other cutting-edge topics. My master's degree was supervised by Professor [Yang Jingmin](https://cs.mnnu.edu.cn/info/1070/1234.htm), and my doctoral degree was supervised by Professor [Li Xiong](https://ssse.sysu.edu.cn/teacher/667). I have published numerous papers and his Google Scholar citations are continuously growing <a href='https://scholar.google.com/citations?user=68X3IpAAAAAJ' target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.

<span class='anchor' id='-news'></span>

# 🔥 News
- *2026.06*: &nbsp;🎉🎉 Admitted to the School of Systems Science and Engineering, Sun Yat-sen University.
- *2025.12*: &nbsp;🎉🎉 Paper [BVAMFPN: Multi-scale feature fusion for rotated object detection in remote sensing based on biological visual attention mechanism](https://doi.org/10.1007/s11554-025-01819-3) is accepted by Journal of Real-Time Image Processing (JRTIP).
- *2025.12*: &nbsp;🎉🎉 Paper [WSADet: A wavelet scale-aware UAV object detector for complex conditions](https://doi.org/10.1016/j.patcog.2025.112965) is accepted by Pattern Recognition (PR).
- *2025.10*: &nbsp;🎉🎉 Paper [Slfmamba: A state space based vision foundation models fine-tuning for domain generalized semantic segmentations](https://doi.org/10.1007/s00530-025-02018-7) is accepted by Multimedia Systems (MMS).
- *2025.10*: &nbsp;🎉🎉 Paper [DGFMamba: Model fine-tuning based on bidirectional state space for domain generalization semantic segmentation](https://doi.org/10.1016/j.imavis.2025.105800) is accepted by Image and Vision Computing (IVC).
- *2025.07*: &nbsp;🎉🎉 Paper [SFANet: Semantic feature aware for domain generalized semantic segmentation](https://doi.org/10.1016/j.engappai.2025.111827) is accepted by Engineering Applications of Artificial Intelligence (EAAI).
<div class="foldable-hidden" id="news-hidden" markdown="1">
- *2025.06*: &nbsp;🎉🎉 Paper [WrdaGAN: A text-to-image synthesis pipeline based on Wavelet Representation and Adaptive Sample Domain Constraint strategy](https://doi.org/10.1016/j.engappai.2025.111305) is accepted by Engineering Applications of Artificial Intelligence (EAAI).
</div>
<button class="foldable-toggle" data-target="news-hidden" data-label="Show all news ▼" style="display:none;">Show all news ▼</button>

<span class='anchor' id='-publications'></span>

# 📝 Publications

<div class='paper-box'>
  <div class='paper-box-left'>
    <div class='paper-box-image-wrap'>
      <div class="badge">JRTIP 2026</div>
      <img src='/images/BVAMFPN.png' alt="sym" width="100%">
    </div>
  </div>
  <div class='paper-box-right'>
    <div class="paper-title"><a href="https://doi.org/10.1007/s11554-025-01819-3" target="_blank" rel="noopener noreferrer"><strong>BVAMFPN</strong>: Multi-scale feature fusion for rotated object detection in remote sensing based on biological visual attention mechanism</a></div>
    <div class="paper-authors">Z Wang, J Yang, <strong>Y Qiao</strong>, W Zhang</div>
    <div class="paper-journal"><em>Journal of Real-Time Image Processing</em>, 2026</div>
    <div class="paper-links"><a href="https://doi.org/10.1007/s11554-025-01819-3" target="_blank" rel="noopener noreferrer"><i class="fas fa-file-text"></i> Paper</a><a href="https://github.com/ssdle/BVAMFPN" target="_blank" rel="noopener noreferrer"><i class="fas fa-code"></i> Code</a><span class="paper-doi"><i class="fas fa-link"></i> DOI: 10.1007/s11554-025-01819-3</span><span class='show_paper_citations' data='68X3IpAAAAAJ:2osOgNQ5qMEC'></span></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-left'>
    <div class='paper-box-image-wrap'>
      <div class="badge">PR 2025</div>
      <img src='/images/WSADet.png' alt="sym" width="100%">
    </div>
  </div>
  <div class='paper-box-right'>
    <div class="paper-title"><a href="https://doi.org/10.1016/j.patcog.2025.112965" target="_blank" rel="noopener noreferrer"><strong>WSADet</strong>: A wavelet scale-aware UAV object detector for complex conditions</a></div>
    <div class="paper-authors">L Shang, <strong>Y Qiao</strong>, H Lei, Z Wu, W Yang</div>
    <div class="paper-journal"><em>Pattern Recognition</em>, 2025</div>
    <div class="paper-links"><a href="https://doi.org/10.1016/j.patcog.2025.112965" target="_blank" rel="noopener noreferrer"><i class="fas fa-file-text"></i> Paper</a><a href="https://github.com/LShang12/WSADet" target="_blank" rel="noopener noreferrer"><i class="fas fa-code"></i> Code</a><span class="paper-doi"><i class="fas fa-link"></i> DOI: 10.1016/j.patcog.2025.112965</span><span class='show_paper_citations' data='68X3IpAAAAAJ:qjMakFHDy7sC'></span></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-left'>
    <div class='paper-box-image-wrap'>
      <div class="badge">MMS 2025</div>
      <img src='/images/SLFMamba.png' alt="sym" width="100%">
    </div>
  </div>
  <div class='paper-box-right'>
    <div class="paper-title"><a href="https://doi.org/10.1007/s00530-025-02018-7" target="_blank" rel="noopener noreferrer"><strong>Slfmamba</strong>: A state space based vision foundation models fine-tuning for domain generalized semantic segmentations</a></div>
    <div class="paper-authors"><strong>Y Qiao</strong>, Y Guan, Q He, Z Li, J Yang, W Yang</div>
    <div class="paper-journal"><em>Multimedia Systems</em>, 2025</div>
    <div class="paper-links"><a href="https://doi.org/10.1007/s00530-025-02018-7" target="_blank" rel="noopener noreferrer"><i class="fas fa-file-text"></i> Paper</a><a href="https://github.com/xiaoxia0722/SLFMamba" target="_blank" rel="noopener noreferrer"><i class="fas fa-code"></i> Code</a><span class="paper-doi"><i class="fas fa-link"></i> DOI: 10.1007/s00530-025-02018-7</span><span class='show_paper_citations' data='68X3IpAAAAAJ:9yKSN-GCB0IC'></span></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-left'>
    <div class='paper-box-image-wrap'>
      <div class="badge">IVC 2025</div>
      <img src='/images/DGFMamba.png' alt="sym" width="100%">
    </div>
  </div>
  <div class='paper-box-right'>
    <div class="paper-title"><a href="https://doi.org/10.1016/j.imavis.2025.105800" target="_blank" rel="noopener noreferrer"><strong>DGFMamba</strong>: Model fine-tuning based on bidirectional state space for domain generalization semantic segmentation</a></div>
    <div class="paper-authors"><strong>Y Qiao</strong>, Y Guan, Z Wang, J Yang, W Yang</div>
    <div class="paper-journal"><em>Image and Vision Computing</em>, 2025</div>
    <div class="paper-links"><a href="https://doi.org/10.1016/j.imavis.2025.105800" target="_blank" rel="noopener noreferrer"><i class="fas fa-file-text"></i> Paper</a><a href="https://github.com/xiaoxia0722/DGFMamba" target="_blank" rel="noopener noreferrer"><i class="fas fa-code"></i> Code</a><span class="paper-doi"><i class="fas fa-link"></i> DOI: 10.1016/j.imavis.2025.105800</span><span class='show_paper_citations' data='68X3IpAAAAAJ:d1gkVwhDpl0C'></span></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-left'>
    <div class='paper-box-image-wrap'>
      <div class="badge">EAAI 2025</div>
      <img src='/images/SFANet.png' alt="sym" width="100%">
    </div>
  </div>
  <div class='paper-box-right'>
    <div class="paper-title"><a href="https://doi.org/10.1016/j.engappai.2025.111827" target="_blank" rel="noopener noreferrer"><strong>SFANet</strong>: Semantic feature aware for domain generalized semantic segmentation</a></div>
    <div class="paper-authors"><strong>Y Qiao</strong>, Y Guan, W Yang, J Yang</div>
    <div class="paper-journal"><em>Engineering Applications of Artificial Intelligence</em>, 2025</div>
    <div class="paper-links"><a href="https://doi.org/10.1016/j.engappai.2025.111827" target="_blank" rel="noopener noreferrer"><i class="fas fa-file-text"></i> Paper</a><a href="https://github.com/xiaoxia0722/SFANet" target="_blank" rel="noopener noreferrer"><i class="fas fa-code"></i> Code</a><span class="paper-doi"><i class="fas fa-link"></i> DOI: 10.1016/j.engappai.2025.111827</span><span class='show_paper_citations' data='68X3IpAAAAAJ:IjCSPb-OGe4C'></span></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-left'>
    <div class='paper-box-image-wrap'>
      <div class="badge">EAAI 2025</div>
      <img src='/images/WrdaGAN.png' alt="sym" width="100%">
    </div>
  </div>
  <div class='paper-box-right'>
    <div class="paper-title"><a href="https://doi.org/10.1016/j.engappai.2025.111305" target="_blank" rel="noopener noreferrer"><strong>WrdaGAN</strong>: A text-to-image synthesis pipeline based on Wavelet Representation and Adaptive Sample Domain Constraint strategy</a></div>
    <div class="paper-authors"><strong>Y Qiao</strong>, Y Guan, S Liao, W Yang, W Ding, L Ouyang</div>
    <div class="paper-journal"><em>Engineering Applications of Artificial Intelligence</em>, 2025</div>
    <div class="paper-links"><a href="https://doi.org/10.1016/j.engappai.2025.111305" target="_blank" rel="noopener noreferrer"><i class="fas fa-file-text"></i> Paper</a><a href="https://github.com/xiaoxia0722/SFANet" target="_blank" rel="noopener noreferrer"><i class="fas fa-code"></i> Code</a><span class="paper-doi"><i class="fas fa-link"></i> DOI: 10.1016/j.engappai.2025.111305</span><span class='show_paper_citations' data='68X3IpAAAAAJ:UeHWp8X0CEIC'></span></div>
  </div>
</div>

# 🎖 Honors and Awards
- *2026.06* Outstanding Graduate
- *2025.12* National Scholarship
- *2025.12* Merit Graduate Student
- *2025.12* "Shizhan" Scholarship
- *2024.12* Merit Graduate Student
- *2024.12* First-Class Scholarship
<div class="foldable-hidden" id="honors-hidden" markdown="1">
- *2023.12* First Prize, Fujian Provincial AI Creativity Competition
</div>
<button class="foldable-toggle" data-target="honors-hidden" data-label="Show all awards ▼" style="display:none;">Show all awards ▼</button>

<span class='anchor' id='-educations'></span>

# 📖 Education
- *2026.09 - Present*, Sun Yat-sen University, School of Systems Science and Engineering, PhD in Electronic Information
- *2023.09 - 2026.06*, Minnan Normal University, School of Computer Science, M.Eng. in Computer Technology
- *2017.09 - 2021.06*, Weifang University, School of Computer Engineering, B.Eng. in Computer Science and Technology

<span class='anchor' id='-invited-talks'></span>

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit.
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. \| [\[video\]](https://github.com/) -->

<span class='anchor' id='-internships'></span>

# 💻 Internships
- *2021.05 - 2021.06*, Autohome, Beijing.
- *2021.03 - 2021.05*, Beijing Yuanquan Technology Co., Ltd., Beijing.
- *2020.11 - 2021.01*, Pactera Technologies, Weifang.

# 👔 Work Experience
- *2021.06 - 2023.06*, Autohome, Beijing.

<script>
(function() {
    document.querySelectorAll('.foldable-toggle').forEach(function(btn) {
        var target = document.getElementById(btn.getAttribute('data-target'));
        if (!target) return;
        var children = target.querySelectorAll('li, .paper-box');
        if (children.length > 0) {
            btn.style.display = 'inline-block';
        }
        var label = btn.getAttribute('data-label') || 'Show more ▼';
        btn.addEventListener('click', function() {
            var expanded = target.classList.toggle('expanded');
            btn.textContent = expanded ? 'Collapse ▲' : label;
        });
    });
})();
</script>
