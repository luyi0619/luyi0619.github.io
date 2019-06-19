#!/usr/local/bin/python3

import subprocess
import os

# brew install imagemagick ghostscript

pdfs = [f for f in os.listdir('../') if f.endswith('.pdf')]

for p in pdfs:
  cmd = "convert -thumbnail x300 -background white -alpha remove '../%s[0]' %s.png" % (p, p[:-4])
  subprocess.run(cmd, shell=True, check=True, text=True)
