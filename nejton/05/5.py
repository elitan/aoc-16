import hashlib

a = 0
counter = 0
output = ""
output2 = [" " for x in range(0,8)]
while counter < 8 or " " in output2:
    md5 = hashlib.md5()
    md5.update("abbhdwsy" + str(a))
    text = md5.hexdigest()
    if text.startswith("00000"):
        if counter < 8:
            output += text[5]
        if text[5] in "01234567" and output2[int(text[5])] == " ":
            output2[int(text[5])] = text[6]
        counter += 1
    a += 1

print "1:", output
print "2: " + "".join(output2)
