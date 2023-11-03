from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import json

URI = "neo4j+s://2432849c.databases.neo4j.io"
AUTH = ("X0VQBfXWOkSDhuKG2DS8CIbnSQclMX7q2K2a1d4_H_Q")

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

def save_car(make, model, reg, year, capacity):
    with _get_connection().session() as session:
        cars = session.run("MERGE (a:Car{make: $make, model: $model, reg: $reg,year: $year, capacity:$capacity}) RETURN a;", make = make, model = model, reg = reg, year =year, capacity = capacity)
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json

def update_car(make, model, reg, year, capacity):
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Car{reg:$reg}) set a.make=$make, a.model=$model, a.year = $year, a.capacity = $capacity RETURN a;", reg=reg, make=make, model=model, year=year, capacity=capacity)
        print(cars)
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json

def delete_car(reg):
    _get_connection().execute_query("MATCH (a:Car{reg: $reg}) delete a;", reg = reg)


#ENDDDDDDDDDDDDDDDDDDDPOINTS
#Implement an endpoint ‘cancel-order-car’ where a customer-id, car-id is passed as parameters. 

def cancel_order_car(customer_id, car_id):
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Customer{customer_id:$customer_id})-[r:BOOKED]->(b:Car{car_id:$car_id}) DELETE r;", customer_id=customer_id, car_id=car_id)
        print(cars)
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json




#Implement an endpoint ‘rent-car’ where a customer-id, car-id is passed as parameters.


def rent_car(customer_id, car_id):
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Customer{customer_id:$customer_id})-[r:BOOKED]->(b:Car{car_id:$car_id}) set b.status = 'rented' RETURN b;", customer_id=customer_id, car_id=car_id)
        print(cars)
        nodes_json = [node_to_json(record["b"]) for record in cars]
        print(nodes_json)
        return nodes_json
    
#Implement an endpoint ‘return-car’ where a customer-id, car-id is passed as parameters.
def return_car(customer_id,car_id):
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Customer{customer_id:$customer_id})-[r:BOOKED]->(b:Car{car_id:$car_id}) set b.status = 'available' RETURN b;", customer_id=customer_id, car_id=car_id)
        print(cars)
        nodes_json = [node_to_json(record["b"]) for record in cars]
        print(nodes_json)
        return nodes_json