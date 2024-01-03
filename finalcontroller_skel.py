from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Final (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

  def do_final (self, packet, packet_in, port_on_switch, switch_id):

    def sender():
        head = packet.find('ipv4')
        msg = of.ofp_flow_mod()
        msg2 = of.ofp_packet_out() 
        msg2.data = packet_in
        msg.match = of.ofp_match.from_packet(packet)
        msg.idle_timeout = 30
        msg.hard_timeout = 30
	if switch_id == 1: # data center switch
		if head.dstip == "10.3.9.90":
			msg2.actions.append(of.ofp_action_output(port = 1))
        		msg.actions.append(of.ofp_action_output(port = 1))
		else:
			msg2.actions.append(of.ofp_action_output(port = 2))
                        msg.actions.append(of.ofp_action_output(port = 2))
	elif switch_id == 2: # core switch
		if head.dstip == "10.3.9.90":
                        msg2.actions.append(of.ofp_action_output(port = 5))
                        msg.actions.append(of.ofp_action_output(port = 5))
                elif head.dstip == "10.1.1.10" or head.dstip == "10.1.2.20":
                        msg2.actions.append(of.ofp_action_output(port = 1))
                        msg.actions.append(of.ofp_action_output(port = 1))
		elif head.dstip == "10.1.3.30" or head.dstip == "10.1.4.40":
                        msg2.actions.append(of.ofp_action_output(port = 2))
                        msg.actions.append(of.ofp_action_output(port = 2))
		elif head.dstip == "10.2.5.50" or head.dstip == "10.2.6.60":
                        msg2.actions.append(of.ofp_action_output(port = 3))
                        msg.actions.append(of.ofp_action_output(port = 3))
		elif head.dstip == "10.2.7.70" or head.dstip == "10.2.8.80":
                        msg2.actions.append(of.ofp_action_output(port = 4))
                        msg.actions.append(of.ofp_action_output(port = 4))
		elif head.dstip == "108.24.31.112":
                        msg2.actions.append(of.ofp_action_output(port = 6))
                        msg.actions.append(of.ofp_action_output(port = 6))
		elif head.dstip == "106.44.82.103":
                        msg2.actions.append(of.ofp_action_output(port = 7))
                        msg.actions.append(of.ofp_action_output(port = 7))
	elif switch_id == 3: # floor 1 switch 1
		if head.dstip == "10.1.1.10":
                        msg2.actions.append(of.ofp_action_output(port = 1))
                        msg.actions.append(of.ofp_action_output(port = 1))
		elif head.dstip == "10.1.2.20":
			msg2.actions.append(of.ofp_action_output(port = 2))
                        msg.actions.append(of.ofp_action_output(port = 2))
		else: 
			msg2.actions.append(of.ofp_action_output(port = 3))
                        msg.actions.append(of.ofp_action_output(port = 3))
	elif switch_id == 4: # floor 1 switch 2
                if head.dstip == "10.1.3.30":
                        msg2.actions.append(of.ofp_action_output(port = 1))
                        msg.actions.append(of.ofp_action_output(port = 1))
                elif head.dstip == "10.1.4.40":
                        msg2.actions.append(of.ofp_action_output(port = 2))
                        msg.actions.append(of.ofp_action_output(port = 2))
                else:
                        msg2.actions.append(of.ofp_action_output(port = 3))
                        msg.actions.append(of.ofp_action_output(port = 3))
	elif switch_id == 5: # floor 2 switch 1
                if head.dstip == "10.2.5.50":
                        msg2.actions.append(of.ofp_action_output(port = 1))
                        msg.actions.append(of.ofp_action_output(port = 1))
                elif head.dstip == "10.2.6.60":
                        msg2.actions.append(of.ofp_action_output(port = 2))
                        msg.actions.append(of.ofp_action_output(port = 2))
                else:
                        msg2.actions.append(of.ofp_action_output(port = 3))
                        msg.actions.append(of.ofp_action_output(port = 3))
	elif switch_id == 6: #floor 2 switch 2
                if head.dstip == "10.2.7.70":
                        msg2.actions.append(of.ofp_action_output(port = 1))
                        msg.actions.append(of.ofp_action_output(port = 1))
                elif head.dstip == "10.2.8.80":
                        msg2.actions.append(of.ofp_action_output(port = 2))
                        msg.actions.append(of.ofp_action_output(port = 2))
                else:
                        msg2.actions.append(of.ofp_action_output(port = 3))
                        msg.actions.append(of.ofp_action_output(port = 3))	

        self.connection.send(msg)
        self.connection.send(msg2)
		 
    	return
    def flood():
        msg = of.ofp_flow_mod()
        msg2 = of.ofp_packet_out() #should this be packet_in?
        msg2.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
        msg2.data = packet_in
        msg.match = of.ofp_match.from_packet(packet)
        msg.idle_timeout = 30
        msg.hard_timeout = 30
        msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
        self.connection.send(msg)
        self.connection.send(msg2) 
        return
    def drop():
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet)
        msg.idle_timeout = 30
        msg.hard_timeout = 30
        self.connection.send(msg)
        return
    deptA = ["10.1.1.10", "10.1.2.20", "10.1.3.30", "10.1.4.40"]
    deptB = ["10.2.5.50", "10.2.6.60", "10.2.7.70", "10.2.8.80"]
    ip_header = packet.find('ipv4') 
    if packet.find('arp') is not None:
	flood()
    elif packet.find('icmp') is not None:
	if ip_header.srcip == "106.44.82.103" and (ip_header.dstip in deptA or ip_header.dstip in deptB or ip_header.dstip == "10.3.9.90"):
		drop()
        elif ip_header.srcip == "108.24.31.112" and (ip_header.dstip in deptB or ip_header.dstip == "10.3.9.90"):
		drop()
        elif ip_header.srcip in deptA and ip_header.dstip in deptB:
		drop()
	elif ip_header.srcip in deptB and ip_header.dstip in deptA:
		drop()
	else:
		sender()
    elif ip_header.srcip == "106.44.82.103" and ip_header.dstip == "10.3.9.90":
	drop()
    elif ip_header.srcip == "108.24.31.112" and ip_header.dstip == "10.3.9.90":
	drop()
    else:
	sender()

  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """
    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.
    self.do_final(packet, packet_in, event.port, event.dpid)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Final(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
