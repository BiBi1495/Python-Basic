# map dùng để thực hiện hàm cho nhiều đối số, các đối số này thường nằm trong list,...
def square(n):
 return(n**2)
 
list1 = [1,2,3,5,8]
list2 = list(map(square,list1))
print(list2)

# filter giống như map nhưng chỉ dùng đc với hàm trả về True hoặc False. Filter sẽ lọc ra những giá trị làm cho hàm trả về True
def even(n):
 if n % 2 == 0:
  return(True)
 else:
  return(False)
list3 = list(filter(even,list1))
print(list3)

# Lambda 
binhphuong = lambda n: n**2 # biểu thức này đại diện cho hàm square như trên nhưng ko cần khai báo.
# Nó đc dùng giống như def nhưng tiện hơn vì ko cần định nghĩa. Nó tiện lợi khi hàm đơn giản.
print(binhphuong(8))

# using lambda with map
list4 = list(map(lambda n: n**2, list1))
print(list4)

# using lambda with filter
list5 = list(filter(lambda n: (n % 2) == 0, list1))
print(list5)
