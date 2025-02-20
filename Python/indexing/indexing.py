#indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step] - slicing operator

credit_number = "1234-5678-9012-3456"
print(credit_number[0]) # 1
print(credit_number[1]) # 2
print(credit_number[:4]) # 1234
print(credit_number[5:9]) # 5678
print(credit_number[5:]) # 5678-9012-3456
print(credit_number[-4:]) # 3456
print(credit_number[::2]) # 135790246
print(credit_number[::-1]) # 6543-2109-8765-4321

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}") # XXXX-XXXX-XXXX-3456
