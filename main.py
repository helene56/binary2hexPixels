
# open text file containing binary code seperated by commas
FILE_PATH = "./binary_files/test.txt"
num_list = ""
with open(FILE_PATH, 'r') as file:
    for line in file:
        for num in line:
            # if num != ',':
            #     num_list += num
            if num == ',':
                continue
            num_list += num

        
print(num_list)
        
