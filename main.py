# pixels wide - needed variable for adjusting padding
PIXELS_WIDE = 17

# file names
binary_file = "test.txt"
hex_file = "new.txt"
# paths
BIN_FILE_PATH = f"./binary_files/{binary_file}"
HEX_FILE_PATH = "./hex_files/"

# empty holder for the binary string
binary_string = ""

# empty holder for binary list
binary_string_list_1 = []

# Functions
def turn_8bit(binary_string, binary_string_list):
    """Takes a binary_string and slices it into 8 characters at a time, and then appends it to binary_string_list.
    The function then returns a list containing the strings in binary_string_list as integers."""
    i = 0
    for _ in range(3):
        binary_string_list.append(binary_string[0+i:8+i])
        i += 8
    binary_integer_list = [int(string, 2) for string in binary_string_list]
    return binary_integer_list

def bit_to_hex(binary_integer_list):
    """takes a binary_integer_list and converts each item into a hexadecimal value and then returns this as a list"""
    hexadecimal_list = [f"0x{num:02X}" for num in binary_integer_list]
    return hexadecimal_list

def add_padding(pixel_width):
    if pixel_width % 8 != 0:
        padding = ""
        needed_padding = (8 - (pixel_width % 8))
        for _ in range(needed_padding):
            padding += "0"
        return padding

# read binary file and write to hex file
with open(BIN_FILE_PATH, 'r') as file:
    with open(f"{HEX_FILE_PATH}/{hex_file}", 'w') as file_2:
        for line in file:
            for num in line:
                if num == ',':
                    padding = add_padding(PIXELS_WIDE)
                    if padding:
                        binary_string += padding
                    binary_int_list = turn_8bit(binary_string, binary_string_list_1)
                    hex_list = bit_to_hex(binary_int_list)
                    for value in hex_list:
                        file_2.write(f"{value}, ")
                    file_2.write("\n")
                    print(hex_list)
                    # reinitilaze as empty holders for the next line in file
                    binary_string = ""
                    binary_string_list_1 = []
                    continue
                if num == '\n':
                    continue
                # print(f"binary_string 2: {binary_string}")
                binary_string += num