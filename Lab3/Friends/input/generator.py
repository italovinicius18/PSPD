import names
from tqdm import tqdm
import random


len_relations = 100_000_000

def read_people():
    with open("people.txt", "r") as f:
        people = f.readlines()
    
    people = [p.replace('\n','') for p in people]

    return people


def generate_random_relations(people):
    relations = set()
    print("Generating random relations...")
    while len(relations) < len_relations:
        print(f'Percentage: {len(relations) / len_relations * 100}%')
        p1 = random.choice(people)
        p2 = random.choice(people)
        if p1 != p2:
            relations.add(f'{p1}, {p2}\n')

    try:
        with open("relations.txt", "w") as f:
            f.writelines(relations)
    except KeyboardInterrupt:
        print("Saving relations interrupted")
        with open("relations.txt", "w") as f:
            f.writelines(relations)
        print("Saving relations interrupted")

people = read_people()

print('Qtd people: ', len(people))
print('Max relations: ', len(people) * len(people))
relations = generate_random_relations(people)
