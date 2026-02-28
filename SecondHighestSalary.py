"""
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
"""


import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    m = {int(j.id.astype(int)): int(j.salary.astype(int)) for idx, j in employee.iterrows()}

    s = [(i,m[i]) for i in m]
    # print(s)
    z = []
    for i,l in s:
        if l not in z:
            z.append(l)
    k = sorted(z, reverse=True)

    print(z)
    if len(k) < 2:
        dt = {
         "SecondHighestSalary": [None]
        }
        return pd.DataFrame(data=dt)
    dt = {
         "SecondHighestSalary": [k[1]]
    }

    # print(dt)

    data = pd.DataFrame(data=dt)
    print(data)
    return data

data = {
    "id": [1,2],
    "salary" : [100,100]
}

dt = pd.DataFrame(data=data)

# print(dt)
print(second_highest_salary(dt))