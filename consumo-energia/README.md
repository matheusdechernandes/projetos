# ⚡ Calculadora de Consumo Elétrico

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?logo=github)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Energia](https://img.shields.io/badge/Projeto-Consumo%20de%20Energia-yellow)


## 📖 Sobre o projeto

A Calculadora de Consumo Elétrico é um programa desenvolvido em Python que estima o consumo mensal de energia de um aparelho.

O cálculo é realizado utilizando a potência do aparelho e seu tempo médio de uso diário. O programa também apresenta uma estimativa do custo mensal de energia.


## 🎯 Objetivo

Ajudar usuários a estimar quanto um aparelho elétrico consome por mês, a partir de dados simples: potência (W) e tempo médio de uso diário (horas).


## 🧮 Fórmula utilizada

O consumo mensal é calculado com a seguinte fórmula:

```text
consumo mensal = (potência × horas de uso por dia × 30) / 1000
```

O resultado é apresentado em quilowatt-hora por mês, ou `kWh/mês`.

Para estimar o custo:

```text
custo estimado = consumo mensal × tarifa do kWh
```

Neste projeto foi utilizada uma tarifa fixa de **R$ 0,75 por kWh**.


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
5. Execute:

```bash
python app.py
```
6. Informe o nome do aparelho, a potência (W) e o tempo de uso diário (horas) quando solicitado.


## 📋 Exemplo de uso

```
⚡ Calculadora de Consumo Elétrico

Nome do aparelho: Geladeira
Potência (em watts): 150
Tempo médio de uso por dia (em horas): 10

📊 Resultado da estimativa
------------------------------
Aparelho: Geladeira
Consumo estimado: 45.00 kWh/mês
Custo estimado: R$ 33.75/mês
```

## 👤 Autor

Feito por Matheus Hernandes como parte de um programa de iniciação em Desenvolvimento de Sistamas I. 🚀