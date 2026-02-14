#!/bin/bash
LOG_DIR="/opt/splunk/var/log/alerts"

echo "Monitoring Splunk alerts..."
tail -f $LOG_DIR/scheduler.log | grep --line-buffered "Alert"
