import glob
import re
from ipaddress import IPv4Interface


def return_network(s):
    r = re.search("ip address (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", s)
    if r is not None:
        return IPv4Interface((r.group(1), r.group(2)))
    else:
        return None


files = glob.glob('C:\\Users\gd.isakov\Desktop\python\JET-python-internal-learning\p4ne\Lab1.6\config_files\*.log')

networks = []

for file in files:
    with open(file, 'r') as f:
        for line in f:
            result = return_network(line)
            if result is not None:
                networks.append(result)

print(*networks, sep="\n")
