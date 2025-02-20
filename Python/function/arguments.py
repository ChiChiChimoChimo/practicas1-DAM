# *args       = allows you to pass multiple non-key arguments to a function
# **kwargs    = allows you to pass multiple key-value arguments to a function
#              * unpacking operator
#              ** packing operator
#            *args must come before **kwargs

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")

shipping_label("John Doe", "123 Main St", "New York", "NY", "10001", "USA", company="ABC Corp", weight="20 lbs", fragile=True)
shipping_label("Jane Doe", "123 Main St", "New York", "NY", "10001", "USA", company="XYZ Corp", weight="10 lbs", fragile=False)

