import time
import csv
import socket

PORT_NUM = 33434

def get_hops(host):
	low = 0
	high = 32
	temp_ttl = 0
	hops = 0
	time = 0

	while low < high:
		if temp_ttl == (high+low)/2:
			break
		else :
			temp_ttl = (high+low)/2
		hops, time = probe(host, temp_ttl)

		if hops == None:
			high = temp_ttl
		elif hops.find(host) != -1:
			return temp_ttl, time
		else:
			low = temp_ttl

	return low, time


def probe(host, ttl=30):
	sending_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.getprotobyname('udp'))
	receiving_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname('icmp'))

	sending_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
	receiving_socket.bind(('', PORT_NUM))
	receiving_socket.settimeout(3)
	start_probe_time = time.time()
	end_probe_time = time.time()+3 #3 is the timeout
	sending_socket.sendto('', (host, PORT_NUM))
	data = None
	address = None
	name = None

	try:
		data, address = receiving_socket.recvfrom(512)
		address = address[0]
		end_probe_time = time.time()

		try:
			name = socket.gethostbyaddr(address)
			name = name[0]
		except Exception, e:
			name = address
		else:
			pass
		finally:
			pass
	except Exception, e:
		pass
	else:
		pass
	finally:
		sending_socket.close()
		receiving_socket.close()
	return address, round((end_probe_time - start_probe_time) *1000)

def print_results(host):
	print host
	host_ip = socket.gethostbyname(str(host))
	var = get_hops(host_ip)

	print 'Reaching %s' % (host)
	print 'The number of router hops is %s' % (var[0])
	print 'The RTT is %s ms \n' % (var[1])

def main():
	my_list = list()

	with open("Targets.txt") as file:
		for line in file:
			my_list.append(str(line).strip('\n'))

	print my_list

	for host in my_list:
		print_results(str(host))

if __name__ == '__main__':
	main()
