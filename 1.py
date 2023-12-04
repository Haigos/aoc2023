text = """
dlcbjflsix5ttvjdxzzeightcffrtfjcjpxtwostrdc
fiveone645fivellfcmqqmnine
hxdtshfive115tfvrzqhgftwojtjrcshgtq
6nqrfrhv17jdxpfmmdt4five
sevenxtpjxnrr1
krzkthreegjnqrfbsdrkqptd33rsvrzvvffqhreight
472ggfive56hgnvz
12tkpchqtnine
vdbsctv6eightth82
fivetngxlttf4
5nss
5onesixsevenphxtmlqhzfcjxrknpv
gldsixrhss186seven6
gnpksz4
4919
pbc19
"""

firstNumber = None
secondNumber = None
total = 0

for i in text:
    if not i.isalnum():
        if firstNumber is not None and secondNumber is not None:
            total += int(firstNumber + secondNumber)
            print(firstNumber, secondNumber, total)
        firstNumber = None
        secondNumber = None
    elif i.isalpha():
        pass 
    elif i.isdigit():
        if firstNumber is None:
            firstNumber = i
            secondNumber = i
        else:
            secondNumber = i

print(total)