
import re

text_str = '2016-10-10 00:00:00'
datetime_part = re.search('\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d', text_str)
print datetime_part.group()




