#!/usr/bin/env python
import readline
import subprocess

subprocess.call(["time", "coverage", "run", "test_rpn.py"])
subprocess.call(["coverage", "report", "-m"])
