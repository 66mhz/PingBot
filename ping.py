import os
import json
from pushover import Client
#set pushover client, hostnames to check, pushover message, and string to store results
client = Client("client goes here", api_token="api token here", device="device name optional")
#add hosts to be checked
hostname = ['localhost', '192.168.0.1']
msg = ""
data = {  "offline":[]}
#open json file and store contents
with open('/home/pi/ping.json') as data_file:
			data = json.load(data_file)
#ping each host set in hostname variable
for host in hostname:
	response = os.system("ping -c 1 " + host)
	if response == 0:
		print str(host), 'is up!'
		#check content for each offline key in json data
		if host in data["offline"]:
			#host is back online, remove host from offline key in json file
			data["offline"].remove(host)
	else:
		#check to see if host is already known as offline
		if host in data["offline"]:
			#host found in offline key, no action necessary
			print "Already sent notification for host " + str(host)
		else:
			#host not known as offline, send notification, add host to offline key
			print str(host), 'is down!'
			data["offline"].append(host)
			msg = msg + "\n" + str(host) + " is down"
	print "-----------------------------------------------------------------------------"
	print " "
#converts our string to json
json_data = json.dumps(data)	
print "Writing json data..."
print json_data
#writes udpated json file
with open('/home/pi/ping.json', 'r+') as f:
    f.seek(0)
    f.write(json.dumps(data))
    f.truncate()
print "Json data written successfully"

if msg:
	#msg has content, send notification
	client.send_message(msg, title="pingbot")
