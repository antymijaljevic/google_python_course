#!/home/amijaljevic/anaconda3/bin/python3

import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opet/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)