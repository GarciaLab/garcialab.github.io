---
layout: course
title: Physical Biology Module
tagline: MBL Physiology Course 2024
course_id: PhysioTheory
term: summer
year: 2024
header_img: teaching.jpg
---
{% assign data_file = site.data.courses.MBLPhysiology.2024 %}


<div class='full'>
<div class="row" style="padding: 20px;">
<h3 class="banner"> About </h3>
{{ data_file.course_info['about']}}
<br/>
<br/>
<h3 class="banner"> People </h3>

<div class='mod modGallery' style="margin: auto; display: block;">
      <ul class='gallery large-block-grid-4 medium-block-grid-3 small-block-grid-2'>
      {% for person in data_file.course_info['people'] %}
        <li style="padding: 5px;">
          <h5 class='subbanner' style="width: 95%; fontsize: 1em;"> {{person.name}} - {{person.role}}</h5>
          <img alt="" src="{{site.baseurl}}/images/people/{{person.img}}" />
            <p style="text-align: center;">
                  {{person.email}}<br/>
          </li>
        {% endfor %}
      </ul>
    </div>
  </div>


<h3 class="banner"> Syllabus </h3>
{% assign syllabus_pdf = data_file.course_info['syllabuspdf'] %}


<table>
<tr>
<th><b> Day </b></th>
<th><b> Topics </b></th>
<th><b> Materials</b></th>
<th><b> Videos</b></th>
</tr>
{% assign no = 1 %}
{% for entry in data_file.course_info['syllabus'] %}
<tr>
  <td>{{entry.date}}</td>
  <td>
  <ul>
  {% for topic in entry.topics %}
  <li>
      {{topic}}</li>
  {% endfor %}
  </ul>
  </td>
  <td>
  <ul>
  {% for mat in entry.materials %}
  <li>
      {% if mat.link %}
      {% if mat.type == 'paper'%}
      <a href="{{site.baseurl}}/courses/papers/{{mat.link}}">
      {% endif %} 
      {%if mat.type == 'external' %}
      <a href="{{mat.link}}">
      {%endif%}
      {% if mat.type == 'notes'%}
      <a href="{{site.baseurl}}/courses/mcb137/2024/lecture_notes/{{mat.link}}">
      {% endif %}
      {{mat.name}}</a> </li> 
    {% else %}
    {{mat.name}}</li>
    {% endif %}  
  {% endfor %} 
  </ul>
  </td>
 <td>
  <ul>
  {% for video in entry.videos %}
  <li>
        <a href="{{video.link}}">{{video.name}}</a>{{topic}}</li>
  {% endfor %}
  </ul>
  </td>

 
  </tr>
{% assign no = no | plus: 1 %}
{% endfor %}
<tr>



