# Atividade de Detecção de Bordas com Operador Sobel

Este repositório contém um projeto simples de detecção de bordas usando o operador Sobel em Python. O código utiliza threads para calcular as imagens de borda nas direções x e y, combinando-as em seguida para obter a imagem de saída.

## Como Utilizar

### Pré-requisitos
- Python 3
- Bibliotecas: numpy, Pillow

Instale as dependências utilizando:

```bash
pip install numpy Pillow
```

### Execução do Código

1. Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/detecao-bordas-threads-python.git
cd detecao-bordas-threads-python
```

2. Execute o código Python:

```bash
python main-threads.py
```

O resultado será exibido e salvo como `coins-saida.png` no diretório `./assets/`.

## Resultados

A seguir está a imagem inicial e o resultado obtido ao aplicar o operador Sobel na imagem de moedas fornecida:

### Imagem Inicial

![Imagem Inicial](./assets/coins.png)

### Imagem Resultado

![Imagem Resultado](./assets/coins-saida.png)

Nas imagens de resultado, as bordas das moedas são realçadas, proporcionando uma visão mais clara das transições de intensidade na imagem original.

Este projeto foi desenvolvido como parte de uma atividade prática com foco na utilização de threads para a detecção de bordas. O código emprega o operador Sobel em Python com suporte a threads e foi criado no âmbito da disciplina de Sistemas Operacionais da Universidade Federal do Rio Grande do Norte (UFRN), oferecida pelo Departamento de Computação e Automação (DCA).

---

Universidade Federal do Rio Grande do Norte  
Departamento de Computação e Automação - DCA
