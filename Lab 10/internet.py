from tree import Tree


def build_sunet():
	# SUNET
	sunet = Tree("66a45.sunet.se")

	def build_kth():
		kth = Tree("kth2.sunet.se")
		kth_intranet = Tree("a5ef-6c.kth.se")
		for namn in ["red-12", "orange-5", "sport-3", "spel-15"]:
			kth_intranet.add_child(Tree(namn))
		kth_services = Tree("645ea5.kth.se")
		for namn in ["webmail.kth.se", "smtp.kth.se", "www.kth.se"]:
			kth_services.add_child(Tree(namn))
		kth.add_child(kth_intranet)
		kth.add_child(kth_services)
		return kth

	def build_su():
		su = Tree("sthlm-universitet.sunet.se")
		services = Tree("65efa64-65edb.su.se")
		for namn in ["www.su.se", "smtp.su.se", "webmail.su.se"]:
			services.add_child(Tree(namn))
		inst = Tree("56afd.f6425-cd8.su.se")
		for namn in ["biblioteket.su.se", "math.su.se", "fysik.su.se"]:
			inst.add_child(Tree(namn))
		su.add_child(services)
		su.add_child(inst)
		return su

	sunet.add_child(build_su())
	sunet.add_child(build_kth())
	return sunet

def build_netnod():
	netnod = Tree("62ef-425.netnod.com")
	netnod.add_child(build_pyttemjuk())
	netnod.add_child(build_sunet())
	netnod.add_child(build_telenor())
	return netnod

def build_telenor():
	telenor = Tree("a8f.9.telenor.se")
	# smallbandsbolaget
	sbbolaget = Tree("cce76-top.smalbandsbolaget.se")
	sb_sthlm = Tree("ns.645-52-stockholm.smalbandsbolaget.se")
	sbbolaget.add_child(sb_sthlm)
	for n in [ "Lisas router", "Familjen Larsson"]:
		sb_sthlm.add_child(Tree(n))
	telenor.add_child(sbbolaget)
	# Judiths nät
	judith = Tree("58.5-ce6.judith-och-judith.se")
	judith_sth = Tree("a-8ed.sth-63.judith-och-judith.se")
	judith.add_child(judith_sth)
	for n in ["dlink-653C", "Kalle hem"]:
		judith_sth.add_child(Tree(n))
	telenor.add_child(judith)
	
	return telenor

def build_verisign():
	verisign = Tree("5e7a-f.verisign.net")
	verisign.add_child(build_banana())
	
	rick_chain = ["Never.gonna.give.you.up.xbfzf.net",
				  "Never.gonna.let.you.down.xbfzf.net",
				  "Never.gonna.run.around.and.desert.you.xbfzf.net",
				  "Never.gonna.make.you.cry.xbfzf.net"]
	rick_top = Tree(rick_chain[0])
	prev = rick_top
	for curr in rick_chain[1:]:
		curr = Tree(curr)
		prev.add_child(curr)
		prev = curr
	verisign.add_child(rick_top)
		
	return verisign

def build_banana():
	chain = ["nforce-gw-2.r1.ams2.nl.com", "ae3.banana.seattle.verisign.net", "ns.services.banana.com", "www.banana.com"]
	banana_top = Tree(chain[0])
	prev = banana_top
	for curr in chain[1:]:
		curr = Tree(curr)
		prev.add_child(curr)
		prev = curr
	return banana_top

def build_pyttemjuk():
	chain = ["netnod-ix-ge-b-sth-1500.net", "sto02.se.as5580.com", "34fb.ns.pyttemjuk.com", "www.pyttemjuk.com"]
	banana_top = Tree(chain[0])
	prev = banana_top
	for curr in chain[1:]:
		curr = Tree(curr)
		prev.add_child(curr)
		prev = curr
	return banana_top

def build_internet():
	global INTERNET
	INTERNET = Tree("internet")
	INTERNET.add_child(build_netnod())
	INTERNET.add_child(build_verisign())

	sw_chain = [
		"Episode.IV.A.NEW.HOPE.75eyjm.net",
		"It.is.a.period.of.civil.war.75eyjm.net",
		"Rebel.spaceships.striking.from.75eyjm.net",
		"a.hidden.base.have.won.their.first.75eyjm.net",
		"victory.against.the.evil.Galactic.Empire.75eyjm.net"
		]
	
	sw_top = Tree(sw_chain[0])
	prev = sw_top
	for curr in sw_chain[1:]:
		curr = Tree(curr)
		prev.add_child(curr)
		prev = curr    
	INTERNET.add_child(sw_top)


def calc_ipaddr(val):
	def find(tree, val):
		if val == tree.get_value():
			return True
		N = tree.num_children()
		if N == 0:
			return False
		for idx in range(N):
			child = tree.get_child(idx)
			res = find(child, val)
			if res == True:
				return str(idx)
			elif res == False:
				continue
			else:
				assert isinstance(res, str)
				return "{}.{}".format(idx, res)
		return False
	global INTERNET
	res = find(INTERNET, val)
	assert isinstance(res, str)
	return res

def known_ipaddr():
	users = {"Lisa hemifrån" : calc_ipaddr("Lisas router"),
			 "Lisa från KTH" : calc_ipaddr("spel-15"),
			 "Kalle hemifrån" : calc_ipaddr("Kalle hem"),
			 "Kalle från KTH" : calc_ipaddr("red-12")
			 }
	print()
	for user in users.keys():
		print("{} har IP-adress {}".format(user, users[user]))
	
def mystery_address():
	bonus = [ "victory.against.the.evil.Galactic.Empire.75eyjm.net",
			  "Never.gonna.make.you.cry.xbfzf.net" ]
	for idx, addr in enumerate(bonus, 1):
		print("Bonus address {}: {}".format(idx, calc_ipaddr(addr)))
	
build_internet()

DNS = {}
DNS["www.kth.se"] = calc_ipaddr("www.kth.se")
DNS["webmail.kth.se"] = calc_ipaddr("webmail.kth.se")
DNS["smtp.kth.se"] = calc_ipaddr("smtp.kth.se")
DNS["www.su.se"] = calc_ipaddr("www.su.se")
DNS["webmail.su.se"] = calc_ipaddr("webmail.su.se")
DNS["smtp.su.se"] = calc_ipaddr("smtp.su.se")
DNS["math.su.se"] = calc_ipaddr("math.su.se")
DNS["biblioteket.su.se"] = calc_ipaddr("biblioteket.su.se")
DNS["www.banana.com"] = calc_ipaddr("www.banana.com")
DNS["www.pyttemjuk.com"] = calc_ipaddr("www.pyttemjuk.com")
