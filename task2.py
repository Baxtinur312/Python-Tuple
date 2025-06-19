students = [("Ali", ["Fizika", "Matematika"]), ("Laylo", ["Ingliz tili"]), ("Jasur", ["Matematika", "Informatika"])]
count = sum("Matematika" in subjects for _, subjects in students)
print(f"{count} talaba Matematika fanini tanlagan.")
