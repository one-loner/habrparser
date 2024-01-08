#!/bin/bash
if (($EUID !=0)); then
     echo Script must be run by root.
     exit
fi
cp parser.py /opt/habr-parser.py
cp habrparser /bin/habrparser
cp parser-bl.py /opt/habr-parser-bl.py
cp habrparser-bl /bin/habrparser-bl
chmod +x /bin/habrparser
chmod +x /bin/habrparser-bl
echo "Done. You can run parser for habr.coom in terminal by commands habrparser and habrparser-bl."
