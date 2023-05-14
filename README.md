# Project 5 - Prestige|Watches Full Stack Web Developer Ecommerce Project


## Table of content
+ [Introduction](#introduction)
+ [User Experience](#user-experience---ux)
+ [Agile Methodology](#agile-methodology)
+ [Wireframes](#wireframes)
+ [Database Schema](#database-schema)
+ [Color Contrast](#colour-contrast)
+ [Site Features](#site-features)
    + [Favicon Icon](#favicon-icon)
    + [Header](#header)
    + [Footer](#footer)
    + [Site Navigation](#site-navigation)
    + [Home Page](#home-page)
    + [About Us Page](#about-us-page)
    + [Product Page](#product-main-page)
    + [Product Detail Page](#product-detail-page)
    + [Product Shopping Bag Page](#product-shopping-bag-page)
    + [Product Shopping Checkout Page](#product-shopping-bag-page)
    + [Product Shopping Checkout Success Page](#product-shopping-checkout-success-page)
    + [Product Management Page](#product-management-page)
    + [My Profile Page](#my-profile-page)
    + [Blog Page](#blog-page)
    + [Customer Reviews Page](#customer-reviews-page)
    + [Contact us Page](#contact-us-page)
    + [Sign Up Page](#sign-up-page)
    + [Sign In Page](#sign-in-page)
    + [Sign Out Page](#sign-out-page)
    + [Error 404 Page](#error-404-page)
    + [Admin Page](#admin-page)
+ [User Interaction Messages](#user-interaction-messages)
+ [Future Features](#future-features)
+ [Web Marketing](#web-marketing)
    + [Facebook Page](#social-media)
    + [Search engine optimization](#search-engine-optimization)
         + [Sitemap.xml](#sitemap.xml)
         + [Robots.txt](#robots.txt)
    + [Mailchimp Email marketing](#mailchimp-email-marketing)
+ [Testing](#testing)
+ [AWS Setup Process](#aws-setup-process)
    + [Create AWS S3 Bucket](#create-aws-s3-bucket)
    + [Create IAM](#create-iam)
+ [Stripe](#stripe)
    + [Webhooks](#webhooks)
+ [Technologies](#technologies)
+ [Libraries](#libraries)
+ [Security Features](#security-features-and-defensive-design)
+ [Form Features](#form-feature--validation)
+ [Database Security](#database-security)
+ [Deployment of this project](#deployment-of-this-project)
    + [Heroku](#heroku)
    + [Elephant SQL Database](#elephant-sql-database)
    + [Github](#github)

+ [Credits](#credits)
+ [Acknowledgement](#acknowledgement)


## Introduction
```diff 
Prestige|Watches A Full Stack Web Development for the Eccommerce Module Project using (Create, Read, Update, Delete)
```

This project is a B2C e-commerce store that is designed and implemented with Python and Django, HTML, CSS and some Javascript. Prestige Watches is online ecommerce store. The store allows the user to purchase a item, view blogs, make comments on blogs, add and delete customer reviews and sign up to newsletters. 

Some the key functions of the services are as below:
+ Purchase Items From The Online Store.
+ Login, Logout and Register Facility.
+ Admin to create, read, edit and delete Products.
+ Users to create, read, edit and delete reviews. 
+ Create feedback via the Contact Us Page.
+ About Us page.
+ User to view blogs and able to like blogs.
+ User to create comments, and function to delete comments. 
+ User to be able to like comments.

<img src="docs/readme-images/am-i-responsive.png" alt = "Prestige|Watches" style="height: 400px; width: 100%;">

[View link to my project 5](https://prestige-watches.herokuapp.com/)


## User Experience - UX
+ Site User Experience
1. As a site user I can create or edit my account so that I can update my details accordingly
2. As a site user I can login in my account so that I can view my order history
3. As a site user I can search for products so that I can find specific products
4. As a site user I can sort products on criteria such as price and category so that I can I have a method of ordering the products which I prefer.
5. As a site user I can browse through products so that I can decide what I may be interested in buying
6. As a site user I can look at product details so that I can decide if I want to purchase it
7. As a site user I can easily add products I want to purchase to a basket so that I can decide whether to purchase or not
8. As a site user I can view the contents of my shopping basket so that I can be able to make any adjustments, if required. 
9. As a site user I can update my bag by adding more or remove products so that I can decide on the number of products I intend to buy
10. As a site user I can view my order summary so that I can verify it before confirming
11. As a site user I can checkout securely so that I can I maintain the level of trust on the site
12. As a site user I can view paginated posts so that I can select which posts to view
13. As a site user I can view all posts so that I can decide what I may be interested in reading
14. As a site user I can comment to the blog posts so that I can express my opinion to the post
15. As a site user I can use the contact form so that I can contact the site owners
16. As a site user I can sign up to newsletter so that I can keep updated on the latest news
17. As a site user I can add, view, delete and edit reviews which customers can view on the main site. 
18. As a site user I can read the sites About us page
19. As a site user I can like blogs and comments created by other users.
20. As a site user I can view paginated reviews so that I can select which review to view.


+ Site Admin Experience
1. As a admin I can manage users' accounts so that I can make any required changes to them if needed
2. As a admin I can manage products so that I can add , update or delete products when necessary
3. As a admin I can view created orders so that I can full fill the orders or ammend if needed
4. As a Admin I can delete any of comments so that I can remove them if I no longer feel they are still necessary or needed
5. As a Admin I can view messages sent via contact form so that I can act upon them
6. As an admin I can manage and create blogs for users to view and like. 
7. As an admin I can manage the blog comments so that I can make amendments if needed
8. As an admin I can manage the review page so that I can make amendments if needed
9. As an admin I can manage the Facebook page in order to attract further customers. 


## Agile Methodology
An Agile Approach was used to develop this site. This was achieved by breaking the project down into smaller tasks.
To complete the overall aim of the website, 21 issues were created as specific tasks called User Stories. These User Stories are small sections of the project designed to accomplish a specific goal. Once the User Story was working effectively it was moved across the Kanban board, in the following working order. 
+ To do
+ In Progress
+ Done

<img src="docs/readme-images/user-stories.png" alt = "Prestige|Watches" style="height: 300px; width: 100%;">

All my user stories were completed and succesfully actioned. The design was based on the Agile Methodology.


 My Projects and User Stories can be viewed here :  [Issues and Projects](https://github.com/users/Shanbashir1/projects/6/views/1 "Github Issues")


 ## Wireframes
Balsamiq wireframes was used to design the wireframes in the design phase of this project. [Balsamiq Wireframes - Click here to view the wireframes](https://balsamiq.cloud/sbwg9ys/pn79h8b/r2278?f=N4IgUiBcCMA0IDkpxAYWfAMhkAhHAsjgFo4DSUA2gLoC%2BQA%3D "Click here to view the wireframes")
The wireframes was edited a few times during the project to be inline witht he project design, I had to make a few adjustments to the design, in order for the design to work. 

+ Home Page design

<img src="docs/wireframes-images/home.png" alt = "Prestige Watche" style="height: 400px; width: 100%;">

+ Product Page design

<img src="docs/wireframes-images/product.png" alt = "Prestige Watche" style="height: 600px; width: 100%;">

<img src="docs/wireframes-images/product_detail.png" alt = "Prestige Watche" style="height: 600px; width: 100%;">

+ Checkout design

<img src="docs/wireframes-images/bag.png" alt = "Prestige Watche" style="height: 600px; width: 100%;">

<img src="docs/wireframes-images/checkout.png" alt = "Prestige Watche" style="height: 600px; width: 100%;">

+ Blog Page design

<img src="docs/wireframes-images/blog.png" alt = "Prestige Watche" style="height: 400px; width: 100%;">

+ Review Page design

<img src="docs/wireframes-images/reviews.png" alt = "Prestige Watche" style="height: 600px; width: 100%;">

+ Contact Page design

<img src="docs/wireframes-images/contact.png" alt = "Prestige Watches" style="height: 600px; width: 100%;">

## Database Schema
Lucid Charts was used to design the unique models used in this project.

<img src="docs/readme-images/lucida.png" alt = "Prestige Watche" style="height: 450px; width: 100%;">

## Colour Contrast
The selection of the colours for the web page was chosen from Color Hex. The colour contrast tried to remain basic and have a good flow of similiar colours throughout the design. However most of my colour code was used via the Bootstrap contrast which was available from the framework, this included colour text and button colours. 

<img src="docs/readme-images/Prestige_Watches.png" alt = "Color Contrast" style="height: 400px; width: 100%;">

## Site Features

### Favicon Icon 
<img src="docs/readme-images/watch_favicon.png" alt = "Favicon" style="height: 100px; width: 20%;">

+ The selected icon was a image of a watch. 
+ The image is displayed on all the pages, throughout the website to give a unique design for the users.
+ The favicon image is a design which contributes to the overall web design.

### Home Page
<img src="docs/readme-images/home.png" alt = "Home" style="height:300px; width: 100%;">

+ The home page is the first page the user lands on when visiting the site. 
+ The home page user the header and the delivery banner feature but does not include the footer. 
+ The home page has a shop now flashing button, which navigates the user to the product page. 
+ The home page also has flashing text to give the page a special feature. 

### Header
<img src="docs/readme-images/header.png" alt = "Header" style="height:70px; width: 100%;">

+ The header is located at the top of the page, displaying the logo-text, The sub-heading, the navigation links, the search bar, my account icon and the shopping basket.
+ The color used for the header was #fffff (white), which was one of the main color used throughout the site to display the background and some area of colour text. 
+ The logo text was black, however the sub-heading text had a combination of gold. 
+ The search button had a link reference of selecting items from the product store. 
+ The navigation link bars had scrolls and redirected users to pages through out the site. The navigation link were simple and easy to navigate through out the site. The navigation links bars also had a hover of underline, to clearly display to the user which tab they were hovering over. 
+ The my account icon, directed the user to the login page, logout page and register page. 
+ The basket had the total cost of the items added and navigated the user to the bag page. 
+ Clicking on the logo header will redirect the user to the home page. 

### Delivery Banner 
<img src="docs/readme-images/banner.png" alt = "Delivery Banner" style="height:70px; width: 100%;">

+ The delivery banner displays to the user a "Free delivery charge on orders over £1000"
+ The banner has been designed using a marquee, with floating text offer the free delivery charge. 
+ A delivery van has been used as the icon for the banner. 
+ The colour contrast has been used of a dark grey background with white text.

### Footer
<img src="docs/readme-images/footer.png" alt = "Footer" style="height:200px; width: 100%;">

+ The footer is contrasted in line with the header banner of dark grey with white text, the bootstrap of text-info has been used for the navigation links. 
+ All links direct the users to pages through out the site.
+ The footer is quite detailed for user to explore relevant information while navigating through the site. 
+ The footer contains the following features 
1. Header Logo 
2. Sub Header 
3. Text Description 
4. Navigation Links 
5. Policies and Newsletters 
6. Social Media Links 
7. Copyright 

### Site Navigation
<img src="docs/readme-images/nav1.png" alt = "Menu" style="height:60px; width: 100%;">

+ Site Navigation is available on both the header and the footer. 
1. All Products, contains the following sub-headings, Price, Rating, Category, All Products, these links navigate the user to the relevant requirements. 
2. Special Offer, contains the following sub-headings, New Arrival, Sale, All Specials these links navigate the user to the relevant requirements. 
3. Join our blog
4. Help contains the following sub-headings, Contact Us, Customer Reviews and About Us these links navigate the user to the relevant requirements. 
5. Account - All Auth, gives the user to Login, Logout, Register
6. Account Admin option - Allows the Admin user to view Product Management, Blog Management, My Profile and Add Reviews.

+ Account Navigation
<img src="docs/readme-images/nav2.png" alt = "Menu" style="height:300px; width: 50%;">

+ Footer Navigations
<img src="docs/readme-images/nav3.png" alt = "Menu" style="height:200px; width: 80%;">

### About Us Page
+ The About us page contains information of the companies information and history. 
+ The format is text based and design has been designed using bootstrap. 
+ The about us page contains information a shop now button which redirects the user to the products page. 


<img src="docs/readme-images/about1.png" alt = "About" style="height:800px; width: 80%;">
<img src="docs/readme-images/about2.png" alt = "About" style="height:800px; width: 80%;">

### Product Main Page
+ On this page, users will see all the products available on the website. All the watches will be displayed on the main page when the user has selected "All Products" or any other product relating links. 

<img src="docs/readme-images/product1.png" alt = "Product" style="height:200px; width: 100%;">

+ The user will be able to sort the products and filter the requirements they would like to search by
+ Once the user selects the product he will be forwarded to the product detail page.

<img src="docs/readme-images/product3.png" alt = "Product" style="height:200px; width: 100%;">

+ Mobile Devices View

<img src="docs/readme-images/product2.png" alt = "Product" style="height:600px; width: 80%;">

+ If the user sign in via the admin login details they will be able to delete, add and edit the products page. 
+ Admin users will have the complete the rights to change and add products on the page. 
<img src="docs/readme-images/product4.png" alt = "Product" style="height:200px; width: 100%;">

+ Mobile Devices View
<img src="docs/readme-images/product5.png" alt = "Product" style="height:500px; width: 100%;">

### Product Detail Page

+ On this page the user will see the selected products with product descriptions and features. 
+  The user will be able to select the quantity, which can be added and then removed using the "+" and "-" icons. 
+ There will also be 2 buttons, 1 button will allow the user to go back the products page to continue shopping, the other button will take the user to the bags page, displaying the qty and order details.  
<img src="docs/readme-images/product6.png" alt = "Product" style="height:300px; width: 80%;">

### Product Shopping Bag Page
+ This feature is called the Shopping bag. Here, users can add products and quantities. Check the total price, and delivery costs and go to the secure checkout to finish the order. Before secure checkout. the user can also change the quantity and remove unwanted products. The user can also leave this page by pressing the button "Keep Shopping", if the user would like to continue than they will proceed to the "secure checkout" page.

<img src="docs/readme-images/shopping_bag.png" alt = "Product" style="height:300px; width: 100%;">

### Product Shopping Checkout Page
+ On this page the user will need to enter his details and credit/debits cards details. The order will also be displayed. The total cost and delivery charges will also be visible to the user. 
+ The user will be able to "adjust the bag" or "complete order" via the buttons. 

<img src="docs/readme-images/shopping_checkout.png" alt = "Checkout" style="height:300px; width: 100%;">

### Product Shopping Checkout Success Page
+ Once the user has completed the checkout they will be direct to the success checkout page, with a receipt confirmation and order reference. The order confirmation will be displayed as follows: 
+ Order Info
+ Order Number
+ Order Date
+ Order Details
+ Delivering To
+ Full Name
+ Address 1
+ Town or City
+ Postal Code
+ Country
+ Phone Number
+ Billing Info
+ Order Total
+ Delivery
+ Grand Total
<img src="docs/readme-images/checkout_success.png" alt = "Checkout" style="height:300px; width: 100%;">

+ Email sent by the server - order confirmation. 
<img src="docs/readme-images/email2.png" alt = "Checkout" style="height:500px; width: 100%;">


### Product Management Page
+ For Admin only 
+ When the website admin is logged in on this page, they can add a new product to the website without going to the admin panel.

<img src="docs/readme-images/product_management.png" alt = "Product" style="height:300px; width: 100%;">

### My Profile Page
+ The profile page is available when the user logs in, the user is able to add his details and view a order history. By adding a profile the user does not need to add his details the next time they place an order, as the information is kept saved.
+ A "Update my delivery info" button is available to the user to acknowlege the changes. 

<img src="docs/readme-images/myprofile.png" alt = "Profile" style="height:300px; width: 100%;">

### Blog Page
+ The blog page is only administrated by the admin, who can add, delete and edit blogs. 
+ The user has the option to like the blogs. Once like the heart will have a number one selected. 

<img src="docs/readme-images/join_blog.png" alt = "Blog" style="height:300px; width: 100%;">

+ The user has option to create, read, update, delete comments. in the comment section. 
+ The user can also like and unlike a comment.

<img src="docs/readme-images/comments.png" alt = "Comments" style="height:200px; width: 100%;">

+ Only the admin can add, edit and delete blogs. The blogs can be ammended via the blog management tab, which is located in the "My Accounts" icon. This can also be managed in the admin panel. 

<img src="docs/readme-images/blog_manage.png" alt = "Blog" style="height:200px; width: 100%;">

### Customer Reviews Page
+ The customer review page is located in the Help navigation links. The user will scroll down fromt help section and select the customer review page. 
+ All logged in users will be able to created a review. The review will however need to be approved by the admin.
+ Once the review has been approved it will display on the customer review main page. 
+ The customer review page will have show star ratings and a comment section for the customer to express it views. 

<img src="docs/readme-images/customer_review.png" alt = "Reviews" style="height:200px; width: 100%;">

+ The user will be able to add a review if they are logged in. The add review tab will be accessible from the "My Account" tab. 
+ The form will be easy to submit for the user 
+ The review will need to be approved by the admin before being allowed to be published. 

<img src="docs/readme-images/add_review.png" alt = "Reviews" style="height:200px; width: 100%;">

+ Admin Reviews - requires approval from the admin, before being published to the site. 

<img src="docs/readme-images/admin_review.png" alt = "Reviews" style="height:200px; width: 100%;">

### Contact Us Page
+ A contact us page is available for users who need to get in touch with the store owners. They have to put their name, email, the subject and the overall message before sending the form, which is then sent to the admin for viewing. 

<img src="docs/readme-images/contactus.png" alt = "Contact Us Page" style="height:300px; width: 100%;">

### Sign Up Page
+ For first time users the user will need to register his/her details and submit the form. 
+ The form will then send a email, the user will need to verify the email so they can activate their account. 

<img src="docs/readme-images/signup.png" alt = "Reviews" style="height:250px; width: 100%;">

+ Verification required via email. With a success message. 

<img src="docs/readme-images/verify_signup.png" alt = "Signup" style="height:120px; width: 100%;">

+ Email sent by the server 
<img src="docs/readme-images/email1.png" alt = "Signup" style="height:280px; width: 100%;">

+ Once user has accepted the link via his email, they redirected back to the site, and requested to verify the email address. 

<img src="docs/readme-images/verify_2.png" alt = "Signup" style="height:100px; width: 100%;">

### Sign In Page

+ On the Login Page, users can log in to the website by inputting their username and password. The user is now registered and will have access to the Registered User website services.

<img src="docs/readme-images/sign_in.png" alt = "SignIn" style="height:180px; width: 100%;">

+ Once signed in the user is naviagted the "Home Page".

### Sign Out Page

+ On the Signout Page, users can confirm that they wish to exit the website.

<img src="docs/readme-images/sign_out.png" alt = "SignOut" style="height:180px; width: 100%;">

### Error 404 Page
+ A 404 page is also available to handle navigation errors with a home link button to take them back to the home page

<img src="docs/readme-images/404_page.png" alt = "404 page" style="height:400px; width: 100%;">

### Newsletter 
+ Users can sign up using their email to receive news, offers and deals straight into their inbox.
+ The newsletter link is located in the footer. 
+ The user will need to subscribe using their email address.

<img src="docs/readme-images/newsletter.png" alt = "404 page" style="height:300px; width: 100%;">

### Privacy Policy
+ The privacy policy is located in the footer 
+ The privacy is a GDPR policy which must be included in to sites which collect data and information of users. 

<img src="docs/readme-images/privacy_policy.png" alt = "404 page" style="height:300px; width: 100%;">

### Facebook Page
+ In terms of marketing, the site has a facebook page to push content and targets some of it's customers through content creation. 

<img src="docs/readme-images/facebook.png" alt = "Facebook page" style="height:300px; width: 100%;">

+ The facebook page targets users and audience to attract further business.

<img src="docs/readme-images/facebook2.png" alt = "Facebook page" style="height:300px; width: 100%;">

### Admin Page 
+ The admin models contains a list of created models in the app.
+ The admin models has a list of action of data which has been inputed by the user.
+ Admin users have more functionality than regular users and have full CRUD functionality over information such as products, order, blogs, reviews, contact us feedbacks and profile information.
Only approved admin users can access this section of the site. It is accessed by adding /admin to the URL home page and signing in.
+ The admin models have all user information, which was entered during sign in , orders etc. 
+ Inputed data can be deleted and edited by the admin. 
+ Orders, reviews, comments, blog and profile can be viewed by the admin and may requrie some approval before being published on the site. 

+ Main Admin Page - Django Administration
<img src="docs/readme-images/admin1.png" alt = "Admin page" style="height:300px; width: 100%;">

Email Address Admin Page - Django Administration
<img src="docs/readme-images/admin2.png" alt = "Admin page" style="height:200px; width: 100%;">

Blog Admin Page - Django Administration
<img src="docs/readme-images/admin3.png" alt = "Admin page" style="height:150px; width: 100%;">

Order Admin Page - Django Administration
<img src="docs/readme-images/admin4.png" alt = "Admin page" style="height:200px; width: 100%;">

Contact Us Message Admin Page - Django Administration
<img src="docs/readme-images/admin5.png" alt = "Admin page" style="height:200px; width: 100%;">

Product Category Admin Page - Django Administration
<img src="docs/readme-images/admin6.png" alt = "Admin page" style="height:200px; width: 100%;">

Product List Admin Page - Django Administration
<img src="docs/readme-images/admin7.png" alt = "Admin page" style="height:400px; width: 100%;">

Customer Reviews Admin Page - Django Administration
<img src="docs/readme-images/admin8.png" alt = "Admin page" style="height:180px; width: 100%;">


## User Interaction Messages
+ The site benefits from messages which alert the user of action they have completed. Below is not a exhausted list but shows some evidence of messages the user recieves. 

+ Checkout Success page for user ordering online. 
<img src="docs/readme-images/checkout_success.png" alt = "Message" style="height:300px; width: 100%;">

+ Admin succesfully added blog on the blog page 
<img src="docs/readme-images/add_blog.png" alt = "Message" style="height:400px; width: 70%;">

+ Admin succesfully delete product on the product page
<img src="docs/readme-images/product_delete.png" alt = "Message" style="height:200px; width: 50%;">

+ Admin succesfully edit product on the product page
<img src="docs/readme-images/product_edit.png" alt = "Message" style="height:200px; width: 80%;">

+ Customer review successfully waiting approval
<img src="docs/readme-images/review_approval.png" alt = "Message" style="height:200px; width: 80%;">

+ Customer review successfully deleted
<img src="docs/readme-images/review_delete.png" alt = "Message style="height:200px; width: 70%;">

+ New user registers to the site 
<img src="docs/readme-images/email_sent.png" alt = "Message" style="height:200px; width: 80%;">

## Future Features
While creating the Project, I realised that the vast input I could add to the design to allow it to have more functionalities. As we have all learnt the timescope involved limits the overall scope.

What I could possibily add as a Future Feature? 

1. Add more variety of products and create better categories for user to apply its search facilities. 
2. Better products layout, with the limited time scope I was not abel to cut the images to the correct length, which resulted in the images being slighly off design and scope. However with limited time and resources the images would be much more user friendly. 
3. User being able to add comments and reviews on the products page .
4. Generally so much to add, to make the site much more efficient and user friendly. 

## Web Marketing 

### Social Media
+ A facebook page was created to build community from the target market. Facebook is free and it also takes little to no time to set up and also it has so many users whom a business can strive to maintain a certain relationship, create content and connect with a target audience. 

<img src="docs/readme-images/facebook.png" alt = "Facebook page" style="height:300px; width: 100%;">

### Search engine optimization
+ Keywords SEO are important for search engines to pick up keywords while users are searching online. 
+ Below are some of the keywords I have used for the site 

<img src="docs/readme-images/seo.png" alt = "SEO" style="height:200px; width: 100%;">

#### Sitemap.xml 
+ A sitemap file with a list of important URLs was added to ensure that search engines are able to easily navigate through the site and understand its structure. This was made using XML-sitemaps.com by following the steps:
1. Paste the URL of the deployed site into XML-sitemaps
2. Download the XML sitemap file
3. Add the file into the projects root folder, named as sitemap.xml

#### Robots.txt
A robots.txt file was created to tell search engines where not to go on the website and increase the quality of the site, ultimately improving the SEO rating.

### Mailchimp Email Marketing
+ Users can subscribe to newsletters by entering their email address.
+ Email Marketing can alert users to special offers and important information. 

## Testing
All of the testing and validation for the project can be viewed here  [Testing and Validation](TESTING.md)


## AWS Setup Process

### Create AWS S3 Bucket
The deployed site uses AWS S3 Buckets to store the webpages static and media files. More information on how you can set up an AWS S3 Bucket can be found below:
1. Create an AWS account [Aws Account](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26state%3DhashArgsFromTB_eu-north-1_2d47c418cc545d17&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge=idLMXSYzWM_UznrYO8-wN9DkMOqXbVBiEDfrbGcwHHc&code_challenge_method=SHA-256)
2. Login to your account and within the search bar type in "S3".
3. Within the S3 page click on the button that says "Create Bucket".
4. Name the bucket and select the region which is closest to you.
5. Underneath "Object Ownership" select "ACLs enabled".
6. Uncheck "Block Public Access" and acknowledge that the bucket will be made public, then click "Create Bucket".
7. Inside the created bucket click on the "Properties" tab. Below "Static Website Hosting" click "Edit" and change the Static website hosting option to "Enabled". Copy the default values for the index and error documents and click "Save Changes".
8. Click on the "Permissions" tab, below "Cross-origin Resource Sharing (CORS)", click "Edit" and then paste in the following code:

```
  [
      {
          "AllowedHeaders": [
          "Authorization"
          ],
          "AllowedMethods": [
          "GET"
          ],
          "AllowedOrigins": [
          "*"
          ],
          "ExposeHeaders": []
      }
  ]
  ```
  9. Within the "Bucket Policy" section. Click "Edit" and then "Policy Generator". Click the "Select Type of Policy" dropdown and select "S3 Bucket Policy" and within "Principle" allow all principals by typing "*".
  10. Within the "Actions" dropdown menu select "Get Object" and in the previous tab copy the "Bucket ARN number". Paste this within the policy generator within the field labelled "Amazon Resource Name (ARN)".
  11. Click "Add statement > Generate Policy" and copy the policy that's been generated and paste this into the "Bucket Policy Editor".
  12. Before saving, add /* at the end of your "Resource Key", this will allow access to all resources within the bucket.
  13. Once saved, scroll down to the "Access Control List (ACL)" and click "Edit".
  14. Next to "Everyone (public access)", check the "list" checkbox and save your changes.

### Create IAM
1. Search for IAM within the AWS navigation bar and select it.
2. Click "User Groups" that can be seen in the side bar and then click "Create group" and name the group 'manage-your-project-name'.
3. Click "Policies" and then "Create policy".
4. Navigate to the JSON tab and click "Import Managed Policy", within here search "S3" and select "AmazonS3FullAccess" followed by "Import".
5. Navigate back to the recently created S3 bucket and copy your "ARN Number". Go back to "This Policy" and update the "Resource Key" to include your ARN Number, and another line with your ARN followed by a "/*".
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "YOUR-ARN-NO-HERE",
                "YOUR-ARN-NO-HERE/*"
            ]
        }
    ]
}
```
6. Ensure the policy has been given a name and a short description, then click "Create Policy".
7. Click "User groups", and then the group you created earlier. Under permissions click "Add Permission" and from the dropdown click "Attach Policies".
8. Select "Users" from the sidebar and click "Add User".
9. Provide a username and check "Programmatic Access", then click 'Next: Permissions'.
10. Ensure your policy is selected and navigate through until you click "Add User".
11. Download the "CSV file", which contains the user's access key and secret access key.

### Inside your Terminal and Workspace 
+ Inside your terminal install the following, using the below commands. 
```
  pip3 install boto3
  pip3 install django-storages 
```

+ Freeze the requirements.txt file by using the following command 
```
pip3 freeze > requirements.txt
```

+ Add "storages" to your installed apps within your settings.py file.
+ At the bottom of the settings.py file add the following code:
```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
```

+ Add the following keys within your Heroku Settings Convig Vars: 
```
"AWS_ACCESS_KEY_ID" and "AWS_SECRET_ACCESS_KEY". These can be found in your CSV file.
```

+ Add the key "USE_AWS", and set the value to True within Heroku.
Remove the "DISABLE_COLLECTSTAIC" variable from Heroku.

+ Within your settings.py file inside the code just written add:
```  
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
Inside the settings.py file inside the bucket config if statement add the following lines of code:
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```

+ In the root directory of your project create a file called "custom_storages.py". Import the following at the top of this file and add the classes below:
```
  from django.conf import settings
  from storages.backends.s3boto3 import S3Boto3Storage

  class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

  class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

```

+ Navigate back to you AWS S3 Bucket and click on "Create Folder" name this folder "media", within the media file click "Upload > Add Files" and select the images for your site.
+ Under "Permissions" select the option "Grant public-read access" and click "Upload".

## Stripe
Stripe is a online payment system to allow online payments, using credit/debit cards. Store owners will need to register for a stripe account, in order to use it's services. To register with stripe you can visit their site [via this link -- STRIPE](https://dashboard.stripe.com/login)

+ The site contains lots of useful documentation and codes to get you started up, once registered you will be able to easily set up test payments and use a developer account to test payments etc. 

### Webhooks 
1. To set up a webhook, sign into your stripe account and click 'Developers' located in the top right of the navbar.

2. Then in the side-nav under the Developers title, click on "Webhooks", then "Add endpoint".

3. On the next page you will need to input the link to your heroku app followed by /checkout/wh/. It should look something like this:

    ```
    https://your-app-name.herokuapp.com/checkout/wh/
    ```
4. Then click "+ Select events" and check the "Select all events" checkbox at the top before clicking "Add events" at the bottom. Once this is done finish the form by clicking "Add endpoint".

5. Your webhook is now created and you should see that it has generated a secret key. You will need this to add to your heroku config vars.

6. On your Heroku app navigate to the config vars section under settings. You will need the secret key you have just generated for your webhook, in addition to your Publishable key and secret key that you can find in the API keys section back in stripe.

Add these values under these keys:

    ```
    STRIPE_PUBLIC_KEY = 'insert your stripe publishable key'
    STRIPE_SECRET_KEY = 'insert your secret key'
    STRIPE_WH_SECRET = 'insert your webhooks secret key'

    Finally, back in your settings.py file in django, insert the following near the bottom of the file:

    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
    STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
    ```


+ Below is successful working webhook response page. 

<img src="docs/readme-images/webhooks.png" alt = "Webhooks" style="height:300px; width: 100%;">

## Technologies
+ HTML - for the structure of the website
+ CSS - to provide styling to the page.
+ JavaScript
+ Python - to write all the logic of the app
+ Django - used as main framework for the app, which both all backend and most frontend elements are built on.
+ Django-allauth: for handing all user models and login functionality.
+ Amazon AWS - was used to host the static files and media
+ Django-crispy-forms: for making the django forms look better.
+ ElephantSQL - used to manage a PostgreSQL database.
+ Bootstrap - Widely used for the design of the site
+ Jquery - to allow some functions to delay or prompt messages.
+ Lucidchart used to make a database diagram.
+ Gitpod - used to connect a browser based VScode to github.
+ Github - used for version control and deployment of the website.
+ Heroku - to deploy the app.
+ CI PEP8 Online Checker - Check all Python code and ammend errors and warnings.
+ JShint - used to validate javascript/Jquery.
+ NuHtmlChecker - used to validate HTML.
+ W3C Jigsaw - CSS checker.
+ Lighthouse - To check the following aspects of a URL: Performance, Progressive Web App, Accessibility, Best Practices and SEO.
+ Google Developer Tools - to view pages on different media screens and ammend changes as developing.
+ Balsamiq Wireframes
Responsive design
+ HTML Viewer - Code Beautify

## Libraries
### Packages/Modules Installed
+ Gunicorn as the server for Heroku
+ Dj_database_url to parse the database URL from the environment variables in Heroku
+ Psycopg2 as an adaptor for Python and PostgreSQL databases
Summernote as a text editor
+ Allauth for authentication, registration and account management
+ Stripe for processing all online and credit card purchases on the website
+ Crispy Forms to style the forms
+ Pillow to process and save all the images downloaded through the database
+ Bootstrap frameworks was used to style the website, add responsiveness and interactivity 

## Security Features and Defensive Design
### User authentication
+ Django's all auth was used for login and sign up functionality.
+ Django's superuser is used to limit access to admin panel.
### Form Feature & Validation
+ Crispy Form was used for the front end.
+ Extensive form validation is used on front end as well as backend.
### Database Security
All secret keys connecting to the database are stored in a env.py file that is never pushed to github. Furthermore, Cross-Site Request Forgery (CSFR) tokens were used on all forms throughout the project.

## Deployment of This Project

I developed this site on Gitpod, using git for version control. Then deployed to Heroku using the following steps:

### Heroku
+ Log in to Heroku or create an account [via this link -- Heroku](https://id.heroku.com/login)

+ Click New and Create New App

+ Select your region.

+ Click Create App button

### Elephant SQL Database
You will then need to create a database to connect to the new created app. We have used ElephantSQL [via this link -- ElephantSQL](https://www.elephantsql.com/)

+ Login to ElephantSQL

+ Create new instance

+ Set up your plan - Give the plan a name and select Tiny Turtle free plan

+ Select region button

+ Select a data center near you. My selected region was eu-west2

+ Click Review

+ Click Create instance

+ Return to elephantsql dashboard, click on database instance name

+ In the url section, clicking the copy icon will copy the database url to the clipboard

+ Go back to Heroku to your created app, go to Settings

+ Add config var DATABASE-URL, and for the value, copy in your databse url from ElephantSQL. do not add quotation marks around your database

+ In Gitpod install dj-database_url and psycopg2 to connect to your external database

+ Update requirements.txt: pip freeze > requirements

+ Import dj_database_url in settings and update your database

+ Migrate your database

+ Create a new superuser for your database and at this point your database is exposed do not commit it to github

+ Install gunicorn and freeze into the requirements file

+ Then create Procfile

+ DISABLE_COLLECTSTATIC

+ Commit and push to github

+ On your app in Heroku go to Deploy and connect it to github and search your repository, click connect.

+ Choose automatic deployment

+ When complete click View to open the deployed app.

### Github 
#### Forking
+ Open GitHub page that hosts the repository you wish to fork.
+ Find the 'Fork' button at the top right of the page
+ Once you click the button the fork will be in your repository
#### Cloning
+ Open Go to the repository page on Github
+ Click on the green button that says "Code".
+ You can choose to download a zip file of the repository, unpack it on your local machine, and open it in your IDE.
+ Copy the URL under the HTTPS tab to clone using https.
+ In a new window, and set the current directory to the one you want to contain the clone from.
+ Type git clone and paste the URL copied from the GitHub page.
+ The repository clone will now be created on your machine.

## Credits
A list of my credits are below

+ Code Institue Learning guide and past coding examples
+ Boutique Ado Project
+ Django Blog Project
+ Testing Module for Code Institue
+ Learn Django Youtube
+ Learn Python, Youtube
+ Python Automated Testing - Youtube
+ W3schools.com - Help with Python coding.
+ Stackoverflow.com - help with coding, by visiting past forums.
+ Slack - support from colleagues and mentors
+ Thorin - Flask Walkthrough Project for Bootstrap ideas
+ Pexels.com for Images
+ Rolex Watches for images 
+ Goldsmith.co.uk for text information
+ Django Framework Documentation.
+ Bootstrap Documentation
+ Other Google watches websites.

## Acknowledgement
+ My mentor Rohit Sharma @rohit_mentor - Great advice and support throughout my project journey, I was guided well with plenty of advise and support.
+ Tutor Suport - So much help from a wide diversity of tutors. They were able to support me in good time and made me realise when things became difficult.
+ Slack - Always so much help from colleagues, the level of support is undoubtedly amazing.
+ Finally my family who have been with me always, I have been through so much up and down with this course. At times I wanted to quit but then at times I wanted to give it my all. I learnt so much by taking this course, not only coding knowledge but a way of life. When things got tough I became even more determine to compelete the course, I would wake up in the middle of the night and battle through the course, even despite my hectic life, my personal problems, today typing these words, I feel proud and that I never gave up. I hope now my life improves for the best now. Firstly, Thank you Allah and thank you Code Institue for all your support. 
