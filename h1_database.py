import os
import sqlite3
from typing import List
from functools import reduce
from operator import add


def execute_query(query_sql: str) -> List:
    '''
    function for sql query execution
    :param query_sql: sql query
    :return: result of query execution
    '''
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql)
    return result


def get_profit() -> None:
    '''
    function which prints the total sum of profit from the table invoice_items
    '''
    query_sql = f'''
        SELECT UnitPrice, Quantity
        FROM invoice_items
        '''
    result_sql = execute_query(query_sql)
    total_profit = round(reduce(add, (price*quantity for price, quantity in result_sql), 0),2)
    print(total_profit)


def get_repeated_first_names() -> None:
    '''
    function that prints the repeated first names from the table customers as well as the number of their occurrences
    '''
    query_sql = f'''
        SELECT FirstName
        FROM customers
        '''
    result_sql = execute_query(query_sql)
    list_of_names = [i[0] for i in result_sql]
    set_of_names = set(list_of_names)
    for name in set_of_names:
        if list_of_names.count(name) > 1:
            print(f'{name}: {list_of_names.count(name)}')


get_profit()
get_repeated_first_names()