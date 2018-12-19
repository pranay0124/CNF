import socket

def main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	print("Server started.")

	while True:
		convertion = dict({("INR", "Dollar"):1/67 , ("Dollar", "INR"):67, ("Pounds","Dollar"):1/0.75, ("Dollar","Pounds"):0.75, ("Yen","Dollar"):1/113.41, ("Dollar","Yen"):113.41})
		data, addr = s.recvfrom(1024)
		data = data.decode()
		print("message from: " + str(addr))
		print("from connect user: " + str(data))
		tokens = str(data).split(" ")
		key = (tokens[0],tokens[3])
		value = float(tokens[1]) * convertion[key]
		print("sending: " + str(data))
		s.sendto(data.encode(), addr)
	s.close()

if __name__ == '__main__':
	main()
