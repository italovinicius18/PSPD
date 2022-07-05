# Requisitos

Para executar o código, primeiramente é necessário instalar o pacotes abaixo:

- pip install grpcio
- pip install grpcio-tools

# Instruções

Primeiramente acesse a pasta "codigo" com o comando:

```sh
cd codigo/
```

Para executar o script de servidor, basta executar o comando:

```sh
python lab_server.py 
```

Agora você pode executar o cliente com o comando:

```sh
python lab_client.py 
```

Caso queira verificar se o protobuf está gerando as classes e funções essenciais, basta executar o comando na pasta codigo:

```sh
python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. lab.proto
```