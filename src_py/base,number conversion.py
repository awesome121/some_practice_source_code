def To_hexadecimal(num):
    hexa_table = '0123456789ABCDEF'
    if num < 16:
        return hexa_table[num]
    else:
        return To_hexadecimal(num//16) + hexa_table[num%16]
    
num = 155
print(To_hexadecimal(num))


def To_binary(num):
    binary_table = '01'
    if num < 2:
        return binary_table[num]
    else:
        return  To_binary(num//2) + binary_table[num%2]
    
num = 10
print(To_binary(num))

def To_anybase(num, base):
    hexa_table = '0123456789ABCDEF'
    if num < base:
        return hexa_table[num]
    else:
        return To_anybase(num//base, base) + hexa_table[num%base]
    
    
num = 62
base = 3
print(To_anybase(num, base))