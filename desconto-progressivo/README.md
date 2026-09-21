# 🛒 Sistema de Desconto Progressivo

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?logo=github)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Desconto](https://img.shields.io/badge/Projeto-Desconto%20Progressivo-orange)

## 📖 Sobre o projeto

O Sistema de Desconto Progressivo é um programa desenvolvido em Python que calcula automaticamente o desconto aplicado a uma compra de acordo com o seu valor total.

O programa solicita ao usuário o valor da compra, identifica a faixa de desconto correspondente e apresenta o valor do desconto e o valor final que deverá ser pago pelo cliente.

## 🎯 Objetivo

Aplicar conceitos básicos de programação em Python, utilizando entrada de dados, estruturas condicionais, cálculos matemáticos e saída de informações.

O programa simula um sistema de descontos utilizado por uma loja online, permitindo calcular automaticamente o valor final da compra.

## 💰 Regras de desconto

O percentual de desconto varia de acordo com o valor total da compra:

| Valor da compra            | Desconto |
| -------------------------- | -------: |
| Menor que R$ 200,00        |       5% |
| De R$ 200,00 até R$ 299,99 |      10% |
| A partir de R$ 300,00      |      15% |

## 🧮 Cálculos utilizados

Primeiramente, o programa identifica o percentual de desconto correspondente ao valor informado pelo usuário.

Depois, o valor do desconto é calculado utilizando a seguinte fórmula:

```text
valor do desconto = valor da compra × percentual de desconto
```

Em seguida, o valor final da compra é calculado:

```text
valor final = valor da compra - valor do desconto
```

### Exemplo

Para uma compra de **R$ 250,00**, o desconto aplicado é de **10%**.

```text
valor do desconto = 250 × 0,10
valor do desconto = 25
```

Portanto:

```text
valor final = 250 - 25
valor final = 225
```

O cliente deverá pagar **R$ 225,00**.

## 🧠 Conceitos utilizados

Durante o desenvolvimento do programa foram utilizados conceitos básicos da linguagem Python, como:

* Entrada de dados com `input()`;
* Conversão de dados com `float()`;
* Estruturas condicionais `if`, `elif` e `else`;
* Variáveis;
* Operações matemáticas;
* Formatação de valores com `f-strings`;
* Exibição de informações com `print()`.

## 🛠️ Tecnologias

<div>
  <img 
    alt="Python"
    title="Python"
    height="40"
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"
  /> <img
        alt="VsCode"
        title="VsCode"
        height="40"
        src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg" 
  />  <img
        alt="Git"
        title="Git"
        height="40"
        src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg"          
  />  <img
        alt="Git"
        title="Git"
        height="40"
        src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg"
  />
</div>

## ▶️ Como executar

1. Tenha o Python instalado no computador.

2. Faça o download ou clone este repositório.

3. Abra a pasta do projeto no VS Code.

4. Abra o terminal.

5. Execute o programa:

```bash
python app.py
```

6. Informe o valor total da compra quando solicitado.

7. O programa exibirá o percentual de desconto, o valor descontado e o valor final da compra.

## 📋 Exemplo de uso

```text
Digite o valor total da compra: R$ 250

--- RESUMO DA COMPRA ---

Valor da compra: R$ 250.00
Desconto aplicado: 10%
Valor do desconto: R$ 25.00
Valor total a pagar: R$ 225.00
```

## 🧪 Exemplos de teste

### Compra abaixo de R$ 200,00

```text
Valor informado: R$ 100,00
Desconto: 5%
Valor do desconto: R$ 5,00
Valor final: R$ 95,00
```

### Compra entre R$ 200,00 e R$ 299,99

```text
Valor informado: R$ 250,00
Desconto: 10%
Valor do desconto: R$ 25,00
Valor final: R$ 225,00
```

### Compra a partir de R$ 300,00

```text
Valor informado: R$ 400,00
Desconto: 15%
Valor do desconto: R$ 60,00
Valor final: R$ 340,00
```

## 👤 Autor

Feito por **Matheus Hernandes** como parte das atividades do curso de **Desenvolvimento de Sistemas I**. 🚀
