# Co List
danhsach = ["abc", 356, ["a", 'abs', 76]]
print(danhsach[2][2]) # in ra phần tử cuối của phần tử cuối của danhsach. string cũng giống list nhưng phần tử của string chỉ là kí tự, phần tử của list thì đa dạng, và chúng ta có thể truy cập đến các phần tử của phần tử của nó
danhsach[1] = "bibi" # có thể thay đổi phần tử của list nhưng ko thay đổi đc phẩn tử của string theo cách này
print(danhsach)

# một số hàm với list
danhsach.append("hehe") # thêm phần tử vào cuối danh sách
print(danhsach)

str=danhsach.pop() # xoá phần tử cuối và hàm này trả về phần tử cuối đó cho biến str
print(danhsach)
print(str)

str1=danhsach.pop(1) # xoá phần tử có số thứ tự là 1 và trả về phần tử đó
print(str1)

# xắp xếp list
str2 = ['b', 'a', 'k', 'e', 'z', 'm']
str2_sorted=str2.sort() # sắp xếp các chữ cái theo bảng chữ cái và hàm này ko trả về cho biến str2_sorted mà trả về cho str2
print(str2)

str2.reverse() # sắp xếp ngc bảng chữ cái và cũng trả về giống như hàm sort
print(str2)
# ngoài ra có thể sắp xếp các số tử nhỏ đến lớn và ngc lại theo cách tương tự
