config = {"prefix": "??"}

with open("TOKEN.txt", "r") as file:
    config["TOKEN"] = file.readline()