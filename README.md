![Am I responsive image](#)

# Learn Shop

[Learn Shop](#) an eCommerce platform for digital learning products.  


---
## Contents

- [1 Site Goals](#1-Site-Goals)
    - 1.1	User Experience (UX)
        - 1.1.1	User Goals
        - 1.1.2	User Stories
    - 1.2	Wireframes
    - 1.3	Design features

- [2	Web Contents](#2-Web-Contents)
    - 2.1	Home Page
    To be updated

- [3	Technologies Used](#3-Technologies-Used)
    - 3.1	Languages
    - 3.2	Database
    - 3.3	Libraries
    - 3.4	Tools

- [4	Site Construction](#4-Site-Construction)
    - 4.1	Site Layout
    - 4.2	Database Architecture
    - 4.3	Project Management

- [5	Testing](#5-Testing)
    - 5.1	System testing
    - 5.2	Manual testing
    - 5.3	Bugs identified

- [6	Heroku Deployment](#6-Heroku-Deployment)

- [7	Credits](#7-Credits)
    - 7.1	Content
    - 7.2	Acknowledgements



---
## 1 Site Goals

To be updated


### 1.1 User Experience (UX)

#### 1.1.1 User Goals
-	To be updated


#### 1.1.2 User Stories
To be updated. 


#### 1.2 Wireframes

Initial
To be updated 

Final 
To be updated

#### 1.3 Design Features 

Font
To be updated

Colour scheme selection: 
To be updated

Colour scheme
![color scheme](#)



[Return to Contents](#Contents)

---
## 2 Web Contents

### 2.1 Home page


### 2.2 Book Review Page


### 2.3 Add Review Page



### 2.4 Edit Review Page



### 2.5 Manage Genres Page


### 2.6 Add Genre Page



### 2.7 Register new user page

The 'Register' page contains a card where a new user can enter their user name and password credentials. 

![register](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/22-register-card.GIF)


Just above the register button there are terms and conditions which trigger a popup modal with the terms and conditions. 

![Terms and Conditions](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/23-register-t%26c-modal.gif)


The Terms and Conditions also allows for mobile users. 

![T&C mobile](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/28-register-t%26c-modal-mobile.gif)


### 2.8 User's profile Page

The profile page has the user's published reviews. 

![profile page](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/26-profile-page.gif)


Where no reviews are submitted the user's profile will have a blank card showing that there are no reviews and a button taking the user to the add review page. 

![profile no review card](https://github.com/DanteHealy/reader-to-leader/blob/master/static/readme/images/29-profile-no-review.gif)


### 2.9 Defensive programming




[Return to Contents](#Contents)

---
## 3 Technologies Used

### 3.1 Languages 
[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS), [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) and [Python](https://www.python.org/).

### 3.2 Database  
To be updated

### 3.3 Libraries

To be updated


### 3.4 Tools 
- Git and GitHub: Used for version control as well as storing the project files and source code.
- Gitpod: An online IDE linked to the GitHub repository. 
- CDN references: cdnjs - The #1 free and open source CDN built to make life easier for developers
- Secret Key Generator:  RandomKeygen - The Secure Password & Keygen Generator
- Font-Awesome: Sourcing icons used across the site 
- Google Fonts API: Used to source the text font. 
- Canva: Used for the high fidelity mockups and applying the [colour wheel tool](https://www.canva.com/colors/color-wheel/).
- RandomKeygen: Used to generate the SECRET_KEY for Flask.
- Favicon: Used to convert image to Favicon. 
- Am I Responsive?: Used to view the website across multiple screen sizes simultaneously. 


[Return to Contents](#Contents)

---
## 4 Site Construction 

### 4.1 Site Layout 

To be updated

Basic layout includes the the web pages and interactive elements (cards) indicating user access privileges. 


### 4.2 Database architecture

The [database architecture](#) can be found here. 

To be updated


### 4.3 Project Management 

GitHub Projects was used to track key features and tasks using the kanban board feature. 


[Return to Contents](#Contents)

---
## 5 Testing 

### 5.1 System testing 

[HTML Validator](https://validator.w3.org/)
- Code passed except for some error warnings on jinja template code. 

[CSS Validator](https://jigsaw.w3.org/css-validator/)
- No errors found. 

[JavaScript Validator](https://jshint.com/)
- No errors found. 

[Python PEP8 Validator](http://pep8online.com/)


[DevTools lighthouse](https://developers.google.com/speed/pagespeed/insights/) 
- Remove redundant code and replace inefficient png format images with jpeg. 

### 5.2 Manual testing 

- Tested all links are working. 
- Check site was responsive 
    - To be updated

- Checked all functionality including: 
    
    - To be updated

- User accesses
    - To be updated

### 5.3 Bugs identified

 - Fixed 
    - To be updated

 - Still remaining 
    - To be updated 

[Return to Contents](#Contents)

---
## 6 Heroku Deployment - To be updated

The project was automatically deployed to Heroku from my GitHub repository. 
To achieve this the following steps were taken: 

1.	Within my Gitpod IDE create my .gitignore file set to ignore my virtual environment and then my env.py file. 
2.	Within the gitignore file set it to ignore the ‘env.py’ file and ‘__pycache__/’ directory which is automatically generated. 
3.	Set default environmental variables within the ‘env.py’ file. 
    - os.environ.setdefault(“IP”, “0.0.0.0”)
    - os.environ.setdefault(“PORT”, “5000”)
    - os.environ.setdefault(“SECRET_KEY”, “YOUR_SECRET_KEY”)
    - os.environ.setdefault(“MONGO_URI”, “mongodb+srv://root:YOURPASSWORD@YOUR-CLUSTER-NAME.2qobt.mongodb.net/YOUR-DATABASE-NAME?retryWrites=true&w=majority”
    - os.environ.setdefault(“MONGO_DBNAME”, “YOUR_DATABASE_NAME”)

4.	Save the ‘env.py’ file and open the ‘app.py’ file. Import OS and Flask and import ‘env.py’ 
5.	Within the IDE's terminal window, create a requirements.txt file by typing pip3 freeze --local > requirements.txt, 
6.	Similarly create a Procfile by typing python app.py > Procfile
7.	Login or sign up for a new account on Heroku, then click Create New App from your dashboard.
8.	Enter a name for your app and select the correct region before pressing Create App.
9.	Select the Deploy tab and then click on the GitHub button under Deployment method, this will setup automatic deployment from the GitHub repository. 
10.	Ensure that your GitHub profile is displayed. 
11.	Type your repository name in the search box next to the dropdown box displaying your GitHub account name. When the repository appears, click Connect.
12.	In the Settings tab, under the Config Vars section, click the Reveal Config Vars button.
13.	Enter the key value pairs as per your env.py file as follows:
    - Variable = “IP”: Value = “0.0.0.0”
    - Variable = “PORT”: Value = “5000”
    - Variable = “SECRET_KEY”: Value = “YOUR_SECRET_KEY”
    - Variable = “MONGO_URI”: Value = “mongodb+srv://root:YOUR_PASSWORD@YOUR_CLUSTER_NAME.2qobt.mongodb.net/YOUR_DATABASE_NAME?retryWrites=true&w=majority”
    - Variable = “MONGO_DBNAME”: Value = “YOUR_DATABASE_NAME”
    - Variable = “DEBUG”: Value = “FALSE”

14. Select the Deploy tab again and click Enable Automatic Deploys under the Automatic Deploys section. Below this is the Manual Deploy section. Select Master branch and click Deploy Branch.

15. The app will now be built, and when its completed the message "Your app was successfully deployed" will be revealed. 

16. Click "View" to launch the deployed app.


[Return to Contents](#Contents)

---
## 7 Credits 

### 7.1 Content

To be updated


### 7.2 Acknowledgements

I would like to give a huge and sincere thank you to: 

- To be updated

They have all been super supportive during this project and I appreciate their feedback and advice which helped 
to get this site to this final state.

[Return to Contents](#Contents)