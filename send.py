import socket as socklib

message = 'Perhatian perhatian -ditra'
targetIP = {'arsa': '10.147.18.42',
            'ditra': '10.147.18.202',
            'ken': '10.147.18.138',
            'jo': '10.147.18.114',
            'sam': '10.147.18.1'}
target = ['arsa', 'ken", "jo", "sam']
targetPort = 9993

mysocket = socklib.socket(socklib.AF_INET, socklib.SOCK_DGRAM)


def broadcast():
    for i in target:
        mysocket.sendto(message.encode(), (targetIP[i], targetPort))


def send(person, message):
    mysocket.sendto(message.encode(), (targetIP[person], targetPort))


type = input('broadcast? y/n: ')
if type == 'y':
    broadcast()
else:
    person = input('target: ')
    message = input('message: ')
    send(person, message)
