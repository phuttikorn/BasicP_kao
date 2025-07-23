moster = 100
Cannon = 10
Sword = 10
Hammer = 5

while True:
    choice = int(input("กรอก 1 เพื่อสู้ กรอก 2 เพื่อออก"))

    if choice == 1:
        fight = int(input("จำนวนรอบที่ต้องการจะสู้"))
        num = 1
        bloodmoster = moster
        for i in range(fight):
                fight1 = int(input("กรอกอาวุธ 1.cannon,2.Sword,3.Hammer"))
                if fight1 == 1:
                    print("ใช้Cannonในการโจมตี")
                    bloodmoster = bloodmoster - Cannon
                    print(bloodmoster)
                elif fight1 == 2:
                    print("ใช้Swordในการโจมตี")
                    bloodmoster = bloodmoster - Sword
                    print(bloodmoster)
                elif fight1 == 3:
                    print("ใช้Hammerในการโจมตี")
                    bloodmoster =  bloodmoster - Hammer 
                    print(bloodmoster)

        if bloodmoster == 0:
            print("Moster ตาย")
        if bloodmoster < 0:
            print("Moster เลือดเหลือ20 ยังไม่ตาย")
            bloodmoster = 20
        if bloodmoster != 0:
            print("ผู้เล่นเพ้")

    elif choice == 2:
        print("ออก")
        break
   



