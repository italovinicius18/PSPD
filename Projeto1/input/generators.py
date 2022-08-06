import requests
import random
from tqdm import tqdm

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

linhas = 500_000_000
tam = len(WORDS)

for i,word in enumerate(WORDS):
    WORDS[i] = word.decode('utf-8')

with open(r'./words.txt', 'w') as fp:
    for i in tqdm(range(linhas)):
        fp.write(f'{random.choice(WORDS)}\n')
    print('Done')