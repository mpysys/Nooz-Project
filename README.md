

# Nooz

![Nooz ](static/images/background_image.jpg 'Shows responsive views of site')

[View the live project here](https://nooz-site.herokuapp.com/ "Link to deployed site - Nooz")

## Table of contents
1. [Introduction](#Introduction)
2. [UX](#UX)
    1. [User Stories](#User-Stories)
    2. [Development Planes](#Development-Planes)
    3. [Design](#Design)
3. [Features](#Features)
    1. [Design Features](#Design-Features) 
    2. [Existing Features](#Existing-Features)
    3. [Features to Implement in the future](#Features-to-Implement-in-the-future)
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
     1. [Main Languages Used](#Main-Languages-Used)
     2. [Additional Languages Used](#Additional-Languages-Used)
     3. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
6. [Testing](#Testing)
     1. [Testing.md](TESTING.md)
7. [Deployment](#Deployment)
     1. [Deploying on Heroku](#Deploying-on-Heroku)
     2. [Forking the Repository](#Forking-the-Repository)
     3. [Creating a Clone](#Creating-a-Clone)
8. [Credits](#Credits)
     1. [Content](#Content)
     2. [Media](#Media)
     3. [Code](#Code)
9. [Acknowledgements](#Acknowledgements)
***

## Introduction

This is the 4th Portfolio project that is needed to complete the FSSD program with Code Institute.

Due to unforseen circumstances in real life (direct family member in hospital, Meta layoffs...) I had to pivot from the initial project I wanted to build to something much simpler, while meeting expectations of the module.

Throughout the project I was using Agile methodologies to plan my project and building iteratively. Once I had made the decision to restart, I followed the Django Blog tutorial from my Code Institute course, adapated it to my needs, was able to execute in a much more efficient way. 

Portfolio Project 4 requires students to build a Full Stack website based on business logics using CRUD. In order to do so, creating an authentication system is mandatory.

My project is a simple news site where registered users can post, comment, edit and delete articles.  Users that are not logged in have only read capabilities.

[Back to top ⇧](#Lettuce-Eat)

## UX 

### User Stories
#### Users:
1.  As a **user**, I can **view a list of articles/posts chronologically** so that **I can easily see if there is an article I would like to view in more detail**.

2.  As a **user** I can **click on an article/post to open it** so that **I can see the actual content and comments on the article/post**.

3.  As a **user** I can **view the number of likes an article/post has** so that **I can have an idea of what people think about it before I read it**.

4.  As a **user** I can **view comments that other user's have made about an article/post** so that **I can see what others think of it and maybe pick up some ideas or advice**.

5.  As a **user** I can **create my own account** so that **I can create, edit, delete, comment and like articles/posts**.

6.  As a **user** I can **navigate around the site** so that **I can choose the things I want to read**.  

7. As a **user** I can **view the articles/posts according to their categories** so that **I can easily filter topics I care about**.

8. As a **logged-in user** I can **add my own categories** so that **I can enable articles/posts to have more accurate categories assigned**.

9.  As a **logged-in user** I can **add my own articles/posts** so that **I can share them on the site too**.

10.  As a **logged-in user** I can **leave a comment on an article/post so that I can share my thoughts with other people**.

11.  As a **logged-in user** I can **like or unlike an article/post** so that **I can help other users to find out if the article/post is popular**.

12. As a **logged-in user** I can **click a button** so that **I can edit an article/post I have previously added**.

13. As a **logged-in user** I can **click a button** so that **I can delete an article/post I have previously added**.

#### Site Admin:
1. As a **Site Admin**, I can **create, read, update and delete articles** so that **I can manage my site content**.


### Development Planes
To create a comprehensive and appealing website, I took inspiration from various news apps that focused on newsfeeds to discover functionality and features that would be needed enabling me to build the user stories above.

#### Strategy
Broken into three categories, the website will attempt to focus on the following target audiences:
- **Roles:**
     - Logged out User
     - Logged in User
     - Admin

- **Demographic:**
     - News hungry users
     - People looking for a community to share and learn
     - Gaming, Tech, Business, Sports, Travel afficionados
     - People who are curious news and trends

- **Psychographics:**
     - Personality & Attitudes:
        - Curious
	    - Vocal

     - Values:
        - Sharing is caring
     - Lifestyles:
        - Anyone interested in topics and current media

The website needs to enable the **user** to:
- See the most recent articles/posts.
- Filter articles/posts by category
- register and log in to enable them to post, edit, delete and comment on articles/posts.
- comment on and like articles/posts.

The website needs to enable the **admin** to:
- Delete & Edit anything on the platform from the admin panel

With the user stories in mind, I did a prioritization exercise which enabled me to prioritize my work:

![Strategy Table](static/site_images/readme/strategy.png 'Strategy Table')

#### Scope
As per the projects requirements, I had to ensure what would be in scope vs. what wouldn't be. In order to do so, I identified the content and functionality requirements as mentioned below:
- **Content Requirements**
     - The user will be looking for:
        - a list of articles/posts.
	    - a list of categories.
	    - a list of comments on each articles/post.
	    - a visual representation of how many people liked the articles/posts

- **Functionality Requirements**
     - The user will be able to:
        - Easily navigate the site to find recent articles/posts.
	    - Be able to select categories and view relevant articles/posts.
	    - Comment on and like articles/posts.

#### Structure
Once the scope was established, I made a visual representation of the user journey:
![Site Map structure](static/readme/journey.png 'User Journey')

#### Skeleton 
Wireframe mockups were created using [Balsamiq](https://balsamiq.com/ 'Balsamiq Website').

Landing Page:
![Home Page Wireframe](static/readme/loggedout.png 'Landing Page - Wireframe')

Home Page:
![About Page Wireframe](static/readme/loggedin.png 'Home Page - Wireframe')

Article/Post Page:
![Recipe Page Wireframe](static/readme/postdetail.png 'Article/Post Page - Wireframe')


### Design

#### Colour Scheme
I leveraged [Color Palette](https://colordesigner.io/ 'Color Palette website') to help choose a color scheme on the back of a background image I chose that worked with the Logo.  I wanted the website to look fresh and focus on the content, not on anything else.

The white background allows the navigation to be obvious and the article newsfeed to be the center piece.

#### Logo
The NOOZ logo was made with Paint by editing the background image (taken from https://stock.adobe.com/) and using the infinity symbol to represent the endless stream of content. 

#### Typography

The main font of the website is Oswald, which has been used everywhere due to it's simple design.  Oswald is a popular, versatile font and it ensures that the most important information on the site is readable.

It was chosen from [Google Fonts](https://fonts.google.com/ 'Google Fonts website')

#### Imagery
The only image we have on the site other than ones uploaded by users is on the landing page when users are either logged out or do not have an account. The idea of this image is to highlight the name of the site/brand to any new comer - to dinstinctly show the user where they are.

The Background Image is from [Adobe Stock](https://stock.adobe.com/ 'Adobe Stock website').


[Back to top ⇧](#Nooz)

## Features

### Design Features
Each page of the website features a consistent responsive navigational system:

- The **Header** contains a conventionally placed logo in the top left of the page (whereby clicking this will redirect users back to the home page) and a navigation bar also starting on the left after the logo. On smaller screens, the navigation bar condenses into a dropdown with navigation options.  

- The **Header Image** on the home page, emphasizes the name of the website and welcomes the user with text

- **Logged in user dropdown** - a dropdown opens in the top right corner when clicking on the users username, enabling them to access an settings, view profile page, edit profile page and log out

- The **Footer** is intentionally simple in order to complement the clean simplicity of the rest of the site.  Clicking on the "By Morgan Monnet" will redirect Morgan Monnet's Github repository. There are also 4 social media links (twitter, reddit, instagram, facebook) that will redirect to the website creators related links
 
### Existing Features
- **Header Logo** - Appearing on every page for brand recognition. Clicking the logo will return the users to the home page, as expected.
- **Header Navigation Bar** - Appearing on every page for a consistently easy and intuitive navigable system.
- **Header Image** - Appears on the home page, by way of an introduction to the theme of the site.
- **Social Icons** - Appearing on every page in the footer, the icons are appropriate representations of the Social Media platforms.
- **Article/post snippets** - Appearing on the home page, the snippets give a brief overview of the article, showing the user profile picture, user who posted, date of posting, title and description of the article/post as well as the category and the number of likes of the article.
- **Add Post/Article form** - Appearing on the add a post page and edit recipe page, the form allows the user to add or edit an article, including adding an image to display, a description and the body.
- **Comment Form** - Appearing on the article/post page, the form submits the user's comment and redirects the user to the article page with the comments up to date.
- **Comments Section** - Appearing on the article page, comments are displayed showing the author's username and the date and time of submission.
- **Like/Unlike Button** - Appearing on the article/post page when the user is logged in, the button allows the user to like or unlike an article/post. If the user is not logged in, they will simply see the number of likes on the page but will be prompted to sign in.
- **Home Page** - A home page that shows the user the site's newsfeed, showcasing a chronological list of articles/posts. In addition, if the user is logged out, a welcome message appears on the landing page a sign in & register button, prompting the user to log in.
- **Categories Page** - A Category page that shows all relevant articles/posts according to the selected category. Users can also click on the category tag on the newsfeed that is at the bottom of each article snippet to filter.
- **Article/Post Detail Page** - An article page whose content changes with the article details of the specified article. Includes features to like and comment as well as edit or delete.
- **Edit/Delete Article/Post Page** - A page designed to allow the user to edit/delete an article if logged in, as long as they are the author.
- **Sign In Page** - A page designed to allow the user to log in using previously created user details; a username and a password.
- **Sign Up Page** - A page designed to allow the user to create a user profile using a username, first name and last name, email and a password that needs to be repeated to ensure it is correct.
- **Settings** - A page designed to allow the user to edit their username, first name, last name and email. They can also reset their password in the 'this form' link.
- **Password Reset Form** - A page designed to help the user reset their password by inputting their old password as well as the new password and verifying it.
- **View/Profile Page** - A page designed to show the user their own profile page, this page is the same as other users profile pages that all users can see. This card contains the image, the biography and the link to social media accounts of said user.
-**Edit Profile** - A page designed to allow the user to edit their bio, profile pic, site and social media urls.



### Features to Implement in the future
- **Like from Newsfeed**
     - **Feature** - This feature would enable the user to click the like button from the newsfeed
     - **Reason for not featuring in this release** - The reason for not releasing this feature was that I ran out of time to implement the feature before the project's due date. This will be developed further in the future after grading is complete.
- **Sharing Urls and formatting posts automatically**
     - **Feature** - This feature would enable users to simply post an image and this would pull the title, tag, description, header image and body from the source and formatting it directly as per the articles format
     - **Reason for not featuring in this release** - I would need to figure out a way to create a browser plug in or learn more about crawling websites on the back of links to pull relevant information
- **Follower system**
     - **Feature** - This feature would create a follower/following system
     - **Reason for not featuring in this release** - I needed to prioritize the development for an MVP, I had to deprioritize this feature.
     -**Follower feed**
     - **Feature** - This feature would user the follower/following system to showcase a newsfeed of only what you are following to hyper customize the feed.
     - **Reason for not featuring in this release** - I needed to prioritize the development for an MVP, I had to deprioritize this feature.
- **Search Articles**
     - **Feature** - This feature would have allowed users to search articles, either by typing keywords.
     - **Reason for not featuring in this release** - Once again, I ran out of time to implement this feature before the project's due date. This will also be developed further in the future after grading is complete.


 
[Back to top ⇧](#Nooz)

## Issues and Bugs 

**Bug** - I intially worked with Django-Ckeditor to use its Rich Text Editor but once i deployed on Heroku with Cloudinary, I was running into various issues that I tried debugging. I tried various collectstatic options (hashed/unhashed) but could not get the editor to work optimally. Without the Rich Text Editor, the articles/posts would appear as an unformatted. 
- ***Solution***: I looked at alternative solutions like Summernote, but that would have required a lot of changes throughout the code. In the end I simply removed the RichTextEditor and left it as a TextField. 

**Bug** - When deploying to Heroku near the end of the project, having not deployed since my initial deployment, I found that the static files were not coming through even though I could see that they were there in my Cloudinary console.
- ***Solution***: I spent rather a long time talking to Tutor Support, I renamed images, I deleted everything out of Cloudinary.  We tried a lot of things.  In the end, I uploaded everything unhashed, which helped

**Issue** - I discovered that if a user puts Emoji's as the name of a new category (in add category) that the whole site comes down and fields a 500 error. Unfortunately this is not something I was able to rectify and as such was left in the code. 


[Back to top ⇧](#Nooz)

## Technologies Used
### Main Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to Python Wiki")
     - Used to implement Django functionality, including building models, forms and views for the app (CRUD).

### Additional Languages Used
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")
     - Used to get and replace Elements from HTML


### Frameworks, Libraries & Programs Used
- [Django](https://www.djangoproject.com/ "Link to Django Project website")
    - Django was used to build the models, forms and views of the app, and was the backbone of this project.
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/ "Link to Bootstrap page")
     - Bootstrap was used to implement the responsiveness of the site, using bootstrap classes.
- [Cloudinary](https://cloudinary.com/ "Link to Cloudinary page")
     - Cloudinary was used as free cloud storage for images uploaded to the site through the recipe forms.
- [Ckeditor](https://ckeditor.com/ "Link to Ckeditor page")
     - Ckeditor was used to allow users to add styling when adding a text editor to site. 
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")
    - Google fonts were used to import the fonts "Poppins" and "Dancing Script" into the style.css file. These fonts were used throughout the project.
- [Font Awesome](https://fontawesome.com/ "Link to FontAwesome")
     - Font Awesome was used on all pages throughout the website to import icons (e.g. social media icons) for UX purposes.
- [Git](https://git-scm.com/ "Link to Git homepage")
     - Git was used for version control by utilizing the GitPod terminal to commit to Git and push to GitHub.
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project after pushing
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
     - Am I Responsive was used to see responsive design throughout the process and to generate mockup imagery to be used.

[Back to top ⇧](#Nooz)

## Testing

Testing information can be found in a separate [testing file](TESTING.md "Link to testing file").

## Deployment

This project was developed using a [GitPod](https://gitpod.io/ "Link to GitPod") workspace. The code was commited to [Git](https://github.com/mpysys "Link to Git") and pushed to [GitHub](https://github.com/ "Link to GitHub") using the terminal.

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Attach the Postgres database:
    - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

3. Prepare the environment and settings.py file:
    - In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    - In your GitPod workspace, create an env.py file in the main directory. 
    - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    - Add the SECRET_KEY value to the Config Vars in Heroku.
    - Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    - Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
    - In settings.py add the following sections:
        - Cloudinary to the INSTALLED_APPS list
        - STATICFILE_STORAGE
        - STATICFILES_DIRS
        - STATIC_ROOT
        - MEDIA_URL
        - DEFAULT_FILE_STORAGE
        - TEMPLATES_DIR
        - Update DIRS in TEMPLATES with TEMPLATES_DIR
        - Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

4. Store Static and Media files in Cloudinary and Deploy to Heroku:
    - Create three directories in the main directory; media, storage and templates.
    - Create a file named "Procfile" in the main directory and add the following:
        - web: gunicorn nooz.wsgi
    - **git push heroku main** and your app will be deployed to Heroku.


## Credits 

### Content
- Most recipes were taken from [BBC GoodFood](https://www.bbcgoodfood.com/ "Link BBC GoodFood website")'. 

### Media
- The images have been sourced from [Adobe Stock](https://stock.adobe.com/).

### Code 
References used:
- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page")
- [Colorlib](https://colorlib.com/ "Link to Colorlib page")
- [Django Docs](https://docs.djangoproject.com/ "Link to Django's Docs")
- [Github](https://github.com/ "Link to Github")

### Other
- [Codemy](https://www.youtube.com/@Codemycom "Link to Codemy Youtube")
- [Coding Entrepreneurs](https://www.youtube.com/@CodingEntrepreneurs "Link to Coding Entrepreneurs")

[Back to top ⇧](#Nooz)

## Acknowledgements

- Thanks also to Code Institute's Tutor Support (Oisin) who helped me get the site deployed correctly over many hours.
- Finally, I would like to thank the student support center as these past 6 months have been really challenging personally and they've given me the space the execute at my pace.

[Back to top ⇧](#Nooz)

***