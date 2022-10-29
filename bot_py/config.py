if __name__ == "__main__":
    with open("TOKEN.txt", "w") as file:
        token = "5683699289:AAEzNmNLZcQZ_c8klXz-DB1Er5Ia82GvvzI"
        file.write(token)


else: 
    with open("TOKEN.txt", "r") as file:
        TOKEN = file.readline()
