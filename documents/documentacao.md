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
&emsp;O planejamento geral da solução é uma etapa fundamental em projetos de inteligência artificial e ciência de dados. É a fase em que se define o que será feito, por que será feito e como será feito, com base no problema real a ser resolvido. Nele são detalhados os dados disponíveis, os objetivos da solução, o tipo de tarefa de aprendizado de máquina mais adequada (como classificação ou regressão), além dos possíveis usos da ferramenta, benefícios esperados e critérios de sucesso. 

&emsp;Para garantir o desenvolvimento organizado e eficiente da solução preditiva, este documento apresenta o planejamento geral do projeto.

##### Dados disponíveis 
&emsp;Os dados utilizados como fonte de aprendizado para o modelo preditivo foram entregues pela faculdade EAFIT. Esses dados são referentes as motas de 775 alunos no primeiro e segundo semestre do ano de 2023: 

- **Período:** Período letivo em que a aula é realizada.
- **Grupo:** Grupo ao qual o aluno pertence.
- **Horário:** Dia da semana e horário da aula do aluno.
- **Tipo de Documento:** Tipo de documento de identificação do aluno. Por exemplo: CC (maior de 17 anos), TI (menor de 18 anos).
- **Idade:** Determina se o aluno é adulto ou menor de idade (17 anos ou mais). Sexo: Sexo do aluno (masculino ou feminino).
- **Nome do Programa Acadêmico:** Nome do programa acadêmico que o aluno está cursando. STEM: Indica se o programa acadêmico está na área STEM (Sim/Não).
- **Semestre 1:** Nota obtida na primeira prova de meio de semestre.
- **Semestre 2:** Nota obtida na segunda prova de meio de semestre.
- **Parte 1 do Projeto:** Nota obtida no primeiro projeto.
- **Parte 2 do Projeto:** Nota obtida no segundo projeto.
- **Oficinas:** Nota média das oficinas.
- **Quizzes:** Nota final da prova.
- **Quiz 1 ao 8:** Notas dos quiz do 1 ao 8.
- **Tempo do Q1 ao Q8:** Tempo, em segundos, que o aluno demorou para fazer o Quiz referente.
- **CalcNotaQuiz:** Nota calculada do teste (média aritmética das notas do teste).
- **MelhoraNotaQuizes:** Indica se houve melhora nas notas do teste (VERDADEIRO/FALSO). As notas podem ser melhoradas completando atividades adicionais e respondendo a perguntas em sala de aula.
- **Quanto Melhora?:** Magnitude da melhora nas notas do teste (diferença entre Quices e CalcQuizNote).
- **Nota Final:** Nota final do curso.
- **Passou?:** Resultado final (Aprovado ou Reprovado no curso).


&emsp; Esse banco de dados fornecido será importante para que seja possível identificar padrões, nível de dificuldade entre as atividades entre outros dados importantes para o treinamento do modelo preditivo.

##### Solução Proposta
&emsp; A instituição EAFIT colocou uma nova matéria de programação em sua grade e, no primeiro ano, teve muitas notas baixas e vários alunos desistindo da matéria antes de acabar. Para solucionar esse problema, será produzido um modelo preditivo que ajudará os professores a administrar o curso, analisando as notas dos alunos e se há chance de reprovação dos mesmos. Com um sistema capaz de prever desempenhos e até prever se o aluno será reprovado ou não, os professores e coordenadores poderão disponibilizar o melhor suporte para os alunos que estão com dificuldade ou até grande risco de reprovação.

##### Tipo de Tarefa

&emsp; A solução engloba duas tarefas de aprendizado de máquina:

- **Classificação:** Utilizada para prever se o aluno será aprovado ou reprovado, categorizando os casos.

- **Regressão:** Aplicada para estimar as notas futuras com base em padrões de desempenho, frequência, participação e tempo de execução das provas.

##### Utilização
&emsp; Com base em dados passados, como notas de quizzes e projetos de alunos de anos anteriores, o sistema preditivo irá ajudar os professores a identificar padrões de notas com o intuito de prever quais terão chances de reprovar a matéria. Assim, os educadores poderão intervir previamente, antes que os alunos atinjam a reprovação. A análise será entregue a partir da semana 5, depois terão atualizações dessa análise entre 3 e 4 semanas

##### Benefícios
&emsp; O projeto facilitará a tomada de decisões mais informadas e oportunas por parte dos professores, permitindo-lhes identificar com eficiência os alunos em risco de reprovação e oferecer-lhes apoio adicional. Além disso, com o acompanhamento e suporte à esses alunos, o desempenho geral dos alunos irá aumentar, terminando a matéria melhor qualificado e preparado para diversas ocasiões.

##### Critério de Sucesso e Métricas
&emsp; Para saber se o modelo preditivo está impactando positivamente, a máquina, primeiramente, necessita acertar qual aluno está com dificuldade ou está caminhando para uma situação agravada de reprovação. Outro ponto que pode ser usado como métrica de sucesso é o aumento do suporte dos professores aos alunos e essa alta nos atendimentos resultar em melhoras nas notas. Além disso, o aumento da escolha, por parte dos alunos, de incluir essa matéria em sua grade curricular também é uma métrica de sucesso.

#### 4.1.4. Value Proposition Canvas
```
Posicione aqui seu canvas.

Remova este bloco ao final
```

#### 4.1.5. Matriz de Riscos
```
Posicione aqui sua matriz.

Remova este bloco ao final
```

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
