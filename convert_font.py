from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Load the TTF font
font_name = 'Danfo-Regular'
font_path = f'./fonts/{font_name}.ttf'  # Replace with the path to your TTF file
font = TTFont(font_path)

# Specify the font size
font_size = 24  # You can adjust this as needed

# Create an ImageFont instance
pil_font = ImageFont.truetype(font_path, font_size)

# Characters to convert

characters = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{{|}}~'

# Function to convert image to hex
def image_to_hex(image):
    image = image.convert('1')  # Convert to 1-bit pixels
    pixels = np.array(image)
    hex_data = []
    for row in pixels:
        hex_row = ', '.join(['0x{:02X}'.format(byte) for byte in np.packbits(row)]) + ','
        hex_data.append(hex_row)
    return hex_data


# Loop through each character and convert to hex
font_hex_data = {}
for char in characters:
    # Create an image with the character
    image = Image.new('L', (font_size, font_size), 0)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), char, 255, font=pil_font)
    
    # Convert the image to hex
    hex_data = image_to_hex(image)
    font_hex_data[char] = hex_data


# Print the hexadecimal data for each character
# for char, hex_data in font_hex_data.items():
#     print(f'Character: {char}')
#     for row in hex_data:
#         print(row)
#     print()

# Save the hex data to a file if needed
with open(f'./hex_files/{font_name}{font_size}.c', 'w') as f:
    f.write('#include "fonts.h"\n')
    f.write("const uint8_t customFont24_Table [] =\n")
    f.write("{\n")
    for char, hex_data in font_hex_data.items():
        f.write(f'//Character: {char}\n')
        for row in hex_data:
            f.write('\t' + row + '\n')
        f.write('\n')
    f.write("};")
