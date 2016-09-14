---
layout: page
ref: about
lang: en
permalink: /about/index.html
title: We, you and the bikes
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

Hi! We are **Martha** and **Moritz**, and this is our blog about our **cycling trip in Latin America**. Who are we? How to describe us? Not an easy question.

Since a while, we planned to show that transportation based on fossil fuels is a really, really bad idea, and alternatives are possible. Originally, we wanted to drive an (old) electric car. After it ran for 10m, we decided that this is not enough and switched to bicylces.

We are both in our thirties and still dream to make the world a better place. Therefore our non-fossil travel plans, first the car and now the cycling trip.
Before we started we both finished our doctoral degrees (Martha says Moritz was rather slow). No we want to clear our heads and took a year off. Martha worked as a biologist on the Evolution of Plants, Moritz as physicist doing scientific peace research.

Currently, the Blog contains {{ total_words }} words and {{ site.posts | size }} Posts in {{ site.categories | size }} categories. It has been said that an average human could read this in approximately <span class="time">{{ total_readtime }}</span> minutes.
The newest entry is {% for post in site.posts limit:1 %}{% if post.description %}<a href="{{ site.url }}{{ post.url }}" title="{{ post.description }}">"{{ post.title }}"</a>{% else %}<a href="{{ site.url }}{{ post.url }}" title="{{ post.description }}" title="Read more about {{ post.title }}">"{{ post.title }}"</a>{% endif %}{% endfor %}, written on {% for post in site.posts limit:1 %}{% assign modifiedtime = post.modified | date: "%Y%m%d" %}{% assign posttime = post.date | date: "%Y%m%d" %}<time datetime="{{ post.date | date_to_xmlschema }}" class="post-time">{{ post.date | date: "%d %b %Y" }}</time>{% if post.modified %}{% if modifiedtime != posttime %}.

