# Full Stack Toolkit: "Empire of Thoughts" Portfolio Project - TESTING

<p id="welcome"></p>

### MANUAL TESTING
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
    <td>Check if the login form allows User who had created his account correctly - to access the home page for authorised users after providing the correct login credentials.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>Add Post form</td>
    <td>Check if the Add Post form does collect the data in the correct way and display the error message when required fields are empty (title, category). Make sure the author field is hidden and the authorized user shows as an author when the entry is posted on the page.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>Edit Post form</td>
    <td>Check if the Edit Post form does collect the data in the correct way and display the error message when required fields are empty (title, category). Make sure the data of chosen to edit post renders in the form fields.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>Detele Form</td>
    <td>Check if the Delete Form removed data from the database when submitted. Make sure, the User is redirected to the homepage after taking an action to submit.</td>
    <td>Pass</td>
  </tr>
      <tr>
    <td>Like/Unlike button</td>
    <td>Check if the button "like" is with no colour by default. Make sure it does toggle to colour when clicked. Check if the count adds 1 when button is clicked (colour) and subtract 1 when button is clicked again (no colour)..</td>
    <td>Pass</td>
  </tr>
      <tr>
    <td>Comment Form</td>
    <td>Check if the Comment form does collect the data as required and send an error message when the required input fields (all) are empty. Make sure the comment does not appear on the page until Admin approves it.</td>
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
    <td>Check if messages display in the top of the page as an alert when User submit form of creation, editing or deleting post / comment (User can only add the comment)</td>
    <td>Pass</td>
  </tr>
        <tr>
    <td>Error pages</td>
    <td>Check if error 404 and 500 display customised html pages.</td>
    <td>Pass</td>
  </tr>
          <tr>
    <td>Pages</td>
    <td>Check if all the pages display correct view and clear, easy to read view.</td>
    <td>Pass</td>
  </tr>
          <tr>
    <td>Footer</td>
    <td>Check if the links to social media accounts in the footer opens in the new tab.</td>
    <td>Pass</td>
  </tr>
</table>


### W3C validator - HTML:
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-landingp.png?raw=true">Landing Page</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-registration.png?raw=true">Registration Page</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-login.png?raw=true">Login Page</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-postview.png?raw=true">Detail Post View Page</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-add-post.png?raw=true">Add Post Page</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-editpage.png?raw=true">Edit Post Page</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-delete.png?raw=true">Delete Post Page</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-add-comment.png?raw=true">Add Comment Page</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-mypage.png?raw=true">MyPage - filered view of User posts</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-cat-list.png?raw=true">Categories/List Page</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-categories.png?raw=true">Categories/Filtered Posts Page</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/valid-html-terms.png?raw=true">Terms and conditions page</a>

## W3C validator - CSS
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/css_validator.png?raw=true">W3C validator for CSS</a>

### UNIT TESTING
I have ran unit tests for forms, views and models:

The coverage raport for blog app:
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/blog-test-coverage-report.png?raw=true" alt="blog/coverage">
</p>

The coverage raport for members app:
<p align="center">
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/coverage_members.png?raw=true" alt="members/coverage">
</p>


## PEP8
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
- <a href="">here</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-test-forms-members.png?raw=true">members/test_forms.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-views-members.png?raw=true">members/views.py</a>


## LIGHTHOUSE



The tests were performed on:
- different browsers: Google Chrome, Firefox, Internet Explorer, Opera and Safari
- different devices: Samsung Galaxy S20+, Samsung Note 10+, iPhone 11, Lenovo TAB m10.
