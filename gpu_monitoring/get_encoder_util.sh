nvidia-smi -q -i $1 | grep Utilization -A 4 | grep Encoder | /usr/bin/awk '{ print $3 }'