---
permalink: /
title: ""
excerpt: ""
author_profile: true
lang: zh
redirect_from: 
  - /zh/about/
  - /zh/about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

# 关于我
乔永超，中山大学系统科学与工程学院26级博士生。主要研究方向为**计算机视觉**与**多模态学习**，涵盖语义分割、行人轨迹预测、具身智能模型等前沿课题。硕士是从[杨敬民教授](https://cs.mnnu.edu.cn/info/1070/1234.htm)，博士是从[李雄教授](https://ssse.sysu.edu.cn/teacher/667)。已发表多篇论文，Google Scholar 引用量持续增长 <a href='https://scholar.google.com/citations?user=68X3IpAAAAAJ' target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>。

<span class='anchor' id='-news'></span>

# 🔥 新闻
- *2026.06*: &nbsp;🎉🎉 被中山大学系统科学与工程学院录取。
- *2025.12*: &nbsp;🎉🎉 论文[BVAMFPN: Multi-scale feature fusion for rotated object detection in remote sensing based on biological visual attention mechanism](https://doi.org/10.1007/s11554-025-01819-3)被Journal of Real-Time Image Processing（JRTIP）接收。
- *2025.12*: &nbsp;🎉🎉 论文[WSADet: A wavelet scale-aware UAV object detector for complex conditions](https://doi.org/10.1016/j.patcog.2025.112965)被Pattern Recognition（PR）接收。
- *2025.10*: &nbsp;🎉🎉 论文[Slfmamba: A state space based vision foundation models fine-tuning for domain generalized semantic segmentations](https://doi.org/10.1007/s00530-025-02018-7)被Multimedia Systems（MMS）接收。
- *2025.10*: &nbsp;🎉🎉 论文[DGFMamba: Model fine-tuning based on bidirectional state space for domain generalization semantic segmentation](https://doi.org/10.1016/j.imavis.2025.105800)被Image and Vision Computing（IMAVIS）接收。
- *2025.07*: &nbsp;🎉🎉 论文[SFANet: Semantic feature aware for domain generalized semantic segmentation](https://doi.org/10.1016/j.engappai.2025.111827)被Engineering Applications of Artificial Intelligence（EAAI）接收。
<div class="foldable-hidden" id="news-hidden" markdown="1">
- *2025.06*: &nbsp;🎉🎉 论文[WrdaGAN: A text-to-image synthesis pipeline based on Wavelet Representation and Adaptive Sample Domain Constraint strategy](https://doi.org/10.1016/j.engappai.2025.111305)被Engineering Applications of Artificial Intelligence（EAAI）接收。
</div>
<button class="foldable-toggle" data-target="news-hidden" data-label="显示全部新闻 ▼" style="display:none;">显示全部新闻 ▼</button>
<span class='anchor' id='-publications'></span>

# 📝 发表论文

<div class='paper-box'>
  <div class='paper-box-left'>
    <div class='paper-box-image-wrap'>
      <div class="badge">JRTIP 2026</div>
      <img src='images/BVAMFPN.png' alt="sym" width="100%">
    </div>
  </div>
  <div class='paper-box-right'>
    <div class="paper-title"><a href="https://doi.org/10.1007/s11554-025-01819-3" target="_blank" rel="noopener noreferrer"><strong>BVAMFPN</strong>: Multi-scale feature fusion for rotated object detection in remote sensing based on biological visual attention mechanism</a></div>
    <div class="paper-authors">Z Wang, J Yang, <strong>Y Qiao</strong>, W Zhang</div>
    <div class="paper-journal"><em>Journal of Real-Time Image Processing</em>, 2026</div>
    <div class="paper-links"><a href="https://doi.org/10.1007/s11554-025-01819-3" target="_blank" rel="noopener noreferrer"><i class="fas fa-file-text"></i> 论文</a><a href="https://github.com/ssdle/BVAMFPN" target="_blank" rel="noopener noreferrer"><i class="fas fa-code"></i> 代码</a><span class="paper-doi"><i class="fas fa-link"></i> DOI: 10.1007/s11554-025-01819-3</span><span class='show_paper_citations' data='68X3IpAAAAAJ:2osOgNQ5qMEC'></span></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-left'>
    <div class='paper-box-image-wrap'>
      <div class="badge">PR 2025</div>
      <img src='images/WSADet.png' alt="sym" width="100%">
    </div>
  </div>
  <div class='paper-box-right'>
    <div class="paper-title"><a href="https://doi.org/10.1016/j.patcog.2025.112965" target="_blank" rel="noopener noreferrer"><strong>WSADet</strong>: A wavelet scale-aware UAV object detector for complex conditions</a></div>
    <div class="paper-authors">L Shang, <strong>Y Qiao</strong>, H Lei, Z Wu, W Yang</div>
    <div class="paper-journal"><em>Pattern Recognition</em>, 2025</div>
    <div class="paper-links"><a href="https://doi.org/10.1016/j.patcog.2025.112965" target="_blank" rel="noopener noreferrer"><i class="fas fa-file-text"></i> 论文</a><a href="https://github.com/LShang12/WSADet" target="_blank" rel="noopener noreferrer"><i class="fas fa-code"></i> 代码</a><span class="paper-doi"><i class="fas fa-link"></i> DOI: 10.1016/j.patcog.2025.112965</span><span class='show_paper_citations' data='68X3IpAAAAAJ:qjMakFHDy7sC'></span></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-left'>
    <div class='paper-box-image-wrap'>
      <div class="badge">MMS 2025</div>
      <img src='images/SLFMamba.png' alt="sym" width="100%">
    </div>
  </div>
  <div class='paper-box-right'>
    <div class="paper-title"><a href="https://doi.org/10.1007/s00530-025-02018-7" target="_blank" rel="noopener noreferrer"><strong>Slfmamba</strong>: A state space based vision foundation models fine-tuning for domain generalized semantic segmentations</a></div>
    <div class="paper-authors"><strong>Y Qiao</strong>, Y Guan, Q He, Z Li, J Yang, W Yang</div>
    <div class="paper-journal"><em>Multimedia Systems</em>, 2025</div>
    <div class="paper-links"><a href="https://doi.org/10.1007/s00530-025-02018-7" target="_blank" rel="noopener noreferrer"><i class="fas fa-file-text"></i> 论文</a><a href="https://github.com/xiaoxia0722/SLFMamba" target="_blank" rel="noopener noreferrer"><i class="fas fa-code"></i> 代码</a><span class="paper-doi"><i class="fas fa-link"></i> DOI: 10.1007/s00530-025-02018-7</span><span class='show_paper_citations' data='68X3IpAAAAAJ:9yKSN-GCB0IC'></span></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-left'>
    <div class='paper-box-image-wrap'>
      <div class="badge">IVC 2025</div>
      <img src='images/DGFMamba.png' alt="sym" width="100%">
    </div>
  </div>
  <div class='paper-box-right'>
    <div class="paper-title"><a href="https://doi.org/10.1016/j.imavis.2025.105800" target="_blank" rel="noopener noreferrer"><strong>DGFMamba</strong>: Model fine-tuning based on bidirectional state space for domain generalization semantic segmentation</a></div>
    <div class="paper-authors"><strong>Y Qiao</strong>, Y Guan, Z Wang, J Yang, W Yang</div>
    <div class="paper-journal"><em>Image and Vision Computing</em>, 2025</div>
    <div class="paper-links"><a href="https://doi.org/10.1016/j.imavis.2025.105800" target="_blank" rel="noopener noreferrer"><i class="fas fa-file-text"></i> 论文</a><a href="https://github.com/xiaoxia0722/DGFMamba" target="_blank" rel="noopener noreferrer"><i class="fas fa-code"></i> 代码</a><span class="paper-doi"><i class="fas fa-link"></i> DOI: 10.1016/j.imavis.2025.105800</span><span class='show_paper_citations' data='68X3IpAAAAAJ:d1gkVwhDpl0C'></span></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-left'>
    <div class='paper-box-image-wrap'>
      <div class="badge">EAAI 2025</div>
      <img src='images/SFANet.png' alt="sym" width="100%">
    </div>
  </div>
  <div class='paper-box-right'>
    <div class="paper-title"><a href="https://doi.org/10.1016/j.engappai.2025.111827" target="_blank" rel="noopener noreferrer"><strong>SFANet</strong>: Semantic feature aware for domain generalized semantic segmentation</a></div>
    <div class="paper-authors"><strong>Y Qiao</strong>, Y Guan, W Yang, J Yang</div>
    <div class="paper-journal"><em>Engineering Applications of Artificial Intelligence</em>, 2025</div>
    <div class="paper-links"><a href="https://doi.org/10.1016/j.engappai.2025.111827" target="_blank" rel="noopener noreferrer"><i class="fas fa-file-text"></i> 论文</a><a href="https://github.com/xiaoxia0722/SFANet" target="_blank" rel="noopener noreferrer"><i class="fas fa-code"></i> 代码</a><span class="paper-doi"><i class="fas fa-link"></i> DOI: 10.1016/j.engappai.2025.111827</span><span class='show_paper_citations' data='68X3IpAAAAAJ:IjCSPb-OGe4C'></span></div>
  </div>
</div>

<div class='paper-box'>
  <div class='paper-box-left'>
    <div class='paper-box-image-wrap'>
      <div class="badge">EAAI 2025</div>
      <img src='images/WrdaGAN.png' alt="sym" width="100%">
    </div>
  </div>
  <div class='paper-box-right'>
    <div class="paper-title"><a href="https://doi.org/10.1016/j.engappai.2025.111305" target="_blank" rel="noopener noreferrer"><strong>WrdaGAN</strong>: A text-to-image synthesis pipeline based on Wavelet Representation and Adaptive Sample Domain Constraint strategy</a></div>
    <div class="paper-authors"><strong>Y Qiao</strong>, Y Guan, S Liao, W Yang, W Ding, L Ouyang</div>
    <div class="paper-journal"><em>Engineering Applications of Artificial Intelligence</em>, 2025</div>
    <div class="paper-links"><a href="https://doi.org/10.1016/j.engappai.2025.111305" target="_blank" rel="noopener noreferrer"><i class="fas fa-file-text"></i> 论文</a><a href="https://github.com/xiaoxia0722/SFANet" target="_blank" rel="noopener noreferrer"><i class="fas fa-code"></i> 代码</a><span class="paper-doi"><i class="fas fa-link"></i> DOI: 10.1016/j.engappai.2025.111305</span><span class='show_paper_citations' data='68X3IpAAAAAJ:UeHWp8X0CEIC'></span></div>
  </div>
</div>
# 🎖️ 荣誉与奖项
- *2026.06* 优秀毕业生
- *2025.12* 国家奖学金
- *2025.12* 三好研究生
- *2025.12* “诗展”奖学金
- *2024.12* 三好研究生
- *2024.12* 一等奖学金
<div class="foldable-hidden" id="honors-hidden" markdown="1">
- *2023.12* 福建省人工智能创意赛一等奖
</div>
<button class="foldable-toggle" data-target="honors-hidden" data-label="显示全部奖项 ▼" style="display:none;">显示全部奖项 ▼</button>

<span class='anchor' id='-educations'></span>

# 📖 教育经历
- *2026.09 - 至今*，中山大学，系统科学与工程学院，电子信息，博士
- *2023.09 - 2026.06*，闽南师范大学，计算机学院，计算机技术，硕士
- *2017.09 - 2021.06*，潍坊学院，计算机工程学院，计算机科学与技术，本科

<span class='anchor' id='-invited-talks'></span>

<!-- # 💬 邀请报告
- *2021.06*，Lorem ipsum dolor sit amet, consectetur adipiscing elit.
- *2021.03*，Lorem ipsum dolor sit amet, consectetur adipiscing elit. \| [\[video\]](https://github.com/) -->

<span class='anchor' id='-internships'></span>

# 💻 实习经历
- *2021.05 - 2021.06*, 汽车之家，北京。
- *2021.03 - 2021.05*, 北京猿圈科技有限责任公司，北京。
- *2020.11 - 2021.01*, 文思海辉技术有限公司，潍坊

# 👔工作经历
- *2021.06 - 2023.06*, 汽车之家，北京。

<script>
(function() {
    document.querySelectorAll('.foldable-toggle').forEach(function(btn) {
        var target = document.getElementById(btn.getAttribute('data-target'));
        if (!target) return;
        var children = target.querySelectorAll('li, .paper-box');
        if (children.length > 0) {
            btn.style.display = 'inline-block';
        }
        var label = btn.getAttribute('data-label') || '显示更多 ▼';
        btn.addEventListener('click', function() {
            var expanded = target.classList.toggle('expanded');
            btn.textContent = expanded ? '收起 ▲' : label;
        });
    });
})();
</script>
