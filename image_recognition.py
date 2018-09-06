# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 10:34:10 2018

@author: A53445
"""

from openalpr import Alpr
import sys

alpr = Alpr("gb", "openalpr.conf", "runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(1)
alpr.set_default_region("gb")

results = alpr.recognize_file("samples/Capture_ne2x.png")#specify the image to detect here

i = 0
for plate in results['results']:
    i += 1
    print("Plate #%d" % i)
    print("   %12s %12s" % ("Plate", "Confidence"))
    for candidate in plate['candidates']:
        prefix = "-"
        if candidate['matches_template']:
            prefix = "*"

        print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))

# Call when completely done to release memory
#alpr.unload()