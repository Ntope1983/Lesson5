#Guess the number with 3 attempts
hide_number=43
total_attempts=3
attempts=0
num=0
while total_attempts>attempts:
    try:
        num = int(input("Μάντεψε τον αριθμό: "))
        attempts += 1
    except ValueError:
        print("Παρακαλώ δώσε έναν έγκυρο αριθμό.")
        continue
    if num==hide_number :
        print("To βρήκες")
        break
    elif num<hide_number:
        print("Εδωσες μικρότερο αριθμό")
    else:
        print("Εδωσες μεγαλύτερο αριθμό")
if attempts==3 and num!=hide_number:
    print("Δυσυχώς χάσατε")