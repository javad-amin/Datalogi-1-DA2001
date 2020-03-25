from internet import INTERNET, DNS, known_ipaddr, mystery_address
import time

def traceroute(frm, to):
	global INTERNET, DNS
	to_addr = to
	if to in DNS:
		to_addr = DNS[to]
	ipaddr_to = [ int(s) for s in to_addr.split(".") ]
	
	print("traceroute: {} -> {} ({})".format(frm, to, to_addr))

											 
	start_t = time.time()
	counter = 1
	def print_pos(node):
		nonlocal counter
		print("{}: {}\t {:.3f} ms".format(counter, node.get_value(),(time.time()-start_t)*1000))
		counter += 1
	
	ipaddr_from = [ int(s) for s in frm.split(".") ]
	def trace_from(addr, node):
		if addr == []:
			print_pos(node)
		else:
			curr_num = addr[0]
			next_addr = addr[1:]
			next_node = node.get_child(curr_num)
			trace_from(next_addr, next_node)
			print_pos(node)

	trace_from(ipaddr_from, INTERNET)
	
	def trace_to(addr, node):
		if addr == []:
			print_pos(node)
		else:
			curr_num = addr[0]
			next_addr = addr[1:]
			next_node = node.get_child(curr_num)
			print_pos(node)
			trace_to(next_addr, next_node)

	trace_to(ipaddr_to, INTERNET)
	 
# run to find out some destination addresses
known_ipaddr()

# # example call
traceroute("0.2.1.0.1", "www.kth.se")
