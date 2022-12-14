# Full Stack Toolkit: "Empire of Thoughts" Portfolio Project - TESTING

<p id="welcome"></p>


## **Table Of Contents**
* [**Testing**](#testing)
  * [**Mannual Testing**](#mannual-testing)
  * [**W3C Validator**](#w3c-validator)
  * [**Unit Testing**](#unit-testing)
  * [**PEP8**](#pep8)
  * [**Lighthouse**](#lighthouse)
* [**Errors and bugs**](#errors-and-bugs)

## **TESTING**

### **MANUAL TESTING**
Tests have been performed several times during all implementation process.
The features, which was taken into a testing in both scenarios: on the desktop and on the devices are listed below.

<table>
  <tr>
    <th>Element</th>
    <th>Expected result</th>
    <th>Status</th>
  </tr>
  <tr>
    <td>Logo and navbar</td>
    <td>Make sure that logo is displayed correctly in the top-left corner of the page and buttons of the menu are: on the right top side on desktop/ in the burger button, which displays the dropdown menu/ on the mobile devices.</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Background image and the light-container/content</td>
    <td>Make sure that the dynamics of the background image does not interfere with the text in the light box. Check if the opacity of the box is strong enough to dispatch correctly all elements.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>Registration Form</td>
    <td>Check if the registration form saves the data about the new User when the User provides the correct data. Make sure all validators work correctly and display the error message.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>Login/Logout</td>
    <td>Check if the login form allows User who had created his account correctly - to access the home page for authorised users after providing the correct login credentials. Check if the button "Logout" bring the User back into the "annonymous" mode.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>Add Post form</td>
    <td>Check if the Add Post form does collect the data in the correct way and display the error message when required fields are empty (title, category). Make sure the author field is hidden??and the authorized??user shows as an author when the entry is posted on the page.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>Edit Post form</td>
    <td>Check if the Edit Post form does collect the data in the correct way and display the error message when required fields are empty (title, category). Make sure the data of chosen??to edit post renders in the form fields.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>Detele Form</td>
    <td>Check if the Delete Form remove data from the database when submitted. Make sure, the User is redirected to the homepage after taking an action to submit.</td>
    <td>Pass</td>
  </tr>
      <tr>
    <td>Like/Unlike button</td>
    <td>Check if the button "like" is with no colour by default. Make sure it does toggle to colour when clicked. Check if the count adds 1 when button is clicked (colour) and subtract??1 when button is clicked again (no colour).</td>
    <td>Pass</td>
  </tr>
      <tr>
    <td>Comment Form</td>
    <td>Check if the Comment form does collect the data as required and send an error message when the required input fields (body, name) are empty. Make sure the comment does not appear on the page until Admin approves it.</td>
      <td>Pass</td>
  </tr>
      <tr>
    <td>Categories</td>
    <td>Check if categories filter the posts in the correct way and display for a user a list of posts from chosen categories in the new page.</td>
    <td>Pass</td>
  </tr>
      <tr>
    <td>Admin Panel</td>
    <td>Check if Admin: (1) can login into an admin panel and have access to the post, comment and categories models as well as to all registered Users, (2) can modify the data connected with those models, (3) can add/edit/delete a category, (4) can approve the comment, (5) can delete User.</td>
    <td>Pass</td>
  </tr>
        <tr>
    <td>URLs</td>
    <td>Make sure all url paths are connected in the correct way and the User is redirected after submitting any form into the correct view.</td>
    <td>Pass</td>
  </tr>
        <tr>
    <td>Messages</td>
    <td>Check if messages display in the top of the page as an alert when User submit form of creation, or editing post and adding the comment.</td>
    <td>Pass</td>
  </tr>
        <tr>
    <td>Error pages</td>
    <td>Check if error 404 and 500 display customised html pages.</td>
    <td>Pass</td>
  </tr>
          <tr>
    <td>Pages</td>
    <td>Check if all the pages display correct template and clear, easy to read view.</td>
    <td>Pass</td>
  </tr>
          <tr>
    <td>Footer</td>
    <td>Check if the links to social media accounts in the footer opens in the new tab.</td>
    <td>Pass</td>
  </tr>
</table>

<p align="right"><a href="#welcome">Bact to top</a></p>

### **W3C validator**
* **HTML Validator**

**Landing Page**
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-landingp.png?raw=true" alt="w3c-landing-page">
</p>

**Registration Page**
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-registration.png?raw=true" alt="w3c-registration">
</p>

**Login Page**
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-login.png?raw=true" alt="w3c-login">
</p>

**Post Detail Page**
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-postview.png?raw=true" alt="w3c-post-detail">
</p>

**Add Post Page**
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-add-post.png?raw=true" alt="w3c-add-post">
</p>

**Edit Post Page**
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-editpage.png?raw=true" alt="w3c-edit-post">
</p>

**Detete Post Page**
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-delete.png?raw=true" alt="w3c-delete-post">
</p>

**Add Comment Page**
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-add-comment.png?raw=true" alt="w3c-addcomment">
</p>

**MyPage - filered view of User posts**
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-mypage.png?raw=true" alt="w3c-mypage">
</p>

**Categories/List Page**
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-cat-list.png?raw=true" alt="w3c-cats/list">
</p>

**Categories/Filtered Posts Page**
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-categories.png?raw=true" alt="w3c-categories/page">
</p>

**Terms and Conditions Page**
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-terms.png?raw=true" alt="w3c-terms">
</p>

<br />
<hr>
<br />

* **W3C validator - CSS**
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/css_validator.png?raw=true" alt="w3c-css">
</p>

<p align="right"><a href="#welcome">Bact to top</a></p>
<br />

### **UNIT TESTING**
I have ran unit tests for forms, views and models:

The coverage raport for blog app:
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/blog-test-coverage-report.png?raw=true" alt="blog/coverage">
</p>

The coverage raport for members app:
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/coverage_members.png?raw=true" alt="members/coverage">
</p>

<p align="right"><a href="#welcome">Bact to top</a></p>

### **PEP8**
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-urls-empire.png?raw=true">empire_blog/urls.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-admin-blog.png?raw=true">blog/admin.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-views-blog.png?raw=true">blog/views.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-forms-blog.png?raw=true">blog/forms.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-models-blog.png?raw=true">blog/models.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-test-views-blog.png?raw=true">blog/test_views.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-test-urls-blog.png?raw=true">blog/test_urls.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-test-models.png?raw=true">blog/test_models</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-test-forms-blog.png?raw=true">blog/test_forms.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-forms-members.png?raw=true">members/forms.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-urls-members.png?raw=true">members/urls.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-test-forms-members.png?raw=true">members/test_forms.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-views-members.png?raw=true">members/views.py</a>

<p align="right"><a href="#welcome">Bact to top</a></p>
<br />

### **Lighthouse**
<br />

<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/lighthouse_desktop_home.png?raw=true" alt="lighthouse">
</p>


The tests were performed on:
- different browsers: Google Chrome, Firefox, Internet Explorer, Opera and Safari
- different devices: Samsung Galaxy S20+, Samsung Note 10+, iPhone 11, Lenovo TAB m10.

<p align="right"><a href="#welcome">Bact to top</a></p>
<hr>

## **ERRORS AND BUGS**
<br />

1. **Issue:**
CKEditor - Rich Text Editor has default size settings which overwrite the styling of the parent element.

**What did I try**
I have customised the toolbar and set the width/height to 100% in my setting.py file.

**Solution**
This solution is valid but is not sustainable. The width of the rich text editor depends on the amount of tools, which are included in the toolbar. So if we leave only 3 tools, the box will automatically change its width to very narrow. However, this solution is fully responsive and the toolbar wraps, when the screen width is smaller.
That may be problematic in terms of UX on the desktop as the width of the text editor is taking only a part of the screen and does not provide the full spectrum of experience it can possibly grant.
From other side, it is a question about how important is the desktop view in the case of social media app and whether it would be a good strategy to place the focus on this feature during the first realise or maybe turn the focus on the mobile devices design (following the agile scrum, the answer for this query can be find by measurements about the devices that have been chosen by the Users the most and applying the changes accordingly).

**Before**
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/text_editor_wrong.png?raw=true" alt="ck-edit-error">
</p>

**After**
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/text_editor_fixed.png?raw=true" alt="ck-edit-error">
</p>

<br />
<hr>
<br />

2. **Issue:**
Uncaught TypeError: Cannot read property *'appendChild'* of null.

<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/errors/js.png?raw=true" alt="iffe">
</p>

**Solution:**
In my base.html file I have added a JavaScript code which calls for an element *user.id*, however this element does not excist in the dom until the User will login into the page. While the application is loaded, the script is automatically looking for this element and through the error as it does not find it. I have applied an IFFE (more about it <a href="https://developer.mozilla.org/en-US/docs/Glossary/IIFE" target="_blank">here</a>)

<br />
<hr>
<br />

3. **Issue:**
Django Registration (User Creation) form comes by default with a bug, which is not a valid HTML.

<br />
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/errors/issues-html-1.png?raw=true" alt="error-html">
</p>

**What did I try**
1. At first I thought the error was caused by my own code, so I have checked all opening/closing tags and made sure the elements in my template were used correctly. That did not solve the problem.
2. I've tried to change the code from *{{ form.as_p }}* to *{{ form }}* but that did not resolve the issue.
3. I have tried to render the form using the crispy forms. That also did not solve the error.
4. I have tried to overwrite the form in my HTML template - by copying the boilerplate of original; django form and changing elements, that were causing the error (changing <*p*> tags which into the <*div*>), which solved the issue with HTML validator, but took away all the functionality which came as a part of the django form (like the error messages).


**Solution:**
I created a for loop which goes through the form elements and renders only the form field and the form label. That means, the help text added by default to the form (like the bullet points with password requirements) does not appear and it is the part that contains the HTML bug. However, the error messages were not displaying - just like in the attempt nr 4, which means approach nr 4 was also correct and could be used instead. In order to display the built-in registration form, django error messages, I added the variable *{{form.errors}}* to the registration html template, just below my form.That made the work, however it requires further improvements as currently the error message shows not only the error information but also the name of input field that was incorrect. For UX purposes, I would advise to render only the actual message.

<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/errors/registration-solved.png?raw=true" alt="solution-registration">
</p>

<br />
<hr>
<br />

4. **Issue:**
Django does not find static files when Debug is set to *False*.
That was an issue, which stood on the way of submitting this project on time and made it impossible to be rewarded with a higher grade I was aiming for, however I got to learn all about the connections that are made between several third party dependencies and different scenarios that can happen during the release process, which is a win by itself and surely it will be very useful in my further dev journey.

<br />

<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/errors/mime-type.png?raw=true" alt="error-devtools">
</p>

**What did I try**
<br/>
At first make sure you have run the collectstatic command in your CLI. Also, if you have set the config VAR in Heroku: *"DISABLE_COLLECTSTATIC = 1"*, you must remove this from the list.
I have also cleaned all the cache and cookies, but the problem remains.

I have tried multiple solutions I have found online. It seems that this issue has no clear answer and different solutions work in different cases. Below I paste the approaches I have taken before I finally found the solution that has worked in my case:

1. Remove the attribute *"rel=stylesheet"* from your css script. This is **NOT** a valid or adviced solution, even if that works because the browser may not read your css file as a stylesheet.

<p align="center">
<img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/errors/approach-1.png?raw=true" alt="approach1">
<br />

2. Change *"href"* to *"src"*. That solution did not work for me either and it does actually contain bad coding practice as the *"src"* is not a valid attribute for the link element so it is not adviced to use, even if that solves the problem.

<p align="center">
<img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/errors/approach2.png?raw=true" alt="approach2">
<br />

3. Add the *"css/text"* type to the mimetype variable in your *settings.py* file. It did not work. Some of the developers suggest turning off the mime checking in your django app, which is also a very bad programming practice.

<p align="center">
<img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/errors/approach3.png?raw=true" alt="approach3">
<br />

4. Add the URLs to the static files into your *urls.py* file. It seems to be a working solution in many cases, however it did not work in my case.

<p align="center">
<img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/errors/approach4.png?raw=true" alt="approach4">
<br />

5. Add the URL to your static files to the urls tupple - following the Django documentation:
<a href="https://docs.djangoproject.com/en/4.1/howto/static-files/">click here</a>.
This solution is also very common in terms of dealing with this problem, however it did not work in my case.

<p align="center">
<img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/errors/approach5.png?raw=true" alt="approach5">
<br />

6. Make sure your relative path is correct.
I have tried to change my relative path in every possible way: "/css/style.css", "./style.css", "css/style.css", "style.css", "/style.css" (and many more), as some of the older colleagues have suggested it is an issue with the incorrect path, which could indicate the 404 page when opening the link from the devtools, but we can also see that the path is correct taking into consideration my dirs:

<p align="center">
<img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/errors/404-css.png?raw=true" alt="404error">
<br />

7. Place the script to your css in the <*img*> element. I have to admit, it was out of desperation and it did not work - I would not advise to implement it into your code even if it does work as it is a very poor and incorrect dev practice.

<p align="center">
<img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/errors/approach6.png?raw=true" alt="approach6">
<br />


**Solution:**
Finally I have found the solution that had worked for me and it was installing the White Noise into my django app, which serves the static files as required. See:
<a href="http://whitenoise.evans.io/en/stable/">White Noice in Django</a>

<p align="center">
<img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/errors/solution.png?raw=true" alt="solution">
<br />
<br />
<p align="right"><a href="#welcome">Bact to top</a></p>