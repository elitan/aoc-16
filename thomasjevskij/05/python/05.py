import hashlib, time

t = time.process_time()
with open('input.txt') as f:
    door = f.readlines()[0].strip()

password1 = ''
password2 = '        '
ii = 1

while ' ' in password2:
    k = '{0}{1}'.format(door, ii)
    m = hashlib.md5()
    m.update(k.encode('utf-8'))
    s = m.hexdigest()
    if s.startswith('00000'):
        password1 += s[5]
        if s[5] in '01234567':
            index = int(s[5])
            if password2[index] == ' ':
                password2 = password2[0:index] + s[6] + password2[index + 1:]

    ii += 1
print('Problem 1: {0}'.format(password1[0:8]))
print('Problem 2: {0}'.format(password2))
t = time.process_time() - t
print('Time elapsed: {0} seconds'.format(t))
