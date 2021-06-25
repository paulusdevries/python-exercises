regex_integer_in_range = r"[1-9][0-9]{5}"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(1\d1|2\d2|3\d3|4\d4|5\d5|6\d6|7\d7|8\d8|9\d9|0\d0))"	# Do not delete 'r'.


import re
P = input()

# print (bool(re.match(regex_integer_in_range, P))
# and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
print(re.match(regex_integer_in_range, P))
print(re.findall(regex_alternating_repetitive_digit_pair, P))
