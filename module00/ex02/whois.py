#!/Users/ztouzri/.brew/bin/python3
from sys import argv, exit

try:
	num = int(argv[1])
except (ValueError, IndexError) as error:
	print("Error")
	exit()
if len(argv) == 2:
	if num == 0:
		print("I'm Zero")
	elif num % 2:
		print("I'm Uneven")
	else:
		print("I'm Even")