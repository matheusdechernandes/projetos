# 💧 Classificador de Consumo de Água

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?logo=github)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Água](https://img.shields.io/badge/Projeto-Consumo%20de%20Água-blue)

## 📖 Sobre o projeto

O **Classificador de Consumo de Água** é um programa desenvolvido em Python para classificar o consumo mensal de água de imóveis.

O projeto simula uma campanha de conscientização ambiental realizada por uma companhia de saneamento.

O sistema analisa o tipo de imóvel e o consumo mensal de água informado pelo usuário e apresenta uma mensagem de orientação.

## 🎯 Objetivo

O objetivo do programa é classificar o consumo de água em imóveis residenciais ou comerciais e apresentar mensagens educativas relacionadas ao uso consciente da água.

## ⚙️ Funcionamento

O programa solicita duas informações:

- Tipo de imóvel: `comercial`, `casa` ou `apartamento`;
- Consumo mensal de água em metros cúbicos (m³).

Após receber os dados, o programa utiliza estruturas condicionais para classificar o consumo.

### 💼 Imóvel comercial

Para imóveis comerciais, o sistema apresenta:

> Tarifa comercial aplicada – consulte o plano corporativo.

### 🏢 Apartamento com consumo menor que 10 m³

O sistema apresenta:

> Consumo econômico – excelente controle de água!

### 🏠 Casa ou apartamento com consumo de até 25 m³

O sistema apresenta:

> Consumo moderado – dentro do padrão residencial.

### ⚠️ Consumo acima de 25 m³

O sistema apresenta:

> Consumo excessivo – adote medidas de economia e verifique vazamentos.

## 💻 Tecnologias utilizadas

- 🐍 Python
- 🐙 GitHub
- 💻 Visual Studio Code
- 🌱 Lógica de Programação

## 🧠 Conceitos utilizados

Durante o desenvolvimento deste projeto foram utilizados alguns conceitos básicos da programação em Python:

- Entrada de dados com `input()`;
- Conversão de valores com `float()`;
- Estruturas condicionais `if`, `elif` e `else`;
- Operadores lógicos `and` e `or`;
- Operadores de comparação;
- Manipulação básica de strings com `.lower()`.

## ▶️ Como executar

### 1. Baixe ou clone este repositório.

```bash
git clone LINK-DO-SEU-REPOSITORIO
```

### 2. Entre na pasta do projeto.

```bash
cd consumo-agua
```

### 3. Execute o programa.

```bash
python app.py
```

## 🖥️ Exemplo de execução

```text
=== CONTROLE DE CONSUMO DE ÁGUA ===

Digite o tipo de imóvel (comercial, casa ou apartamento): apartamento

Digite o consumo mensal de água em m³: 8.5

Consumo econômico – excelente controle de água!
```

Outro exemplo:

```text
=== CONTROLE DE CONSUMO DE ÁGUA ===

Digite o tipo de imóvel (comercial, casa ou apartamento): casa

Digite o consumo mensal de água em m³: 18

Consumo moderado – dentro do padrão residencial.
```

## 📂 Estrutura do projeto

```text
consumo-agua/
│
├── app.py
└── README.md
```

## 🌱 Conscientização

Além de praticar programação, este projeto aborda a importância do consumo consciente de água.

Pequenas atitudes, como evitar desperdícios e verificar vazamentos, podem contribuir para a preservação dos recursos naturais.

## 👨‍💻 Autor

**Matheus Hernandes**

Estudante de Desenvolvimento de Sistemas.