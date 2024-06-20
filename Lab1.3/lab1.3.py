from pysnmp.hlapi import *

snmp_name = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_interfaces = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

result_names = getCmd(
    SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('10.31.70.209', 161)),
    ContextData(),
    ObjectType(snmp_name)
)

result_interfaces = nextCmd(
    SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('10.31.70.209', 161)),
    ContextData(),
    ObjectType(snmp_interfaces),
    lexicographicMode=False
)

for answer in result_names:
    for s in answer[3]:
        print(s)

for answer in result_interfaces:
    for i in answer[-1]:
        print(i)
