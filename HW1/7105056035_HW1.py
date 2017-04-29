#!/usr/bin/env python2
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel,info

def MininetTopo():
	net = Mininet(topo=None,build=False)
	
	info("Create Switch node\n")
	switch1 = net.addSwitch("s1")
	switch2 = net.addSwitch("s2")
	switch3 = net.addSwitch("s3")
	
	info("Create Host node\n")
	host1 = net.addHost("h1")
	host2 = net.addHost("h2")
	host3 = net.addHost("h3")

	info("Link switch to host\n")
	net.addLink(switch1, host1)	
	net.addLink(switch2, host2)	
	net.addLink(switch3, host3)	
	
	info("Link switch to switch\n")
	net.addLink(switch1, switch2)	
	net.addLink(switch1, switch3)	
	net.addLink(switch2, switch3)

	info("Start network\n")
	net.start()
	

	info("Adding Flow\n")
	switch1.cmdPrint("ovs-ofctl add-flow s1 in_port=1,actions=output:2,3")
	switch1.cmdPrint("ovs-ofctl add-flow s1 in_port=2,actions=output:1")
	switch1.cmdPrint("ovs-ofctl add-flow s1 in_port=3,actions=output:1")

		
	switch2.cmdPrint("ovs-ofctl add-flow s2 in_port=1,actions=output:2,3")
	switch2.cmdPrint("ovs-ofctl add-flow s2 in_port=2,actions=output:1")
	switch2.cmdPrint("ovs-ofctl add-flow s2 in_port=3,actions=output:1")

	switch3.cmdPrint("ovs-ofctl add-flow s3 in_port=1,actions=output:2,3")
	switch3.cmdPrint("ovs-ofctl add-flow s3 in_port=2,actions=output:1")
	switch3.cmdPrint("ovs-ofctl add-flow s3 in_port=3,actions=output:1")

	CLI(net)

	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	MininetTopo()

