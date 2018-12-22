import socket
import threading
import csv
# from xlrd import open_workbook
from openpyxl import load_workbook
clients = list()
rollnumbers = list()
questions = list()
answers = list()
# loc = ('E:\CNF\CNF - Assignments\m12\CNF_Week_2')
def thfunc(c):
    while True:
        data = c.recv(1024)
        data = data.decode()
        # wb = load_workbook('E:\CNF\CNF - Assignments\m12\CNF_Week_2\data1.xlsx')
        # sheet = wb.get_sheet_by_name('data') 
        # sheet.cell_value(0, 0)
        with open('data.csv') as csvfile :
            file = csv.reader(csvfile, delimiter=',') 
            for j in file :
                rollnumbers.append(j[0])
                questions.append(j[1])
                answers.append(j[2])
  
        for i in range(1,10): 
            if (data not in rollnumbers) :
                c.send(("ATTANDANCE FAILURE : ").encode())
            if (data in rollnumbers) :
                if(questions[i] == rollnumbers[i]) :
                    question = questions[i]
                    c.send(question.encode())


def main():
    totalconnec = int(input("Please provide number of users: "))
    host = '127.0.0.1'
    port = 8001
    sockobj = socket.socket()
    sockobj.bind((host, port))
    sockobj.listen(1)
    for i in range(0, totalconnec):
        connec, addr = sockobj.accept()
        print("Connection established with " + str(addr))
        clients.append(connec)
        thread = threading.Thread(target = thfunc, args = (clients[i],))
        thread.start()
    sockobj.close()

if __name__ == '__main__':
    main()

