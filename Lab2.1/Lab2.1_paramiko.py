import paramiko
from time import sleep
import re

BUF_SIZE = 100*1024
TIMEOUT = 2
USER = "restapi"
PASSWORD = "j0sg1280-7@"

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_connection.connect("10.31.70.209", username=USER, password=PASSWORD, look_for_keys=False, allow_agent=False)
session = ssh_connection.invoke_shell()

session.send('terminal length 0\n\n')
out = session.recv(BUF_SIZE)
print(out)

sleep(2)

session.send('\n\nshow interfaces\n\n')
sleep(2)
out = session.recv(BUF_SIZE).decode()

for line in out.splitlines():
    if m := re.match("^([A-Z].+?) is", line):
        print("Interface " + m.group(1))
    if m := re.match("^.+?([0-9]+) packets input, ([0-9]+) bytes", line):
        print("Packets/bytes input: ", m.group(1), "/", m.group(2))

    if m := re.match("^.+?([0-9]+) packets output, ([0-9]+) bytes", line):
        print("Packets/bytes output: ", m.group(1), "/", m.group(2))

ssh_connection.close()
