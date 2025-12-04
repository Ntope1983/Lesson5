
ListN=[]
while True:
    try :
        x=input("Δώσε έναν αριθμό μεταξύ του 3 και του 20")
        N=int(x)
        if N >= 3 and N<=20 :
            break
        print("Μη εγκυρη τιμη εισγωγής")
    except ValueError:
        print("Μη εγκυρη τιμη εισγωγής")

for i in range (N):
    try:
        x = input("Δώσε έναν ακεραιο αριθμό μεταξύ του 10 και του 20")
        Int = int(x)
        if Int >= 10 and Int <= 20:
            ListN.append(Int)
            continue
        print("Μη εγκυρη τιμη εισγωγής")
    except ValueError:
        print("Μη εγκυρη τιμη εισγωγής")

ListN.sort()
print(ListN)