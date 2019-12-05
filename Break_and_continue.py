# break and continue

print("for loop 1 with break")
for i in range(20):
 if i > 10:
  break
 else:
  print(i)

print("\nfor loop 2 with continue")
for i in range(20):
 if i < 10:
  if i % 2 == 0:
   continue
  print(i)

# khi gặp break thì chương trình sẽ dừng hẳn 1 vòng lặp (while, for) gần lệnh break nhất
# còn lại các vòng lặp bên ngoài vẫn chạy bt
# khi gặp continue thì chương trình bỏ qua bước đang chạy của vòng lặp và 
# tiếp tục chạy bước tiếp theo trong vòng lặp (ko bỏ qua vòng lặp mà chỉ bỏ qua bước hiện tại)
