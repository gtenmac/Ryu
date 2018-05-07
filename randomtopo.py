from mininet.cli import CLI
from mininet.topo import Topo
from mininet.node import RemoteController
from mininet.net import Mininet
from functools import partial
from mininet.util import dumpNodeConnections
import random
import os

class MyTopo( Topo ):

	def build(self):
 		rand_switch = random.randrange(2,4,2)
		print("switch node = ",rand_switch)
		for m in range(rand_switch):
 			s = self.addSwitch('s%s'%(m+1))
			T.switch_ary.append(s)
			rand_host = random.randrange(2,6,2)
			print("host node = ",rand_host)
			for n in range(rand_host):
				T.num+=1
				host = self.addHost('h%s'%(T.num))
				T.host_ary.append(host)
				self.addLink(host,s)
		for m in range(rand_switch-1):
			self.addLink(T.switch_ary[m],T.switch_ary[m+1])

class T:
	host_ary=[]
	switch_ary=[]
	num=0

if __name__ == '__main__':
	topo=MyTopo()
	net = Mininet(topo=topo)
	net.start()
	CLI(net)
