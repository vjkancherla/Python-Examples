#!/usr/bin/env python3

import subprocess

p1 = subprocess.Popen(["dnf", "list", "--installed"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "php"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
p3 = subprocess.Popen(["awk", "'{print $1}'"], stdin=p2.stdout, stdout=subprocess.PIPE)
p2.stdout.close()
output = p3.communicate()
print(output)
