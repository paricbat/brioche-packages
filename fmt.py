#!/usr/bin/env python3

import subprocess
import os

if __name__ == "__main__":
    for x in os.walk("packages"):
        if x[2].count("project.bri") == 1:
            print("formatting {}".format(x[0]))
            subprocess.run(["brioche", "fmt", "-p", x[0]])
