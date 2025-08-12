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

&emsp; Com base nas diretrizes apresentadas no PMBOK® Guide (PMI, 2021) e no conhecimento consolidado acerca da análise de riscos, elaborou-se a matriz de riscos do projeto com o objetivo de identificar, classificar e propor estratégias de mitigação para as ameaças potenciais ao desenvolvimento da solução. Essa abordagem permite antecipar problemas, minimizar impactos negativos e assegurar maior controle sobre as variáveis que podem comprometer o desempenho do modelo preditivo desenvolvido para a Universidade EAFIT, apresentado na figura xx.

<div align="center">

<sup>Figura xx: Matriz de riscos do projeto</sup>

<img src="../assets/matrizRiscos.png">

<sup>Fonte: Material produzido pelos autores</sup>

</div>

&emsp; A seguir, os riscos identificados são apresentados com base em cinco dimensões: categoria, ameaça, impacto, probabilidade e estratégia de mitigação. A classificação por categorias segue as diretrizes do PMBOK® Guide (PMI, 2021), visando facilitar o agrupamento, a análise e a priorização das ameaças ao longo do desenvolvimento do projeto. As categorias adotadas — Técnico, Humano, Organizacional e Acadêmico — refletem as diferentes naturezas dos riscos e permitem uma abordagem mais direcionada em sua gestão.

&emsp; O primeiro risco refere-se à possibilidade de treinar o modelo preditivo com uma quantidade insuficiente de dados, classificado como de natureza técnica. Trata-se de um risco de impacto muito alto, pois a escassez de dados inviabiliza o treinamento adequado do modelo e compromete todo o desenvolvimento do projeto. A probabilidade estimada é de 10%, uma vez que o parceiro institucional assumiu o compromisso de fornecer os dados necessários, reduzindo a chance de indisponibilidade. A estratégia de mitigação consiste em levantar previamente a quantidade mínima de dados amostrais e solicitar oficialmente à universidade a sua disponibilização.

&emsp; Outro risco identificado está relacionado ao descumprimento de prazos, classificado como humano. Essa ameaça envolve a possibilidade de membros do grupo não concluírem suas atividades no prazo definido, o que pode atrasar etapas subsequentes, gerar sobrecarga em alguns integrantes e comprometer a entrega de funcionalidades do MVP. O impacto é considerado alto e a probabilidade estimada em 30%, com base em experiências anteriores que indicam a necessidade de melhorar a definição de prazos e a comunicação. Para mitigar esse risco, recomenda-se reavaliar os prazos considerando o tempo de aprendizado e de testes, atualizar periodicamente o status das atividades e manter comunicação constante sobre eventuais impedimentos.

&emsp; Também foi identificada a dificuldade na aplicação de modelos preditivos, enquadrada na categoria acadêmica. Essa situação pode ocorrer quando houver obstáculos na implementação de um ou mais modelos apresentados durante as aulas. O impacto é moderado, pois, embora seja possível recorrer a modelos alternativos testados, há risco de que estes apresentem desempenho inferior ao originalmente planejado. A probabilidade de ocorrência é de 10%, considerando o suporte contínuo de professores e monitores. A mitigação envolve buscar auxílio técnico sempre que surgirem dificuldades, recorrendo à monitoria e ao corpo docente especializado.

&emsp; Por fim, considera-se o risco de desenvolver um modelo com baixa acurácia, classificado como técnico. Um desempenho insatisfatório compromete a utilidade prática da solução, podendo gerar diagnósticos incorretos sobre o risco de reprovação e afetar a credibilidade do projeto perante os stakeholders institucionais. Esse risco tem impacto alto e probabilidade estimada em 20%, já que, apesar dos esforços da equipe em testar diferentes algoritmos e estratégias de modelagem, podem ocorrer limitações nos dados ou ajustes inadequados. A mitigação proposta inclui a realização de experimentos com múltiplos algoritmos, aplicação de validação cruzada, otimização de hiperparâmetros e solicitação de feedback técnico a professores e monitores especializados.

**4.1.5.2. Oportunidades**

&emsp; Além da identificação e análise dos riscos, é relevante reconhecer e explorar as oportunidades que o projeto oferece. A partir dessa perspectiva, elaborou-se a matriz de oportunidades com o propósito de potencializar fatores favoráveis, agregar valor ao desenvolvimento da solução e maximizar os benefícios dessa etapa de construção. Essa abordagem permite direcionar esforços para iniciativas que fortaleçam o trabalho do grupo e ampliem o impacto positivo do modelo preditivo desenvolvido para a Universidade EAFIT, apresentado na figura xx.

<div align="center">

<sup>Figura xx: Matriz de oportunidades do projeto</sup>

<img src="../assets/matrizOportunidades.png">

<sup>Fonte: Material produzido pelos autores</sup>

</div>

&emsp; As oportunidades identificadas no projeto foram descritas considerando três dimensões principais: oportunidade, impacto e probabilidade. Essa análise possibilita reconhecer e explorar fatores que podem agregar valor tanto ao desenvolvimento da solução quanto à formação acadêmica e profissional dos integrantes do grupo. A organização dessas informações de maneira clara contribui para embasar decisões estratégicas e maximizar os benefícios potenciais ao longo da execução do projeto.

&emsp; A primeira oportunidade está relacionada ao intercâmbio cultural, envolvendo a troca de experiências com a instituição parceira e o contato com metodologias de ensino aplicadas em outro país. Como nenhum dos integrantes do grupo teve, até então, a oportunidade de conhecer a Colômbia, esta experiência representa uma excelente chance de ampliar a compreensão sobre a realidade educacional e cultural local, enriquecendo não apenas o aprendizado acadêmico, mas também a vivência pessoal de cada participante. O impacto dessa oportunidade é considerado muito alto, e sua probabilidade de concretização chega a 90%, uma vez que o longo período de colaboração com a instituição colombiana torna praticamente certa a interação direta com seus profissionais e a troca de experiências que irão aprofundar o contexto da aplicação do modelo preditivo.

&emsp; A segunda oportunidade refere-se ao trabalho com análise de dados, no qual a equipe poderá aplicar técnicas para solucionar uma necessidade real de uma instituição de ensino de grande relevância na América Latina. Para muitos integrantes, essa será a primeira experiência prática na construção de um modelo preditivo, o que torna o projeto um recurso valioso para o desenvolvimento de competências técnicas e para o fortalecimento do portfólio profissional. O impacto é classificado como alto, e a probabilidade de concretização é de 90%, pois a equipe estará exposta a diferentes tipos de modelos preditivos e ambientes de execução, garantindo a todos a oportunidade de compreender os fundamentos da área e adquirir conhecimentos essenciais para futuros avanços na ciência de dados.

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

[Númeração de acordo com a ordem alfabética]. <a name="ref[Numeração de acrodo com a ordem alfabética]"></a> [PMI – Project Management Institute. Um guia do conhecimento em gerenciamento de projetos (Guia PMBOK®): guia do conhecimento em gerenciamento de projetos. 7. ed. Newtown Square, PA: Project Management Institute, 2021.](https://www.academiaplaorc.com.br/wp-content/uploads/2024/07/Guia-PMBOK-7a-Edicao.pdf)  


## <a name="attachments"></a>Anexos
```
Utilize esta seção para anexar materiais como manuais de usuário, documentos complementares que ficaram grandes e não couberam no corpo do texto etc.

Remova este bloco ao final
```
