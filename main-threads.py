import threading
import numpy as np
from PIL import Image

# Função para calcular Gx em uma região específica da imagem
def calcular_gx(regiao, resultado):
    Gx = np.zeros_like(regiao, dtype=np.int32)
    for i in range(1, regiao.shape[0] - 1):
        for j in range(1, regiao.shape[1] - 1):
            Gx[i, j] = (regiao[i + 1, j - 1] + 2 * regiao[i + 1, j] + regiao[i + 1, j + 1]) - \
                        (regiao[i - 1, j - 1] + 2 * regiao[i - 1, j] + regiao[i - 1, j + 1])
            Gx[i, j] = max(0, min(255, Gx[i, j]))  # Saturação
    resultado.append(Gx)

# Função para calcular Gy em uma região específica da imagem
def calcular_gy(regiao, resultado):
    Gy = np.zeros_like(regiao, dtype=np.int32)
    for i in range(1, regiao.shape[0] - 1):
        for j in range(1, regiao.shape[1] - 1):
            Gy[i, j] = (regiao[i - 1, j + 1] + 2 * regiao[i, j + 1] + regiao[i + 1, j + 1]) - \
                        (regiao[i - 1, j - 1] + 2 * regiao[i, j - 1] + regiao[i + 1, j - 1])
            Gy[i, j] = max(0, min(255, Gy[i, j]))  # Saturação
    resultado.append(Gy)

# Função principal
def main():
    # Carregar a imagem em nível de cinza
    imagem_path = './assets/coins.png'
    imagem = np.array(Image.open(imagem_path).convert('L'))

    # Inicializar listas para armazenar os resultados das threads
    resultado_gx = []
    resultado_gy = []

    # Criar threads para calcular Gx e Gy
    thread_gx = threading.Thread(target=calcular_gx, args=(imagem, resultado_gx))
    thread_gy = threading.Thread(target=calcular_gy, args=(imagem, resultado_gy))

    # Iniciar as threads
    thread_gx.start()
    thread_gy.start()

    # Aguardar o término das threads
    thread_gx.join()
    thread_gy.join()

    # Obter os resultados das threads
    gx = resultado_gx[0]
    gy = resultado_gy[0]

    # Calcular a imagem de saída G
    g = gx + gy
    g = np.clip(g, 0, 255)  # Saturação

    # Mostrar ou salvar a imagem de saída
    imagem_saida = Image.fromarray(g.astype(np.uint8))
    imagem_saida.show()
    imagem_saida.save('./assets/coins-saida.png')

if __name__ == "__main__":
    main()
