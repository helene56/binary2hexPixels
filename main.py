
#pseudo code
# read first line in binary text file and transfer to string
# when , or \n reached add padding on the string (padding have to determined by a function)
# seperate into 8 bit and append to a list that holds the seperated strings
# turn every 8 bit into a integer
# turn every 8 bit integer into hexadecimal
# write line to hex file
# empty binary string holder
# next line repeat..

# read_binary(filepath)
# turn_8bit()
# turn_hex()
# write_to_hexfile()
# empty_string
binary_string_list_1 = []

# should add something that determines the range, now it is set to fit a binary number that is 24 bit
def turn_8bit(binary_string, binary_string_list):
    i = 0
    for _ in range(3):
        binary_string_list.append(binary_string[0+i:8+i])
        i += 8
    binary_integer_list = [int(string, 2) for string in binary_string_list]
    return binary_integer_list

def bit_to_hex(binary_integer_list):
    hexadecimal_list = [f"0x{num:02X}" for num in binary_integer_list]
    return hexadecimal_list


# open text file containing binary code seperated by commas
BIN_FILE_PATH = "./binary_files/test.txt"
HEX_FILE_PATH = "./hex_files/"
binary_string = ""
with open(BIN_FILE_PATH, 'r') as file:
    with open(f"{HEX_FILE_PATH}/new.txt", 'w') as file_2:
        for line in file:
            for num in line:
                if num == ',':
                    continue
                if num == '\n':
                    print(f"binary_string: {binary_string}")
                    binary_string += "0000000"
                    binary_int_list = turn_8bit(binary_string, binary_string_list_1)
                    hex_list = bit_to_hex(binary_int_list)
                    for value in hex_list:
                        file_2.write(f"{value} ")
                    file_2.write("\n")
                    print(hex_list)
                    binary_string = ""
                    binary_string_list_1 = []

            binary_string += num

# def read_binary(filepath):
#     global binary_string
#     with open(filepath, 'r') as file:
#         for line in file:
#             for num in line:
#                 if num == ',' or num == '\n':
#                     return
#                 binary_string += num


# binary_string += "0000000"

# binary_integer = int(binary_string, 2)

# hexadecimal_string = hex(binary_integer)

# slice1 = binary_string[0:4]






# for n in range(3):
#     binary_string_list.append(binary_string[0+i:8+i])
#     i += 8

# print(binary_string_list)


# binary_integer_list = [int(string, 2) for string in binary_string_list]
        
# print(binary_integer_list)

# hexadecimal_list = [f"0x{num:02X}" for num in binary_integer_list]
# print(hexadecimal_list)
# will make a function for reading a line and then writing line later
# with open(f"{HEX_FILE_PATH}/new.txt", 'w') as file:
#     for value in hexadecimal_list:
#         file.write(f"{value} ")
#     file.write("\n")