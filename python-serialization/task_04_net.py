#!/usr/bin/python3
"""
Module that contains start_server() and send_data() functions
"""
import socket
import json


def start_server():
    """
    Function that sets up a server using the socket library
    """
    HOST = '127.0.0.1'
    PORT = 38945

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()

        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                print(json.loads(data))


def send_data(dictionary):
    """
    Function that acts as the client
    """
    HOST = '127.0.0.1'
    PORT = 38945

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(json.dumps(dictionary).encode())
