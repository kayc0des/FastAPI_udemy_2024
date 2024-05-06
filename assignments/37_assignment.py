''' Python Functions '''

def user_dict(firstname, lastname, age):
    dict = {
        'firstname': firstname,
        'lastname': lastname,
        'age': age
    }
    return dict

print(user_dict('John', 'Kavinsky', 26))