#!/usr/bin/env python
from scapy.all import send,IP,load_contrib

load_contrib('mpls')
p = Ether(type=34887)/IP(dst='10.0.0.2')/MPLS()
p = MPLS(p)
# print(p.show())
send(p,count=4)