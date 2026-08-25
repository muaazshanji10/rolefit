fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[1])
print(fruits[2:])
print(fruits[3:])

player = {"name": "Baleba", "position": "8", "potential": "high"}
print(player["position"])

numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers)
print(unique_numbers)

numbers[1] = 7
numbers.append(67)
numbers.remove(2)
print(numbers)

player = {"name": "Baleba", "position": "8"}
player["position"] = "6"          # change an existing value
player["age"] = 20                 # add a brand new key entirely
print(player)

numbers = [1, 2, 3, 4, 5]
doubled = []
for n in numbers:
    doubled.append(n * 2)
print(doubled)   # [2, 4, 6, 8, 10]

squares = [n*n for n in numbers]
print(squares)

greater_than_2 = [n for n in numbers if n>2]
print(greater_than_2)

scores = [45, 82, 91, 33, 67, 78, 12, 99, 56, 71]

double_scores = [n*2 for n in scores]
scores_more_than_50 = [n for n in scores if n > 50]
double_scores2 = [n*2 for n in scores_more_than_50]
print(double_scores)
print(scores_more_than_50)
print(double_scores2)

player_ages = {"Salah": 32, "Saka": 22, "Foden": 24, "Bellingham": 21, "Kane": 31}

print(len(scores))
print(sum(scores))
print(max(scores))
print(min(scores))
print(player_ages.keys())

print(player_ages.values())

even_scores = [n for n in scores if n%2 == 0]
print(even_scores)


scores_60 = [n for n in scores if n > 60]
len(scores_60)

print({key: value*2 for key, value in player_ages.items()})

print(sorted(scores))
print(sorted(scores, reverse=True))

{key: value for key, value in player_ages.items() if value <= 25}