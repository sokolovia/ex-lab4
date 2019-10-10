#!/usr/bin/env python3
from math import fabs
data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
print(sorted(data, key=lambda x: fabs(x)))
# Реализация задания 3