# simplestatcollector

simple stat collector made with python writes data to influxdb which can easily be visualized with grafana
i wanted a dead simple and ultra lightweight system monitoring for my rpi4 docker swarm.
so i made one

please ckeck the configuration from lin 9 - 18 in the collector.py before installing
the standart interval for is 5min

/etc/crontab
```python
*/5 *    * * *  ubuntu   /usr/bin/python3 /home/ubuntu/collector.py
```
