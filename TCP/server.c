#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define TAM 500000

typedef struct Dados
{
    float menor, maior;
    int menorIndice, maiorIndice;
} Dados;

typedef struct Indice{
  float numero;
  int posicao;
} Indice;

Dados menor_maior(float *vetor)
{
    Dados dados;
    int i;
    dados.menor = vetor[0];
    dados.maior = vetor[0];

    for (i = 0; i < TAM; i++)
    {
        if (vetor[i] < dados.menor)
        {
            dados.menor = vetor[i];
            dados.menorIndice = i;
        }
        if (vetor[i] > dados.maior)
        {
            dados.maior = vetor[i];
            dados.maiorIndice = i;
        }
    }
    
    return dados;
}

void trata_cliente(int socketCliente)
{
    float vetor[TAM];
    float numeroAtual;
    int indiceAtual = 0;
    unsigned int tamanhoVetor = TAM * sizeof(float);
    unsigned int tamanhoRecebido;
    Dados dados;

    // Recebe o vetor
    Indice indice;
    while (indiceAtual < TAM)
    {
        tamanhoRecebido = recv(socketCliente, &indice, sizeof(Indice), 0);

        if (tamanhoRecebido == 0)
        {
            break;
        }

        vetor[indice.posicao] = indice.numero;
        indiceAtual++;
    }

    dados = menor_maior(vetor);

    send(socketCliente, &dados, sizeof(Dados), 0);
    close(socketCliente);
    exit(0);

}

int main()
{
    int servidorSocket;
    int socketCliente;
    struct sockaddr_in servidorAddr;
    struct sockaddr_in clienteAddr;
    unsigned short servidorPorta;
    unsigned int clienteLength;

    servidorPorta = 5556;

    // Abrir Socket
    if ((servidorSocket = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0)
        printf("falha no socker do Servidor\n");

    // Montar a estrutura sockaddr_in
    memset(&servidorAddr, 0, sizeof(servidorAddr)); // Zerando a estrutura de dados
    servidorAddr.sin_family = AF_INET;
    servidorAddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servidorAddr.sin_port = htons(servidorPorta);

    // Bind
    if (bind(servidorSocket, (struct sockaddr *)&servidorAddr, sizeof(servidorAddr)) < 0)
        printf("Falha no Bind\n");

    // Listen
    if (listen(servidorSocket, 10) < 0)
        printf("Falha no Listen\n");

    while (1)
    {
        clienteLength = sizeof(clienteAddr);
        if ((socketCliente = accept(servidorSocket,
                                    (struct sockaddr *)&clienteAddr,
                                    &clienteLength)) < 0)
            printf("Falha no Accept\n");

        printf("Conexão do Cliente %s\n", inet_ntoa(clienteAddr.sin_addr));

        trata_cliente(socketCliente);
        close(socketCliente);
    }
    close(servidorSocket);
}