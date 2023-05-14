# Project 5 - Prestige|Watches Full Stack Web Developer Ecommerce Project

## Table of content

+ Validation Testing 
    + HTML
        + [NU-HTML-CHECKER](#html-testing-using-nu-html-checker)
    + CSS
        + [W3-JIGSAW.ORG](#css-validator-using-jigsaww3)
    + Javascript 
        + [JShint](#javascript--jquery-using-jshint)
    + Python Pep8 Online Checker
        + Bag App - [Bag App](#bag-app)
        + Checkout App - [Checkout App](#checkout-app)
        + Blog App - [Blog App](#blog-app)
        + Contact Us App - [Contact Us App](#contact-us-app)
        + Home App - [Home App](#home-app)
        + Newsletter App - [Newsletter App](#newsletter-app)
        + Prestige_Watches App - [Main App](#prestige_watches-app)
        + Product App - [Product App](#product-app)
        + Profiles App - [Profiles App](#profile-app)
        + Reviews App - [Reviews App](#reviews-app)
        + Manage.py - [Manage.py](#manage.py) 
+ [Lighthouse Testing](#lighthouse-testing)
+ [Browser Testing](#browser-testing)
+ [Device Testing](#device-testing)
+ [Manual Testing](#manual-testing)
    + [Home Page](#home-page)
    + [Product Page and Bag Page](#product-page--bag-page)
    + [Checkout Page](#checkout-page)
    + [Join Our Blog Page](#join-our-blog)
    + [Contact Us Page](#contact-us-page)
    + [Reviews Page](#reviews-page)
    + [Profile Page](#profile-page)
    + [404 Error Page](#404-error-page)
    + [Login Page](#login-page)
    + [Register Page](#register-page)
    + [Logout Page](#logout)
    + [Django Admin Page](#admin-page)

+ [Automated Testing](#automated-testing)

+ [Bugs](#bugs)
    + [Fixed Bugs](#fixed-bugs)
    + [Unfixed Bugs](#unfixed-bugs)

## Testing & Validation Checks 

## HTML Testing using NU-HTML-CHECKER

+ Testing Mode - No Warnings and Errors

<img src="docs/test-images/nu-html1.png" alt = "Nu HTML Checker" style="height:280px; width: 100%;">

+ Deployed Mode - No Warnings and Errors

<img src="docs/test-images/nu-html2.png" alt = "Nu HTML Checker" style="height:280px; width: 100%;">

All my pages was checked via nu-html-checker, initally i got 25 errors, mostly due to unclosed div tags or stray tags, these were quickly rectified and the code was rechecked and recieved no errors or warnings. The main error I had was a marquee tag I used for the banner, the marquee is no longer a valid tag and so I had to remove it and change this over. 

## CSS Validator using JIGSAW.W3

+ Base CSS checker by direct input - Found no errors
<img src="docs/test-images/css-validator.png" alt = "CSS Validator" style="height:220px; width: 100%;">

+ Checkout CSS checker by direct input - Found no errors
<img src="docs/test-images/css-validator2.png" alt = "CSS Validator" style="height:220px; width: 100%;">

+ Full deployed site - Found no errors
<img src="docs/test-images/css-validator3.png" alt = "CSS Validator" style="height:220px; width: 100%;">

## Javascript & JQuery using JSHINT

All my check for Javascript and JQuery was checked using JShint. I received no errors or warning at the time of checking the code. The code was checked by pasting in the relevant scripts in to Jshint and checking for errors. 

+ Jshint Validator
<img src="docs/test-images/jshint1.png" alt = "Jshint" style="height:280px; width: 100%;">

<img src="docs/test-images/jshint2.png" alt = "Jshint" style="height:280px; width: 100%;">

<img src="docs/test-images/jshint3.png" alt = "Jshint" style="height:280px; width: 100%;">

<img src="docs/test-images/jshint4.png" alt = "Jshint" style="height:250px; width: 100%;">

## Python - PEP8 Online checker (Code Institute Version)

All code was checked via the CI Python Linter, all code received no errors and warnings. 

### Bag App

+ For the bag app the CI Python Linter was used to check the python code, for the following files Urls.py, Context.py and Views.py.

<img src="docs/test-images/bag_urls.png" alt = "Python" style="height:250px; width: 100%;">

<img src="docs/test-images/bag_context.png" alt = "Python" style="height:250px; width: 100%;">

<img src="docs/test-images/bag_views.png" alt = "Python" style="height:250px; width: 100%;">

### Checkout App

+ For the checkout app the CI Python Linter was used to check the python code, for the following files Urls.py, Context.py, signals, admin, webhooks and views.

<img src="docs/test-images/checkout_url.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/checkout_form.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/checkout_signal.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/checkout_views.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/checkout_webhook_handler.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/checkout_webhook.png" alt = "Python" style="height:260px; width: 100%;">

### Blog App

+ For the blog app the CI Python Linter was used to check the python code, for the following files Urls.py, signals, widget, admin and views.

<img src="docs/test-images/blog_admin.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/blog_form.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/blog_models.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/blog_url.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/blog_view.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/blog_widget.png" alt = "Python" style="height:260px; width: 100%;">

### Contact Us App

+ For the contact us app the CI Python Linter was used to check the python code, for the following files Urls.py, signals, widget, admin and views.

<img src="docs/test-images/contact_form.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/contact_admin.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/contact_model.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/contact_views.png" alt = "Python" style="height:260px; width: 100%;">

### Home App

+ For the home app the CI Python Linter was used to check the python code, for the following files Urls.py and Views.py.

<img src="docs/test-images/home_views.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/home_url.png" alt = "Python" style="height:260px; width: 100%;">

### Newsletter App 

+ For the newsletter app the CI Python Linter was used to check the python code, for the following files Urls.py and Views.py.

<img src="docs/test-images/newsletter_view.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/newsletter_url.png" alt = "Python" style="height:260px; width: 100%;">

### Prestige_Watches App (Main)

+ For the main app the CI Python Linter was used to check the python code, for the following files setting, Urls.py and views.

<img src="docs/test-images/main_setting.png" alt = "Python" style="height:260px; width: 100%;">

+ I had few errors/warnings on the settings.py which displayed that some lines were too long, however after getting confirmation from Tutor Support, I was advised these can be left alone, as these were on not to be edited as they were involved with the django auth_password validators. 

<img src="docs/test-images/main_url.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/main_view.png" alt = "Python" style="height:260px; width: 100%;">

### Product App
+ For the main app the CI Python Linter was used to check the python code, for the following files admin, forms, models, urls, views and widgets.

<img src="docs/test-images/product_admin.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/product_form.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/product_model.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/product_url.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/product_views.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/product_widgets.png" alt = "Python" style="height:260px; width: 100%;">

### Profiles App
+ For the main app the CI Python Linter was used to check the python code, for the following files admin, forms, models, urls and views.

<img src="docs/test-images/profile_form.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/profile_model.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/profile_url.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/profile_views.png" alt = "Python" style="height:260px; width: 100%;">

### Reviews App
+ For the main app the CI Python Linter was used to check the python code, for the following files admin, forms, models, urls and views.

<img src="docs/test-images/reviews_admin.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/reviews_form.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/reviews_model.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/reviews_url.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/reviews_views.png" alt = "Python" style="height:260px; width: 100%;">

<img src="docs/test-images/reviews_widgets.png" alt = "Python" style="height:260px; width: 100%;">


### Manage.py
+ The manage.py was also checked using the CI Python Linter.

<img src="docs/test-images/manage.py.png" alt = "Python" style="height:260px; width: 100%;">

## Lighthouse Testing

Lighthouse was used to test Performance, Best Practices, Accessibility and SEO on Desktop.

<img src="docs/test-images/lighthouse.png" alt = "Testing" style="height:400px; width: 100%;">

+ Some imporovements could of have been done, to make the score reach the high 90's, images sizes was the main factor with why the scores were quite low. These can be changed to have all the same class, which would improve the scores.

## Browser Testing
The project was tested extensively on Google Chrome and Safari browsers, where no browser compatibility issues came up.

## Device Testing
The project was tested on a multitude of devices: several iPhones, android phones, linux laptops and Macbook Pro. The website was properly responsive on all devices.

## Manual Testing
### Home Page 
Manual Testing was carried out throughout the site to check the whether the site met the requirements of the expected results below. 

| Element                    | Location       | Action          | Expected Result               | Pass/Fail |
| -------------------------- | -------------- | --------------- | ----------------------------- | --------- |
| Site Logo                  | Navigation Bar | Click           | Redirect to home page         | Pass      |
| Header Text                | Navigation Bar | Click           | Redirect to home page         | Pass      |
| Search bar                 | Navigation Bar | Click + Search  | Product item is searched      | Pass      |
| My Account - Logout Mode   | Navigation Bar | Click + Display | Display Login & Register      | Pass      |
| Checkout basket            | Navigation Bar | Click + Display | Display £0.00, direct to bag page | Pass      |
| All Product Links          | Navigation Bar | Click + Display | Scroll down display options and direct user to directed searches         | Pass      |
| Special Offer Links        | Navigation Bar | Click + Display | Scroll down display options and direct user to directed searches         | Pass      |
| Join our Blog              | Navigation Bar | Click + Display | Direct user to blog page      | Pass      |
| Help Links                 | Navigation Bar | Click + Display | Scroll down display options and direct user to directed pages           | Pass      |
| My Account - Login Mode    | Navigation Bar | Click + Display | Display Logout, Add Review and My Profile              | Pass      |
| Shop Now Button            | Navigation Bar | Click + Display | Direct user to All Products   | Pass      |

<img src="docs/test-images/home.site.png" alt = "Testing" style="height:400px; width: 100%;">

### Product Page & Bag Page
Manual Testing was carried out throughout the site to check the whether the site met the requirements of the expected results below.

| Element                    | Location       | Action          | Expected Result                                                    | Pass/Fail |
| -------------------------- | -------------- | --------------- | -------------------------------------------------------------------| --------- |
| Product Count              | Product Page   | Display         | Product Count to display total amount of product loaded on site    | Pass      |
| Sort By Filter             | Product Page   | Click + Display | Filter by Price, Name, Category ascending and descending order     | Pass      |
| Products                   | Product Page   | Display         | Display product image, name, price, gender, rating and brand       | Pass      |
| Products Display           | Product Page   | Display         | Display 4 products on each line                                    | Pass      |
| Product Detail Display     | Product detail | Display         | Display product image, name, price, gender, rating, brand, description, features, qty, keep shopping & add to bag button | Pass      |
| Keep Shopping Button       | Product detail | Click + Direct  | Click keep shopping button redirects user to products page         | Pass      |
| Add to bag button          | Product detail | Click + Display | Success Message, Mini checkout screen display with image and cost  | Pass      |
| Add to bag button          | Product detail | Click + Display | Item added to shopping basket, basket updated with new cost        | Pass      |
| Add to bag button          | Product detail | Click + Display | If order over £1000 user given free delivery                       | Pass      |
| Quantity                   | Product detail | Click + Display | Qty increment working + = increase - = decrease qty                | Pass      |
| Go to checkout button      | Product detail | Click + Display | Button taken user to bag page, display order details & costings    | Pass      |

<img src="docs/test-images/testing1.png" alt = "Testing" style="height:400px; width: 100%;">

### Checkout Page
Manual Testing was carried out throughout the site to check the whether the site met the requirements of the expected results below.

| Element                    | Location       | Action          | Expected Result                                                    | Pass/Fail |
| -------------------------- | -------------- | --------------- | -------------------------------------------------------------------| --------- |
| Checkout Page              | Checkout Page  | Display         | Order details and totals, a form to show customer details and card information| Pass      |
| First Name Field           | Checkout Page  | Display & Fill  | If field not completed then directed to field to be filled         | Pass      |
| Email Field                | Checkout Page  | Display & Fill  | If field not completed then directed to field to be filled         | Pass      |
| Delivery Field             | Checkout Page  | Display & Fill  | If field not completed then directed to field to be filled         | Pass      |
| Card Field                 | Checkout Page  | Display & Fill  | If field not completed or entered incorrectly the field is rejected and directed to field to be re-filled         | Pass      |
| Complete Order Button      | Checkout Page   | Click + Direct | Click complete order button redirects user to checkout success     | Pass      |
| Checkout Success           | Checkout success| Display        | Success Message and form showing users completed order             | Pass      |
| Checkout out offers button | Checkout success| Click + Direct | Direct the user to the product special offer page                  | Pass      |
| Order sent to user email   | Checkout success| Form Sent      | Order confirmation sent to the user via email                      | Pass      |
| Order saved in Admin       | Admin           | Form Sent      | Order send to admin panel                                          | Pass      |

<img src="docs/test-images/checkout_success.png" alt = "Testing" style="height:400px; width: 100%;">

### Join Our Blog
Manual Testing was carried out throughout the site to check the whether the site met the requirements of the expected results below.

| Element                    | Location       | Action          | Expected Result                                                    | Pass/Fail |
| -------------------------- | -------------- | --------------- | -------------------------------------------------------------------| --------- |
| Join our blog page         | Blog Page      | Display         | Display blog post from admin                                       | Pass      |
| Features                   | Blog Page      | Display         | Display blog title, header, date, time, author and like icon       | Pass      |
| Blog                       | Post Blog      | Click + Direct  | When clicked user is direct to blog                                | Pass      |
| Post Blog                  | Post Blog      | Display         | Display blog, date, time created on, author, likes and description of blog.    | Pass      |
| Product Detail Display     | Product detail | Display         | Display product image, name, price, gender, rating, brand, description, features, qty, keep shopping & add to bag button | Pass      |
| Blog Home Page button      | Post Blog      | Click + Direct  | When clicked user is direct to blog                                | Pass      |
| User Logged Out Mode       | Post Blog      | Display         | Unable to comment or like blogs and comments. Request user to login| Pass      |
| User Logged In Mode        | Post Blog      | Click + Login   | User able to like comments and blogs, user able to write comments  | Pass      |
| Login Button               | Post Blog      | Click + Direct  | User redirected to sign in page                                    | Pass      |
| Comments                   | Post Blog      | Display         | Display date, time created on, and like option                     | Pass      |
| Pagination                 | Blog Page      | Display         | Display 4 blogs on a page, paginated to 4 blogs, next & previous page working | Pass      |


<img src="docs/readme-images/join_blog.png" alt = "Testing" style="height:400px; width: 100%;">

### Contact Us Page 
Manual Testing was carried out throughout the site to check the whether the site met the requirements of the expected results below.

| Element                    | Location       | Action          | Expected Result                                                    | Pass/Fail |
| -------------------------- | -------------- | --------------- | -------------------------------------------------------------------| --------- |
| First Name Field           | Contact Us     | Display & Fill  | If field not completed then directed to field to be filled         | Pass      |
| Last Name Field            | Contact Us     | Display & Fill  |If field not completed then directed to field to be filled          | Pass      |
| Email Field                | Contact Us     | Display & Fill  | If field not completed then directed to field to be filled         | Pass      |
| Subject Field              | Contact Us     | Display & Fill  | If field not completed then directed to field to be filled         | Pass      |
| Message Field              | Contact Us     | Display & Fill  | If field not completed then directed to field to be filled         | Pass      |
| Send Button                | Contact Us     | Click & Display | If any field not completed then directed to fields to be filled    | Pass      |
| Form Post                  | Contact Us     | Post            | Post form to admin panel for viewing                               | Pass      |

<img src="docs/test-images/contact_error.png" alt = "Testing" style="height:200px; width: 100%;">

### Reviews Page 
Manual Testing was carried out throughout the site to check the whether the site met the requirements of the expected results below.

| Element                    | Location       | Action          | Expected Result                                                    | Pass/Fail |
| -------------------------- | -------------- | --------------- | -------------------------------------------------------------------| --------- |
| Reviews                    | Review Page    | Display         | Display review by, created on, subject, rating stars, review and image|     Pass      |
| User Logged Out Mode       | Review Page    | Display         | Unable to edit/delete a created review                             | Pass      |
| User Logged Out Mode       | Account Icon   | Display         | Unable to add a review                                             | Pass      |
| User Logged In Mode        | Account Icon   | Display         | Able to add a review                                               | Pass      |
| User Logged In Mode        | Review Page    | Display         | Able to edit and delete a review                                   | Pass      |
| Logged in Edit review      | Review Page    | Click & Redirect| Click edit review, redirect page to edit review and view form      | Pass      |
| Edit review                | Edit Review    | Click & Display | Make changes to edit form and submit form using button, POST changes| Pass      |
| Submit Button              | Edit Review    | Click & Redirect| Submit button and page directed to review page, POST FORM          | Pass      |
| Delete Review              | Review Page    | Click & Delete  | Delete review, display success message confirming deletion         | Pass      |
| Delete Review              | Review Page    | Display         | Remove delete review                                               | Pass      |
| Add Review                 | Account Icon   | Click & Redirect| Remove delete review                                               | Pass      |
| Title Field                | Add Review     | Display & Fill  | If field not completed then directed to field to be filled         | Pass      |
| Customer Review Field      | Add Review     | Display & Fill  | If field not completed then directed to field to be filled         | Pass      |
| Rating Field               | Add Review     | Display & Fill  | If field not completed then directed to field to be filled         | Pass      |
| Select Image Field         | Add Review     | Display & Fill  | If field not completed then directed to field to be filled         | Pass      |
| Submit Button              | Add Review     | Click & Display | If any field not completed then directed to fields to be filled    | Pass      |
| Form Post                  | Add Review     | Post            | Post form to admin panel for viewing                               | Pass      |
| Success Message            | Add Review     | Message         | Waiting for approval success message                               | Pass      |

<img src="docs/test-images/delete_review.png" alt = "Testing" style="height:200px; width: 100%;">

### Profile Page 
Manual Testing was carried out throughout the site to check the whether the site met the requirements of the expected results below.

| Element                    | Location       | Action          | Expected Result                                                    | Pass/Fail |
| -------------------------- | -------------- | --------------- | -------------------------------------------------------------------| --------- |
| Profile Page               | Profile Page   | Display         | User information is saved and view order history if user is logged in| Pass    |
| User Logged Out Mode       | Profile Page   | Display         | Unable to view profile                                             | Pass      |
| User Logged In Mode        | Profile Page   | Display & Fill  | Able to update profile page and view existing orders               | Pass      |
| Update Button              | Profile Page   | Submit Form     | Update profile information for user                                | Pass      |
| Form sent                  | Profile Page   | Form send       | Updated information send to the admin panel                        | Pass      |
| Order History              | Profile Page   | Display         | View order History and click order number to see checkout success  | Pass      |


<img src="docs/test-images/profile.png" alt = "Testing" style="height:300px; width: 100%;">

### Login Page
Manual Testing was carried out throughout the site to check the whether the site met the requirements of the expected results below.

| Element                    | Location       | Action          | Expected Result                                                    | Pass/Fail |
| -------------------------- | -------------- | --------------- | -------------------------------------------------------------------| --------- |
| Username                   | Sign In Page   | Display & Fill  | If field not completed then directed to field to be filled         | Pass      |
| Password                   | Sign In Page   | Display & Fill  | If field not completed then directed to field to be filled         | Pass      |
| Remember me                | Sign In Page   | Display & Fill  | Able to tick to remember login details                             | Pass      |
| Home Button                | Sign In Page   | Redirect page   | Page is redirected back to the home page                           | Pass      |
| Sign In Button             | Sign In Page   | Sign In         | Sign in using the credentials - page success                       | Pass      |
| Once_signed_in             | Sign In Page   | Display         | You have successfully signed in as {first_name}                    | Pass      |
| Forgot Password            | Sign In Page   | Display & Fill  | Fill email address to be emailed a link to reset password          | Pass      |

<img src="docs/test-images/login.png" alt = "Testing" style="height:300px; width: 100%;">

### Register Page

| Element         | Location      | Action           | Expected Result                                                              | Pass/Fail |
| --------------- | ------------- | ---------------- | ---------------------------------------------------------------------------- | --------- |
| Username        | Register Page | Insert Data      | 1\. Field fill in compulsary                                                 | Pass      |
| Email           | Register Page | Insert Data      | 1\. Field fill in optional                                                   | Pass      |
| Password        | Register Page | Insert Data      | 1\. Field fill in compulsary                                                 | Pass      |
| Password(again) | Register Page | Insert Data      | 1\. Field fill in compulsary - same as password                              | Pass      |
| Sign Up Button  | Register Page | Click, Send data | Once information has been submitted correctly the form is sent to Admin Page | Pass      |
| Once_Registered | Home Page     | Success Message  | Success message and keep user signed in                                      | Pass      |

<img src="docs/test-images/register.png" alt = "Testing" style="height:300px; width: 100%;">


### Logout
| Element         | Location    | Action          | Expected Result                       | Pass/Fail |
| --------------- | ----------- | --------------- | ------------------------------------- | --------- |
| Main Page       | Logout Page | View            | Display logout page confirmation      | Pass      |
| Sign Out Button | Logout Page | Click + Logout  | Log user out                          | Pass      |
| Sign Out Button | Logout Page | Success Message | Successfully Logged out               | Pass      |
| Sign Out Button | Home Page   | Home Page       | Redirect to Home page once logged out | Pass      

<img src="docs/readme-images/sign_out.png" alt = "Login" style="height:300px; width: 100%;">

### 404 Error Page

| Element           | Location | Action          | Expected Result                                                                       | Pass/Fail |
| ----------------- | -------- | --------------- | ------------------------------------------------------------------------------------- | --------- |
| Page not found    | 404 Page | View            | Any page not recognised or typing error the page will direct the user to the 404 page | Pass      |
| Url error         | 404 page | view            | Any URL not correctly displayed will take the user to the 404 page                    | Pass      |
| Home Page Buttton | 404 page | Click + Display | The home page button redirects the user from the 404 page back to the home page       | Pass      |

<img src="docs/readme-images/404_page.png" alt = "Admin" style="height:300px; width: 100%;">


### Admin Page

+ Admin data for Join our Blog Page 

<img src="docs/test-images/blog_test.png" alt = "Admin" style="height:300px; width: 100%;">

+ Comments data for Join our blog Page

<img src="docs/test-images/comment_test.png" alt = "Admin" style="height:300px; width: 100%;">

+ Admin data for Contact Page

<img src="docs/test-images/contact_test.png" alt = "Admin" style="height:300px; width: 100%;">

+ Admin data for Register Email Address

<img src="docs/test-images/email_test.png" alt = "Admin" style="height:300px; width: 100%;">

+ Admin data for Confirmed Orders 

<img src="docs/test-images/orders_test.png" alt = "Admin" style="height:300px; width: 100%;">

+ Admin data for uploaded products

<img src="docs/test-images/product_test.png" alt = "Admin" style="height:300px; width: 100%;">

+ Admin data for customer reviews - also waiting for approval

<img src="docs/test-images/reviews_test.png" alt = "Admin" style="height:300px; width: 100%;">

+ Admin data for users registered 

<img src="docs/test-images/user_test.png" alt = "Admin" style="height:300px; width: 100%;">

| Element         | Location      | Action           | Expected Result                                                              | Pass/Fail |
| --------------- | ------------- | ---------------- | ---------------------------------------------------------------------------- | --------- |
| Email Address   | Admin Page    | Post Data        | Registered email address display in the admin panel                          | Pass      |
| User            | Admin Page    | Post Data        | Registered users display in the admin panel                                  | Pass      |
| Comments        | Admin Page    | Post Data        | Returned comments display in the admin panel                                 | Pass      |
| Blog            | Admin Page    | Post Data        | Blogs created by the admin only can be viewed her and created her            | Pass      |
| Checkout Orders | Admin Page    | Post Data        | Orders placed by user which are successful are displayed here                | Pass      |
| Contact         | Admin Page    | Post Data        | Returned comments display in the admin panel                                 | Pass      |
| Products        | Admin Page    | Post Data        | Uploaded products are displayed here, they can be edited and deleted         | Pass      |
| Reviews         | Admin Page    | Post Data        | Customer reviews can be viewed her but require approval                      | Pass      |


## Automated Testing 

I managed to get some automated tests done for my project. Ideally I wanted to much more automated tested but I was informed for this project that automated testing is not a necessity. Automated was done on most of the apps. I have attached coverage reports for the some of the app, which automated testing was carried out for.

+ To undertake Automated Testing the following code need to be entered in the Database section in the Setting.py file, any other code need to be commented out so the testing can take place. 
```
   DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```


+ Coverage report for blog app

<img src="docs/test-images/coverage_blog.png" alt = "Automated Testing" style="height:300px; width: 100%;">

+ Coverage report for contact us app

<img src="docs/test-images/coverage_contact.png" alt = "Automated Testing" style="height:300px; width: 100%;">

+ Coverage report for Main app

<img src="docs/test-images/coverage_main_app.png" alt = "Automated Testing" style="height:300px; width: 100%;">

+ Coverage report for Reviews app

<img src="docs/test-images/coverage_reviews.png" alt = "Automated Testing" style="height:300px; width: 100%;">

## Bugs 

### Fixed Bugs 

| Element         | Location      | Action           | Expected Result                                                              | Pass/Fail |
| --------------- | ------------- | ---------------- | ---------------------------------------------------------------------------- | --------- |
| Bug 1            | Login, Logout, Register| No Success Message        | When the user was signing in, or out the success messages was not displaying.                         | Pass      |

+ This particular bug was realised during testing. I realised that when users were using the all auth templates, the success messages were not displaying. I managed to fixed the bug, as the issue related to missing text script in my Home app, template index.html. This was rectified and the bug fixed. 

<img src="docs/test-images/bug1.png" alt = "Bugs" style="height:100px; width: 60%;">


| Element         | Location      | Action           | Expected Result                                                              | Pass/Fail |
| --------------- | ------------- | ---------------- | ---------------------------------------------------------------------------- | --------- |
| Bug 2           | Banner        | Marquee tag      | Initially created a banner with a marquee tag, during testing I realised that this tag was invalid and therefore not compliant with the W3C HTML validator checker. This had to be removed and reverted to CSS.                         | Pass      |

+ This bug was also realised during testing. I realised that the marquee tag was outdated and invalid during my HTML validaton. I also got some feedback from tutor support, who informed me that this should be implemented via css. I decided to use a different format and so used CSS and the bug was fixed. 

<img src="docs/readme-images/banner.png" alt = "Bugs" style="height:100px; width: 100%;">

| Element         | Location      | Action           | Expected Result                                                              | Pass/Fail |
| --------------- | ------------- | ---------------- | ---------------------------------------------------------------------------- | --------- |
| Bug 3           | Responsive    | All site         | I had alot of reponsive design issues, but these were rectified using bootstrap classes.                         | Pass      |

+ This bug was also realised during testing. I realised that alot of pages had alot of z-scrolls, alot of time went into resolving these from the app templates. Hopefully now I feel like I have now mastered the boostrap format. 


## Unfixed Bugs
Fortunately I did not have any bugs which I was not able to fix, I set myself targets and with a thorough testing plan I was able to eliminate all bugs and errors, which were identified during building my project.