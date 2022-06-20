struct operandos{ 
    float v[500000];
    int len;
};

struct valor{
    float menor;
    float maior;
    int indiceMaior;
    int indiceMenor;
};

program PROG {
    version VERS {
        valor acharValores(operandos) = 1;
    } = 110011;
} = 55000555;