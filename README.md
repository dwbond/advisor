Advisor
===

SRCT Advisor is a dynamic web application that lets users create, compare, and
share course trajectories towards graduation. (Not intended as a replacement for
formal academic advising.)

On Contributing
---

Advisor is still in its very early states and needs all the help it can get.
Even if you don't feel like you can be helpful the more technical aspects, we
definitely need designers, technical writers, and testers.

There are many things that can be done with this project (see the "To Do"
section), but sometimes it's the small things that count, so don't be afraid of
contributing just a small spelling mistake.

If you need help at all please contact and SRCT member. We want people to
contribute, so if you are struggling, or just want to learn we are more than
willing to help.

The project lead for this project is **Daniel Bond**. *dbond2@gmu.edu*

Please visit the [SRCT Wiki](http://wiki.srct.gmu.edu/) for more information
on this and other SRCT projects, along with other helpful links and tutorials.

Setup
---

To get started, you'll need the following installed:

* [Python 2.7.3](http://www.python.org/download/)
* [Django 1.6](https://www.djangoproject.com/download/)
* [Git](http://git-scm.com/book/en/Getting-Started-Installing-Git/)
* [Pip](http://www.pip-installer.org/en/latest/installing.html)
* [virtualenv](http://www.virtualenv.org/en/latest/index.html#installation)

Type the following commands in your terminal (if you're on Windows,
[Cygwin](http://www.cygwin.com/) is recommended, or you can install a
[virtual machine](https://www.virtualbox.org/wiki/Downloads) and install a
distribution of [Linux](http://www.ubuntu.com/download/desktop) to it (select
the 32 bit version).

(also, ssh keys...)

``bash``
``git clone http://git.gmu.edu/srct/advisor.git``
``cd advisor``
``mkdir ~/.virtualenvs``
``virtualenv ~/.virtualenvs/advisor``
``source ~/.virtualenvs/advisor/bin/activate``
``pip install -r requirements.txt``
create the database
``python manage.py schemamigration trajectories --initial``
``python manage.py syncdb`` (the username and password are just for your
machine-- you can set it as merely "me" and "password" if you like)
``python manage.py runserver``

Next, open your web broswer of choice, and go to http//:127.0.0.1:8000/. You
won't see too much. You'll need to add the courses and programs to the database.

I've written some documentation in the docs folder about using the admin
interface and creating some models. Use the same username and password you set
up when you did the `syncdb` command.

How Advisor Works
---

**Models**

*Courses*

Each course has basic information (name, department, credits), but more
importantly has prerequisites and corequisites. Prereqs and Coreqs can accept
null values or 

*CourseCollections*

*Programs*

*Students*

*Trajectories*

**Templates**

<table>
  <tr>
    <td>Template Name</td>
    <td>Function</td>
  </tr>
  <tr>
    <td>index</td>
    <td>This is where students can create a new trajectory. (The portion where
    they enter all of their clases should disappear if they've 
  </tr>
  <tr>
    <td>create</td>
    <td>Based on the information passed in from the </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
  </tr>
</table>

To-do
---

**First orders of business**

*Matters of Functionality*

* how do you make coreqs work? right now it assumes that a coreq has to come
first, but that's obviously not how they work
* there are going to be some issues if you can name a trajectory, but each
semester is actually a trajectory...
* Display when the student is going to graduate, and accept the semester number
for trajectories
* Add support for APs, and fix the "login required" stuff
* Javascript to count the number of credits selected

*Forms and Views*

* some sort of javascript on the comparison page
* Forms on the index and create pages need to submit information
* Forms on index and create pages also need to expand to an additional fields;
also needs to take into consideration the max available, show alerts
* does the create page need to reload in between submissions? ajax or a new
page?  **different page for now, that might actually be "better"**
* LDAP auth/login
* comparison page needs some lovely analytics on the compared trajectories for
the user
* polishing, like privacy policy

*Database and Webscraping*

* scraping the site to populate the database
* moving over to mysql
* scraping of catalog.gmu.edu for the database (this also means that with a
single command everyone can be working on the same database :3)
* autocomplete js for the course name field (after a user puts in the department
abbreviation and the course name (note unlike bookshare this information needn't
be editable)
* map "Second Semester Junior" and the like to numbers for the graduation feature

**Pipe Dreams**

* Making trajectories "public" within the system, so that they can be shared
with other students.
* Making trajectories "public" outside of the system, so that they can be shared
on social and messaging sites.
* Support departments to create sample trajectories for their students.
* Identifying if courses are available in the semester desired, and if so,
getting professor information, CRNs, and what have you.
* An integrated "schedulizer"-type app for the classes that you've selected you
want for that semester.
* Make sure that the loginrequired works as initially intended, that you only
need to sign in in order to save or compare trajectories... this way prospective
students can put their potential trajectories together

About GMU SRCT
---
