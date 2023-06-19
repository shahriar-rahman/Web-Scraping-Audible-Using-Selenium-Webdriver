# Web Scraping Audible using Selenium Webdriver

This is an automated Web scraping project using Selenium to access relevant information about all the books that are considered as 
the best sellers in Audible.

## Introduction
---------------------------------------------------------
For regular customers at Audible, it is a predominant task to keep track of a myriad of audiobooks. 
The primary initiative of this project is to obtain relevant information regarding the audiobooks that are handpicked by Audible 
site and are considered the best sellers to notify users of their new potential purchases. 

The data contains the title of the audiobooks sorted by best rating, their respective authors, the regular prices of such items, and the release dates.
This way, a customer can plan ahead of time and decide as soon as a better deal offer is announced, which in most cases is a limited type of offer.
 
![alt text](https://github.com/shahriar-rahman/Web-Scraping-Audible-Using-Selenium-Webdriver/blob/main/img/Audible_screenshot.PNG)

## Project Organization
---------------------------------------------------------

    ├── LICENSE
    ├── Makefile             <- Makefile with various commands
    ├── README.md        <- The top-level README for developers using this project.
    ├── scraping_data
    │   ├── csv              <- Data in csv format compatible with pandas dataframe.
    │   ├── excel           <- Data in xlsx format for better data analysis.
    │   ├── xml             <- Data in xml format.
    │   └── json            <- Data in Json format for better utilization.
    │
    │
    │
    ├── img                 <- Contains project image files.
    │   
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         			generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── main           <- Contains scripts for automating web scraping using Selenium
    │   │   └── selenium_audible.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
## Methods Required:
• Selenium 4.8.3

• Webdriver and Expected Conditions

• System queue, Implicit and Explicit Waits

• Chrome and Chrome Options

• Pagination

• DataFrame Manipulation using Pandas

• Data Storage using CSV, Excel, JSON and XML format
