from functools import reduce

people = [{'имя': 'Маша', ' рост ': 160},
    {'имя': 'Саша', ' рост ': 80},
    {'name': 'Паша',' рост ': 80}]

height_total = 0
height_count = 0
for person in people:
    if ' рост ' in person:
        height_total += person[' рост ']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

print(average_height    )

heights =list(map(lambda x: x[' рост '],filter(lambda e: ' рост ' in e, people)))
print(heights)
if len(heights) > 0:
    average_height = sum(heights) / len(heights)
print(average_height)
