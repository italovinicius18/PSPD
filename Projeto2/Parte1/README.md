Processos para rodar o código:

```sh
nc -lk 9999 < test.txt
```

Agora em outro terminal execute o comando:

```sh
python3 network_wordcount.py localhost 9999
```