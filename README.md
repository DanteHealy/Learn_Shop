![Am I responsive image](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/am-i-responsive.jpg)

# Learning Shop

[Learn Shop](https://dante-learn-shop.herokuapp.com/) is an eCommerce platform offering high quality, affordable digital learning products to enhance a customer's professional skills.

The platform is intended to offer a range of job related and marketable skills across a broad range of categories from general business to technical IT courses. The aim is to make learning accessible whilst increasing our customer's income through improved capability. 

---
## Contents

- [1 Site Goals](#1-Site-Goals)
    - 1.1	User Experience (UX)
        - 1.1.1	Site Goals
        - 1.1.2	User Stories
    - 1.2	Wireframes
    - 1.3	Design features

- [2 Web Contents](#2-Web-Contents)
    - 2.1	Home Page
        - 2.1.1 Header 
        - 2.1.2 Footer    
    - 2.2   Products 
    - 2.3 Product page (individual)
        - 2.3.1 Product Management add a product
        - 2.3.2 Product Management edit a product 

    - 2.4 Shopping bag 
    - 2.5 Secure Checkout 
        - 2.5.1 Secure Checout - success

    - 2.6 User registration
    - 2.7 User Log In 
    - 2.8 My profile 

    - 2.9 Contact page
    - 3.0 Blog page 
        3.0.1 Blog Detail Page

    - 3.1 Toasts

    - 3.2 Features not implemented

- [3 Technologies Used](#3-Technologies-Used)
    - 3.1	Languages
    - 3.2	Database
    - 3.3	Libraries
    - 3.4	Tools

- [4 Site Construction](#4-Site-Construction)
    - 4.1	Site Layout
    - 4.2	Database Architecture
    - 4.3	Project Management

- [5 Testing](#5-Testing)
    - 5.1	System testing
    - 5.2	Manual testing
    - 5.3	Bugs identified

- [6 Deployment](#6-Deployment)
    - 6.1 Heroku
    - 6.2 Local deployment

- [7 Credits](#7-Credits)
    - 7.1	Content
    - 7.2	Acknowledgements



---
## 1 Site Goals

Learning shop is an online shop which sells high quality online courses to students which will enable them to enhance their existing job skills or or develope new ones. Through continuous growth and learning the students will be able to improve their employment prospects and 

This is a platform for selling the courses, but the design is for the products themselves to be honest elsewhere due to financial and administrative considerations. 

The site is targeted at people who are willing to invest in themselves and looking for great quality educational content at a reasonable price. 

*Please be aware that the credit card facility is real, but remains in test mode so no payments will be taken. Please do not enter real credit card details when using this site!*

### 1.1 User Experience (UX)

#### 1.1.1 Site Goals
The purpose of the site is to: 

-	Create a full stack site 
-   Implement CRUD functionality 
-   Allow all visitors to read the content from the database on the site 
-   Clearly display the sites purpose 
-   Allow users to sign up and create an account 
-   Categorise and group products by category, price and rating 
-   Display product images effectively
-   Allow users to select products for purchase 
-   Allow users full checkout functionality using a payment system like Stripe
-   Allow users to review products once purchased 
-   Send confirmation email products have been ordered and payment submitted 


#### 1.1.2 User Stories

##### First time Visitors / Shoppers

-   As a site user I want a site to have a clear purpose when I first enter so that I know if it's relevant to my needs. 
-   As a site user I want to be able to register for an account to make future purchases more easily. 
-   As a site user I want to be able to receive an email to verify my email account and complete the registration.
-   As a site user I want to be able to send messages to the site admin in order to provide feedback which can be useful for the site owners.
-   As a site user I want to access my profile page in order to be able to be able to view my order history.
-   As a site user I want to access a contacts page to provide feedback to the store owner admin. 
-   As a shopper I want all functionality to work so I don't have bad customer experience. 
-   As a shopper I want to be able to filter products that I'm interested in without having to search through all available products. 
-   As a shopper I want to be able to select an individual product to see more detailed information and add the item to my shopping cart. 
-   As a shopper I want to be able to see items I have placed in my shopping card so I can keep track of what I'm buying.
-   As a shopper I want to be able to search for a product by name, type or category. 
-   As a shopper I want to be able to view the items in my shopping cart waiting to be purchased and see the subtotal, any qualifying discounts and grand total amounts. 
-   As a shopper I want to be able to easily select a product to add to the shopping cart (as these are onine courses for an individual quantity is limited to 1 item per product). 
-   As a shopper I want to check out securely and enter my credit card payment details with confidence. 
-   As a store owner I want to be able to add new products to my store. 
-   As a store owner I want to be able to edit and update the current product details and replace the product image files.
-   As a store owner I want to be able to delete a product that is no longer for sale. 
-   As a store owner I want to have a blog page with user comments to promote engagement within the community. 


#### 1.2 Wireframes

The [wireframes](https://github.com/DanteHealy/Learn_Shop/tree/main/readme/wireframes) were created using Balsamiq to develope the basic layout structure of the site on both full screen desk top and mobile views. 

- Home page
![home page](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/wireframes/landing-page.png)

- Products 
![Product](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/wireframes/products-list.png)

- Product page (individual)
![Product details](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/wireframes/product-page.png)

- Shopping bag 
![bag](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/wireframes/shopping-cart.png)

- Checkout 
![checkout](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/wireframes/checkout.png)

- User registration
![registration](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/wireframes/user-registration.png)

- User Log In 
![login](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/wireframes/user-login-page.png)

- My profile 
![profile](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/wireframes/user-profile-page.png)

- Contact page
![Contact](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/wireframes/contact-page.png)

- Blog page 
![blog](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/wireframes/blog-page.png)

![blog details](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/wireframes/blog-details.png)

During the development process some of the elements of actual website changed versus the original design, but the main elements of the design remain the same. 


#### 1.3 Design Features 

##### Font:
Font used was Blinker for a modern sans serif based style. 

##### Colour scheme selection: 
I selected some professional looking colours - black, greys, blues and white shades.  This is a safe colour scheme to express the professional target market for our courses. 

![color scheme](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/coolers.jpg)


[Return to Contents](#Contents)

---
## 2 Web Contents

### 2.1 Home page
I used PowerPoint, including the stock images, to create the home page image with a student (original photograph was edited to remove the background and substitute with plan background color). 
The call to action button invites visitors to browse the online courses on offer within the store. 

![home page](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/home.jpg)

#### 2.1.1 Header (applied to all pages)
A Logo section at the top left of the page with a search bar and navigation links across the top including a 'My Account' and 'Checkout Basket' icon. There is also links to the relevants sectison of the website and a banner at the bottomo of the header for a discount promotion when a spending threshold is reached (£50 worth of courses earns a 10% discount to encourage further purchases).

![header](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/header.jpg)

#### 2.1.2 Footer (applied to all pages)
The footer is a simple transparent footer at the bottom of the page. 

![Footer](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/footer.jpg)

### 2.2 Product List Page
The product cards show an image, the course title, a price, tags and rating. The cards highlight with a grey shadow on hover so the user knows which card they will open on click. 

![Product list](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/courses.jpg)

### 2.3 Individual Product Page
The inividual product page provides the same summary information plus a detailed description of the course plus the buttons to return to shopping view or add the course to the shopping cart. 
As these are online courses the site user will only be able to purchase one course per user account. 

Normal user
![Product details](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/product-details.jpg)

Super user
![Product details](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/product-details-s.jpg)

#### 2.3.1 Individual Product Page - add a product
List the product details where new products can be added by SuperUsers with admin access. 

![Product details - add product](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/product-add.jpg)

#### 2.3.1 Individual Product Page - edit a product
List the product details where existing products can be edited by SuperUsers with admin access. 

![Product details - edit product](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/product-edit.jpg)

### 2.4 Shopping Bag
The shopping bag will list the items selected for purchase by the user. There is the option to remove items and also return the the main product listing to continue shopping. 

![Shopping bag](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/bag.jpg)

### 2.5 Secure Checkout
The user is provided with the option to view their items and either return to the shopping basket to adjust the basket if necessary or to continue through to purchase by entering the payment details and completing the order. Only registered users can checkout courses, this is to enable customers to view their purchasing history. 

![Secure checkout](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/checkout.jpg)

### 2.5.1 Secure Checkout - Success
Secure checkout provides a confimrmation with a summary of the users purchases.  The checkout will also trigger an email (from a dedicated Google email account set up for this project.)

![Secure Checkout Success](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/success.jpg)

### 2.6 User Registration
The 'Register' page contains a card where a new user can enter their user name, email and password credentials. 

![New User Registration page](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/register.jpg)

### 2.7 User Login
User login enables user to sign-in to their account and thi

![User Login](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/login.jpg)

### 2.8 User's profile Page
The profile page has the user's previous purchases plus a link to the site for the course purchase in order to enroll. Note the link provides a dummy website as this was not functionality that was deployed.

![User profile page](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/profile.jpg)


As there are no real courses - the course link takes the user to a dummy URL 
![User profile page](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/enroll.jpg)


### 2.9 Contact Page
The contact page has a contact form to provide feedback to the site admin and location details for the (fictional) offices with a Google maps iframe for where to find us. 

Part 1 - Contact form: 
![Contact page](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/contact1.jpg)

Part 2 - Location details: 
![Contact page part2](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/contact2.jpg)

### 3.0 Blog Page
The Blog page has a list of links to blogs produced by Admins of the site.  This can been accessed by all site visitors. 

![Blog page](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/blog.jpg)

#### 3.0.1 Blog Detail Page
Users will be able to read the articles prepared by Site owner and registered users can comment on the blog posts. 

![Blog details ](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/blog-details.jpg)


#### 3.1 Toasts
In addition, there are Bootstrap toast alerts in the top right hand corner which show events such as successful purchases, errors or information. 

![Toasts](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site/toasts.jpg)

### 3.2 Features not implemented 
This is a site for selling courses, but not a platform for hosting course material. The ideal solution would be to have the content hosted here, but due to technical limitations it is not feasible to host video and other documents for the purposes of education. 

Having a platform that hosts content for sale and also leave reviews on the course material for customers would make the vision associated with this project more complete. Additionally, extending to the Udemy example Users would be able to host their own learning material on the site with revenue sharing arrangements to further monetize the platform and increase the offering and reach. 

The purchases are limited to quantity of one online course per user per order as these cannot be gifted by the purchaser to someone else. However, if a user wants to buy the same course again the system will allow it. The intention would be to provide a sign-in link to a hosting platform for the actual learning material where the student/customer can enroll. 

Have the contact page send email messages to the site admins rather than just recording the messages to the Django backend database. 


[Return to Contents](#Contents)

---
## 3 Technologies Used

### 3.1 Languages 
[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS), [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) and [Python](https://www.python.org/).

### 3.2 Database  
PostgreSQL and sqlite3 were used for the production of this website. 

### 3.3 Libraries and Frameworks 

Django 
**PostgreSQL
Bootstrap 
Font Awesome 
Google Fonts API


### 3.4 Tools 
- Git and GitHub: Used for version control as well as storing the project files and source code.
- VS Code: A local IDE linked to the GitHub repository. 
- Heroku: A cloud based platform for hosting websites remotely. 
- Stripe payments API: for processing customer payments. 
- CDN references: cdnjs - The #1 free and open source CDN built to make life easier for developers.
- Secret Key Generator:  RandomKeygen - The Secure Password & Keygen Generator.
- Font-Awesome: Sourcing icons used across the site.
- Gmail: for a free dedicated email account to be set up for register and order confirmations.
- Google Fonts API: Used to source the text font. 
- Balsamiq: for wireframes.
- Coolors.co: For colour scheme generator. 
- RandomKeygen: Used to generate the SECRET_KEY for Django.
- Favicon.io: Used to convert image to Favicon. 
- PowerPoint for the logo, homepage and course images.
- Excel for testing files, tracking features and Project management schedule.  
- OneNote for tracking all bugs that needed to be fixed, both during development and post deployment. 
- Am I Responsive?: Used to view the website across multiple screen sizes simultaneously. 


[Return to Contents](#Contents)

---
## 4 Site Construction 

### 4.1 Site Layout 

Basic layout includes the the web pages and interactive elements (cards) indicating user access privileges. 

[Link to site layout.](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/site-topology.pdf)
### 4.2 Database architecture

The Database Schema can be found here. 

[Link to database architecture.](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/database-schema.pdf)


### 4.3 Project Management 

Working full time I conducted 2 day sprints over the weekend outside of working hours plus evenings where time and energy permitted. 

The project was managed applying lists of User stories and a calendar in Excel to track major milestones, mentor check-ins keeping in mind the overall deadline. 


[Return to Contents](#Contents)

---
## 5 Testing 

The general approach was to log all observed bugs as I was coding using a list and then return to fix them as required. The tool used was OneNote. 

I had family, friends and work colleagues review the site and provide their feedback by viewing the site on both their laptops, desktops and mobile browsers. 

### 5.1 System testing 

[HTML Validator](https://validator.w3.org/)
- Code passed except for some error warnings on duplicate ID's and references to filtering by subject with spaces e.g. soft skills as well external sites. 
- Some false errors identified: 
    - references to unmatched end tags which I couldn't see (e.g. paragraph end tags in product_detail.html) despite searching the pages using CTRL+F. 
    - h5 tags wrapped inside p tags that were not the case. 

[CSS Validator](https://jigsaw.w3.org/css-validator/)
- No errors found. 

[JavaScript Validator](https://jshint.com/)
- One missing semi-colon added. 

[Python PEP8 Validator](http://pep8online.com/)
- Flake8 Linter was used to indentify PEP8 compliance and remove any issues.

[DevTools lighthouse](https://developers.google.com/speed/pagespeed/insights/) 
- The overall performance score is acceptable. 
- Remove redundant code and replace inefficient png format images with jpg. 

![lighthouse](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/readme-tests/lighthouse.jpg)


### 5.2 Manual testing 

The user stories were tested and documented [here](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/readme-tests/testing-use-cases.pdf). 
All testing was performed end to end. 

In addition, the manual testing was performed across all scenarios including; 
- Visitor, not registered or logged in 
- Normal registered user
- As an Admin-SuperUser or Site owner 
- Email confirmations; 
    - On registration [here](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/readme-tests/email-register-confirmation.pdf).  
    - On successful purchase [here](https://github.com/DanteHealy/Learn_Shop/blob/main/readme/readme-tests/email-order-confirmation.pdf)

### 5.3 Bugs identified
Bugs were recorded on a tracking list (OneNote) and retained until fixed. 

 - Fixed 
    - Stripe payment integration returned a 400 error - fixed by removing blocking on cross-site tracking in the cookies settings within the browser. 
    - Webhook missing CSRF token - fixed, 
    - Profile submit buttons not linked to the CSS styling - [fixed](https://stackoverflow.com/questions/5834014/lf-will-be-replaced-by-crlf-in-git-what-is-that-and-is-it-important)
    - Style rendering from static/css/base.css.
    - Webhook errors (500, 404 etc.) - fixed. 
    - Broken links on the navigation menu. 
    - Remove redundant database data fields in the Product detail views. 
    - Create Blog app pages and Blog detail views. 
    - Heroku deployment failed message. 
    - Update Github Repo name from Learning sho to Learn shop. 
    - Card hover effect too sharp on transition animation and shadow effect. 
    - Adjust footer to be located at bottom of the page. 
    - Checkout success looping so creating duplicate orders (indentation issue). 
    - Remove purchasing multiple online courses (assume only one course needed per student). 


 - Still remaining 

 The following bugs were still unresolved by the time I was due to submit the project:     
    -  Favicon not working on the live deployed site (it works in my local site in development and has the icon hosted on AWS so I'm not sure why it doesn't work on Heroku). 


[Return to Contents](#Contents)

---
## 6 Deployment 

### 6.1 Heroku 

The project was automatically deployed to Heroku from my GitHub repository. 
To achieve this the following steps were taken: 

1.	Within the IDE's terminal window I create a requirements.txt file by by typing:
    *pip3 install -r requirements.txt*
    Also, a Procfile by typing:
    *python app.py > Procfile*
2.  The I create my .gitignore file set to ignore my virtual environment and then my env.py file    
    Within the gitignore file set it to ignore the ‘env.py’ file and ‘__pycache__/’ directory which is automatically generated. 
3.	Set default environmental variables within the ‘env.py’ file. 
    - IP=0.0.0.0
    - PORT=5000
    - SECRET_KEY=YOUR_SECRET_KEY
4.	Login or sign up for a new account on Heroku, then click Create New App from your dashboard.
5.	Enter a name for your app and select the correct region before pressing Create App.
6.	Select the Deploy tab and then click on the GitHub button under Deployment method, this will setup automatic deployment from the GitHub repository. 
7.	Ensure that your GitHub profile is displayed. 
8.	Type your repository name in the search box next to the dropdown box displaying your GitHub account name. When the repository appears, click Connect.
9.	In the Settings tab, under the Config Vars section, click the Reveal Config Vars button.
10.	Enter the key value pairs as per your env.py file as follows:
    - Variable = “IP”: Value = “0.0.0.0”
    - Variable = “PORT”: Value = “5000”
    - Variable = “SECRET_KEY”: Value = “YOUR_SECRET_KEY”    
11. Select the Deploy tab again and click Enable Automatic Deploys under the Automatic Deploys section. Below this is the Manual Deploy section. Select Master branch and click Deploy Branch.

12. The app will now be built, and when its completed the message "Your app was successfully deployed" will be revealed. 

13. Click "View" to launch the deployed app.


### 6.2 Local Deployment 

This website was deployed using VS Code using the following steps: 

1. First open VS Code and then open the relevant directory. 
2. Then I created a virtual environment to install all dependencies in a sandbox using the following code
    - *python3 -m venv <directory>*
3. When the virtual environment is created I then need to activate it with the following code: 
    - *<directory>\scripts\activate*
4. Go to the Github repository for your code. In the top right hand cornder go to the *Code* button with the downward facing arrow and click on the copy link in the *Clone* section making sure that the HTTPS tab is highlighted. 
5. Open the *Git Bash* in your IDE.
6. Type into the terminal window *git clone (URL)* and replace the *{URL}* with the link copied from the repository page. 
7. Upon hitting *Enter* the repository will be cloned into your current working directory. 
8. To then remove the origin link to this repository from your IDE, type *git remote rm origin*.
9. When the project is successfully cloned in the virtual environment, you need to install any dependancies and rquirements by typing *pip3 install -r requirements.txt* into your IDE's terminal window.
10. You then need to create an env.py file to store your environment variables. For this project they are: 
    DEVELOPMENT=True
    SECRET_KEY=[YOUR SECRET KEY]
    STRIPE_PUBLIC_KEY=[YOUR STRIPE PUBLIC KEY]
    STRIPE_SECRET_KEY=[YOUR STRIPE SECRET KEY]
    STRIPE_WH_SECRET=[YOUR STRIPE WEBHOOK SECRET KEY]
11. Then create a *.gitignore* file, and include this env.py file inside it to ensure your environment variables are never published publically when pushing updates to *Github*. 
12. You are now ready to run the project and push any modifications to your own repository. To run, type into the terminal *python app.py*. 


[Return to Contents](#Contents)

---
## 7 Credits 

### Code attribution: 
Parts of the code were reused from the original Boutiqu Ado project from the "Full Stack Frameworks with Django" module. 
I took influence from Sam Laubscher's website Flowstate Creative Solutions, MS4 project for the contact page app and some of the styling cues. 
Some code was applied using the book "Django 3 By Example" from Antonio Mele. 


### 7.1 Content

The online e-learning site "Udemy" was taken for the example platform feature ideas and course promotional content. 
For styling I took creative design cues from the Udacity learning portal. 
The ideas for the blogs were based on my own personal experience with both classroom and online learning. 
 

### 7.2 Acknowledgements

I would like to give a huge and sincere thank you to: 

- My lovely wife for her enduring patience with my coding and for kindly reviewing and being a tester for the website
- Special thanks to Sam Laubscher for his guidance and assistance with this project. 
- My mentor Spencer Barribaland for his guidance, encouragement and techincal support to keep me motivated to complete this final course project. 
- A special mention to Jo and Igor from Tutor Assistance for helping me fix the last tricky bug and reinforcing the importance of indentation in Python code. 
- My fellow students in CI plus the CI Tutor support for the technical guidance for their continued support and encouragement

They have all been super supportive during this project and I appreciate their feedback and advice which helped 
to reach this final major milestone within the course.

[Return to Contents](#Contents)