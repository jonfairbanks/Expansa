![Expansa](https://raw.githubusercontent.com/jonfairbanks/Expansa/master/expansa.png)

# Expansa
Python3 Multi-Threaded Reverse Shell Prototype

### Prerequisites
- Python 3.x
- PIP


### Server
###### Setup:
 - Update Host and Port in server.py
 - Launch the script with `python3 server.py`
 - Wait for clients to connect...

######  Commands:
 - `list`: Prints a directory of connected clients. Can be used in conjunction with select.
 - `select`: Used to select a remote client returned by the list command. Expects a number.
 - `quit`|`exit`: Exit the current client session.


### Client Setup
- Launch the client-side script with `python3 client.py`
- [Optional] Convert client.py to an .EXE using: `python3 setup.py build`


### Changelog
 - **v1.0**: Initial Release
 - **v1.1**: Improved Error Handling
 - **v1.2**: Multi-Connection Support
 
