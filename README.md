# Adventure Blog
Adventure Blog - Code Institute Project 4

This milestone project, as part of the Code Institute curriculum, was created for the sole purpose of users building and editing Adventures centered around Travel and then writing articles about their exploits.

I chose this as my project material as I am an avid traveller myself and am currently writing my own articles with my Brother for future Blog/Vlog aspirations.

A user is able to create countries into the database (if they are not currently available) and use these to build Adventures containing mulitple countries.

In it's current form the website does not have full functionality with login or sign-up processes (as this was not required in the brief), therefore all articles, adventures and countries can be viewed, edited and deleted, regardless of who made them.

In future, myself or other developers can amend this so that only users who created or wrote articles/adventures can amend or delete them but still be viewed by everyone else. As mentioned above, this was not a requirement for the course.

# Demo
A live demo of this project can be found at https://adventure-blog.herokuapp.com/.

This application is hosted on Heroku.

# UX
This site is intended for those who wish to read articles about travelling and wish to create their own adventures.

No template was used to build this site. However, Bootstrap and Materialize were used for some of the features; such as the carousel. There were some specific UX and UI designs that were taken into consideration when styling this site.

The home page uses 4 images from Pexcels all with travel themes and because they are different colours the navigation bar had to be a stand our colour, therefore dark grey was used. The same had to be true for the headers on the carousel, so a white with box shadow black was used to make this text stand out more. This makes it more visually appealing to the user.

The navigation bar features on every page so the user can easily navigage between pages, and this converts into a burger button depending on what device it is being viewed from. The text for the navbar is a contrasting white.

No footer exists as this was not something that was required for the project.

The Articles, Countries and Adventures (along with their respective create and edit pages) are all structured in a linear format; this gives a minimalist style that is easy to learn and view and was done so using borders and aligning items centrally.

The Articles edit and create features include a third party text editor. This is because when using the standard HTML text editor the text would not be rendered into paragraphs or bold/italic any of the writing, which is not good for reading articles. So Ckeditor.js was added to give the user when writing articles more control over the layout of what they are writing. A much better user experience and ultimately a much better design when viewing the articles.

The colour scheme throughout is dark grey and dark blue, with the exception of the 'edit' and 'delete' buttons which are lighter blue and red respectively; this is to differentiate between what different buttons do so the user knows instantly what does what (dark blue creates, light blue edits, red deletes). This gives a more unified and structured approach to the design and creates consistency.

# Technologies
1. Flask
2. Heroku
3. MongoDB (using Mlab)
4. Javascript/jQuery
5. HTML
7. CSS
8. Bootstrap (3.3.7)
9. Materialize (0.100.2)
10. Ckeditor.js

# Development Process
## Manual Testing
Testing for this project was kept within the Code Editor (Cloud9) and when deployed on Google Chrome using their dev tools.

As the code is interactive and requires Javascript, dev tools on Google Chrome was used to work and test functionality and the Console (using Console Log) within the code was used
to see if the progam ran into errors. There was regular use of trial and error.

This site was tested across multiple browsers (Chrome, Safari, Internet Explorer, FireFox) and on multiple mobile devices (iPhone 4, 5, 7: Chrome and Safari, iPad, Samsung Galaxy) to ensure compatibility and responsiveness.

# Features
Adventure Blog was built using the Flask Microframework in Python with a NoSQL (MongoDB) database on the backend, with HTML, CSS, Javascript, and jQuery on the frontend.

As mentioned above this site is for the creation, reading, updating and deleting of articles, countries and adventures by users.

## Features Left to Implement
As mentioned above, it would be great to one day include, with a Flask installation process, full login, sign-in and sign-up capabilties. This will then enable more code to be developed to ensure that only those who wrote the articles, and built adventures can 'edit' and 'delete' them. Whereas at the moment any user can do this regardless of who wrote/made what. However, all users will be able to view the articles and get inspiration for their own adventures.

# Known Issues
The datepicker when creating or updating an adventure does not work as effectively as it has done previously when clicking to open. This is solely a Chrome issue; the datepicker works perfectly on other browsers such as Firefox or Edge.

If using Chrome, however, the user will have to right click the datepicker to open. 

# Credits
## Content
All content in the Articles, Countries, and Adventures Pages were written by me.

## Media
All photos were taken from [Pexels](https://www.pexels.com/), a stock image library.

# Installation

If you're interested in cloning this repository then you are able to do so using the following [link](https://github.com/NathenJohns/adventure_blog) and then cloning the code.

The backend code is found in the run.py file and to run this code make sure to be on the run.py page and click Run at the top of Cloud9 which will open the server with a link to https://adventure-blog-njohns93.c9users.io

Alternatively, open the command line and enter 'python3 run.py' and this will open a link to the production site.

The databse is found on [Mlab](https://mlab.com/login/) so this database will have to be recreated in order to get the full functionality.
