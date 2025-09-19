#!/bin/bash
# Simple example of synchronizing zone files between servers
#rsync -avz /etc/bind/db.farhad.local server03:/etc/bind/db.farhad.local
if [ -f /etc/bind/db.farhad.local ]; then
    echo "Zone file exists: /etc/bind/db.farhad.local"
else
    echo "Zone file NOT found!"
fi
