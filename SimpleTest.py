questions = {
    "q1":{
        "vopros":"[1] Назовите фамилию и имя человека, открывшего зависимость между силой тока, напряжение и сопротивление проводника",
        "variants":["1. Анри Ампер", "2. Георг Ом", "3. Исаак Ньютон"],
        "true":2
    },
    "q2":{
        "vopros":"[2] Какое качество видео идёт после 720p",
        "variants":["1. 1080p", "2. 1440p", "3. 840p"],
        "true":1
    }
}

err, right = 0,0

for key, value in questions.items():
    if key:
        print(value["vopros"])
        for quest in value["variants"]:
            print(quest)
        user = int(input("Введите ваш ответ:"))
        if user == value["true"]:
            right += 1
        else:
            err += 1

print("Правильных ответов: {}".format(right))
print("Неправильных ответов: {}".format(err))