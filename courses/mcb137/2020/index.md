---
layout: course
title: MCB137/237 Spring 2020
tagline: Physical Biology of the Cell
course_id: mcb137
term: spring
year: 2020
header_img: teaching.jpg
---
{% assign data_file = site.data.courses.mcb137.spring_2020 %}


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
                  Office Hours: <br/>{{person.office_hours}}</p><br/>
          </li>
        {% endfor %}
      </ul>
    </div>
  </div>

<h3 class="banner"> Course Structure </h3>
{{ data_file.course_info['structure'] }}

<h3 class="banner"> Homework </h3>
<div>
<table>
<tr>
  <th><b>Title</b></th>
  <th><b>Due Date </b></th>
  <th><b>Solutions</b></th>  
</tr>
{% for hw in data_file.course_info['Homework'] %}
<tr>
  <td><a href="{{site.baseurl}}/courses/{{page.course_id}}/{{page.year}}/{{hw.link}}">{{hw.title}}</a></td>
  <td> {{hw.due}} </td>
  <td> <a href="{{hw.solutions}}"> Solutions </a></td>
</tr>
{%endfor%}
</table>


<h3 class="banner"> Syllabus </h3>

<table>
<tr>
<th><b> Lecture Number </b></th>
<th><b> Date </b></th>
<th><b> Topics </b></th>
<th><b> Materials </b></th>
</tr>
{% assign iter = 0 %}
{% for day in data_file.course_info['syllabus'] %}
<tr>
  <td>{{day.number}}</td>
  <td>{{day.date}}</td>
  <td>{{day.topics}}</td>
  <td>{{day.materials}}</td>
  </tr>
{% endfor %}
<tr>



