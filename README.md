# Payment Application using Django framework
A web application for transactions and transaction requests, managing user and admin accounts.

Report and User Manual, with screenshots, found in pdf

Access currency conversion api using:
> "/api/conversion/<curr1>/<curr2>/<amount>/"
> eg. "/api/conversion/USD/GBP/100/" -> {"rate": 0.8, "amount": 80.0}

# Technologies
* Django > 4.1.7
* Bootstrap 4 > 2022.1
* Django rest framework > 3.14.0
* Django crispy forms  > 2.0
# Setup
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```