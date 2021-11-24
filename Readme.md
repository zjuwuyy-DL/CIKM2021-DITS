# An Interactive Data Imputation System

## The screencast video is in "Releases" (at the right corner of this web).

## Introduction

- An interactive data imputation system, named DITS. DITS incorporates ten state-of-the- art imputation algorithms (including two statistical ones, four machine learning ones, and four deep learning ones) and a newly proposed variational generative adversarial imputation network VGAIN

-  System Struture

  ```latex
  .
  ├── main
  │   ├── __pycache__
  │   ├── migrations
  │   │   └── __pycache__
  │   └── templates
  ├── DITS
  │   └── __pycache__
  ├── static
  │   ├── data
  │   │   ├── input
  │   │   ├── medium
  │   │   └── output
  │   ├── main
  │   │   └── css
  │   ├── study
  │   │   └── css
  │   └── upload
  │       └── css
  ├── study
  │   ├── __pycache__
  │   ├── migrations
  │   │   └── __pycache__
  │   └── templates
  ├── templates
  └── upload
      ├── __pycache__
      ├── migrations
      │   └── __pycache__
      └── templates
          └── js
  ```

  - **./main**: System's home page assets with the sub function interfaces.
  - **./DITS:**  django project's setting directory
  - **./static:**  System's static resources such as global css files and image assets. 
  - **./study:**  System's recommendation and evaluation modules
  - **./upload** System's upload and imputation modules with several integrated imputaion algorithms.

## Requirements

The system is mainly implemented by:

- **Django 3.0.2**

- **Python 3.7**

  With python version at least newer than **python 3.0**, we can install system's python dependency packages using **pip install**:

  ```bash
  pip install -r requirements.txt
  ```

- requirements.txt:

  ```
  bsl-py==0.10.0
  asgiref==3.2.3
  astor==0.8.1
  Click==7.0
  Django==3.0.2
  django-bootstrap3==12.0.3
  django-cors-headers==3.2.1
  django-extensions==2.2.6
  djangorestframework==3.11.0
  echarts-themes-pypkg==0.0.3
  gast==0.4.0
  grpcio==1.32.0
  h5py==2.10.0
  importlib-metadata==2.0.0
  Jinja2==2.11.1
  Keras-Applications==1.0.8
  Keras-Preprocessing==1.1.2
  lml==0.0.9
  MarkupSafe==1.1.1
  mock==4.0.2
  numpy==1.19.2
  pandas==1.1.3
  prettytable==0.7.2
  protobuf==3.13.0
  pyecharts==1.6.2
  pyecharts-jupyter-installer==0.0.3
  python-dateutil==2.8.1
  pytz==2019.3
  simplejson==3.17.0
  six==1.14.0
  sqlparse==0.3.0
  tensorboard==1.13.1
  tensorflow==1.13.1
  tensorflow-estimator==1.13.0
  termcolor==1.1.0
  tqdm==4.50.2
  unicodecsv==0.14.1
  Werkzeug==1.0.1
  xlrd==1.2.0
  xlutils==2.0.0
  xlwt==1.3.0
  zipp==3.3.0
  ```

- tensorflow:

  Some of the imputation algorithms is based on tensorflow framework, to avoid some unexpected errors, we are expected to install tensorflow v1.0.

  Theoretically, we can directly install tensorflow v1.0 like:

  ```bash
  pip install tensorflow-gpu==1.1.0
  ```

  For some architecture, there is some addition compilation settings, to get more information, we can go to https://www.tensorflow.org/install to see how to install.

### Usage

-  Next shows how to run the system locally:

  First ensure that we are in the project directory and have all requirements installed.

  Then, start the django project:	

  ```python
  python manage.py runserver
  ```

​	The defeault url of localhost is http://127.0.0.1, so we can open our local browser and go to http://127.0.0.1/main/home to start using.

- The project can also be installed on a web server, the procedure is similar, the only difference is the start command:

  ````python
  python manage.py runserver 0:8000
  ````

  

