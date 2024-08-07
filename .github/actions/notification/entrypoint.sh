#!/bin/sh -l

python3 mail.py --smtp_server="$1" --smtp_port="$2" --username="$3" --password="$4" --from_email="$5" --to_email="$6" 
