command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
commands1 = command1.strip().split()
vlans1 = commands1[-1].split(',')
commands2 = command2.strip().split()
vlans2 = commands2[-1].split(',')
vlans1 = set(vlans1)
vlans2 = set(vlans2)
i = vlans1 & vlans2
i = list(i)
print(i)