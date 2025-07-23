# # haverice = True
# # havespoon = False
# # havehand = True

# # if haverice:
# #     if havespoon:
# #         print("กินข้าว")
# #     elif havehand:
# #         print("กินข้าวเหนียว")


# Grade = int(input("Enter your Grade"))

# if Grade >= 0:
#     if Grade <= 100:
#         if Grade >= 80:
#             print("A")
#         if Grade >= 70:
#             if Grade < 80:
#                 print("B")
#         if Grade >= 60:
#             if Grade < 70:
#                 print("C")
#         if Grade >= 50:
#             if Grade < 60:
#                 print("D")
#         if Grade < 50:
#             print("F")

# for i in range(1,10,2):
#     print(i)

# i = 0
# while i < 5:
#     print(i)
#     i = i + 1



while True:
    choice = int(input("กรอก 1 เพื่อบวกเลข, กรอก 2 เพื่อออก"))

    if choice == 1:
        num = int(input("จำนวนที่ต้องการจะบวก"))
        sumation = 0

        for i in range(num):
            num1 =int(input("กรอกเลข"))
            sumation = sumation + num1 

        print("ผลลัพธ์",sumation)

    if choice == 2:
        print("บาย บาย")
        break