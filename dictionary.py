# sehirler = ['karabük', 'istanbul']
# plakalar = [78, 34]

# print(plakalar[sehirler.index('karabük')])

# plakalar = {'karabük' : 78, 'istanbul': 34}

# print(plakalar['karabük'])
# print(plakalar['istanbul'])

# plakalar['ankara'] = 6
# plakalar['karabük'] = "new value"

# print(plakalar)

users = {
    'aliyılmaz': {
        'age' : 5,
        'email' : "aliyilmaz@gmail.com",
        'address' : 'istanbul',
        'phone' : 54648653,
        'roles' : ['user']
     },

     'mehmetyılmaz': {
        'age' : 45,
        'email' : "mehmetyilmaz@gmail.com",
        'address' : 'karabük',
        'phone' : 546445653,
        'roles' : ['admin', 'user']
     }
}

print(users['aliyılmaz']['roles'][0])
