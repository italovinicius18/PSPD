struct operandos{ 
    float v[500000];
    int len;
};

struct valor{
    float numero;
    int indice;
};

program PROG {
    version VERS {
        valor acharMenor(operandos) = 1;
        valor acharMaior(operandos) = 2;
    } = 110011;
} = 55000555;