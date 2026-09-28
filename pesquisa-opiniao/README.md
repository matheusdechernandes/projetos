# 📊 Pesquisa de Opinião - TudoWeb

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?logo=github)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Projeto](https://img.shields.io/badge/Projeto-Pesquisa%20de%20Opinião-orange)

## 📖 Sobre o projeto

Este projeto foi desenvolvido como atividade do curso Técnico em Desenvolvimento de Sistemas.

O programa simula uma pesquisa de opinião realizada pela empresa de marketing **TudoWeb** para saber o grau de satisfação dos clientes em relação ao atendimento prestado.

A pesquisa registra o nome, a idade e a opinião de cada entrevistado.

As opções disponíveis são:

- `1` - EXCELENTE
- `2` - BOM
- `3` - RUIM

Ao final da pesquisa, o programa informa a quantidade de respostas **EXCELENTE** e **RUIM**.

## 🎯 Objetivo

O objetivo da atividade é praticar conceitos básicos de programação em Python, principalmente:

- Entrada de dados com `input()`;
- Conversão de valores com `int()`;
- Estrutura de repetição `for`;
- Estruturas de decisão `if`, `elif` e `else`;
- Uso de contadores;
- Exibição de resultados na tela.

## ⚙️ Funcionamento

O programa realiza a pesquisa com **50 entrevistados**.

Para cada pessoa, são solicitados:

1. Nome;
2. Idade;
3. Opinião sobre o atendimento.

Depois que todos os entrevistados responderem, o programa apresenta:

- Quantidade de respostas **EXCELENTE**;
- Quantidade de respostas **RUIM**.

## 🧪 Teste com 10 entrevistados

Para testar o programa com apenas 10 entrevistados, conforme solicitado na atividade, basta alterar temporariamente esta linha:

```python
for entrevistado in range(1, 51):
```

para:

```python
for entrevistado in range(1, 11):
```

Após realizar o teste e registrar os prints da execução, deve-se retornar o valor para `51`, para que a versão final realize a pesquisa com 50 entrevistados.

## ▶️ Como executar

1. Tenha o Python instalado no computador.
2. Abra a pasta do projeto no Visual Studio Code.
3. Abra o arquivo `app.py`.
4. Execute o programa pelo terminal:

```bash
python app.py
```

## 💻 Exemplo de execução

```text
=== PESQUISA DE SATISFAÇÃO TUDOWEB ===

Entrevistado 1
Digite o nome: Ana
Digite a idade: 25
Opinião sobre o atendimento:
1 - EXCELENTE
2 - BOM
3 - RUIM
Digite sua opinião: 1
Resposta registrada: EXCELENTE
-----------------------------------

Entrevistado 2
Digite o nome: Carlos
Digite a idade: 31
Opinião sobre o atendimento:
1 - EXCELENTE
2 - BOM
3 - RUIM
Digite sua opinião: 3
Resposta registrada: RUIM
-----------------------------------
```

Ao final:

```text
=== RESULTADO DA PESQUISA ===
Quantidade de respostas EXCELENTE: 1
Quantidade de respostas RUIM: 1
```

## 📂 Estrutura do projeto

```text
pesquisa-opiniao/
│
├── app.py
└── README.md
```

## 📸 Prints para entrega

Para completar a atividade, deverão ser adicionados ao repositório prints mostrando:

- O código do programa;
- A execução do teste com 10 entrevistados;
- O resultado final exibido pelo programa.

Uma opção é criar uma pasta chamada `prints` dentro do repositório:

```text
pesquisa-opiniao/
│
├── app.py
├── README.md
└── prints/
    ├── codigo.png
    └── execucao.png
```

## 👨‍💻 Autor

**Matheus Hernandes**

Estudante do curso Técnico em Desenvolvimento de Sistemas.
