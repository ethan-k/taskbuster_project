import string
import random

chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')
 
SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(50)])
f = open("key.txt", 'w')
f.write(SECRET_KEY)
print (SECRET_KEY)