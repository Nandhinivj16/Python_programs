#break
print("enter list of numbers.enter z to exit")
list_num=[]

while True:
    inp=input()
    if inp =='z':
        break
    list_num.append(int(inp))
print(list_num)

#continue
str1="A,B,C,D,E"
str2=''
for i in str1:
        if i ==',':
            continue
        str2=str2+i
print(str2)

str1="A,B,C,D,E"
str2=''
for i in str1:
        if i ==',':
            pass
        else:
         str2=str2+i
print(str2)

#split and join
letters="abc def ghi jkl"
split_list = letters.split(' ')
print(split_list)

str_join='_'.join(split_list)
print(str_join)
