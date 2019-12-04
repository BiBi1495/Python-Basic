# Co begin with file 

# open and close the file

str1 = open("filename.txt", "wb")
# ta còn cách mở file khác như sau: with open("filename.txt", "ưb") as str1:
# Đối số str1 là một giá trị chuỗi chứa tên của các file mà bạn muốn truy cập. 
# filename.txt là tên file mà bạn muốn mở. Nếu file này ko nằm chung tệp với file python đang viết thì bạn phải chỉ rõ đường dẫn
# Các "wb" xác định các chế độ của file được mở ra như read, write, append,... Đây là thông số tùy chọn và chế độ truy cập file mặc định là read (r).

str1.name # trả về tên file đang mở
str1.cloed # trả về True nếu file đang đóng, False nếu file đang đc mở
str1.mode # trả về chế độ của file đang đc mở. Ở đây sẽ trả về file text "wb"
str1.close() # đóng file đang đc mở

# read file 

f = open('vidu.txt', 'r') # mở file chỉ để đọc
str= f.read() # trả về nội dung file vào biến string str
str2 = f.read([5]) # trả về 5 - 1 = 4 kí tự đầu tiên trong nội dung file
print ('Noi dung file la:\n', str)

line1 = f.readline(0) # trả về từng dòng trong file. Hàm f.readline() trả về 1 list gồm các pt là các string là các dòng theo thứ tự
line2 = f.readline(1)
print ('Dòng 1: ', line1)
print ('Dòng 2: ', line2)

# write file 
f.write( "Python là ngôn ngữ tốt nhất") # ghi chuỗi trong ngoặc kép vào vị trí con trỏ ở trong file

# rename file 
os.rename("<tên file hiện tại>", "<tên file mới>")

# remove file 
os.remove("<tên file>")

# vị trí trong file. Sau đây là ví dụ mới

# Mở file
file = open("plc.txt", "r+") # r+ là chế độ để đọc và ghi
str = file.read(10); # đọc 9 kí tự đầu tiên trong file
print("Chuỗi đã đọc là: ", str)

# Kiểm tra con trỏ hiện tại
vitri = file.tell();
print("Con trỏ hiện tại: ", vitri)

# Đặt lại vị trí con trỏ tại vị trí đầu file
vitri = file.seek(0, 0);
str = file.read(10);
print("Chuỗi đã đọc là : ", str)
#Phương thức tell() sẽ nói cho bạn biết vị trí hiện tại bên trong file. Nói cách khác, việc đọc và ghi tiếp theo sẽ diễn ra trên các byte đó.
#Phương thức seek(offset, from) thay đổi vị trí hiện tại bên trong file.
#Tham số offset là chỉ số byte để được di chuyển.
#Tham số from xác định vị trí tham chiếu mà từ đó byte được di chuyển.
#Nếu from là 0 thì sử dụng phần đầu file như là vị trí tham chiếu
#Nếu from là 2 thì sử dụng phần cuối file như là vị trí tham chiếu.

# Đóng file
file.close()

# một ví dụ về vị trí của con trỏ
f = open("file.txt", "r")
print(f.read()) # đọc toàn bộ file, sau đó con trỏ sẽ nằm tại vị trí cuối file. Và nếu bạn đọc toàn bộ file một lần nữa thi sẽ ko đọc đc gì cả. Vì vậy muốn đọc thì phải đặt lại vị trí con trỏ về đầu file
f.seek(0)
print(f.read())
