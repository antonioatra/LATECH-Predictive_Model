# Inteli - Instituto de Tecnologia e Liderança

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="assets/inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
</p>

# LATECH

## THROXY

## Integrantes:

-   <a href="https://www.linkedin.com/in/luiz-hinuy-0995252b1?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app">Luiz Hinuy</a>
-   <a href="https://www.linkedin.com/in/hugo-montan-393b49175/">Hugo Montan</a>
-   <a href="https://www.linkedin.com/in/leandro-precaro-barankiewicz-filho-8a293a345/">Leandro Precaro Brankiewicz Filho</a>
-   <a href="https://www.linkedin.com/in/yuriboczar/">Yuri Lessa Boczar</a>
-   <a href="https://www.linkedin.com/in/messias-olivindo/">Messias Olivindo</a>
-   <a href="https://www.linkedin.com/in/carlos-quaglia-309088357/">Carlos Quaglia</a>
-   <a href="https://www.linkedin.com/in/antonio-augusto-tavares-ribeiro-andr%C3%A9-613937345?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app">Antonio Augusto Tavares Ribeiro André</a>

## Professores:

### Orientador(a)

-   <a href="https://www.linkedin.com/in/profclaudioandre/">Claudio Fernando André</a>

### Instrutores

-   <a href="https://www.linkedin.com/in/bryan-kano/">Bryan Kano Ferreira</a>
-   <a href="https://www.linkedin.com/in/gui-cestari/">Guilherme Henrique de Oliveira Cestari</a>
-   <a href="https://www.linkedin.com/in/renato-penha/">Renato Penha</a>
-   <a href="https://www.linkedin.com/in/fernando-pizzo-208b526a/">Fernando Pizzo Ribeiro</a>
-   <a href="https://www.linkedin.com/in/laizaribeiro/">Laíza Ribeiro Silva</a>

## 📝 Descrição

&emsp; O projeto, desenvolvido em parceria com a Universidade EAFIT, tem como objetivo criar um modelo preditivo capaz de identificar, de forma antecipada, estudantes em risco de reprovar no curso de programação. A instituição enfrenta o desafio de detectar dificuldades acadêmicas apenas em estágios avançados do semestre, o que limita as oportunidades de intervenção e apoio.<br>
&emsp; A solução proposta é um sistema de análise preditiva que utiliza dados históricos e parciais — como notas de avaliações, quizzes, tempo de resolução e informações demográficas — para estimar a probabilidade de aprovação antes do término do curso. O modelo fará previsões contínuas e atualizadas a cada 4 semanas, permitindo aos docentes agir rapidamente com estratégias personalizadas, como tutorias, revisões ou atividades de reforço.<br>
&emsp; Com isso, espera-se otimizar os recursos de acompanhamento, reduzir taxas de reprovação e evasão, além de promover melhorias no desempenho acadêmico. A ferramenta também oferecerá insights sobre quais fatores mais influenciam o resultado final, apoiando decisões pedagógicas baseadas em dados.
&emsp; Aqui nós temos um video em espanhol explicando como entrar na plataforma e o que ela faz: <a href="https://youtu.be/V4tN3LteRU8"> LaTech Funcionamento</a>

## 📁 Estrutura de pastas

```
/ (raiz do projeto)
│
├── README.md
│
├── dashboard/
│   ├── app.py                      # Streamlit app principal
│   ├── requirements.txt            # Dependências específicas do dashboard
│   ├── modelos_treinados/          # Arquivos .pkl com modelos treinados para o dashboard
│   └── src/                        # Código do frontend / componentes do dashboard
│
├── assets/
│   ├── inteli.png
│   └── ... (imagens e mídias usadas na documentação)
│
├── documents/
│   └── documentacao.md             # Documentação do projeto
│
├── notebooks/
│   ├── notebook.ipynb              # Notebook principal com o modelo usado
│   ├── requirements.txt            # Dependências para os notebooks (se aplicável)
│   ├── anexos/                     # Notebooks e materiais suplementares
│   └── dados/                      # Dados tratados (arquivos .csv, .xlsx, etc.)
│
│
├── .gitattributes
└── .gitignore
```

## 💻 Execução dos projetos

## Requisitos

-   Python 3.8+ (recomenda-se 3.10)
-   Git
-   VS Code com extensões: Python e Jupyter
-   Arquivos do projeto (clone do repositório).

## Execução local (VS Code + Python)

1. Clone o repositório:
    ```
    git clone <URL_DO_REPOSITORIO>
    cd <REPO>
    ```
2. Crie e ative um ambiente virtual:
    - Windows:
        ```
        python -m venv .venv
        .venv\Scripts\activate
        ```
    - macOS / Linux:
        ```
        python -m venv .venv
        source .venv/bin/activate
        ```
3. Atualize pip:
    ```
    pip install --upgrade pip
    ```
4. Rode os notebooks:

    - Instale as dependências

    ```
    pip install -r notebooks/requirements.txt
    ```

    - Certifique-se de que os arquivo com os dados do primeiro e segundo semestre estão na raiz do projeto com os seguintes nomes: `Datos_Anonimo_20231_v2.xlsx` e `Datos_Anonimo_20231_v2.xlsx`.
    - Selecione o intérprete Python do ambiente `.venv`.
    - Para trabalhar com notebooks Jupyter, abra o arquivo `.ipynb` em `notebooks/` e use a extensão Jupyter.

5. Execute a aplicação Streamlit localmente:
    - Instale as dependências
    ```
    pip install -r dashboard/requirements.txt
    ```
    - Rode o projeto
    ```
    cd dashboard && streamlit run app.py
    ```
    - O Streamlit abrirá a interface no navegador (provavelmente http://localhost:8501).
    - Caso queira, interrompa com Ctrl+C no terminal para parar a aplicação.

## 🗃 Histórico de lançamentos

-   1.0.0 - 11/10/2024
    -   [sprint 5] Lançamento da primeira versão do modelo preditivo com documentação.
-   0.6.0 - 27/09/2024
    -   [sprint 4] Comparação de modelos preditivos
-   0.3.1 - 13/09/2024
    -   [sprint 3] Preparação de dados e modelo preditivo preliminar
-   0.2.7 - 30/08/2024
    -   [sprint 2] Análise exploratória e levantamento de hipóteses
-   0.1.3 - 16/08/2024
    -   [sprint 1] Documentação de entendimento do negócio

## 📋 Licença/License

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/Inteli-College/2025-2A-T15-IN03-G05">LATECH</a> by Inteli, Yuri Boczar, Messias Olivindo, Carlos Quaglia, Antonio André, Leandro Precaro, Luiz Hinuy e Hugo Montan is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
