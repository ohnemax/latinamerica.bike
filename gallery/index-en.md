---
layout: gallery
lang: en
ref: gallery-index
title: Favorites
---

{% assign images=site.data.galeriebeschreibung | where:"fav", "x" %}

<ul class="gallerygrid">
{% for file in images %}
<li>
  <a class="fancybox" rel="group" href="{{ site.url }}/images/{{ file.folder }}/{{ file.filename }}" title="{{ file[page.lang] }}"><img src="{{ site.url }}/images/{{ file.folder }}/{{ file.filename }}" alt="" /></a>
  <div>{{ file[page.lang] }}</div>
</li>
{% endfor %}
</ul>
