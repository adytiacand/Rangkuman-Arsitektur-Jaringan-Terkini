from mininet.topo import Topo
from mininet.cli import CLI
from mininet.log import setLogLevel, info

class MyTopo( Topo ):  
    "Simple topology example."

    def addSwitch(self, name, **opts):
        kwargs ={'protocols':'OpenFlow13'}
        kwargs.update(opts)
        return super(MyTopo, self).addSwitch(name, **kwargs)

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        info('\n***Add Hosts ***\n')
        Host1 = self.addHost( 'h1' , ip='10.1.0.1/24' )
        Host2 = self.addHost( 'h2' , ip='10.1.0.2/24' )
        Host3 = self.addHost( 'h3' , ip='10.2.0.3/24' )
        Host4 = self.addHost( 'h4' , ip='10.2.0.4/24' )
        Host5 = self.addHost( 'h5' , ip='10.3.0.5/24' )
        Host6 = self.addHost( 'h6' , ip='10.3.0.6/24' )

        info('\n***Add Switches ***\n')
        Switch1 = self.addSwitch('s1')
        Switch2 = self.addSwitch('s2')
        Switch3 = self.addSwitch('s3') 

        # Add links
        info('\n***Add Links for Hosts***\n')
        self.addLink( Host1, Switch1 )
        self.addLink( Host2, Switch1 )
        self.addLink( Host3, Switch2 )
        self.addLink( Host4, Switch2 )
        self.addLink( Host5, Switch3 )
        self.addLink( Host6, Switch3 )

        info('\n***Add Links between Switches***\n')
        self.addLink( Switch1, Switch2 ) 
        self.addLink( Switch2, Switch3 )
        self.addLink( Switch1, Switch3 )

topos = { 'mytopo': ( lambda: MyTopo() ) }