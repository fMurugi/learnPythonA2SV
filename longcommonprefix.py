def long_common_prfix(strs):   
    

    prefix = strs[0]

    for string in strs[1:]:
        while string.find(prefix) != 0:
            prefix = prefix[:-1]

            if not prefix:
                return ""


    return prefix

strs=["flower","flow","flight"]
print(long_common_prfix(strs))

str = 'flow'
if not str:
    print("it is empty")
str2 ="abcd"
result = ""

for char in str:
    for char2 in str2:
        result+=char
        result+=char2

print(result)

# zip returns