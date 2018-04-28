from ryu.base import app_manager
from ryu.ofproto import ofproto_v1_3
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER,CONFIG_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet,ipv4,mpls

class Test(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
    def __init__(self,*args,**kwargs):
        super(Test,self).__init__(*args,**kwargs)
        print('init')
        self.mac_to_port = {}

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures,CONFIG_DISPATCHER)
    def switch_features_handler(self,ev):
        print('switch features handler')
        dp = ev.msg.datapath
        ofp = dp.ofproto
        ofp_parser = dp.ofproto_parser

        match = ofp_parser.OFPMatch()
        actions = [ofp_parser.OFPActionOutput(ofp.OFPP_CONTROLLER,ofp.OFPCML_NO_BUFFER)]
        self.add_flow(dp,match,0,actions)

    def add_flow(self,dp,match,priority,actions):
        print('add_flow')
        ofp = dp.ofproto
        ofp_parser = dp.ofproto_parser
        ins = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS,actions)]
        mod = ofp_parser.OFPFlowMod(datapath=dp,priority=priority,match=match,instructions=ins)
        dp.send_msg(mod)

    @set_ev_cls(ofp_event.EventOFPPacketIn,MAIN_DISPATCHER)
    def packet_in_handle(self,ev):
        print('packet in ')
        msg = ev.msg
        dp = msg.datapath
        ofp = dp.ofproto
        ofp_parser = dp.ofproto_parser
        
        in_port = msg.match['in_port']
        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocols(ethernet.ethernet)[0]
        mpls_value = pkt.get_protocols(mpls.mpls)
        print(mpls_value)

        dst = eth.dst
        src = eth.src
        dpid = dp.id
        self.mac_to_port.setdefault(dpid, {})
        self.mac_to_port[dpid][src] = in_port
        print(self.mac_to_port,self.mac_to_port[dpid],dst,src)
        if dst in self.mac_to_port[dpid]:
            print('had')
            out_port = self.mac_to_port[dpid][dst]
        else:
            print('flood')
            out_port = ofp.OFPP_FLOOD
        
        actions = [ofp_parser.OFPActionPushMpls(34887),ofp_parser.OFPActionSetField(mpls_label=2),ofp_parser.OFPActionOutput(out_port)]
        
        if out_port != ofp.OFPP_FLOOD:
            print('out_port != ofp.OFPP_FLOOD')
            match = ofp_parser.OFPMatch(in_port,eth_dst = dst)
            self.add_flow(dp,match,1,actions)
        
        data=None
        if msg.buffer_id == ofp.OFP_NO_BUFFER:
            data=msg.buffer_id
        out = ofp_parser.OFPPacketOut(datapath=dp,buffer_id=msg.buffer_id,in_port=in_port,actions=actions,data=data)
        dp.send_msg(out)


        