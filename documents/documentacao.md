# Documentação Modelo Preditivo - Inteli

```
INSTRUÇÕES GERAIS (remova este trecho ao final)

Você deve editar este documento utilizando notação markdown - siga as convenções neste link 
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
```

## Nome da Solução
### Nome do grupo
#### (preencha aqui os nomes dos integrantes, em ordem alfabética, separados por vírgula)

## Sumário
[1. Introdução](#c1)

[2. Objetivos e Justificativa](#c2)

[3. Metodologia](#c3)

[4. Desenvolvimento e Resultados](#c4)

[5. Conclusões e Recomendações](#c5)

[6. Referências](#c6)

[Anexos](#attachments)


## <a name="c1"></a>1. Introdução
```
Apresente de forma sucinta o parceiro de negócio, seu porte, local, área de atuação e posicionamento no mercado. Maiores detalhes deverão ser descritos na seção 4. Descreva resumidamente o problema a ser resolvido (sem ainda mencionar a solução). 

Remova este bloco ao final
```

## <a name="c2"></a>2. Objetivos e Justificativa
### 2.1 Objetivos
```
Descreva resumidamente os objetivos gerais e específicos do seu parceiro de negócios.

Remova este bloco ao final
```

### 2.2 Proposta de solução
```
Descreva resumidamente sua proposta de modelo preditivo e como esse modelo pretende resolver o problema, atendendo os objetivos.

Remova este bloco ao final
```

### 2.3 Justificativa
```
Faça uma breve defesa de sua proposta de solução, escreva sobre seus potenciais, seus benefícios e como ela se diferencia.

Remova este bloco ao final
```

## <a name="c3"></a>3. Metodologia
```
Descreva a metodologia CRISP-DM e suas etapas de desenvolvimento, citando o referencial teórico. Você deve apenas enunciar os métodos, sem dizer ainda como eles foram aplicados, nem quais resultados foram obtidos.

Remova este bloco ao final
```

## <a name="c4"></a>4. Desenvolvimento e Resultados
### 4.1. Compreensão do Problema
#### 4.1.1. Contexto da indústria 
```
Descreva os principais players, modelos de negócio e tendências acerca dos modelos preditivos.

Remova este bloco ao final
```
#### 4.1.2. Análise SWOT 
```
Posicione aqui sua análise SWOT.

Remova este bloco ao final
```

#### 4.1.3. Planejamento Geral da Solução
```
a) quais os dados disponíveis (fonte e conteúdo - exemplo: dados da área de Compras da empresa descrevendo seus fornecedores).
b) qual a solução proposta (pode ser um resumo do texto da Seção 2.2).
c) como a solução proposta deverá ser utilizada.
d) quais os benefícios trazidos pela solução proposta.
e) qual será o critério de sucesso.

Remova este bloco ao final
```

#### 4.1.4. Value Proposition Canvas
```
Posicione aqui seu canvas.

Remova este bloco ao final
```

#### 4.1.5. Matriz de Riscos

&emsp; A análise de riscos e oportunidades em um projeto é uma etapa essencial no desenvolvimento de um modelo preditivo, pois permite mitigar possíveis problemas e, ao mesmo tempo, identificar oportunidades que possam alavancar a entrega do MVP. Segundo o PMBOK® Guide (PMI, 2021), o gerenciamento de riscos compreende os processos de planejamento, identificação, análise, resposta, monitoramento e controle de riscos e oportunidades que possam surgir ao longo do ciclo de vida do projeto. Com base nesse entendimento, propõe-se a seguinte divisão em matriz de riscos e matriz de oportunidades:


**4.1.5.1. Riscos:**

<div align="center">

<sup>Figura : Matriz de riscos do projeto</sup>

<img src="../assets/matrizRiscos.png">

<sup>Fonte: Material produzido pelos autores</sup>

</div>

&emsp; A seguir, os riscos identificados são apresentados com base em cinco dimensões: categoria, ameaça, impacto, probabilidade e estratégia de mitigação. A classificação por categorias segue as diretrizes do PMBOK® Guide (PMI, 2021), visando facilitar o agrupamento, a análise e a priorização das ameaças ao longo do desenvolvimento do projeto. As categorias adotadas — Técnico, Humano, Organizacional e Acadêmico — refletem as diferentes naturezas dos riscos e permitem uma abordagem mais direcionada em sua gestão.

&emsp; **4.1.5.1.1. Dados insuficientes**

- **Categoria:** Técnico
- **Ameaça:** Treinar o modelo preditivo com uma quantidade insuficiente de dados.
- **Impacto:** (Muito alto): A escassez de dados inviabiliza o treinamento adequado do modelo, comprometendo toda a elaboração do projeto.
- **Probabilidade (10%):** O parceiro institucional comprometeu-se a fornecer os dados necessários, tornando baixa a chance de indisponibilidade de material para análise.
- **Mitigação:** Levantar previamente a quantidade mínima de dados amostrais necessária e solicitar oficialmente à universidade a disponibilização desses dados.

&emsp; **4.1.5.1.2. Descumprimento de prazos**

- **Categoria:** Humano
Ameaça: Membros do grupo não concluírem suas atividades dentro dos prazos definidos, atrasando etapas subsequentes do projeto.
- **Impacto (Alto):** Tarefas atrasadas podem paralisar o desenvolvimento em determinado estágio, gerar sobrecarga em alguns membros ou até comprometer a entrega de funcionalidades do MVP.
- **Probabilidade (30%):** Com base na experiência adquirida em projetos anteriores, espera-se que os membros consigam estabelecer prazos realistas e comunicar eventuais dificuldades com antecedência. Contudo, reconhece-se que o grupo ainda está em processo de aprendizado, o que torna eventuais falhas compreensíveis.
- **Mitigação:** Reavaliar prazos com base na experiência passada, considerando o tempo de aprendizado e testes. Realizar atualizações periódicas do status das atividades e manter comunicação constante sobre obstáculos no desenvolvimento.

&emsp; **4.1.5.1.3. Dificuldades na aplicação de modelos preditivos**

- **Categoria:** Acadêmico
Ameaça: Dificuldade na implementação de um ou mais modelos apresentados durante as aulas.
- **Impacto (Moderado):** Caso um modelo não seja aplicável, o projeto poderá recorrer aos demais modelos testados. Entretanto, há risco de desempenho inferior em relação ao modelo originalmente planejado.
- **Probabilidade (10%):** Com o suporte contínuo do professor e da monitoria, espera-se que qualquer dificuldade técnica possa ser superada com auxílio qualificado.
- **Mitigação:** Solicitar apoio técnico sempre que surgirem dificuldades na aplicação de modelos, recorrendo à monitoria ou ao corpo docente especializado.

&emsp; **4.1.5.1.4. Fazer um modelo com baixa acurácia**

- **Categoria:** Técnico
Ameaça: Desenvolver um modelo preditivo com acurácia insuficiente para gerar resultados confiáveis e úteis na prática.
- **Impacto (Alto):** Um modelo com baixo desempenho compromete a utilidade da solução, podendo gerar diagnósticos incorretos sobre o risco de reprovação dos alunos. Isso afetaria diretamente a credibilidade do projeto junto aos stakeholders institucionais e reduziria o potencial de aplicação prática.
- **Probabilidade (20%):** Embora o grupo esteja empenhado em testar diferentes algoritmos e estratégias de modelagem, existe a possibilidade de que os dados não sejam suficientemente robustos ou que os ajustes (tuning) não sejam ideais para alcançar uma acurácia satisfatória.
- **Mitigação:** Realizar testes com múltiplos modelos preditivos, aplicar validação cruzada, otimizar hiperparâmetros e, se necessário, solicitar feedback técnico dos professores e monitores especializados em ciência de dados.

**4.1.5.2. Oportunidades**

<div align="center">

<sup>Figura : Matriz de oportunidades do projeto</sup>

<img src="../assets/matrizOportunidades.png">

<sup>Fonte: Material produzido pelos autores</sup>

</div>>

&emsp; As oportunidades identificadas no projeto foram descritas considerando três dimensões principais: oportunidade, impacto e probabilidade. A análise dessas oportunidades permite reconhecer e potencializar fatores que podem agregar valor ao desenvolvimento da solução e à formação dos integrantes do grupo. Assim como na seção anterior, a estruturação clara desses elementos favorece a tomada de decisões estratégicas durante a execução do projeto.

&emsp; **4.1.5.2.1. Intercâmbio cultural**

- **Oportunidade:** Possibilidade de trocar experiências culturais com a instituição parceira, além de conhecer as metodologias de ensino aplicadas em outro país.
- **Impacto (Muito alto):** Considerando que nenhum dos integrantes do grupo teve, até então, a oportunidade de conhecer a Colômbia, este projeto representa uma excelente chance de ampliar a compreensão sobre a realidade educacional e cultural local, enriquecendo tanto a experiência acadêmica quanto pessoal dos envolvidos.
- **Probabilidade (90%):** Devido ao longo período de colaboração com a instituição colombiana, a interação com seus profissionais é praticamente garantida, permitindo a troca de experiências rotineiras que ajudarão a contextualizar e aprofundar a aplicação do modelo preditivo.

&emsp; **4.1.5.2.2. Trabalhar com análise de dados**

- **Oportunidade:** Aplicar técnicas de análise de dados para resolver uma dor real de uma instituição de ensino de grande relevância na América Latina.
- **Impacto (Alto):** Por se tratar da primeira experiência de muitos integrantes na construção de um modelo preditivo, o projeto representa uma oportunidade valiosa de aprendizado prático e de enriquecimento do portfólio profissional.
- **Probabilidade (90%):** A equipe será exposta a diferentes modelos preditivos e ambientes de execução, o que garantirá a todos a oportunidade de compreender os fundamentos da área e adquirir conhecimentos essenciais para o avanço futuro na ciência de dados.


#### 4.1.6. Personas
```
Posicione aqui suas Personas (indique se são personas que utilizam o modelo e/ou se são afetadas pelo modelo).

Remova este bloco ao final
```

#### 4.1.7. Jornadas do Usuário
```
Posicione aqui seus mapas de jornadas do usuário que utiliza o modelo.

Remova este bloco ao final
```

#### 4.1.8 Política de Privacidade
```
Posicione aqui sua política de privacidade em acordo com a LGPD

Remova este bloco ao final
```

### 4.2. Compreensão dos Dados

#### 4.2.1. Exploração de dados
```
Apresentar a estatística descritiva básica de cada coluna, identificar se a coluna é numérica ou categórica e pelo menos 3 gráficos para visualizar a relação entre colunas escolhidas pelo grupo.

Remova este bloco ao final
```

#### 4.2.2. Pré-processamento dos dados
```
Apresentar quais foram as ações realizadas de limpeza (tratamento de missing values e remoção de outliers) e transformação (normalização e codificação) das colunas. Se houverem outliers, cite quais são e qual(is) correção(ões) será(ão) aplicada(s).

Remova este bloco ao final
```

#### 4.2.3. Hipóteses
```
Descreva três hipóteses sobre a relação dos dados e o problema. Justifique cada uma delas. 

Remova este bloco ao final
```

### 4.3. Preparação dos Dados e Modelagem
```
Caso seu projeto seja Modelo Supervisionado, apresentar: 
a) Organização dos dados (conjunto de treinamento, validação e testes)
b) Modelagem para o problema (proposta de features com a explicação completa da linha de raciocínio).
c) Métricas relacionadas ao modelo (pelo menos 3).
d) Apresentar o primeiro modelo candidato, e uma discussão sobre os resultados deste modelo (discussão sobre as métricas para esse modelo candidato).

Caso seu projeto seja Modelo Não-Supervisionado, apresentar:
a) Modelagem para o problema (proposta de features com a explicação completa da linha de raciocínio).
b) Primeiro modelo candidato para o problema.
c) Justificativa para a definição do K do modelo.
d) Escolha de um tipo de sistema de recomendação e a justificativa para essa escolha.

Remova este bloco ao final
```

### 4.4. Comparação de Modelos
```
- Descrever e justificar a escolha da métrica de avaliação dos modelos com base no que é mais importante para o problema ao 
  se medir a qualidade desses modelos;
- Descrever ao menos três modelos candidatos, seus respectivos algoritmos, seus tunings de hiperparâmetros e suas métricas 
  alcançadas;

Remova este bloco ao final
```

### 4.5. Avaliação
```
- Descreva a solução final de modelo preditivo e justifique a escolha. Alinhe sua justificativa com a Seção 4.1, resgatando o entendimento 
  do negócio e das personas, explicando de que formas seu modelo atende os requisitos e definições. 
- Descreva também um plano de contingência para os casos em que o modelo falhar em suas predições.
- Além disso, discuta sobre a explicabilidade do modelo (se aplicável) e realize a verificação de aceitação ou refutação das hipóteses.
- Se aplicável, utilize equações, tabelas e gráficos de visualização de dados para melhor ilustrar seus argumentos. 

Remova este bloco ao final
```

## <a name="c5"></a>5. Conclusões e Recomendações
```
Escreva, de forma resumida, sobre os principais resultados do seu projeto e faça recomendações formais ao seu parceiro de negócios em relação ao uso desse modelo. Você pode aproveitar este espaço para comentar sobre possíveis materiais extras, como um manual de usuário mais detalhado na seção “Anexos”. Não se esqueça também das pessoas que serão potencialmente afetadas pelas decisões do modelo preditivo e elabore recomendações que ajudem seu parceiro a tratá-las de maneira estratégica e ética. 

Remova este bloco ao final
```

## <a name="c6"></a>6. Referências
```
Incluir as principais referências de seu projeto, para que seu parceiro possa consultar caso ele se interessar em aprofundar. Não se esqueça de formatar as referências conforme a ABNT.

Remova este bloco ao final
```

## <a name="attachments"></a>Anexos
```
Utilize esta seção para anexar materiais como manuais de usuário, documentos complementares que ficaram grandes e não couberam no corpo do texto etc.

Remova este bloco ao final
```
