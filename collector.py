#!/usr/bin/env python

import datetime
import psutil
import socket
from influxdb import InfluxDBClient

# influx configuration - edit these
ifuser = "ssc"
ifpass = "password"
ifdb   = "simplestatcollector"
ifhost = "192.168.178.11"
ifport = 8086

# configure network device name and disk path
net = ('eno1')
drive =('/')
sensor = ('coretemp') # for rpi4 put in: ('cpu_thermal')

#get hostname and take a timestamp for this measurement
hostname = socket.gethostname()
time = datetime.datetime.utcnow()

# collect some stats from psutil
cpu = psutil.cpu_percent(interval=1)
disk = psutil.disk_usage(drive)
mem = psutil.virtual_memory()
load = psutil.getloadavg()
temp = (psutil.sensors_temperatures().get(sensor)[0][1])
bsend = (psutil.net_io_counters(pernic=True).get(net)[0])
breceived = (psutil.net_io_counters(pernic=True).get(net)[1])

# format the data as a single measurement for influx
data = [
    {
        "measurement": hostname,
        "time": time,
        "fields": {
            "cpu": cpu,
            "load_1": load[0],
            "load_5": load[1],
            "load_15": load[2],
            "disk_percent": disk.percent,
            "disk_free": disk.free,
            "disk_used": disk.used,
            "mem_percent": mem.percent,
            "mem_free": mem.free,
            "mem_used": mem.used,
            "temp": temp,
            "bsend": bsend,
            "breceived": breceived
        }
    }
]

# connect to influx
ifclient = InfluxDBClient(ifhost,ifport,ifuser,ifpass,ifdb)

# write the measurement
ifclient.write_points(data)