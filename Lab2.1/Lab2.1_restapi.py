import requests
USER = "restapi"
PASSWORD = "j0sg1280-7@"

headers = {
    "accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

url = "https://10.31.70.209/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces"

r = requests.get(url=url, headers=headers, auth=(USER, PASSWORD), verify=False)

if r.status_code == 200:
    data = r.json()
    interfaces = data["Cisco-IOS-XE-interfaces-oper:interfaces"]["interface"]
    for interface in interfaces:
        print(f"Interface: {interface['name']}")
        print(f"Input packets/bytes {interface['statistics']['in-unicast-pkts']}/{interface['statistics']['in-octets']}")
        print(f"Output packets/bytes {interface['statistics']['out-unicast-pkts']}/{interface['statistics']['out-octets']}")
        print("--- --- ---")
