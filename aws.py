import pwd

users = pwd.getpwall()

for user in users:
    print(user.pw_name)




import pwd

for user in pwd.getpwall():
    if user.pw_uid >= 1000:
        print(user.pw_name)
