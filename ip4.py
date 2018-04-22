from ryu.ofproto import inet
from ryu.lib.packet import ipv4

pkt_ipv4 = ipv4.ipv4(dst='192.0.2.1',src='192.0.2.2',proto=inet.IPPROTO_TCP)
print pkt_ipv4.dst
print pkt_ipv4.src
print pkt_ipv4.proto