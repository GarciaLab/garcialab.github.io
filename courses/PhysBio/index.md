---
layout: course
title: Studies in the Physical Biology at UC Berkeley 
tagline: Physical Biology of the Cell
course_id: PhysBio
term: 
year: 
header_img: teaching.jpg
---
{% assign data_file = site.data.courses.PhysBio %}


<div class='full'>
<div class="row" style="padding: 20px;">
<h3 class="banner"> About </h3>
{{ data_file.course_info['about']}}
<br/>
<br/>

<h3 class="banner"> Table of Contents </h3>
<ul>
  {% for entry in data_file.course_info['content'] %}
  <li><a href="#{{entry.id}}">{{entry.title}}</a></li>
  {%endfor%}
</ul>


<h3 class="banner"> E. coli growth simulations </h3>
<div>
<table>
<tr>
  <th><b><a id = "ecoli">Example</a></b></th>
  <th><b>Date Last Updated </b></th>
  <th><b>Code</b></th>
  <th><b>Data</b></th>  
</tr>
{% for hw in data_file.course_info['Ecoli'] %}
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


<h3 class="banner"> Gene expression  </h3>
<div>
<table>
<tr>
  <th><b><a id = "gexpression">Example</b></a></th>
  <th><b>Date Last Updated </b></th>
  <th><b>Code</b></th>
  <th><b>Data</b></th>  
</tr>
{% for hw in data_file.course_info['GeneExpression'] %}
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


<h3 class="banner"> Biological dynamics  </h3>
<div>
<table>
<tr>
  <th><b><a id = "biodynamic">Example</b></a></th>
  <th><b>Date Last Updated </b></th>
  <th><b>Code</b></th>
  <th><b>Data</b></th>  
</tr>
{% for hw in data_file.course_info['GeneExpression'] %}
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



