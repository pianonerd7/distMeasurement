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

		temp_ttl = (high+low)/2
		hops, time = prob(host, temp_ttl)

		if hops.find(host) != -1:
			return temp_ttl, time
		elif hops == None:
			high = temp_ttl
		else:
			low = temp_ttl

	return low, time

def prob(host, ttl):
	sending_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.getprotobyname('udp'))
	receiving_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname('icmp'))

	sending_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
	receiving_socket.bind(('', PORT_NUM))
	receiving_socket.settimeout(3)
	start_prob_time = time.time()
	end_prob_time = time.time()+3 #3 is the timeout
	sending_socket.sendto('', (host, PORT_NUM))
	data = ''
	address = ''
	name = ''

	try:
		data, address = receiving_socket.recvfrom(512)
		address = address[0]
		end = time.time()

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
	return address, round((end_prob_time - start_prob_time)*1000)

def print_results(host):

	host_ip = socket.gethostbyname(host)
	var = get_hops(host_ip)

	print 'Reaching %s' % (host)
	print 'The number of router hops is %s' % (var[0])
	print 'The RTT is %s \n' % (var[1])

def main():
    my_list = list()
    
    with open("Destinations.csv") as file:
    	for line in file:
    	    my_list.append(str(line))

    #for host in my_list:
    for host in ['google.com', 'amazon.com', 'case.edu']:
    	#print host
    	print_results(host)

if __name__ == '__main__':
    main()
