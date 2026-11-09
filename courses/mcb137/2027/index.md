---
layout: course
title: MCB137L/237L Spring 2027
tagline: Physical Biology of the Cell
course_id: mcb137
term: spring
year: 2027
header_img: teaching.jpg
---
{% assign data_file = site.data.courses.mcb137.spring_2027 %}


<style>
.parallax:has(+ .full .course-2027) .modSectionHeader.big h2,
.parallax:has(+ .full .course-2027) .modSectionHeader.big h3 {
  font-size: 4rem;
  font-weight: bold;
  line-height: 1.15;
  letter-spacing: 0;
  margin: 0;
}
.parallax:has(+ .full .course-2027) .special-title { margin-bottom: 12px; }
.parallax:has(+ .full .course-2027) .modSectionHeader.big h3 { text-transform: uppercase; }
@media (max-width: 768px) {
  .parallax:has(+ .full .course-2027) .modSectionHeader.big h2,
  .parallax:has(+ .full .course-2027) .modSectionHeader.big h3 { font-size: 2rem; }
}
.full > .row:has(> .course-2027) { margin-top: 0 !important; }
.course-2027 { padding: 0 20px; }
.course-2027 .row { margin-left: 0; margin-right: 0; }
.course-2027 .gallery p { overflow-wrap: anywhere; }
.course-2027 table { width: 100%; table-layout: fixed; }
.course-2027 th { overflow-wrap: anywhere; }
</style>
<div class='full course-2027'>
<div class="row" style="padding: 20px;">
{% capture syllabus_url %}{{site.baseurl}}/courses/{{page.course_id}}/{{page.year}}/syllabus_pdf/{{data_file.course_info.syllabuspdf.link}}{% endcapture %}
<h3 class="banner"> About </h3>
{{ data_file.course_info['about']}}
<p style="margin-top: 20px;"><strong><a href="{{syllabus_url}}">Download the full syllabus (PDF)</a></strong></p>
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

<h3 class="banner" style="margin-top: 50px;">Doing Research with AI</h3>
<p>{{ data_file.course_info['research_ai'] }}</p>

<h3 class="banner">Course Policies </h3>
{{ data_file.course_info['policies'] }}
<p style="margin-top: 24px;"><a href="{{syllabus_url}}">Read the full syllabus for complete course policies.</a></p>

<h3 class="banner"> Tentative Course Schedule </h3>
<p>Topics and supporting workshops may evolve in response to project needs.</p>
<p><strong><a href="{{syllabus_url}}">Download the full syllabus (PDF)</a></strong></p>
<div style="overflow-x: auto;">
<table>
<tr>
<th><b> Number </b></th>
<th><b> Date </b></th>
<th><b> Topics </b></th>
<th><b> Materials</b></th>
<th><b> Discussion</b></th>
<th><b> Videos</b></th>
</tr>
{% assign no = 1 %}
{% for entry in data_file.course_info['syllabus'] %}
<tr>
  <td>{{no}}</td>
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
      <a href="{{site.baseurl}}/courses/mcb137/{{page.year}}/lecture_notes/{{mat.link}}">
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
  {% for disc in entry.discussion %}
  <li>
      {% if disc.link %}
      {% if mat.type == 'paper'%}
      <a href="{{site.baseurl}}/courses/papers/{{mat.link}}">
      {% endif %}
      {%if disc.type == 'external' %}
      <a href="{{mat.link}}">
      {%endif%}
      {{disc.name}}</a> </li>
    {% else %}
    {{disc.name}}</li>
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
</table>
</div>

<h3 class="banner"> Homework </h3>
<div style="overflow-x: auto;">
<table>
<tr>
  <th><b>Title</b></th>
  <th><b>Due Date</b></th>
  <th><b>Required Materials</b></th>
  <th><b>Solutions</b></th>
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
</div>

<h3 class="banner"> Reading Materials </h3>

<h4>Research and Teaching with AI</h4>
<h5>Teaching with AI</h5>
<ul>
  <li>
    <a href="https://aiandeducation.mit.edu/report/">MIT AI and Education Report</a>. This report is quite inspiring in terms of thinking of teaching with AI not in a manner that is adversarial to the students, but that encourages collaboration for figuring out how to incorporate these tools into our teaching while being effective at learning the scientific process and how to be creative.
  </li>
</ul>

<h5>How AI is reshaping science</h5>
<ul>
  <li>
    <a href="https://www.its.caltech.edu/~matilde/AImathNew.pdf">Matilde Marcolli: Duet for the End of Math (PDF)</a>. A great short article on what should really constitute success in mathematics and in science in general encouraging us to ask ourselves what is the mathematics that lives only inside you and nowhere else.
  </li>
</ul>

</div>
