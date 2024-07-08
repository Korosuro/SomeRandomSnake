#password generator with 8 random characters (upper, lower, number)

import random
import string 

def PWGen (size=16, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

print(PWGen())