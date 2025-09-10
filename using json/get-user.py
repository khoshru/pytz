import json
def get_user():

    users_input= input("Enter your  username")
    
    with open('db.json','r') as j:
        database = json.load(j)

    print(  database['users'])
    database['users'].append({"name" : users_input})
    
    with open('db.json' , 'w') as db:
        json.dump(database, db)
    
get_user()
