---
layout: default
title: Tidbits
---

# Tidbits

<a href="https://www.nathanmyers.co" class="subtitle-link"><em>Nathan Myers</em></a>

---

<ul class="post-list">
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <span class="post-meta"><span class="post-date">{{ post.date | date: "%b %-d, %Y" }}.</span><span class="post-wordcount">{{ post.content | number_of_words }} words.</span></span>
    </li>
  {% endfor %}
</ul>
