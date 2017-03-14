#!/usr/bin/env python
import readline
import subprocess
subprocess.call("./runTests.sh")
subprocess.call(["coverage", "run", "test_rpn.py"])
subprocess.call(["coverage", "report", "-m"])
