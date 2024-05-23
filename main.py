
# open text file containing binary code seperated by commas
FILE_PATH = "./binary_files/test.txt"
HEX_FILE_PATH = "./hex_files/"
binary_string = ""
with open(FILE_PATH, 'r') as file:
    for line in file:
        for num in line:
            # if num != ',':
            #     num_list += num
            if num == ',' or num == '\n':
                continue
            binary_string += num

    

binary_string += "0000000"

binary_integer = int(binary_string, 2)

hexadecimal_string = hex(binary_integer)

slice1 = binary_string[0:4]
print(binary_string)
i = 0
binary_string_list = []
for n in range(3):
    print(n)
    binary_string_list.append(binary_string[0+i:8+i])
    i += 8

print(binary_string_list)


binary_integer_list = [int(string, 2) for string in binary_string_list]
        
print(binary_integer_list)

hexadecimal_list = [f"0x{num:02X}" for num in binary_integer_list]
print(hexadecimal_list)

with open(f"{HEX_FILE_PATH}/new.txt", 'w') as file:
    for value in hexadecimal_list:
        file.write(f"{value} ")
    file.write("\n")