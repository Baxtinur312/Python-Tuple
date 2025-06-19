people = [("Ali", 24), ("Laylo", 30), ("Jasur", 19)]
# Dastlab birinchi odamni eng katta deb olaylik
oldest_person = people[0]

for person in people[1:]:
    if person[1] > oldest_person[1]:
        oldest_person = person

print(f"{oldest_person[0]} — {oldest_person[1]} yosh")
