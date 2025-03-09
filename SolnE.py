str=input("enter text : ")
dict={}

def replace_char(str):
    for i in range(len(str)):
        if str[i] in dict:
            str=str[:i]+ "*" + str[i+1:]
        dict[str[i]]=i
    return str

print(replace_char(str))