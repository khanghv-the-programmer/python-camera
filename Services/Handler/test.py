data = {'Users':[{'full_name':'Test','user_name':'admin','password':'admin'},{'full_name':'Test1','user_name':'admin1','password':'admin1'}]}

for user in data['Users']:
    full_name = user['full_name']
    user_name = user['user_name']
    password = user['password']
    print('fullname: '+full_name+' username: '+user_name)