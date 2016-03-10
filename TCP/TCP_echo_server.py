#!/usr/bin/env python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 2222))
s.listen(10)
while True:
  conn, addr = s.accept()
  while True:
    data = conn.recv(1024)
    if not data:
      break
    if 'close' in data:
      conn.close()
    conn.send(data)

