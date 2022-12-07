import hashlib
string ="hello how are you?"
encoded=string.encode()
result=hashlib.sha256(encoded)
print("String: ",end="")
print(string)
print("Hash value: ",end="")
print(result)
print("Hexadecima equivalent ",result.hexdigest())
print("Digest size: ",end="")
print(result.digest_size)
print("Block size: ",end="")
print(result.block_size)


