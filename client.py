#!/usr/bin/env python
from scapy.all import send,IP,load_contrib

load_contrib('mpls')
p = IP(dst='10.0.0.4')/MPLS()

send(p,count=4)