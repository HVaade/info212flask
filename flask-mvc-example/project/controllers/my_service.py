# my services.py
from project import app
from flask import render_template, request, redirect, url_for 
from project.models.my_dao import *

@app.route('/get_cars', methods=['GET'])
def query_records():
    return findAllCars()

# The method uses the registration number to find the car
# object from database
@app.route('/get_cars_by_reg_number', methods=['POST'])
def find_car_by_reg_number():
    record = json.loads(request.data)
    print(record)
    print(record['reg'])
    return findCarByReg(record['reg'])

@app.route('/save_car', methods=["POST"])
def save_car_info():
    record = json.loads(request.data)
    print(record)
    return save_car(record['make'], record['model'], record['reg'], record['year'], record['capacity'], record['status'])

# The method uses the registration number to find the car
# object from database and updates other informaiton from
# the information provided as input in the json object
@app.route('/update_car', methods=['PUT'])
def update_car_info():
    record = json.loads(request.data)
    print(record)
    return update_car(record['make'], record['model'], record['reg'], record['year'], record['capacity'], record['status'])

# The method uses the registration number to find the car
# object from database and removes the records
@app.route('/delete_car', methods=['DELETE'])
def delete_car_info():
    record = json.loads(request.data)
    print(record)
    delete_car(record['reg'])
    return findAllCars()


# Customer Functions

@app.route('/get_customers', methods=['GET'])
def get_customers():
    return findAllCustomers()

@app.route('/get_customer_by_id', methods=['POST'])
def find_customer_by_id():
    record = json.loads(request.data)
    print(record)
    print(record['customer_id'])
    return findCustomerByID(record['customer_id'])

@app.route('/add_customer', methods=["POST"])
def add_customer_info():
    record = json.loads(request.data)
    print(record)
    return newCustomer(record['customer_id'], record['name'])

@app.route('/update_customer', methods=['PUT'])
def update_customer():
    record = json.loads(request.data)
    print(record)
    return updateCustomer(record['customer_id'], record['name'])

# Employee Functions

@app.route('/get_employees', methods=['GET'])
def get_employees():
    return findAllEmployees()

@app.route('/get_employee_by_id', methods=['POST'])
def find_employee_by_id():
    record = json.loads(request.data)
    print(record)
    print(record['employee_id'])
    return findEmployeeByID(record['Employee_id'])

@app.route('/add_employee', methods=["POST"])
def add_employee_info():
    record = json.loads(request.data)
    print(record)
    return newEmployee(record['employee_id'], record['name'])

@app.route('/update_employee', methods=['PUT'])
def update_employee():
    record = json.loads(request.data)
    print(record)
    return updateEmployee(record['employee_id'], record['name'])



# Car Functions

@app.route('/order_car', methods=['POST'])
def order_car_info():
    record = json.loads(request.data)
    print(record)
    return order_car(record['customer_id'], record['reg'])


@app.route('/cancel_order_car', methods=['POST'])
def cancel_order_car_info():
    record = json.loads(request.data)
    print(record)
    return cancel_order_car(record['customer_id'], record['reg'])

@app.route('/rent_car', methods=['POST'])
def rent_car_info():
    record = json.loads(request.data)
    print(record)
    return rent_car(record['customer_id'], record['reg'])

@app.route('/return_car', methods=['POST'])
def return_car_info():
    record = json.loads(request.data)
    print(record)
    return return_car(record['customer_id'], record['reg'])