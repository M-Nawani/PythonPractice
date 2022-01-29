with open("file1.txt") as file1:
    file_1_list = file1.readlines()

with open("file2.txt") as file2:
    file_2_list = file2.readlines()

# Using a for loop
result = []
for content in file_1_list:
    if content in file_2_list:
        stripped_content = content.strip()
        result.append(int(stripped_content))

# Using a list comprehension
result_comprehension = [int(content) for content in file_1_list if content in file_2_list]

print(result)
print(result_comprehension)
