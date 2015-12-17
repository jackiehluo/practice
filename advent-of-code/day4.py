import hashlib

string = 'bgvyzdsv'
n = 0

while True:
    h = hashlib.new('md5')
    h.update("%s%d" % (string, n))
    if h.hexdigest()[:5] == '00000':
        break
    n += 1

print n