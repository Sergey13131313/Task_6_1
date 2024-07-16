# Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX.
# Однако, в оборудовании cisco MAC-адреса используются в
# формате XXXX.XXXX.XXXX.
# Написать код, который преобразует MAC-адреса в формат cisco
# и добавляет их в новый список result. Полученный список
# result вывести на стандартный поток вывода (stdout) с помощью print.

mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]

result = []
for x in mac:
    result.append(x.replace(':', '.'))
print(result)