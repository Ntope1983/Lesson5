#the user give number until user type quit and the program cal the square
while True:
    try :
        x=input("Δώσε έναν Έγκυρο αριθμό")
        if x=="quit" :
            break
        print(f"To τετράγωνο του αριθμού {x} είναι¨{float(x)*float(x)}")
    except ValueError:
        print("Μη εγκυρη τιμη εισγωγής")