#!/bin/bash
echo "Which installation do you want to perform? [s]erver, [c]lient or [b]oth?"
read VAR

if  [ $VAR == s ]; then
  docker-compose up -d
  exit 1
elif [ "$VAR" == c ]; then
  USER=$(/usr/bin/whoami)
  FIRST='*/5 *    * * * '
  SECOND='  /usr/bin/python3'
  SCRIPT_DIR=$(pwd)
  sudo sed -i '$ a '"$FIRST $USER $SECOND $SCRIPT_DIR"'/collector.py' /etc/crontab
  exit 1  
else
  if [ "$VAR" == b ]; then
      docker-compose up -d
      
      USER=$(/usr/bin/whoami)
      FIRST='*/5 *    * * * '
      SECOND='  /usr/bin/python3'
      SCRIPT_DIR=$(pwd)
      sudo sed -i '$ a '"$FIRST $USER $SECOND $SCRIPT_DIR"'/collector.py' /etc/crontab
    exit 1
fi
fi