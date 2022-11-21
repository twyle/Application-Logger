# echo-client.py

import socket
import json

HOST = "0.0.0.0"  # The server's hostname or IP address
PORT = 5959  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(json.dumps({'Data': 'some data'}), 'utf-8'))

print('Done')