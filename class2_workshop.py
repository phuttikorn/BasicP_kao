distance = int (input("Enter Your distance : "))

if distance <= 50:
    print(" pay 10 bath")
elif distance <= 100:
    print(" pay 15 bath")
elif distance <= 300:
    print(" pay 25 bath")
elif distance <= 500:
    print(" pay 35 bath")
elif distance > 500:
    print(" pay 45 bath")  
else:
    print("ไม่เอาเงิน")
