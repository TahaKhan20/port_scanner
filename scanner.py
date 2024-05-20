import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
	

	print("-" * 50)
	print("Scanning Target IP ", target)
	print("Time started: ", datetime.now())
	print("-" * 50)
	
	try:
		for port in range(1, 100):
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			result = s.connect_ex((target,port))
			if result == 0:
				print("Port {} is connected successfully".format(port))
	except KeyboardInterrupt:
		print("\nExiting Program")
		sys.exit()
	except socket.gaierror:
		print("Hostname could not be resolved")
		sys.exit()
	except socket.error:
		print("Couldn't connect to server")
	
else:
	print("Invalid arguments")
	print("correct format is: python3 scanner.py <ip>")
	
