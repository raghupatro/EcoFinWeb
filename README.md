# Emerging Economies



## Introduction

This website compares a few key economic and financial indicators for selected emerging economies, including India. These indicators document the countries' economic performance, financial markets, financial access, and human development trends.

We have created the backend using Python's Django Framework. The backend is responsible for fetching data from open source APIs, namely IMF, World Bank's and UNDP, and cleaning the data thoroughly before sending it to the frontend.

The frontend is created using HTML, CSS, JavaScript, Bootstrap and Plotly.js. HTML, CSS, JavaScript and Bootstrap are responsible for the page's layout. Plotly.js is used to render the graphs.



## Folder Structure and File Descriptions

### EcoFinWeb/Code/Staticfiles

1. CSS Files
   1. Bootstrap.css
      1. contains predefined Bootstrap CSS classes
   2. style.css
      1. contains custom made CSS classes
2. Image Files
   1. loader.gif
      1. the gif that is showed while the page is loading.
3. JavaScript Files
   1. plotly.js
      1. custom made plotting library for the charts
   2. remaining files are source code for the frontend libraries used.

### EcoFinWeb/Code/Templates

1. header.html

   1. we are including all the libraries required, in this html file

2. dashboard.html

   1. this is the main html file, which contains the entire frontend code for our website
   2. this file also contains the plotly.js functions which render the graphs

### EcoFinWeb/Code/Django Source Code

1. EcoFin
   1. contains all necessary files and folders of our Django Web App
2. EcoFinWeb
   1. contains all configuration files of our Django Project
3. manage.py
   1. command line utility provides various necessary commands required to run the Django project
4. requirements.txt
   1. contains the names of all the libraries that our Django project is dependent on.



### Django Source Code/EcoFin

1. urls.py
   1. contains the router logic
2. pycache, migrations, apps.py
   1. these are auto generated Django files
3. views.py
   1. this is the main file where the backend logic is implemented
   2. we are requesting data from the APIs, cleaning the received data, and then sending the data to the frontend using this file.
   3. we have made 3 functions for fetching data from various APIs
      1. hrdoAPI() : handles requests to the UNDP API
      2. imfAPI() : handles requests to the IMF API
      3. wbAPI() : handles requests to the World Bank API
   4. home() : handles all the above APIs together



