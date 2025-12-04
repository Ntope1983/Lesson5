# The user gives 10 numbers the program calc and print the result
i=0
sum=0
while i<10:
    try :
        x=input("Δώσε έναν Έγκυρο αριθμό")
        sum=sum+float(x)
        print(f"To αθροισμα των αριθμών είναι: {sum}")
        i+=1
    except ValueError:
        print("Μη εγκυρη τιμη εισγωγής")