#!/usr/bin/env python
from scapy.all import send,IP,load_contrib,Ether

load_contrib('mpls')
p = Ether()/IP(dst='10.0.0.4')
p = MPLS(p)
print(p.show())
# test
# send(p,count=4)