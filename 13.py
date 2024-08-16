from ipaddress import ip_network

ip_adr = ip_network('192.168.32.160/255.255.255.240')

c = 0
for i in ip_adr:
    if bin(int(i)).count('1') % 2 == 0:
        c += 1

print(c)