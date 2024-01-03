#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

class final_topo(Topo):
  def build(self):
	#creating hosts for floor 1
	h10 = self.addHost('h10', mac='00:00:00:00:00:01', ip='10.1.1.10/24', defaultRoute="h10-eth1")
	h20 = self.addHost('h20', mac='00:00:00:00:00:02', ip='10.1.2.20/24', defaultRoute="h20-eth1")
	h30 = self.addHost('h30', mac='00:00:00:00:00:03', ip='10.1.3.30/24', defaultRoute="h30-eth1")
	h40 = self.addHost('h40', mac='00:00:00:00:00:04', ip='10.1.4.40/24', defaultRoute="h40-eth1")
	#creating hosts for floor 2
	h50 = self.addHost('h50', mac='00:00:00:00:00:05', ip='10.2.5.50/24', defaultRoute="h50-eth1")
        h60 = self.addHost('h60', mac='00:00:00:00:00:06', ip='10.2.6.60/24', defaultRoute="h60-eth1")
        h70 = self.addHost('h70', mac='00:00:00:00:00:07', ip='10.2.7.70/24', defaultRoute="h70-eth1")
        h80 = self.addHost('h80', mac='00:00:00:00:00:08', ip='10.2.8.80/24', defaultRoute="h80-eth1")
	#creating trusted/untrusted hosts and the server
	h_trust = self.addHost('h_trust', mac='00:00:00:00:00:09', ip='108.24.31.112/24', defaultRoute="h_trust-eth1")
	h_untrust = self.addHost('h_untrust', mac='00:00:00:00:00:10', ip='106.44.82.103/24', defaultRoute="h_untrust-eth1")
	h_server = self.addHost('h_server', mac='00:00:00:00:00:11', ip='10.3.9.90/24', defaultRoute="h_server-eth1")

	#creatung the switches
	s1 = self.addSwitch('s1') #data center
	s2 = self.addSwitch('s2') #core switch
	s3 = self.addSwitch('s3') #floor1 switch1
	s4 = self.addSwitch('s4') #floor1 switch2
	s5 = self.addSwitch('s5') #floor2 switch1
        s6 = self.addSwitch('s6') #floor2 switch2

	#connecting everything together
	#connecting the switches to the core switch
	self.addLink(s1, h_server, port1=1, port2=1) # links data center to the server host port 1 for data center port 1 for server host
	self.addLink(s1, s2, port1=2, port2=5)       # links data center to the core switch port 2 for data center port 5 for core switch
	self.addLink(s2, h_trust, port1=6, port2=1)  # links the core switch to the trust host core switch port 6 trust host port 1
        self.addLink(s2, h_untrust, port1=7, port2=1) # links the core switch to the untrusted host core switch port 7 host port 1
	self.addLink(s2, s3, port1=1, port2=3)	      # links the core switch to floor 1 switch 1 core switch port 1 floor 1 switch 1 port 3 
	self.addLink(s2, s4, port1=2, port2=3)        # links the core switch to floor 1 switch 2 core switch port 2 floor 1 switch 2 port 3
	self.addLink(s2, s5, port1=3, port2=3)        # links the core switch to floor 2 switch 1 core switch port 3 floor 2 switch 1 port 3
        self.addLink(s2, s6, port1=4, port2=3)	      # links the core switch to floor 2 switch 2 core switch port 4 floor 2 switch 2 port 3

	#connecting the floor switches to the host

	self.addLink(s3, h10, port1=1, port2=1)       # links floor 1 switch 1 with host 10 floor 1 switch 1 port 1 host 10 port 1
	self.addLink(s3, h20, port1=2, port2=1)	      # links floor 1 switch 1 with host 20 floor 1 switch 1 port 2 host 20 port 1
	self.addLink(s4, h30, port1=1, port2=1)       # links floor 1 switch 2 with host 30 floor 1 switch 2 port 1 host 30 port 1
        self.addLink(s4, h40, port1=2, port2=1)       # links floor 1 switch 2 with host 40 floor 1 switch 2 port 2 host 40 port 1
	self.addLink(s5, h50, port1=1, port2=1)       # links floor 2 switch 1 with host 50 floor 2 switch 1 port 1 host 50 port 1
        self.addLink(s5, h60, port1=2, port2=1)       # links floor 2 switch 1 with host 60 floor 2 switch 1 port 2 host 60 port 1
	self.addLink(s6, h70, port1=1, port2=1)       # links floor 2 switch 2 with host 70 floor 2 switch 2 port 1 host 70 port 1
        self.addLink(s6, h80, port1=2, port2=1)       # links floor 2 switch 2 with host 80 floor 2 switch 2 port 2 host 80 port 1

def configure():
  topo = final_topo()
  net = Mininet(topo=topo, controller=RemoteController)
  net.start()
  CLI(net)
  
  net.stop()


if __name__ == '__main__':
  configure()
