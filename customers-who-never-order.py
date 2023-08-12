import pandas as pd

""" +-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID and name of a customer.
 

Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
customerId is a foreign key (reference columns) of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
 

Write a solution to find all customers who never order anything.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+ """

data_customers = [
    ['1', 'Joe'],
    ['2', 'Henry'],
    ['3', 'Sam'],
    ['4', 'Max']
]

data_orders = [
    ['1', '3'],
    ['2', '1']
]

customers = pd.DataFrame(data_customers, columns=['id', 'name']).astype(
    {'id':'Int64', 'name':'object'}
)

orders = pd.DataFrame(data_orders, columns=['id', 'customerId']).astype(
    {'id':'Int64', 'customerId':'Int64'}
)

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    never_order = customers[~customers.id.isin(orders.customerId)][["name"]].rename(
        {"name": "Customers"}, axis="columns"
    )

    return never_order

customers_never_orderes = find_customers(customers, orders)