#Nested Loops
Best_Friends=["Βλάσσης","Λάκης","Μιχαλής"]
guests = [
    "Γιάννης",
    "Μαρία",
    "Βλάσσης",
    "Γιώτα",
    "Κώστας",
    "Κατερίνα",
    "Κατερίνα",
    "Βασιλική",
    "Μπαμπης",
    "Χριστίνα"]
friends=0
for Best_Friend in Best_Friends:
    for guest in guests:
        if Best_Friend==guest:
            friends += 1
            break
if friends>=2:
    print(f"Αποδέχομαι τη πρόσκληση με {friends} καλυτερους φίλους")
else :
    print(f"Δεν αποδέχομαι τη πρόσκληση με {friends} καλυτερους φίλους")