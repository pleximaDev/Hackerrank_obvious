# -*- coding: utf-8 -*-
import math
# import numpy
AB = int(raw_input())
BC = int(raw_input())
# AC = math.sqrt(AB**2 + BC**2)
# MC = AC/2
# out = str(math.degrees(math.asin(MC/BC)))
# print out[:(len(out) - 2)] + "°"
print str(int(round(math.degrees(math.atan2(AB,BC)))))+'°'



