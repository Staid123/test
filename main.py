import json

# зчитую файл test.json
with open('test.json', 'r') as file:
    data = json.load(file)


animal = data.get("animal")

# звуки тварин
animal_sounds = {
    "dog": "bark",
    "cat": "meow",
    "cow": "moo",
    "rat": "pipi",
    "alien": "KILL"
}

# Виводимо звук відповідно до значення поля animal
sound = animal_sounds.get(animal, "Unknown animal")
print(sound)