import random
import string

characters = string.ascii_letters
digits = string.digits
# symbols = string.punctuation

length = 8


password = "".join(random.sample(characters+digits, length))
print(password)

