from base64 import b64decode
from Crypto.Cipher import AES
import os
#import sys

key = b64decode("suDAAcy4+1Srzo5b+ljIxYc3wUhof5clyoTRiGaDH40=")
iv = b64decode("fURGR+PL4oDfiHI7FZ8fLg==")
#AES.block_size = 128
#AES.key_size = 256

dude = AES.new(key, AES.MODE_CBC, iv)
dir = "./Share/"

def pwn(file):
	with open(dir + file, "rb") as f, open(dir + file.replace(".crpt", ''), "wb") as pwn:
		data = f.read()
		data.replace(iv, b'')
		dec_data = dude.decrypt(data)
		#print(dec_data[16::])
		pwn.write(dec_data[16::])

files = os.listdir('Share/')
for file in files:
	pwn(file)
