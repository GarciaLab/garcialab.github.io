---
layout: course
title: Studies in the Physical Biology at UC Berkeley 
tagline: Physical Biology of the Cell
course_id: 
term: 
year: 
header_img: teaching.jpg
---
{% assign data_file = site.data.courses.mcb137.spring_2022 %}


<div class='full'>
<div class="row" style="padding: 20px;">
<h3 class="banner"> About </h3>
{{ data_file.course_info['about']}}
<br/>
<br/>

<h3 class="banner"> Content Structure </h3>
{{ data_file.course_info['structure'] }}


<h3 class="banner"> E. coli growth simulations </h3>
<div>
<table>
<tr>
  <th><b>Example</b></th>
  <th><b>Date Last Updated </b></th>
  <th><b>Code</b></th>
  <th><b>Data</b></th>  
</tr>
{% for hw in data_file.course_info['Homework'] %}
<tr>
  <td>{%if hw.link %}<a href="{{site.baseurl}}/courses/{{page.course_id}}/{{page.year}}/hw/{{hw.link}}">{{hw.title}}</a>{%else %}{{hw.title}}{%endif%}</td>
  <td> {{hw.due}} </td>
  <td>
  <ul>
  {% for mat in hw.materials %}
  <li>
  {%if mat.link %}
    {% if mat.type == 'paper' %}
    <a href="{{site.baseurl}}/courses/papers/{{mat.link}}">
    {% elsif mat.type == 'chapter' %}
    <a href="{{site.baseurl}}/courses/chapters/{{mat.link}}">
    {% elsif mat.type == 'data' %}
    <a href="{{site.baseurl}}/courses/data/{{mat.link}}">
    {% elsif mat.type == 'external' %}
    <a href="{{mat.link}}">
    {% endif %}
  {{mat.name}}</a></li>
  {%else %}
  {{mat.name}}</li>
  {%endif%}
  {%endfor%}
  </ul>
  </td>
  <td> 
    <ul>
    {% for sol in hw.solutions %}
    <li>
    {% if sol.link %}
    {% if sol.type == 'external' %}
    <a href="{{sol.link}}"> {{sol.name}}</a></li> 
    {% else %}
    {{sol.name}}</li>
    {% endif %}
    {% else %}
    {{sol.name}}</li>
    {%endif%}
    {% endfor %}
    </ul></td>

</tr>
{%endfor%}
</table>

<tr>



