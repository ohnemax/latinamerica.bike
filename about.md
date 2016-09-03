---
layout: page
permalink: /about/index.html
title: Ich, du und das Auto
tags: [About]
imagefeature: fourseasons.jpg
chart: true
---

Hallo, wir sind **Moritz** und **Martha** und dies ist unser Blog über unseren **Elektrotransporter** und seine Idee dahinter.  

Momentan besteht er aus {{ total_words }} Wörtern und {{ site.posts | size }} Posts in {{ site.categories | size }} Kategorien. Es wird behauptet der Durchschnittsmensch könnte dies in ungefähr <span class="time">{{ total_readtime }}</span> Minuten lesen. {% if featuredcount != 0 %} Wir haben <a href="{{ site.url }}/featured">{{ featuredcount }} ausgewählte Artikel</a>, die auf jedenfall lesenwert sind.{% endif %} 
Der neuste Post ist {% for post in site.posts limit:1 %}{% if post.description %}<a href="{{ site.url }}{{ post.url }}" title="{{ post.description }}">"{{ post.title }}"</a>{% else %}<a href="{{ site.url }}{{ post.url }}" title="{{ post.description }}" title="Read more about {{ post.title }}">"{{ post.title }}"</a>{% endif %}{% endfor %} vom {% for post in site.posts limit:1 %}{% assign modifiedtime = post.modified | date: "%Y%m%d" %}{% assign posttime = post.date | date: "%Y%m%d" %}<time datetime="{{ post.date | date_to_xmlschema }}" class="post-time">{{ post.date | date: "%d %b %Y" }}</time>{% if post.modified %}{% if modifiedtime != posttime %}.

Wer sind wir so? Wie beschreibt man uns? Ich weiß auch nicht.
An sich wollen wir der Welt zeigen, dass Fortbewegungsmittel auf fossilen Brennstoffen echt kacke sind und das es auch  mit regenerativen Energien geht. 

Wir sind um die dreißig und träumen immer noch davon die Welt zu verbessern. Deswegen stecken wir viel Zeit und Energie in den Bus. 
Nebenbei machen wir beide unseren Doktor, Moritz in der naturwissenschaftlichen Friedensforschug und ich (Martha) beschäftige mich mit der Evolution von Pflanzen.


