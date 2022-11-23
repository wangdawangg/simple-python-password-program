# author = Ignasius Grina Dawang Majaya
# NIM = 210104025 TK21A1
# Universitas Duta Bangsa Surakarta

def password():
    passwrd = input("Input your Password : ")
    pas = len(passwrd)
    if pas < 12:
        print("Error!!!") 
        print("Password min. 12 Character with num(number) on first string and character ^ at the end of String!")
        password()
    elif pas >= 12:
        if passwrd[-1] == "^" and passwrd[0].isdigit():
            print("Password accepted")
        elif not passwrd[0].isdigit() and passwrd[-1] == "^":
            print("Error!! Password not accepted")
            print("Password must contain num(number) at the beginning!")
            password()
        elif passwrd[0].isdigit() and passwrd[-1] != "^":
            print("Error!! Password not accepted")
            print("Password must contain ^ at the end!")
            password()
        elif not passwrd[0].isdigit() and passwrd[-1] != "^":
            print("Error!! Password not accepted")
            print("Password must contain num(number) at the beginning! \nPassword must contain ^ at the end!")
            password()
password()