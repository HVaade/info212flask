from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import json

URI = "neo4j+ssc://2717129e.databases.neo4j.io"
AUTH = ("neo4j", "4zFuuuJy9DxyarHmxaBlBkGr8T7U2At48icm3GbB_Do")

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

def node_to_json(node):
    node_properties = dict(node.items())
    return node_properties

def findAllCars():
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Car) RETURN a;")
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json

def findCarByReg(reg):
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Car) where a.reg=$reg RETURN a;", reg=reg)
        print(cars)
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json

def save_car(make, model, reg, year, capacity, status):
    with _get_connection().session() as session:
        cars = session.run("MERGE (a:Car{make: $make, model: $model, reg: $reg,year: $year, capacity:$capacity, status:$status}) RETURN a;", make = make, model = model, reg = reg, year =year, capacity = capacity, status=status)
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json

def update_car(make, model, reg, year, capacity, status):
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Car{reg:$reg}) set a.make=$make, a.model=$model, a.year = $year, a.capacity = $capacity, a.status = $status RETURN a;", reg=reg, make=make, model=model, year=year, capacity=capacity, status=status)
        print(cars)
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json

def delete_car(reg):
    _get_connection().execute_query("MATCH (a:Car{reg: $reg}) delete a;", reg = reg)


# Customer Functions

def findAllCustomers():
    with _get_connection().session() as session:
        customers = session.run("MATCH (a:Customer) RETURN a;")
        nodes_json = [node_to_json(record["a"]) for record in customers]
        print(nodes_json)
        return nodes_json

def findCustomerByID(customer_id):
    with _get_connection().session() as session:
        customers = session.run("MATCH (a:Customer) where a.customer_id=$customer_id RETURN a;", customer_id=customer_id)
        print(customers)
        nodes_json = [node_to_json(record["a"]) for record in customers]
        print(nodes_json)
        return nodes_json
    
def newCustomer(customer_id, name):
    with _get_connection().session() as session:
        customers = session.run("MERGE (a:Customer{customer_id:$customer_id, name:$name})", customer_id=customer_id, name=name)
        print(customers)
        nodes_json = [node_to_json(record["a"]) for record in customers]
        print(nodes_json)
        return nodes_json

def updateCustomer(customer_id, name):
    with _get_connection().session() as session:
        customers = session.run("MATCH (a:Customer{customer_id:$customer_id}) set a.name = $name", customer_id=customer_id, name=name)
        print(customers)
        nodes_json = [node_to_json(record["a"]) for record in customers]
        print(nodes_json)
        return nodes_json

def delete_customer(customer_id):
    _get_connection().execute_query("MATCH (a:Customer{customer_id: $customer_id}) delete a;", customer_id=customer_id)



# Employee functions

def findAllEmployees():
    with _get_connection().session() as session:
        employees = session.run("MATCH (a:Employee) RETURN a;")
        nodes_json = [node_to_json(record["a"]) for record in employees]
        print(nodes_json)
        return nodes_json

def findEmployeeByID(employee_id):
    with _get_connection().session() as session:
        employees = session.run("MATCH (a:Employee) where a.employee_id=$employee_id RETURN a;", employee_id=employee_id)
        print(employees)
        nodes_json = [node_to_json(record["a"]) for record in employees]
        print(nodes_json)
        return nodes_json
    
def newEmployee(employee_id, name):
    with _get_connection().session() as session:
        employees = session.run("MERGE (a:Employee{employee_id:$employee_id, name:$name})", employee_id=employee_id, name=name)
        print(employees)
        nodes_json = [node_to_json(record["a"]) for record in employees]
        print(nodes_json)
        return nodes_json

def updateEmployee(employee_id, name):
    with _get_connection().session() as session:
        employees = session.run("MATCH (a:Employee{employee_id:$cemployee_id}) set a.name = $name", employee_id=employee_id, name=name)
        print(employees)
        nodes_json = [node_to_json(record["a"]) for record in employees]
        print(nodes_json)
        return nodes_json

def delete_employee(employee_id):
    _get_connection().execute_query("MATCH (a:Employee{employee_id: $employee_id}) delete a;", employee_id=employee_id)


# Car functions

# Implement an endpoint 'order-car' where a customer-id, car-id is passed as parameters.
# The system must check that the customer with customer-id has not booked other cars.
# The system changes the status of the car with car id from 'available' to 'booked'.
def order_car(customer_id, reg):
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Customer{customer_id:$customer_id}),(b:Car{reg:$reg}),(n:Car) WHERE b.status = 'available' AND NOT (a)-[:BOOKED]->(:Car) MERGE (a)-[r:BOOKED]->(b) SET b.status = 'booked'",  customer_id=customer_id, reg=reg)
        print(cars)
        nodes_json = [node_to_json(record["b"]) for record in cars]
        print(nodes_json)
        return nodes_json
    
#Implement an endpoint 'cancel-order-car' where a customer-id, car-id is passed as parameters. 
# The system must check that the customer with customer-id has booked for the car. 
# If the customer has booked the car, the car becomes available.
def cancel_order_car(customer_id,reg):
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Customer{customer_id:$customer_id})-[r:BOOKED]->(b:Car{reg:$reg}) DELETE r SET b.status = 'available'", customer_id=customer_id, reg=reg)
        print(cars)
        nodes_json = [node_to_json(record["b"]) for record in cars]
        print(nodes_json)
        return nodes_json
    
# Implement an endpoint "rent-car' where a customer-id, car-id is passed as parameters.
# The system must check that the customer with customer-id has a booking for the car.
# The car's status is changed from 'booked' to 'rented'.
def rent_car(customer_id,reg):
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Customer{customer_id:$customer_id})-[r:BOOKED]->(b:Car{reg:$reg}) SET b.status = 'rented'", customer_id=customer_id, reg=reg)
        print(cars)
        nodes_json = [node_to_json(record["b"]) for record in cars]
        print(nodes_json)
        return nodes_json
    
# Implement an endpoint return-car' where a customer-id, car-id is passed as parameters.
# Car's status (e.g., ok or damaged) during the return will also be sent as a parameter.
# The system must check that the customer with customer-id has rented the car. 
# The car's status is changed from 'booked' to 'available' or "damaged'.
def return_car(customer_id,reg):
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Customer{customer_id:$customer_id})-[r:BOOKED]->(b:Car{reg:$reg}) WHERE b.status = 'rented' DELETE r SET b.status = CASE WHEN b.status = 'rented' THEN 'available' ELSE 'damaged' END", customer_id=customer_id, reg=reg)
        print(cars)
        nodes_json = [node_to_json(record["b"]) for record in cars]
        print(nodes_json)
        return nodes_json