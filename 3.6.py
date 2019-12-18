ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
tunnel = """ 
Protocol: 		OSPF
Prefix: 		10.0.24.0/24
AD/Metrix: 		110/41
Next-Hop: 		10.0.13.3
Last update: 	3d18h
Outbound: 		Interface: FastEthernet0/0
		"""
print (tunnel)