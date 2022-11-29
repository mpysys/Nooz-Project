
# Nooz - Testing 

[Main README.md file](/README.md)

[View live project](https://nooz-site.herokuapp.com/)

[View GitHub repository](https://github.com/mpysys/Nooz-Project)

***
## Table of contents
1. [Testing User Stories](#Testing-User-Stories)
2. [Manual Testing](#Manual-Testing)
3. [Automated Testing](#Automated-Testing) 
     - [Code Validation](#Code-Validation)
     - [Browser Validation](#Browser-Validation)
4. [User Testing](#User-Testing)


***

## Testing User Stories

#### User Stories:
1. As a **user**, I can **view a list of all posts/articles** so that **I can easily see if there is topic that I would like to view in more detail**.
  
    - The list of articles/posts appears as a 'newsfeed' on the home page.

2. As a **user** I can **click on an article/post to open it** so that **I can see all the detail**.
    
    - On each article snippet on the homepage is a brief overview of the article and its description, that when clicked, redirects the user to the article/post page where the user can see the article/post in full detail.

3. As a **user** I can **view the number of likes an article has** so that **I can have an idea of what people think about it before click to read more details**.

    - On the article/post snippet, the total number of likes of the article is displayed next to a thumb icon. The number of likes is also shown on the detailed article page.

4. As a **user** I can **view comments that other user's have made on an article/post** so that **I can see what others think of it**.

    - A comments section has been added to the detailed article/post pages, showing the author's username and the date/time the comment was left.

5. As a **user** I can **create my own account** so that **I can comment and like articles/posts**.

    - There is a sign in and sign up option, which advises the user on the landing page to log in to access certain content. The user will be required to be signed in to access protected content, such as the like and comment features.

6. As a **user** I can **navigate around the site** so that **I can choose the things I want to read**.

    - The navigation bar is visible at the top of every page and there are navigation links in the footer at the bottom of every page. 

7. As a **logged-in user** I can **submit my own articles/posts** so that **I can share them on the site too**.

    - If the user is logged in, they can navigate to the Add Post page and fill in the form to add their own post/article.  If they are not logged in, they are given the option to log in or register.

8. As a **logged-in user** I can **leave a comment on an article/post so that I can share my thoughts with other people**.

    - The field to leave a comment is at the bottom of the article detail page.  

9. As a **logged-in user** I can **like or unlike an article/post** so that **I can help other users to find out if an article/post is popular**.

    - If the user is logged in, the user will be able to like or remove their like from articles/posts. The number of likes is automatically incremented and the change is visible both on the article page and the article snippet on the home page.

10. As a **logged-in user** I can **click a button** so that **I can edit a post/article I have previously submitted**.

    - When a user is logged in, they will be able to see two linkson the article detail page if they are the author of the article.  Clicking the "Edit" link will take the user to the Edit article page where they can amend their article and re-submit it to the site. Logged in users will also be able to see this from the homepage for articles they wrote

11. As a **logged-in user** I can **click a button** so that **I can delete a post/article I have previously submitted**.

    - When a user is logged in, they will be able to see two links on the article detail page if they are the author of the recipe.  Clicking the "Delete" link will delete the user's recipe. Logged in users will also be able to see this from the homepage for articles they wrote

[Back to top](#Lettuce-Eat---Testing)

## Manual Testing

### Common Elements Testing
Manual testing was conducted on the following elements that appear on every page:

- Test that website works from different devices (pc/mac/ios/android)

- Test logged in versus logged out features

- Test emojis in articles, posts, comments & categories
- Test that Logo redirects to home screen.

- Test that Nav Links work.

- Test that Footer Links work.

- Test that Social Links work and open in a new page.

### Home Page
Manual testing was conducted on the following elements of the [Home Page](https://nooz-site.herokuapp.com/):
     
- Test that logged in user interface displays username.

- Test user profile updates & settings

- Test image uploads 

### Article Page/Edit Article Page
Manual testing was conducted on the following elements of the [Recipe Page](https://nooz-site.herokuapp.com/post/24) and [Edit Recipe Page](https://nooz-site.herokuapp.com/post/24):

- Test that article can be edited by author only.

- Test that article can only be deleted by author.

- Test that a warning is given before a user deletes an article.
     
- Test that articles can be liked and unliked when logged in, from newsfeed and article detail page.
     
- Test that comments can be submitted.

### New Post Page
Manual testing was conducted on the following elements of the [Add Recipe Page](https://nooz-site.herokuapp.com/new_post/):

- Test that articles create unique primary key.
     
- Test that articles are saved.

- Test that users can see new posts.
     
### Sign in/Sign Out/Sign Up Pages
Manual testing was conducted on the following elements of the [Sign In Page](https://nooz-site.herokuapp.com/subs/login/), [Sign Out Page](https://nooz-site.herokuapp.com/subs/logout/) and [Sign Up Page](https://nooz-site.herokuapp.com/subs/register/):

- Users can register, log in and logout.

### Pages are Responsive
- Manual testing was conducted for responsiveness on large, medium and small screens.

[Back to top](#Nooz---Testing)

## Automated Testing

### Code Validation
The [W3C Markup Validator](https://validator.w3.org/ "Link to M£C Markup Validator Site") service was used to validate the `HTML` and `CSS` code used. The [PEP8 Python Validator](http://pep8online.com/ "Link to the PEP8 Python Validator Site") was used to validate the `Python` code used.

**Results:**

- HTML Pages - Code Validation

HTML validation - all pages clear.

- CSS stylesheet - Code Validation

CSS tested clear.

- Python Files - Code Validation

**Files tested**

nooz - urls.py

nooz - settings.py

nooz2 - admin.py

nooz2 - forms.py

nooz2 - models.py

nooz2 - urls.py

nooz2 - views.py

All files tested clear.

### Browser Validation
- Chrome
- Edge
- Opera
- Firefox

## User testing 
My group of friends were asked to review the site and documentation to point out any bugs and/or user experience issues. Their helpful advice throughout the process led to a few small UX changes in order to create a better experience. 

[Back to top ⇧](#Nooz---Testing)

***