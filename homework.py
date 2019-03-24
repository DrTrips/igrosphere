import hashlib

<<<<<<< HEAD
my_name = "a.kulikov"
m = hashlib.md5()
m.update(my_name.encode())

if __name__ == "__main__":
    print(f"Task completed by {my_name}! md5 hash is {m.hexdigest()}")
