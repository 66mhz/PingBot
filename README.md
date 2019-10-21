# PingBot
Python script that pings multiple user-defined hosts and sends a Pushover alert if a host is offline. Can be used with a cron job to regularly validate whether a website or hosts on a local network are accessible. 

## Requirements 

Python 2.7

[Pushover API Client by Thibauth](https://github.com/Thibauth/python-pushover)

## Getting Started

Install Pushover API Client - you can install python-pushover from Pypi with:
```
$ pip install python-pushover
```

Or you can install it directly from GitHub:
```
git clone https://github.com/Thibauth/python-pushover.git
cd python-pushover
pip install .
```

Set Pushover client, api, and device name
```
client = Client("client goes here", api_token="api token here", device="device name optional")
```

Set hostnames to check
```
hostname = ['localhost', '192.168.0.1', 'google.com']
```

Run the script
```
$ python ping.py
```
