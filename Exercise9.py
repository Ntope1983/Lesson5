hide_number=43
while True:
    try:
        num = int(input("Μάντεψε τον αριθμό: "))
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