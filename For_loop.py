# for loop

a = "Python"
b = ['i', 'am', 'a', 'student']
list = [("a", 2),"string1", ["r", 126]]
tuple = (1, 2, 3, 4, 5)
dict = {'k1': 'v1', 'k2': 6, "k3": 9}
set = {1, 2, 3, 4, 5}

print("\nfor string:")
count = 0
for i in a:
 if i == 't':
   count += 1
print('amount of letter "t" is ', count)

print("\nfor list:")
string =''
for i in b:
 string = string + i + ' '
print(string)

for i in list:
 print(i)

print("\nfor tuple:")
count = 0
for i in tuple:
 count += i
print(count)

print("\nfor dictionary:")
for k, v in dict.items():
 print(k)
 print(v)
for k in dict.keys():
 print(k)
for v in dict.values():
 print(v)

print("\nfor set:")
for i in set:
 print(i)
 
# for loop có thể dùng cho nhiều loại data như trên nhưng chúng phải đc đưa về dạng có index. 
# ví dụ như với dictionary ta phải truy cập với các items, key và values, đầu ra của chúng là các list
# tương tự đối với while loop
