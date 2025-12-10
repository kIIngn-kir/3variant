# Файл converter.py
# Автор: Белоусов В.В.

num = input("Введите число: ")
base = input("Укажите исходную систему (dec/bin/hex): ").lower()

if base == "dec":
    dec_num = int(num)
elif base == "bin":
    dec_num = int(num, 2)
elif base == "hex":
    dec_num = int(num, 16)
else:
    print("Ошибка: неизвестная система счисления")
    exit()

print(f"DEC: {dec_num}")
print(f"BIN: {bin(dec_num)[2:]}")
print(f"HEX: {hex(dec_num)[2:].upper()}")
