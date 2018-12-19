import socket

def main():
	host = '127.0.0.1'
	port = 8080

	s = socket.socket()
	s.bind((host, port))

	s.listen(1)
	c, addr = s.accept()
	print ("connection from: " + str(addr))
	while True:
		convertion = dict({("INR", "Dollar"):1/67 , ("Dollar", "INR"):67, ("Pounds","Dollar"):1/0.75, ("Dollar","Pounds"):0.75, ("Yen","Dollar"):1/113.41, ("Dollar","Yen"):113.41})
		data = c.recv(1024)
		data = data.decode()
		if not data:
			break
		print ("from connected user: " + str(data))
		tokens = str(data).split(" ")
		key = (tokens[0],tokens[3])
		value = float(tokens[1]) * convertion[key]
		print ("sending: " + str(value))
		c.send(str(value).encode())
	c.close()

if __name__ == '__main__':
	main()


