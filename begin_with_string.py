# Co string 15, 16, 17
mystring = "abcdefgHJKlmn"

print(mystring[2:6], "\n")
#print(mystring[::]) lỗi vì hai dấu hai chấm nghĩa là bạn sẽ phải điền step ở cuối, nếu ko điền thì sẽ lôi
print(mystring[::2],"\n")
print(mystring[6:1:-2], '\n')

print(mystring.upper()) # in ra chữ hoa
print(mystring.lower()) # in ra chữ thường

# chia string bởi dấu hiệu nào đó
newstr = "shi is mi sister hinght"
print(newstr.split()) # chia các chữ bởi khoảng trống
print(newstr.split('i')) # chia các chữ bởi kí tự i
