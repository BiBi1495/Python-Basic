# Co tuple 24

tupl = (['a', 3, 'r'], 'stri', 2) # khởi tạo giá trị của tuple bằng ngoặc tròn, còn đối với list là ngoặc vuông, đối với dictionary là ngoặc nhọn
lis = [1, 4, 7]

# truy cập
print(tupl[0][1]) # cách truy cập giống với list và dictionary

# hàm index và count
tupl = ('a', 'b', 'b')
lis = ['a', 'b', 'b']

print(tupl.index('a')) # cho ra vị trí của kí tự a
print(lis.index('b')) # hàm này cũng áp dụng đc cho list

print(tupl.count('b')) # cho ra số lần lặp lại của kí tự b
print(lis.count('a')) # hàm này cũng áp dụng đc cho list

# thay đổi - điểm khác biệt giưa list và tuple

tupl[1] = 1 # dòng này gây lỗi đối với tuple nhưng list thì có thể đc
