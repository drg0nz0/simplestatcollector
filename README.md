# simplestatcollector

simple stat collector made with python writes data to influxdb which can easily be visualized with grafana

please change the "ifhost" inside of the collector.py
the standart interval for is 5min

/etc/crontab
```python
*/5 *    * * *  ubuntu   /usr/bin/python3 /home/ubuntu/collector.py
```