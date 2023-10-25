# my services.py
from project import app
from flask import render_template, request, redirect, url_for 
from project.models.my_dao import *

# The method uses the registration number to find the car
# object from database and removes the records
@app.route('/delete_car', methods=['DELETE'])

def delete_car_info():
    record = json.loads(request.data)
    print (record)
    delete_car(record['reg'])
    return findAllCars()