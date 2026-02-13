import pandas as pd


'''
Input: 
Person table:
+----------+----------+-----------+
| personId | lastName | firstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+
Address table:
+-----------+----------+---------------+------------+
| addressId | personId | city          | state      |
+-----------+----------+---------------+------------+
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |
+-----------+----------+---------------+------------+
Output: 
+-----------+----------+---------------+----------+
| firstName | lastName | city          | state    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+
Explanation: 
There is no address in the address table for the personId = 1 so we return null in their city and state.
addressId = 1 contains information about the address of personId = 2.


'''

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:

    data = {
        "firstName": [],
        "lastName" : [],
        "city": [],
        "state": []
    }
    for row,p in person.iterrows():
        data["firstName"].append(p.firstName)
        data["lastName"].append(p.lastName)
        for r,add in address.iterrows():
            get_list_per = person.personId.to_list()
            if add.personId == p.personId:
                data["city"].append(add.city)
                data["state"].append(add.state)

            elif add.personId in get_list_per:
                get_list = address.personId.to_list()

                if p.personId not in get_list:                                                                                                                                                  
                    data["city"].append(None)
                    data["state"].append(None)
        


    print(data)
    try:
        df = pd.DataFrame(data=data)
    except ValueError:
        print(data)

    else:
        print(df)
{
    'firstName': ['Allen'], 
    'lastName': ['Wang'], 
    'city': [], 
    'state': []}

# data
person_data = {
    "personId": [1, 2],
    "lastName": ["Wang", "Alice"],
    "firstName": ["Allen", "Bob"]
}

df1 = pd.DataFrame(data=person_data)
# Address table
address_data = {
    "addressId": [1, 2],
    "personId": [2, 3],
    "city": ["New York City", "Leetcode"],
    "state": ["New York", "California"]
}

df2 =  pd.DataFrame(data=address_data)


combine_two_tables(person={
    'firstName': ['Allen'], 
    'lastName': ['Wang'], 
    'city': [], 
    'state': []}, address=df2)