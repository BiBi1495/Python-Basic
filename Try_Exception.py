# Error and Exceptions
# Ngoại lệ có thể là bất kỳ điều kiện bất thường nào trong chương trình mà phá vỡ luồng thực thi chương trình đó. 
# Bất cứ khi nào một ngoại lệ xuất hiện, mà không được xử lý, thì chương trình ngừng thực thi và vì thế code không được thực thi.
# Python đã định nghĩa sẵn rất nhiều ngoại lệ. 
# Nếu bạn thấy bất cứ code nào là khả nghi (có thể gây ra ngoại lệ) thì bạn có thể phòng thủ chương trình của mình bằng 
# cách đặt các khối code khả nghi này trong một khối try. Khối try này được theo sau bởi lệnh except. Sau đó, nó được theo sau bởi các lệnh mà xử lý vấn đề đó.

b = input()
try: # nếu ko có khối try-except thì khi nào có lỗi xảy ra thì ctrinh sẽ ngừng chạy
 a = 4/int(b) # bất cứ khi nào ngoại lệ xảy ra thì các lệnh trong khối try đều dừng lại.
# và nhảy xuống khối except, nếu trong khối except đc tìm đúng lỗi như ở trên. 
# trong trường hợp này là lỗi chia cho 0 đc python định nghĩa là ZeroDivisionError.
# Nếu ko đc tìm đúng lỗi thì khối else sẽ đc thực hiện. Và cuối cùng là chạy tiếp các lệnh sau đó.
 print("block try occur")
except ZeroDivisionError: # nếu ở đây chỉ ghi là except: thì tất cả các lỗi sẽ đều đc tìm đúng và đc xử lý như nhau
# có thể thêm các khối except tương tự như trên để xử lý các lỗi khác nhau
 print("error : division 0")
else: # nếu lỗi đc tìm đúng thì khối else sẽ ko đc thực hiện
 print("block else occur")
print("After block try-except-else")

# Tự xây dựng exception bằng câu lệnh raise exception
try:
 x = input('Nhập một số trong khoảng 1-10: ')
 if x<1 or x>10:
 raise Exception # cau lenh raise la de tao ra exception, moi khi co cau lenh raise thi 1 exception dc tao ra
 print("Bạn vừa nhập một số hợp lệ")
except:
 print("Số bạn vừa nhập nằm ngoài khoảng cho phép")
# nếu bạn nhập một số bên ngoài các phạm vi cho phép, các lệnh print trong các except block sẽ được thực hiện.

# raise Exceptions dung de tao ra 1 exception
print(1)
raise ValueError
print(2)
# ket qua in ra man hinh la
#1
#ValueError

# khối lệnh try-finally
try:
 f = open("test.txt",encoding = 'utf-8')
 # thực hiện các thao tác với tệp
finally: # các lệnh trong khối finally luôn chạy cho dù có lỗi xảy ra hay ko
 f.close()
#ta có thể yên tâm file được đóng đúng ngay cả khi phát sinh ngoại lệ khiến chương trình dừng đột ngột.

# lệnh Assert dùng để kiểm tra điều kiện có đúng hay ko. nếu ko thì xảy ra AsertionError
temp = 10
assert temp > 20 # biểu thức temp > 20 phải có dạng True hoặc False
print("after assert")
# kết quả in ra 
#AssertionError

# ta cũng có thể thêm text sau điều kiện để nó in ra sau chữ AssertionError
temp = 10
assert temp > 20, "temp have to > 20"
# kết quả in ra 
#AssertionError:temp have to > 20
