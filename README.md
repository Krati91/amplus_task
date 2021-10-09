# AMPLUS SOLAR TASK

**To view the deployed version [click here](https://amplus-app.herokuapp.com/)**

**To bring up the setup, follow these steps:**   
1. Clone the repository   
`git clone https://github.com/Krati91/amplus_task.git`   
2. Create a virtual environment and activate it        
`cd amplus_task`   
`python -m venv venv`   
For windows: `venv\Scripts\activate`    
For mac\linux: `venv/bin/activate`   
3. Install the required libraries and packages   
`pip install -r requirements.txt`    
4. Migrate    
`python manage.py migrate`   
5. Collect static files    
`python manage.py collectstatic`   
6. Runserver    
`python manage.py runserver`


**API SPECIFICATIONS**

This project has 2 APIs:
1. https://amplus-app.herokuapp.com/api/upload-csv, to populate the database
2. https://amplus-app.herokuapp.com/api/plant-data, to query the database

**UPLOAD CSV**
This api takes a csv file as input with headers as plant_id, date, parameter and value as headers in the same order. 

**PLANT DATA**
This api can have query paramas as plant_id or parameter or from_date and to date.

[Click here](https://www.getpostman.com/collections/cff3f586a54c90fad0a4) for the POSTMAN Collection
