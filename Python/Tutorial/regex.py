import re

original_string = '1234&abc_python regex'
result_filter = re.findall('\d', original_string)
print(result_filter)