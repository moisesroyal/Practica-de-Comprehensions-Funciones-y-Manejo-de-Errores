import sys
print(sys.path)

import re
text = 'Mi numero de telefono es 507 6244 5981, el codigo del pais es 507, mi numero de la suerte 16'
result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)