

import random
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
number="0123456789"
symbol="!@#$%^&*?."
special=random.choices(symbol,k=2)
capital=random.choices(upper,k=3)
lower=random.choices(lower,k=4)
result=special + capital + lower
print(f"generated password is:","".join(result))
