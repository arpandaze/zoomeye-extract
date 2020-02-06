import requests
import threading

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

validIP = ['213.81.216.121:80', '201.163.210.226:80', '191.54.0.18:8080', '62.21.40.50:80', '86.124.252.208:80', '118.173.127.69:81', '73.129.184.74:81', '87.189.35.40:80', '122.163.177.244:80', '95.174.111.67:80']
brutIPList = []
portsToScan = ['8080','443','80','22','23','4444']
for i in validIP:
    for k in portsToScan:  
        splited = i.split(":")
        ipSplit = splited[0].split(".")
        for j in range(256):
            brutIPList += ['.'.join([ipSplit[0],ipSplit[1],ipSplit[2],str(j)])+':'+k]

def fuckyou(inp_ip):
    try:
        print("Scanning: {}\n".format(inp_ip))
        requests.get("http://{}".format(inp_ip))
        #newValidIPs += [inp_ip]
        print("WOWOWOWOWO {}".format(inp_ip))
    except:
        print("This IP Sucks: {}\n".format(inp_ip))
        pass

for i in range(len(brutIPList)):
    threading.Thread(target=fuckyou, args=(brutIPList[i],)).start()