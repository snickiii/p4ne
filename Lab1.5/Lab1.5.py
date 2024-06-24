import glob

files = glob.glob('C:\\Users\gd.isakov\Desktop\python\JET-python-internal-learning\p4ne\Lab1.5\config_files\*.log')

addresses = set()

for file in files:
    with open(file, 'r') as f:
        for line in f:
            if line.find("ip address") == 1:
                addresses.add(line.replace("ip address", "").strip())

print(*addresses, sep='\n')
