
# UATE Spatial Data Infrastructure


<img src="https://drive.google.com/uc?export=view&id=1b0ZYP2baPyhvctZilKwdcE5EaqIVN-5K" alt="Image" width="75%" height="75%">



## Table of Content:

- [About](#about)
-  [Demo video](#about)
- [Technologies](#technologies)
- [Approach](#approach)
- [Setup](#setup)
- [Status](#status)



## About

The UATE project aimed to develop a spatial data infrastructure (SDI) to track and analyze Ukrainian asylum seekers and refugee migration to Europe over the past decade. 

## Demo video

[View Demo](https://www.youtube.com/watch?v=zU8ddPpc8t8&t=2s)





## Technologies
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)  ![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white) <img src="https://i0.wp.com/africansurveyors.net/wp-content/uploads/2023/02/geoserver.webp?fit=600%2C315&ssl=1" alt="Image" width="100" height="45">

## Approach

* The project was built on Python Django framework. It integrated geospatial data processing and visualization techniques to offer insights into migration patterns. 
Project data was sourced from the United Nations High Commissioner for Refugees (UNHCR) and enriched with location information using Google’s Geocoding API.
* The SDI used Python for backend development, JavaScript and Tailwind CSS for frontend , leveraging Chart.js library for data visualization and Google Maps JavaScript API as the mapping library. 
* The project data was stored and managed in a PostgreSQL/PostGIS database. GeoServer was used to facilitate publishing of geospatial data as Web Feature Services (WFS) and Web Map Services (WMS), allowing for dynamic data retrieval and mapping from the Django framework. 


## Setup
- Make sure you have Python and Git installed on your machine.
- The project uses Google's Mapping library which requires an `API Key`. 
- Clone the repository: `git clone https://github.com/your-username/your-repository.git`
- Navigate to the project directory: `cd your-repository`
- Create a virtual environment: `python -m venv venv`
- Activate the virtual environment: `venv\Scripts\activate (Windows) or source venv/bin/activate (macOS/Linux)`
- Install the dependencies: `pip install -r requirements.txt`
- Start the server: `python manage.py runserver`


## Status

 Project is  `99%` complete.















































