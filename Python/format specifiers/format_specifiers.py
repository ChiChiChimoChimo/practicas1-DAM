# format specifiers = {:flags} format a value on what flags are inserted


# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate 3 spaces, fill with 0s
# :< = left align
# :> = right align
# :^ = center align
# :+ = use plus sign to indicate a positive value
# :- = use minus sign to indicate a negative value
# :, = use comma as separator
# : = use space as separator
# := = place a sign  to the leftmost positio

price1 = 3.13159
price2 = -987.45
price3 = 123456789.123456789

print(f"{price1:.2f}") # 3.13
print(f"{price2:.2f}") # -987.45
print(f"{price3:.2f}") # 123456789.12