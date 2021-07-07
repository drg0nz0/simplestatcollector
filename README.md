# simplestatcollector

simplestatcollector made with python writes system statistic data to an influxdb which can easily be visualized with grafana.

i wanted a dead simple and ultra lightweight system monitoring for my rpi4 docker swarm.

please check the configuration from line 9 - 18 in the collector.py before installing.
the standart interval for is 5min

/etc/crontab
```python
*/5 *    * * *  ubuntu   /usr/bin/python3 /home/ubuntu/collector.py
```
