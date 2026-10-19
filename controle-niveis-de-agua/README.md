# 💧 Controle de Níveis de Água

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Reposit%C3%B3rio-black?logo=github)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)
![Projeto](https://img.shields.io/badge/Projeto-Monitoramento%20de%20%C3%81gua-cyan)

## 📖 Sobre o projeto

O **Controle de Níveis de Água** é um programa simples desenvolvido em Python para simular o monitoramento de um reservatório.

O sistema mostra no terminal a situação do nível de água usando uma cor diferente para cada condição. Para isso, utiliza a biblioteca **Colorama**.

O projeto foi desenvolvido como atividade do curso técnico em Desenvolvimento de Sistemas, utilizando listas, funções e estruturas de decisão.

## 🎯 Objetivo

Exibir um alerta colorido de acordo com o nível atual de água do reservatório, facilitando a identificação da situação.

## 🚦 Níveis do reservatório

| Nível | Situação | Cor |
|---|---|---|
| 1 | Muito baixo (crítico) | 🔴 Vermelho |
| 2 | Baixo | 🟡 Amarelo |
| 3 | Médio | 🟢 Verde |
| 4 | Alto | 🔵 Ciano |
| 5 | Muito alto (alerta) | 🔵 Azul |

## 🛠️ Tecnologias utilizadas

- Python 3
- Biblioteca Colorama
- Terminal do computador

## ▶️ Como executar

**1.** Instale o Python 3 no computador, caso ainda não esteja instalado.

**2.** Abra o terminal na pasta do projeto e instale a biblioteca:

```bash
pip install -r requirements.txt
```

**3.** Execute o programa:

```bash
python controle_niveis_agua.py
```

> Em alguns computadores, é necessário utilizar `python3` no lugar de `python`.

## 🧪 Como testar

No arquivo `controle_niveis_agua.py`, altere a variável `nivel_atual` para um número de **1 a 5** e execute o programa novamente.

Exemplo com `nivel_atual = 3`:

```text
=== CONTROLE DE NÍVEIS DE ÁGUA ===
Nível 3: Médio
```

A linha que informa o nível aparece em **verde** no terminal. Nos demais níveis, a cor muda de acordo com a tabela acima.

Também é possível testar `nivel_atual = 6` para verificar a mensagem de nível inválido.

## 🧠 O que aprendi

Nesta atividade, pratiquei o uso de **listas** para armazenar situações, **funções** para organizar o código, **if/elif/else** para definir cores e a biblioteca **Colorama** para destacar mensagens no terminal.

Também utilizei `Style.RESET_ALL` para restaurar a cor padrão após o alerta.

## 📁 Arquivos do projeto

- `controle_niveis_agua.py` — código principal do sistema.
- `requirements.txt` — dependência necessária para executar o programa.
- `README.md` — explicação e orientações do projeto.

## ✅ Status do projeto

Concluído para os requisitos da atividade.
