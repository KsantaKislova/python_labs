CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
cammands = CONFIG.strip().split()
vlans = cammands[-1].split(',')
print(vlans)