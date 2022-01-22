import socket as socklib

sock = socklib.socket(socklib.AF_INET, socklib.SOCK_DGRAM)
myIP = "10.147.18.202"
myPort = 9993
sock.bind((myIP, myPort))

stop = False
while not stop:
    print("waiting for message...")
    data, addr = sock.recvfrom(1024)
    print(f"received message: {data}")
    stop = input("stop? y/n") == "y"
