words = ("apple", "banana", "strawberry", "kiwi")
# Dastlab birinchi so‘zni eng uzun deb olaylik
longest = words[0]
for word in words[1:]:
    if len(word) > len(longest):
        longest = word

print(longest)

