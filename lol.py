import pwd

username = "john"

try:
    user = pwd.getpwnam(username)
    print("User exists:", user.pw_name)
    print("UID:", user.pw_uid)
    print("Home:", user.pw_dir)
    print("Shell:", user.pw_shell)
except KeyError:
    print("User does not exist")
