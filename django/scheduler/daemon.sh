#!/bin/bash

# Replace these three settings.
PROJDIR="/var/django/scheduler"
PIDFILE="$PROJDIR/scheduler.pid"
port="10042"

cd $PROJDIR
if [ -f $PIDFILE ]; then
    kill `cat -- $PIDFILE`
    rm -f -- $PIDFILE
fi

exec /usr/bin/env - \
  PYTHONPATH="../python:.." \
  ./manage.py runfcgi host=127.0.0.1 port=$port pidfile=$PIDFILE

