import hashlib
text = input('Enter whatever string to hash: ')
username = input('Enter username: ')
#greeting = "Start where you are with what you have and do what you can do. Wish you all the best and thanks a lot !!!"

hash_text = hashlib.md5(text.encode())
hash_username = hashlib.md5(username.encode())
#hash_greeting = hashlib.md5(greeting.encode())

print(hash_text.hexdigest())
print(hash_username.hexdigest())
#print(hash_greeting.hexdigest())
