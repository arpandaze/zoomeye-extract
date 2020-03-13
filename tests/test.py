import requests
import multiprocessing

with open('scrapedIPs.txt') as file:
    ipList = file.read().split("\n")
    try:
        ipList.remove('')
    except:
        pass

validIP = []
for i in ipList:
    try:
        val = requests.get("http://{}".format(i))
        validIP += [i]
        #print(val.content)
    except:
        pass

portsToScan = ['8080','443','80','22','23','4444']
for i in validIP:
    for k in portsToScan:  
        splited = i.split(":")
        ipSplit = splited[0].split(".")
        for j in range(256):
            brutIPList += ['.'.join([ipSplit[0],ipSplit[1],ipSplit[2],str(j)])+':'+k]

def scan(inp_ip):
    try:
        print("Scanning: {}\n".format(inp_ip))
        requests.get("http://{}".format(inp_ip))
        #newValidIPs += [inp_ip]
        print("Alive IP: {}".format(inp_ip))
    except:
        print("Dead IP: {}\n".format(inp_ip))
        pass

def echo(i):
    print(i)

if __name__ == "__main__":
    for i in range(10):
        procs = []
        process = multiprocessing.Process(target=scan, args=(i,))
        procs.append(process)
        process.start()