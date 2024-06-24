from ipaddress import IPv4Network
import random


class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        self.net = random.randint(0x0b000000, 0xdf000000)
        self.mask = random.randint(8, 24)
        IPv4Network.__init__(self, (self.net, self.mask), strict=False)

    def key_value(self):
        return int(self.net + self.mask) << 32

    def check(self):
        return (self.is_global and not
        (self.is_private or self.is_loopback or
         self.is_reserved or self.is_multicast or
         self.is_link_local or self.is_unspecified))


def sort(subnet):
    return subnet.key_value()


addr_list = []

while len(addr_list) < 50:
    network = IPv4RandomNetwork()
    if network.check() and network not in addr_list:
        addr_list.append(network)

print(*(sorted(addr_list, key=sort)), sep='\n')