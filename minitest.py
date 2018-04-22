from mininet.log import setLogLevel,info
from mininet.net import Mininet
from mininet.cli import CLI

def MininetTopo():
    net = Mininet()

    info("Create host nodes.\n")
    lefthost = net.addHost("h1")
    righthost = net.addHost("h2")

    info("Create switch node.\n")
    switch = net.addSwitch("s1",failMode = 'standalone')

    info("Create Link.\n")
    net.addLink(lefthost,switch)
    net.addLink(righthost,switch)

    info("Build and Start network.\n")
    net.bulid()
    net.start()

    info("Run mininet CLI.\n")
    CLI(net)

if __name__=="__main__":
    setLogLevel('info')
    MininetTopo()