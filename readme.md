# Face Counting App

![MTCNN Architecture](https://debuggercafe.com/wp-content/uploads/2020/10/mtcnn_arch.png)

Este é um aplicativo de contagem de faces desenvolvido em Python, utilizando a biblioteca `facenet-pytorch` para detecção de faces com MTCNN e uma interface gráfica criada com Tkinter.

## Funcionalidades

- Detecção e contagem de faces em uma imagem.
- Interface gráfica para escolha da imagem e visualização dos resultados.
- Configuração do limiar de confiança para a detecção das faces.
- Exibição da imagem com marcação das faces detectadas.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Tkinter**: Interface gráfica.
- **facenet-pytorch (MTCNN)**: Detecção de faces.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

```bash
pip install torch facenet-pytorch pillow

