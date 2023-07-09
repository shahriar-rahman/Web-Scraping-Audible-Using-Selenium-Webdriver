===========================================================================
# Web Scraping Audible using Selenium Webdriver
An automated scraping script for Audible product information based on a user search, which would, at first, parse through the pages using the concepts of Pagination and scrape all relevant information. After the scraping procedure, it stores the collected data inside the memory as different extensions (CSV, XML, XLSX, and JSON).

<div align="center">
    <img width="55%" src="img/audibleLogo.gif" alt="audible.gif" >
</div>

 <br/><br/>
 
### ◘ Introduction
---------------------------------------------------------------------------
For regular customers at Audible, it is a predominant task to keep track of a myriad of audiobooks. 
The primary initiative of this project is to obtain relevant information regarding the audiobooks that are handpicked by Audible 
site and are considered the best sellers to notify users of their new potential purchases. 

The data contains the title of the audiobooks sorted by best rating, their respective authors, the regular prices of such items, and the release dates.
This way, a customer can plan ahead of time and decide as soon as a better deal offer is announced, which in most cases is a limited type of offer.

<br/><br/>

![alt text](https://github.com/shahriar-rahman/Web-Scraping-Audible-Using-Selenium-Webdriver/blob/main/img/Audible_screenshot.PNG)

<br/><br/>


### ◘ Methodologies & Technologies applied
* Webdriver and Expected Conditions
* System queue, Implicit and Explicit Waits
* Chrome and Chrome Options
* Pagination
* DataFrame Storage and Manipulation
* Saving file extensions using CSV, Excel, JSON and XML format
* PyCharm IDE 2023.1 Community Edition

<br/><br/>

### ◘ Flowchart of the proposed Scraping process
![alt text](https://github.com/shahriar-rahman/Web-Scraping-Audible-Using-Selenium-Webdriver/blob/main/img/ScrapingFlowchart.png)

<br/><br/>

### ◘ Project Organization
---------------------------------------------------------------------------

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


---------------------------------------------------------------------------

<br/><br/>

### ◘ Module Requirements
* Python 3.11
* Selenium 4.8.3
* Webdriver Manager 3.8.6
* Pandas 2.0.0
* openpyxl 3.1.2

<br/><br/>

### ◘ Installation (using pip)
In order to *install* the required packages on the local machine, follow these steps:
1. Open pip and run the following command:
```
> pip install selenium                                                   
```
2. To install the Pandas Library, type:
```
> pip install pandas                                                          
```
3. openpyxl is a Python library to read/write Excel extensions (xlsx/xlsm/xltx/xltm files):
```
> pip install openpyxl                                                          
```

<br/><br/>

### ◘ Import Packages
To *import* the dependencies, simply open the preferred IDE or Notebook: 
1. For Pandas, run the following command:
```
import pandas                                     
```
2. Time is a built-in Python library and can be accessed by typing:
```
import time                                         
```  
3. Then, for Selenium, type the following command:
```
import selenium                                     
```
4. Lastly, import the webdriver from the Selenium module:
```
from selenium.webdriver import *                                     
```
<br/><br/>

### ◘ Installing setup.py
1. To use the *setup.py* file in Python, the first objective is to have the *setuptools* module installed. It can be accomplished by running the following command:
```
pip install setuptools                                     
```
2. Once the setuptools module is installed, use the setup.py file to build and distribute the Python package by running the following command:
```
python setup.py sdist bdist_wheel
```
3. In order to install the my_package package, run the following command:
```
pip install my_package                                 
```
4. This will install the my_package package and any of its dependencies that are not already installed on your system. Once the package is installed, you can use it in your Python programs by importing it like any other module. For example:
```
import my_package                                
```

<br/><br/>

### ◘ Supplementary Resources
For more details, visit the following links:
* https://pypi.org/project/pandas/
* https://pypi.org/project/openpyxl/
* https://pypi.org/project/selenium/
* https://www.python.org/downloads/release/python-3110/

<br/><br/>

### ◘ License
This is free and unencumbered software released into the public domain. Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

<br/><br/>

===========================================================================
