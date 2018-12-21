import socket
from random import randint
import threading

def guess(s):
    c,addr = s.accept()
    print("Connection from : " + str(addr))
    ranNum = randint(0,50)
    print("RandNum: " + str(ranNum))
    guesses = 0
    while True:
        data = c.recv(1024)
        data = data.decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = int(data)
        guesses = guesses + 1
        value = ""
        if(data == ranNum):
            value = "correct, the guesses are: " + str(guesses)
            c.send(str(value).encode())
            c.close()
            return
        if(data < ranNum) :
            value = "Your number is less than guess"
        if(data > ranNum) :
            value = "Your number is greater than guess"
        c.send(str(value).encode())

def main():
    host = '127.0.0.1'
    port = 8001

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)

    t = list()
    for i in range(0,3):       
        t1 = threading.Thread(target=guess, args=(s,))
        t.append(t1)
        t[i].start()

    for i in range(0,3):
        t[i].join()

if __name__ == "__main__":
    main()
    
