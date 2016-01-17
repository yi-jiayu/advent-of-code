from tqdm import tqdm
from hashlib import md5

TARGET = '000000'
SECRET_KEY = 'yzbqklnj'
nonce = 0
hash_ = ''

with tqdm() as pbar:
    while hash_[0:len(TARGET)] != TARGET:
        nonce += 1
        attempt = SECRET_KEY + str(nonce)
        m = md5()
        m.update(str.encode(attempt))
        hash_ = m.hexdigest()
        pbar.update(1)

print(nonce)
