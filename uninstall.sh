#!/bin/bash
if (($EUID !=0)); then
     echo Script must be run by root.
else
     rm /opt/habr-parser.py
     rm /bin/habrparser
     echo "Done. Habrparser removed from your computer."
fi
