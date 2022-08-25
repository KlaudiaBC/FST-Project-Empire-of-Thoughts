# Full Stack Toolkit: "Empire of Thoughts" Portfolio Project
## Welcome!

<p id="welcome"></p>

## This is my Portfolio 4 Project regarding the Code Institute's Diploma in Software Development (E-commerce Applications).
It is a social media platform based on the blog principles - built with Django / Python /Bootstrap and deployed on Heroku.

See the live project <a href="#">here</a>.

<p align="center">
  <img src="#" alt="">
</p>

## **Table Of Contents**
* [**Agile**](#agile)
  * [**Planning Phase**](#planning-phase)
  * [**Product roadmap**](#product-roadmap)
  * [**Release planning**](#release-planning)
  * [**Sprint planning**](#sprint-planning)
  * [**Daily stand-ups**](#daily-stand-ups)
  * [**Sprint review and retrospective**](#sprint-review-and-retrospective)
* [**Implementation**](#implementation)
* [**UX Design**](#ux-design)
  * [**Scope**](#scope)
  * [**Skeleton**](#structure) 
    * [**Wireframes**](#wireframes)
    * [**Database Schema**](#database-schema)
  * [**Surface**](#surface)
    * [**Color scheme**](#color-scheme)
    * [**Typography**](#typography)
* [**Testing**](#testing)
* [**Deployment**](#deployment)
* [**Technologies used**](#technologies-used)
* [**Acknowledgements**](#acknowledgements)


## **Agile**
### **Planning Phase**
The current trends on social media are often referring to a mental health awareness.

At first I collected the data about online activity and tags connected with mental health awareness.
I have also collected the data in accordance with global statistics about mental illnesses. Following the <a href="https://www.who.int/news-room/fact-sheets/detail/mental-disorders" target="_blank">WHO statistics</a> the amount of people who suffer for particular illness is listed below:
* Depression 264 mln
* Bipolar 45 mln
* Schizophrenia 20 mln
* Autism 75 mln
* ADHD 366 mln
* PTSD 8 mln in a given year
* Personality disorders 608.4 mln

Second step was to talk directly to the customers in order to understand their needs and desires in online blogging. I've chosen two people who are very active in social media networks and treat the topic of mental health. After a brainstorming session with clients (about 30 minutes) I had a brief information about the Persona, who I decided to test more via survey. See the survey preview here:
<a href="https://www.survio.com/survey/d/W7P5X0P5Q7L8K7E6X?preview=1" target="_blank">E-Diary trends and Consumer behavior survey</a>

The results have shown that exactly half of responders struggle with depression or other mental health issues:

#### Activity in social media:
* All of the responders are checking social media everyday and the majority of them spend more than 2h daily.
* Over half of responders like to read posts and comments.
* 30% of responders belong to the support groups on Facebook.
* 40% responders admit that they write long messages to their friends on the social communicators and that writing helps them express themselves.
* Only 20% of responders do not post anything on social media.

#### Extra features:
1. Very important:
Comment section, discussion panel - 80% responders admit that support from others is very important for them
2. Important:
Daily affirmations - 60% responders admit that motivation quotes and affirmation are quite important
3. Useful:
Q&A block - All of them consider the possibility to ask questions online as an important feature
*Please see the full results attached*
 
Following my course with Code Institute, I also took one of the challenges from the learning material and created a short video presenting the planning process.
Please, see the video published on my YouTube channel: (link)


### **Product roadmap**
After analyzing the results of the survey and comparing them with a principles stated during the brainstorm session, I was able to create an image of Persona and the basic road map with the requirements to achieve minimum viable product.

<a href="https://prezi.com/view/jZmEUduLODT7R7EPVC5b/" target="_blank">See the results in this presentation.</a>

At this point I started to develop a product backlog in Jira, where I stated: Epics containing User Stories. Each User Story had assigned story points, tasks and a priority label based on the MoSCoW prioritisation technique.
See user stories here.

<p align="center">
  <img src="" alt="backlog_jira">
</p>


### **Release planning**
According to the Agile principles, I created two work sprints (cycles). I created my Sprints for the time of 2 weeks, where each week contains 30h of work, which is equal to the workforce of one part-time working developer (in this case I have assigned all the tasks to myself). Based on the story points I was able to estimate the time of each User Story and assign them into Sprints. The Story Points are equal to:

Story Points | Importance | Time
---|---|---
2p | small task | up to 2h of work
4p | middle task | up to 4h of work
8p | big task | more than 4h of work

The big task should not take more than 8h of work.


### **Sprint planning**
In the first part of work (Sprint 1) the team should deliver Minimum Variable Product, which means create a basic newsfeed page, which is accesible for a User after registration. User should be able to add, edit and delete post as well as leave the comment. The Admin panel should be customised.
The second Sprint contains adding more features like: categories, likes and MyPage (where User can see only his own posts and keep track of them). Before the second Sprint begins, the realization should be discussed with the Client and necessary changes should be added to the workflow.
As you can see on the pictures below, I have not achieve the tasks connected with comment section, therefore those tickets was added to my second Sprint.

Jira backlog in the beggining of Sprint 1:
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/jira_one_backlog.png?raw=true" alt="backlog_sprint_one">
</p>

Jira backlog in the beggining of Sprint 2:
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/jira_backlog_two.png?raw=true" alt="backlog_sprint_two">
</p>

### **Daily stand-ups**
This point of agile development would be necessary, if there was more than one developer working on the project. The short daily stand-up meeting helps the team accomplish their tasks by brief update on the work done and work which is planned for that day. I have been reviewing the workflow on the beginning of each day of development to keep track of the achieved tasks in comparison to the estimated time so that I could later implement the changes into a Second Sprint.

### **Sprint review and retrospective**
After the end of the First Sprint I had scheduled a meeting with my mentor to discuss the current development and seek further review or advice. Secondly I have also presented the deployed page to the clients and had another brainstorm session to discuss further development. With all the changes included in the backlog, I was then ready to begin working on the Second Sprint.

<p align="right"><a href="#welcome">Bact to top</a></p>


## **Implementation**

### 1. Create a basic Django project.
At the beginning I had installed *Django* into my workspace and created a Django project via command in the terminal: *"django-admin startproject empire_blog"* Where *"empire_blog"* is my project name.
Then I created an application: *"python3 manage.py createapp blog"*, where *"blog"* is the name of my Django app.
The reason I have named the app *"blog"* is because that will help to separate the blog-specific behaviors from the functionality of different applications that may be built into this project later.
I have added the new application to the installed apps variable in the 'settings.py' file.

<p align="center">
  <img src="" alt="sprint_one_board_1">
</p>


### 2. Create first views and URLs.
In order to display a basic http page, I had created a new file called "blog_one.html" (later called: "index.html") and I added an *h1* tag containing heading: *"Empire of Thoughts"*. Then in the *views.py* file I added a function, which renders my html page on request. I imported my view into the *urls.py* file and added the path to my *urlpatterns* tuple. I run the migrations to save all the changes in my app.


### 3. Create an Superuser.
In the terminal I had created a <b>superuser</b>, via django command: *"python3 manage.py createsuperuser"*
Then I checked if the admin page is displayed when I add */admin* into a URL on my local server to make sure superuser was added correctly.


### 4. Initial deployment.
Once the template of my application was done, I had followed the walkthrough with the <b>Code Institute</b> according to the FST unit and processed with deployment on Heroku (see more: Deployment).


### 5. Create "Post" model
In order to create a new model *POST*, at first I have created an *entity relationship diagram* (ERD). The next step was to convert it into a Django model. It is worth mentioning that *"Author"* has a data relationship type *"one-to-many"* because one User can publish many journals. In Django terminology, one-to-many association links two tables based on *Foreign Key* column. Similar situation is with the *"Category"* dropdown menu, which supposed to be added in the further implementations.

*DateTime* - blogs usually show the most recent posts, therefore have set the order of displaying the posts - in accordance to the date they were published - from the newest to the oldest (descending order). In order to display desired format of the date (by the default: date, time), in the *settings.py* I have specified the date format to: dd/mm/rr.
<p align="center">***</p>

Once my ERD was all in place, I had add:
- the meta class, which allows to change the behavior of my input fields - in this case I wanted my post to be displayed in descending order
- string method (which returns a string representation of an object)

I have done the migration and saved the changes.
<p align="center">***</p>

Acces the model via Admin Panel:
In order to have access to my *Post* model via the admin panel, I had to import this model into my *admin.py* file and link it into my admin panel.
Then I have logged into my admin panel to make sure all changes have been applied correctly. In the Admin Panel I had created two random posts, needed for further implementations.
I also added a WYSIWYG *("what you see is what you get")* editor, which allows Admin to using the <a href="https://summernote.org/" target="_blank">Summernote</a> integration.


### 6. Create templates
In order to reduce the amount of repeated code, I created a *base.html* file and stored it in a new file called *"templates"*. In this file I added hard-coded elements of my application: navbar and footer. Thanks to this, in all HTML files I have created, I needed to add only the content of the page, without necessity to copy and update the common parts everytime there is a change.

<p align="center">***</p>


### 7. CRUD for Users:

<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/jira_crud.png?raw=true" alt="jira_crud">
</p>

### Create
Next point was to create a view, where User can access the input form and insert the data.
At first I created a new template called *"add_post.html"*.

<b>Views:</b>
I chose to use the class based views because it allows me to add code that's reusable (one view can inherit from another).

I used generic views (classes), which is a Django build-in feature that allows to reduce the code, based on similar patterns in created views.

At first I imported a generic library into my views.py file.
I also imported the Post model.
I created a new view: *"AddPost"* with a parameter: *Create View*, which- as the name suggests- is responsible for creating a view for a user.
In the view I specified a model (Post model), a template I just created and fields I wanted to display for a user (title, author and body).

<b>URLs</b>
In the *"urlpatterns"* tuple I had defined the mapping between the URL and view I just created. It contains 3 elements:
- the pattern: the URL that should be mapped
- the Python path to the view
- the name- needed to perform reversing.

Then I moved into the *"add_post.html"* file where I created a form with a POST method.
Just below the opening form tag, I've added the *CSRF token* - which is a secure random token that prevents hackers attacks.
I used the custom Django form system to display the form: *form.as_p*, which displays each element of the form as a paragraph.

I moved into my model.py file and added a new function to the Post model: *get_absolute_url*, which tells Django how to calculate the URL for an object. In other words, it allows the user to redirect the app into the desired URL, once the User submits a request for sending data.

### Read (publish)
At this point the User was able to input the data and send it into a database.
The next step was to create a new view which will render this data for the User.
I had followed 3-steps ways of implementing this functionality:
1. Create a template (*"posts.html"*)
2. Create a view including: model, queryset (set to descending order) and template_name (desired html file).
3. Add a new path to *urls_patterns*.

To display the added Posts from my database, I've added to my HTML file an iteration ("for" statement) through a post list (all the posts added with a status=1 / *published*) and rendered each element.

### Update / Edit
I created a new template: *"update.html"*
The update page contains the same elements as the *"add_post.html"*, the only difference is applied in the view, which will import the data into a fields (so the input form will not be empty).
In the views.py: create a view with a generic class *"UpdateView"* as a parameter.
I specified the model, template_name and fields which User can update.
I didn't add the form into this class because the *UpdateView* class automatically added this form.
Urls: the last step was to map the path to my new created view in the *urls.py* file.

### Delete
The process of creating the *Delete* function was very similar to the previous ones.
At first I created a new View and set its parameter to *"DeleteView"*.
All functions connected with deleting data from the database are included in this generic view.
Then in my new template called *"delete.html"*, I've added a form with POST method. This form contains only the *"submit"* button as no input is required.
In the *urls.py* file I've added a new path, leading to my *delete.html* file.
To my *DeleteView* class I've added a new function (imported from *django.urls*), which redirects the User to the *Home Page* after submitting the form (deleting post).

<p align="center">***</p>

### 8. User authentication

<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/jira_registration.png?raw=true" alt="jira_registration">
</p>

According to the platform policy, CRUD should be available only for *registered* Users. To restrict those options, I have added authentication.

Authentication contains functions which are not related with blog functions, therefore to make it clear and easily accessible, I have created a new app called *"members"*, designed to store the User model and the registration form.

I added the *"members"* app to my *settings.py* file.
I included all the urls from the *"members"* app in the *blog/urls.py* as well as all the urls which come as built in part of django authentication system.

In my members app:
I've created a new *"templates"* folder and added 3 new html files: register, login and terms.
In the *views.py* file I imported a *UserCreationForm*.
I assigned this form to my new view: *Register*, I also added my template and set the *success_url* redirecting to the *Login* page. I added a url path to this view into the *members/urls.py* file.
Last point was to add the *UserCreationForm* to my HTML file.

The registration form by default contains 3 input fields: *username, password* and *repeat password*.
In order to add the input field for *email adress* I imported this form into my *members/forms.py* file and created a new form (based on the Django default form), where I specified a filed for email as well as set the bootstrap class: *"form-control"* for styling purposes.

In the *settings.py* file I have added redirect urls for *LOGIN* and *LOGOUT*.

In the *base.html* I have created an *"if" statement*, which will render a landing page (only allowing for registration or login) for a new User and will display the *Home* page (with all features available via navigation panel) for the authenticated User.

I haven't created a view for the *Login* page as the form comes with the Django authentication package. I connected the buttons in my navigation bar to the URL for *Registration* and *Login*.
From now on, the full page is available only for registered Users.


<p align="right"><a href="#welcome">Bact to top</a></p>


## **UX Design**

### **Scope**
Empire of Thoughts (ET) is a social networking website which allows users, who register for free profiles, to write a personal journal as well as read and comment journals of others.
The mission of ET is to provide a safe environment for people who struggle with mental health issues or those who have concern for mental health, where users can share their stories and thoughts with related communities.
Categorization of journals via adding a category included in the category recognition, will allow users to find people who match their problems.
During registration, users can choose their own nick, which will allow them to keep the actual identity anonymous. The comment section is designed for support and conversation. The rules are specified in accordance to the help/support groups created on social media, where certain behaviors- common for the social media platforms (like hate speech or themes about the suicide) are filtered and blocked in some cases by a web Administrator. The *Admin* can delete posts/comments added by a user as well as delete the user's account if his actions online are against the rules.

### **Skeleton** 
**Wireframes:**

**Database Schema**


**Surface**

All my previous projects were based on strong, dark colors therefore I decided to try something different. According to Canva.com, one of the biggest trends in social media graphic design will be UI digitalism, which *"adopts the aesthetic of cyberspace: flat shapes, clean lines, and neutral colors"*. Taking into consideration that the target user signs up to share simple words and his struggles with mental health- simplicity and melancholic style make the website a calm sanctuary, where the user can escape from noise and put his thoughts together.
I had used the common parts of the most popular social media platforms and online blogs and introduced a simple, clear design:

<b>Base</b> (common for each page of application):

*Logo and navbar:* Sticky top includes logo (left side) and the navbar on the right side (burder-menu on the mobile devices)
Menu includes following:
 - For new User: Register, Login
 - For registered Users: Home, MyPage, Category, AddPost, Logout.

<p align="center">
  <img src="" alt="navbar">
</p>

Footer - on the bottom of the page, contains information about the author, links to social media accounts (buttons/icons) and link to the Regulations.

<p align="center">
  <img src="" alt="footer">
</p>

Background photo: contains an image of green leaves with the white background and is sticky to the page. Each page displays elements inside the cards wrapped in a container with a light background and soft border, so the image in the background is partly covered and does not distract the User.

<p align="center">
  <img src="" alt="main_page">
</p>

<b>Content of the pages:</b>

Register page - contains one card with registration form and buttons to submit or to go back.

<p align="center">
  <img src="" alt="register_page">
</p>

Login page - contains one card with login form and buttons to submit or go back.

<p align="center">
  <img src="" alt="login_page">
</p>

Newsfeed page (Home): The posts are wrapped in the card element and displayed in descending order. Each card has the same size and contains: the category, topic, date of creation, the author, snippet of the post content. Button *"Read more"* moves the User to the detalic view of the chosen post.

<p align="center">
  <img src="" alt="home_page">
</p>

MyPage - render the same view as the home page, but display filtered posts- only the one which was created by the User. There are two buttons added into a post card: *"Edit"* and *"Delete"*.

<p align="center">
  <img src="" alt="my_page">
</p>

Detalic view page - render the: title, author, date and body of the particular post. Below there is a *"like"* button - User can like and unlike the post by clicking the *"like"* icon. Third part of the container is a comment section, where all added and approved by Admin comments are displayed in ascending order. On top of this section is located an *"Add comment"* button which render the Add Comment Form.

<p align="center">
  <img src="" alt="view_page">
</p>

AddComment - render the add comment form.

<p align="center">
  <img src="" alt="add_comment">
</p>

Add post page - render the form with 3 required inputs: title, body and category.

<p align="center">
  <img src="" alt="addpost_page">
</p>

Edit post page - render the same page as "Add post" with uploaded data of the particular post User wants to edit.

<p align="center">
  <img src="" alt="edit_page">
</p>

Delete post page - render a card element with request to confirm the choice.

<p align="center">
  <img src="" alt="delete_page">
</p>

**Color scheme**

**Typography**
As a font I have chosen *sans serif*, also following the main trends in 2022. This font is very common for the UI digitalism because it is simple to read. The ET portal is based on text therefore it is crucial to make sure, the user will not experience any uncomfort while reading.
In order to add some dynamic to the page, I have set the *"logo"* font to the *Dancing Script*, which is a friendly and lively script, breaking out the monotonic look of the standard sans serif font.

<p align="right"><a href="#welcome">Bact to top</a></p>

## **Technologies Used**
I have used the following technologies and support sources:
- <a href="https://www.djangoproject.com/" target="_blank">Django 3.2.15</a> as a back-end framework
- <a href="https://www.python.org/" target="_blank">Python 3.8.11</a> as a main programming language
- <a href="https://www.djangoproject.com/" target="_blank">JavaScript</a> as a additional programming language
- <a href="https://getbootstrap.com/" target="_blank">Bootstrap v.4.6</a> as a front-end framework
- <a href="https://www.heroku.com/" target="_blank">Heroku</a> for deployment
- <a href="https://www.atlassian.com/" target="_blank">Jira Software</a> for Agile Scrum
- <a href="https://prezi.com/" target="_blank">Prezi</a> for presentation
- <a href="https://www.survio.com/" target="_blank">Survio</a> for a survey
- <a href="https://animista.net/" target="_blank">Animista</a> for animation on landing page
- <a href="https://www.flaticon.com/" target="_blank">Flaticon</a> by Freepik / for all icons included

<p align="right"><a href="#welcome">Bact to top</a></p>

## **Acknowledgements**

In this place I would like to thank everyone, who added an knowledge and value to this project:
- <a href="https://codeinstitute.net/" target="_blank">Code Institute</a> course, materials and walkthroughs - especially the walkthrough "I Think Therefore I Blog"
- lead and support of my Code Institute Mentor - Guido Cecilio
- Code Institute Slack Community
- <a href="https://www.w3schools.com/" target="_blank">W3schools</a>
- <a href="https://stackoverflow.com/" target="_blank">Stack Overflow</a>
- <a href="https://ordinarycoders.com/blog/article/django-user-register-login-logout" target="_blank">"A Guide to User Registration, Login, and Logout in Django"</a> by < ordinary > coders
- <a href="https://dev.to/lawrence_eagles/causes-of-heroku-h10-app-crashed-error-and-how-to-solve-them-3jnl" target="_blank">"Causes of Heroku H10-App Crashed Error And How To Solve Them"</a> by Dev.to
- <a href="https://realpython.com/python-django-blog/" target="_blank">"Build a Blog Using Django, Vue, and GraphQL"</a> by Real Python
- <a href="https://realpython.com/django-hosting-on-heroku/" target="_blank">"Hosting a Django Project on Heroku"</a> by Real Python
- <a href="https://www.atlassian.com/agile/project-management/user-stories" target="_blank">"User stories with examples and a template"</a> by Atlassian
- <a href="https://www.easyagile.com/blog/how-to-write-good-user-stories-in-agile-software-development/" target="_blank">"How to Write Good User Stories in Agile Software Development"</a> by EasyAgile
- <a href="https://www.knowledgehut.com/blog/agile/powerful-tips-for-writing-the-best-user-stories-in-scrum" target="_blank">"Powerful Tips for Writing the Best User Stories in Scrum"</a> by Knowledgehut
- <a href="https://www.canva.com/learn/social-media-design-trends-2022/" target="_blank">"7 Social Media Graphic Design Trends to Build Your Brand in 2022"</a> by Canva
- <a href="https://www.digitalinformationworld.com/2022/03/here-are-social-media-design-trends-you.html?m=1" target="_blank">"Social Media Design Trends You Should Know About in 2022"</a> by 
- <a href="https://inkbotdesign.com/ui-elements/" target="_blank">"7 Essential UI Elements for Social Websites"</a> by Inkbot Design
- <a href="https://www.techcronus.com/blog/building-social-networking-platform-with-python-django-framework/" target="_blank">"Building Social Networking Platform With Python Django Framework"</a> by Techcronus
- <a href="https://softwareengineering.stackexchange.com/questions/335925/do-i-store-blog-posts-in-a-database-and-how-do-i-continue-to-make-posts" target="_blank">"Do I store blog posts in a database? And how do I continue to make posts?"</a> by Software Engineering
- <a href="https://influencermarketinghub.com/social-media-graphic-design-trends/#:~:text=In%202022%2C%20expect%20to%20see,elements%2C%20but%20everything%20is%20intentional" target="_blank">"The 20 Biggest Social Media Graphic Design Trends to Watch For in 2022"</a> by Influencer
- <a href="https://www.aimprosoft.com/blog/how-to-build-a-social-media-website/" target="_blank">"How to Create a Social Media Network Site Like Facebook"</a> by Aimprosoft
- <a href="https://www.djangoproject.com/" target="_blank">Django documentation</a> by Django
- <a href="" target="_blank">name</a> by 
- <a href="" target="_blank">name</a> by 

<p align="right"><a href="#welcome">Bact to top</a></p>