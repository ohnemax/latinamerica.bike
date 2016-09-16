---
layout: page
ref: about
lang: de
permalink: /ueber/index.html
title: Wir, du und die Fahrräder
tags: [About]
chart: true
---

{% assign total_words = 0 %}
{% assign total_readtime = 0 %}
{% assign featuredcount = 0 %}
{% assign statuscount = 0 %}

{% for post in site.posts %}
    {% assign post_words = post.content | strip_html | number_of_words %}
    {% assign readtime = post_words | append: '.0' | divided_by:200 %}
    {% assign total_words = total_words | plus: post_words %}
    {% assign total_readtime = total_readtime | plus: readtime %}
    {% if post.featured %}
    {% assign featuredcount = featuredcount | plus: 1 %}
    {% endif %}
{% endfor %}

Hallo, wir sind **Moritz** und **Martha** und dies ist unser Blog über unsere **Fahrradtour in Südamerika**. Wer sind wir so? Wie beschreibt man uns? Das ist gar nicht so einfach.

An sich wollen wir der Welt zeigen, dass Fortbewegungsmittel auf fossilen Brennstoffen echt kacke sind und Reisen auch anders geht. Nachdem unser (altes) Elektroauto zwar inzwischen 10m gefahren ist, dies aber leider nicht ausreicht um die Welt zu bereisen, sind wir fürs erste auf's Rad umgestiegen. 

Wir sind beide um die dreißig und träumen immer noch davon die Welt zu verbessern. Deswegen auch die Idee mit dem Elektroauto und jetzt diese Reise. Bevor wir los sind haben wir, mehr oder minder flott, unseren Doktortitel gemacht und wollen jetzt erst mal den Kopf frei bekommen. Moritz hat als Physiker in der naturwissenschaftlichen Friedensforschug promoviert und Martha hat sich als Biologin mit der Evolution von Pflanzen beschäftigt.

Momentan besteht der Blog aus {{ total_words }} Wörtern und {{ site.posts | size }} Posts in {{ site.categories | size }} Kategorien. Es wird behauptet der Durchschnittsmensch könnte dies in ungefähr <span class="time">{{ total_readtime }}</span> Minuten lesen. 
Der neuste Post ist
{% for post in site.posts limit:1 %}
  {% if post.description %}
    <a href="{{ site.url }}{{ post.url }}" title="{{ post.description }}">"{{ post.title }}"</a>
  {% else %}
    <a href="{{ site.url }}{{ post.url }}" title="{{ post.description }}" title="Read more about {{ post.title }}">"{{ post.title }}"</a>
  {% endif %}
{% endfor %}
vom
{% for post in site.posts limit:1 %}
  {% assign modifiedtime = post.modified | date: "%Y%m%d" %}
  {% assign posttime = post.date | date: "%Y%m%d" %}
  <time datetime="{{ post.date | date_to_xmlschema }}" class="post-time">{{ post.date | date: "%d %b %Y" }}</time>
{% endfor %}


