#!/bin/bash
if (($EUID !=0)); then
     echo Script must be run by root.
     exit
fi
cp parser.py /opt/habr-parser.py
cp habrparser /bin/habrparser
chmod +x /bin/habrparser
echo "Done. You can run parser for habr.coom in terminal by command habrparser."
