# Detector de Movimento com OpenCV

Projeto desenvolvido em Python utilizando a biblioteca **OpenCV** para realizar a detecção de movimentos em tempo real através da câmera do computador.

O sistema captura imagens consecutivas da webcam, compara os frames e identifica alterações na imagem, destacando as regiões onde há movimentação.

## 🚀 Tecnologias utilizadas

- Python
- OpenCV
- Processamento de imagens
- Visão computacional

## ⚙️ Funcionalidades

- Captura de vídeo em tempo real utilizando a webcam.
- Comparação entre frames consecutivos.
- Cálculo da diferença absoluta entre imagens.
- Conversão da imagem para escala de cinza.
- Aplicação de desfoque gaussiano para reduzir ruídos.
- Aplicação de limiarização (Threshold) para destacar diferenças.
- Dilatação para melhorar a identificação das regiões movimentadas.
- Detecção de contornos na imagem.
- Identificação de movimentos com base na área dos contornos.
- Desenho de retângulos ao redor das regiões onde o movimento foi detectado.
- Exibição de alertas no terminal quando um movimento é identificado.

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd detector_de_movimento
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 5. Instale a dependência

```bash
pip install opencv-python
```

## ▶️ Como executar

Execute o arquivo principal:

```bash
python app.py
```

A câmera será inicializada e o sistema começará a detectar movimentos em tempo real.

Para encerrar a execução, pressione a tecla **Q**.

## 🧠 Como funciona?

O processo de detecção de movimento segue as seguintes etapas:

1. **Captura dos frames:** o sistema captura dois frames consecutivos da webcam.
2. **Diferença entre imagens:** utiliza `cv2.absdiff()` para identificar as diferenças entre os frames.
3. **Escala de cinza:** converte a imagem para tons de cinza utilizando `cv2.cvtColor()`.
4. **Desfoque gaussiano:** aplica `cv2.GaussianBlur()` para reduzir ruídos.
5. **Threshold:** utiliza `cv2.threshold()` para destacar as regiões com diferenças significativas.
6. **Dilatação:** aplica `cv2.dilate()` para ampliar as regiões detectadas.
7. **Detecção de contornos:** utiliza `cv2.findContours()` para encontrar as áreas onde ocorreu movimentação.
8. **Identificação do movimento:** filtra os contornos com área inferior a 5000 pixels.
9. **Marcação:** utiliza `cv2.boundingRect()` e `cv2.rectangle()` para desenhar retângulos ao redor dos movimentos detectados.

## 📁 Estrutura do projeto

```text
detector_de_movimento/
│
├── app.py
├── README.md
└── venv/
```

## 🎯 Objetivo do projeto

Este projeto tem como objetivo estudar e aplicar conceitos de processamento de imagens e visão computacional utilizando Python e OpenCV, desenvolvendo um sistema simples de detecção de movimento em tempo real.

**Desenvolvido com Python e OpenCV.**
