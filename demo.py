import random
import string

def generate_short_code(length=8):
    characters = string.ascii_letters + string.digits
    print(characters)
    return ''.join(random.choices(characters, k=length))


f = [1,2,4,5]
print(f[-1])
