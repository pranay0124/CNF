import socket
import threading

def receivedata(s):
    while True:
        data = s.recv(1024)
        data = data.decode()
        print("SECRET QUESTION : " + data)

def main():
    host = '127.0.0.1'
    port = 8001
    print("MARK ATTANDANCE ROLL NUMBER : ")
    rollnumber = input()


    sockobj = socket.socket()
    sockobj.connect((host, port))

    sockobj.send(str(rollnumber).encode())

    threading.Thread(target = receivedata, args = (sockobj, )).start()

    while True:
        message = input()
        sockobj.send(("SECRET ANSWER : " + message).encode())
        data2 = s.recv(1024)
        data2 = data2.decode()
        if(data2 == "ATTANDANCE FAILURE") :
            threading.Thread(target = receivedata, args = (sockobj, )).start()
        if(data2 == "ATTANDANCE SUCCESS") :
            sockobj.close()

if __name__ == '__main__':
        main()  