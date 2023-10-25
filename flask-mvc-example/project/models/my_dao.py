from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import json

URI = "YOUR-URI"
AUTH = ("neo4j", "YOUR-AUTH-KEY")

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

def node_to_json(node):
    node_properties = dict(node.items())
    return node_properties

def delete_car(reg):
    _get_connection().execute_query("MATCH (a:Car{reg: $reg}) delete a;", reg = reg)