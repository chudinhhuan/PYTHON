
# f = open("PYTHON/work_file/ten_moi.txt","w",encoding="utf-8")
# for i in range(11):
#     f.write(f"Day la dong thu {i} \n")

# f.close()

# f=open("PYTHON/work_file/new_name.txt","a",encoding="utf-8")
# for i in range(11):
#     f.write(f"Day la dong thu {i}\n")
# f.close()

# Để chắc chắn luôn đóng tệp sau khi mở
# cach 1
# f = open("PYTHON/work_file/ten_moi1.txt",encoding="utf-8")
# try:
#     for i in range(12):
#         f.write(f"day al dong thu {i}\n")
# finally:
#     f.close()
# cach 2 
# with open("PYTHON/work_file/ten_moi1.txt",encoding="utf-8") as f:
#     for i in range(10):
#         f.write(f"day la dong thu{i}\n")

# # read file
# f = open("PYTHON/work_file/ten_moi.txt",'r',encoding="utf-8")
# print(f.read(10))
# f.close()

# --- doc 1 row
f = open("PYTHON/work_file/ten_moi.txt",'r',encoding="utf-8")
# doc 1 row
print(f.readline())
# doc all row
print(f.readlines())
f.close()