#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <math.h>

#define TAM 500000

typedef struct Dados{
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

float f_aleat() {
    return (float)rand() / (float)RAND_MAX * TAM;
}

void inicia_vetor(float *vetor) {
    int i;
    for (i = 0; i < TAM; i++) {
        vetor[i] = pow((i - (f_aleat()/2)),2);
        vetor[i] = sqrt(vetor[i]);
        // printf("%f\n", vetor[i]);
    }
}

int main() {
	int clienteSocket;
	struct sockaddr_in servidorAddr;
	unsigned short servidorPorta;
	char *IP_Servidor;
	float vetor[TAM];
    Dados dados;
	unsigned int tamanhoVetor = TAM * sizeof(float);

	int bytesRecebidos;
	int totalBytesRecebidos;

	IP_Servidor = "127.0.0.1";
	servidorPorta = 5556;

	// Criar Socket
	if((clienteSocket = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0)
		printf("Erro no socket()\n");

	// Construir struct sockaddr_in
	memset(&servidorAddr, 0, sizeof(servidorAddr)); // Zerando a estrutura de dados
	servidorAddr.sin_family = AF_INET;
	servidorAddr.sin_addr.s_addr = inet_addr(IP_Servidor);
	servidorAddr.sin_port = htons(servidorPorta);

	// Connect
	if(connect(clienteSocket, (struct sockaddr *) &servidorAddr, 
							sizeof(servidorAddr)) < 0)
		printf("Erro no connect()\n");

    inicia_vetor(vetor);

	// Enviar vetor
	Indice indice;
	for(int i = 0; i < TAM; i++) {
		indice.numero = vetor[i];
		indice.posicao = i;
		if(send(clienteSocket, &indice, sizeof(Indice), 0) < 0)
			printf("Erro no send()\n");
	}

	// Receber dados
    int tamanhoRecebido;
	
	if((tamanhoRecebido = recv(clienteSocket, &dados, sizeof(dados), 0)) < 0)
		printf("Erro no recv()\n");
	
	printf("Indice do maior: %d\n", dados.maiorIndice);
	printf("Maior valor: %f\n", dados.maior);
	printf("Indice do menor: %d\n", dados.menorIndice);
	printf("Menor valor: %f\n\n", dados.menor);
	

	close(clienteSocket);
	exit(0);
}
