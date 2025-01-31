import json

with open("question.json", 'r') as files:
    content = files.read()

data = json.loads(content)

score = 0
for question in data:
    print(question["question"])
    for index, alternative in enumerate(question["alternative"]):
        print(f'{index + 1} - {alternative}')
    user_choice = int(input('Enter your choice: '))
    question["user_choice"] = user_choice
    if question["correct"] == question["user_choice"]:
        score += 1

print(data)
print(score, "/", len(data))
