# Documentação Modelo Preditivo - Inteli

## LATECH: Modelo preditivo para identificação de alunos em risco de reprovação
### Integrantes (THROXY):
- <a href="https://www.linkedin.com/in/antonio-augusto-tavares-ribeiro-andr%C3%A9-613937345?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app">Antonio Augusto Tavares Ribeiro André</a>
- <a href="https://www.linkedin.com/in/carlos-quaglia-309088357/">Carlos Quaglia</a>
- <a href="https://www.linkedin.com/in/hugo-montan-393b49175/">Hugo Montan</a>
- <a href="https://www.linkedin.com/in/leandro-precaro-barankiewicz-filho-8a293a345/">Leandro Precaro Brankiewicz Filho</a>
- <a href="https://www.linkedin.com/in/luiz-hinuy-0995252b1?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app">Luiz Hinuy</a>
- <a href="https://www.linkedin.com/in/messias-olivindo/">Messias Olivindo</a>
- <a href="https://www.linkedin.com/in/yuriboczar/">Yuri Boczar</a>

## Sumário
[1. Introdução](#c1)

[2. Objetivos e Justificativa](#c2)

[3. Metodologia](#c3)

[4. Desenvolvimento e Resultados](#c4)

[5. Conclusões e Recomendações](#c5)

[6. Referências](#c6)

[Anexos](#attachments)


## <a name="c1"></a>1. Introdução

&emsp; Fundada em 1960 por um grupo de empresários de Medellín, a EAFIT nasceu com o propósito de formar profissionais para os setores de gestão, finanças e tecnologia, estabelecendo desde o início um forte vínculo com o desenvolvimento socioeconômico da região (EAFIT HISTORIA, 2025). Reconhecida pelo governo colombiano como universidade em 1971, a instituição expandiu sua oferta acadêmica para incluir escolas de Engenharia, Ciências e Humanidades, Direito e Música, adaptando-se às necessidades da sociedade e consolidando sua posição como um centro educacional de destaque.

&emsp; O reconhecimento oficial como universidade pelo Ministério da Educação, em 1971, marcou um ponto de inflexão que acelerou a diversificação acadêmica e a expansão institucional. A partir dos anos 1970, a EAFIT consolidou novas escolas e programas além da Administração, incluindo Engenharia e, posteriormente, Ciências e Humanidades, Direito e Música, em sintonia com as necessidades emergentes da sociedade e com a modernização do tecido econômico regional (EAFIT HISTORIA NOTICIAS, 2025). Esse crescimento veio acompanhado de uma profunda atuação no território: o campus de La Aguacatala, no sul de Medellín, tornou-se referência urbana e cultural, com atividades acadêmicas, científicas e de extensão que expressam a missão institucional de inspirar vidas, criar conhecimento e transformar a sociedade (EAFIT HISTORIA, 2025).

&emsp; Entre seus egressos notáveis, a EAFIT formou líderes como Aníbal Gaviria, ex-governador de Antioquia, e Claudia Patricia Restrepo Montoya, ex-vice-ministra de Cultura da Colômbia, testemunhos do compromisso da instituição com uma formação ética, crítica e orientada ao serviço público. Apesar desse histórico, a universidade enfrenta o desafio contemporâneo de otimizar a experiência de aprendizagem em um contexto cada vez mais digital. Neste projeto, propomos desenvolver um modelo preditivo que antecipe a probabilidade de reprovação de estudantes, apoiando a tomada de decisão pedagógica e a personalização de intervenções (EAFIT NOTICIAS, 2025).

&emsp; Apesar de seu histórico de sucesso, a EAFIT enfrenta o desafio de otimizar a experiência de aprendizado dos estudantes em um contexto cada vez mais digital. O problema consiste na necessidade de desenvolver uma metodologia para adaptar estratégias de ensino de países mais desenvolvidos à realidade e aos recursos da Colômbia.

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
&emsp; Neste projeto, será usada a metodologia CRISP-DM (Cross Industry Standard Process for Data Mining). Basicamente, essa metodologia serve para ajudar a criar modelos a partir da análise de dados, com o objetivo de identificar possíveis problemas e no caso atual, será usada para ajudar a prever alunos com chance de reprovação. Pensada por um conjunto de empresas de mineração de dados, como SPSS e Daimler-Benz, por volta dos anos 1990, é dividida em 6 etapas denominadas Entendimento do negócio, Entendimento dos dados, Preparação dos dados, Modelagem, Avaliação e por ultimo Implementação. Um ponto importante é que o CRISP-DM não é uma linha reta: o processo é iterativo, ou seja, quando é terminado uma etapa, sempre existe a chance de voltar para uma anterior e melhorar o que já foi feito. As seis etapas dessa metodologia são:

- **Entendimento do negócio**: Essa etapa consiste em compreender o que deve ser feito, para quem e com qual objetivo final o projeto será desenvolvido. Aqui é realizada uma análise completa da empresa e de sua principal dor (problema), para que o desafio seja resolvido da forma mais eficiente possível. É importante ressaltar que, se essa fase não for bem conduzida, todo o projeto corre sério risco de ficar comprometido.

- **Entendimento dos dados**: Essa etapa vem logo após o entendimento do negócio e tem como foco levantar questionamentos sobre os dados que serão usados no projeto. É nesse momento que se avalia quais dados estão disponíveis, sua qualidade e relevância para o problema. A partir dessas análises, normalmente ocorre a coleta dos dados necessários. No caso deste projeto, por uma decisão de escopo, essa coleta não foi realizada, mas a etapa ainda serve para refletir sobre como os dados podem apoiar na solução do problema.

- **Preparação dos dados**: Com os dados em mãos, essa etapa é dedicada ao tratamento e ao pré-processamento, ou seja, corrigir valores nulos, lidar com outliers, enriquecer os dados e selecionar as variáveis mais relevantes para o modelo. Em geral, é uma das fases mais demoradas e também uma das mais revisitadas do processo, já que os dados precisam passar por ajustes constantes ao longo do projeto para garantir a qualidade dos resultados.

- **Modelagem**: Essa é, geralmente, a etapa mais aguardada do processo, embora muitas vezes seja uma das mais rápidas. Aqui é definido qual tipo de modelo será utilizado e quais atributos (variáveis) vão compor sua construção. É também nesse momento que o modelo é efetivamente treinado e começam a aparecer os primeiros resultados, como métricas de desempenho — por exemplo, a acurácia em um modelo preditivo.

- **Avaliação**:Com os resultados da modelagem em mãos, essa é a hora de analisar se o desempenho do modelo realmente atende às expectativas definidas no início do projeto. Métricas como a acurácia são comparadas com os objetivos de negócio para verificar se o modelo é útil na prática. Caso os resultados não sejam satisfatórios, a equipe pode voltar a etapas anteriores — como a preparação dos dados — para refinar o conjunto utilizado e tentar melhorar os resultados. Esse caráter de revisão torna essa fase essencial para garantir que o modelo seja de fato eficaz e aplicável.

- **Implementação**:Sendo a etapa final do processo, a implementação (ou deploy) é quando o modelo é colocado em produção e começa a gerar impacto real para o negócio ou empresa. A forma como isso acontece pode variar bastante de projeto para projeto. Um exemplo comum é disponibilizar o modelo em um serviço na nuvem, permitindo que membros da equipe da empresa possam utilizá-lo diretamente para apoiar decisões ou operações.

&emsp; Por fim, o grande benefício de usar a metodologia CRISP-DM é que ela ajuda a conectar a criação do modelo preditivo com o entendimento real do negócio. No caso deste projeto, isso significa olhar de perto como funciona a dinâmica dos alunos e como os fatores analisados impactam diretamente no risco de reprovação. A partir dessa visão, é possível desenvolver um modelo preditivo mais certeiro sempre com base e inteiramente focado no problema que estiver trabalhando. Além disso, o processo iterativo é um ponto muito forte da metodologia, já que se os resultados obtidos não forem bons, apenas voltar alguns passos e refazer os passos como fosse a primeira vez.

## <a name="c4"></a>4. Desenvolvimento e Resultados
### 4.1. Compreensão do Problema
#### 4.1.1. Contexto da indústria e 5 forças de Porter
##### 1. Contexto da indústria:

&emsp;A Universidad EAFIT é uma instituição privada sem fins lucrativos, fundada em Medellín, que se consolidou como protagonista no cenário acadêmico colombiano e regional. Reconhecida por sua excelência acadêmica e inovação, ocupa a 56ª posição entre 437 universidades no QS World University Rankings: Latin America & the Caribbean 2025, sendo a principal instituição fora de Bogotá e uma das cinco melhores universidades privadas da Colômbia. Entre seus principais concorrentes estão a Universidad de los Andes, líder no segmento privado e classificada em 7º lugar na América Latina, referência em pesquisa de ponta; a Universidad Pontificia Bolivariana (UPB), também sediada em Medellín e posicionada na 84ª colocação, com atuação multidisciplinar; e a Universidad CES, 33ª na região e especializada nas áreas de saúde e engenharia biomédica.

&emsp;Com um modelo de negócios sustentado pela diversificação de receitas, a EAFIT apresenta 57,4% de sua receita total proveniente de programas de graduação (COP 154.443 milhões), 21,6% de pós-graduação (COP 58.213 milhões) e o restante originado de educação executiva, consultorias corporativas e pesquisa aplicada. Em 2022, as receitas por serviços de ensino totalizaram COP 268.940 milhões. Sua solidez financeira foi reconhecida em maio de 2019, quando a Fitch Ratings elevou sua nota de crédito de longo prazo de AA+ para AAA(col), ressaltando alta liquidez, baixo endividamento e operação robusta — classificação retirada em abril de 2020 por decisão comercial da agência.

&emsp;O setor de ensino superior na Colômbia passa por transformações aceleradas. Estudos apontam que 69% dos estudantes preferem modelos flexíveis de aprendizagem, seja no formato online, híbrido ou blended. A adoção de ferramentas de inteligência artificial já alcança 92% do corpo discente, exigindo da EAFIT políticas claras de uso e integridade acadêmica. Paralelamente, as microcredentials ganham espaço como percursos de aprendizagem curtos, flexíveis e reconhecidos, impulsionando debates regionais liderados pela UNESCO IESALC para padronização e garantia de qualidade.

&emsp;Nesse contexto, a EAFIT se posiciona para capitalizar essas mudanças, investindo em inovação pedagógica, integração tecnológica e ampliação de parcerias estratégicas, visando não apenas manter sua relevância no cenário acadêmico, mas também antecipar tendências e moldar o futuro da educação superior na América Latina.

##### 2. 5 forças de Porter:

&emsp;No livro *Competitive Strategy: Techniques for Analyzing Industries and Competitors* (1986), Michael Porter apresenta o modelo das **Cinco Forças**, um método para avaliar a atratividade e a dinâmica competitiva de um setor. Essa estrutura identifica os principais elementos que influenciam o desempenho e a lucratividade das empresas.

- **Rivalidade no Setor**: intensidade da competição entre empresas já estabelecidas, manifestada por estratégias como redução de preços, fortalecimento de marca, inovação e melhoria no atendimento.
- **Influência dos Fornecedores**: capacidade dos fornecedores de impactar custos e qualidade, afetando diretamente a rentabilidade das empresas compradoras.
- **Poder dos Consumidores**: grau em que os clientes podem exigir preços mais baixos ou maior qualidade, pressionando margens de lucro.
- **Entrada de Novos Concorrentes**: facilidade ou dificuldade para que novas empresas ingressem no mercado, determinada por barreiras de entrada como capital inicial, regulamentações e diferenciação de marca.
- **Produtos ou Serviços Substitutos**: presença de alternativas que atendem à mesma necessidade, limitando preços e influenciando a demanda.

<div align="center">

  <sub>Figura : 5 forças de Porter </sub>

  <img src="../assets/5forcas.png">

  <sup>Fonte: Imagem retirada do site https://ufabcjr.com.br/</sup>

</div>

**Rivalidade entre concorrentes existentes**

&emsp;A Universidad EAFIT atua no setor de ensino superior colombiano, especialmente no segmento privado, caracterizado por um número moderado de instituições de grande porte e forte reputação acadêmica. Seus principais concorrentes diretos incluem a Universidad de los Andes, líder no ranking nacional, a Universidad Pontificia Bolivariana (UPB) e a Universidad CES, todas com forte presença em áreas estratégicas de ensino e pesquisa. Essa rivalidade é intensificada por fatores como reputação acadêmica, qualidade do corpo docente, internacionalização, infraestrutura e inovação pedagógica. Apesar disso, a EAFIT diferencia-se por seu posicionamento como a principal universidade privada fora de Bogotá, pela diversificação de receitas e pela oferta de programas inovadores em múltiplas áreas do conhecimento, o que fortalece sua marca e a mantém competitiva no cenário nacional e regional.

**Poder de barganha de fornecedores**

&emsp;No setor educacional, os fornecedores podem incluir desde editoras acadêmicas e plataformas tecnológicas até prestadores de serviços de manutenção, segurança e alimentação. A EAFIT, por ser uma instituição de grande porte e com sólida situação financeira, tem poder de negociação elevado, podendo diversificar fornecedores e adotar soluções internas para reduzir dependências estratégicas. Sua posição consolidada no mercado permite estabelecer contratos de longo prazo em condições favoráveis, além de buscar parcerias acadêmicas e tecnológicas que geram benefícios mútuos, diminuindo o risco de impactos significativos advindos de aumento de custos ou mudanças nas condições de fornecimento.

**Poder de barganha de compradores**

&emsp;Os "compradores" no contexto da EAFIT são os estudantes e suas famílias, que avaliam não apenas o preço das mensalidades, mas também a qualidade do ensino, a empregabilidade dos egressos, as oportunidades de intercâmbio e o reconhecimento acadêmico. No segmento premium da educação superior privada, o poder de barganha é moderado: embora os alunos possam optar por outras instituições de prestígio, a reputação, a localização estratégica e o portfólio diversificado da EAFIT reduzem a elasticidade da demanda. No entanto, com o aumento da oferta de cursos online, híbridos e microcredentials — muitas vezes a preços menores —, cresce a pressão para que a EAFIT mantenha diferenciais claros de valor agregado, reforçando a importância de inovação contínua e experiência acadêmica de excelência.

**Ameaça de novos entrantes**

&emsp;O ingresso de novos competidores relevantes no ensino superior colombiano é dificultado por barreiras como altos investimentos em infraestrutura, acreditações, corpo docente qualificado e reputação acadêmica, além de regulamentações rigorosas. Apesar disso, o avanço da educação online e de plataformas globais de cursos representa uma ameaça indireta, pois reduz as barreiras geográficas e oferece alternativas de formação a custos competitivos. Nesse cenário, a EAFIT mitiga o risco por meio de expansão de programas digitais, parcerias internacionais e fortalecimento de sua marca como centro de excelência acadêmica e inovação.

**Ameaça de produtos substitutos**

&emsp;As principais alternativas ao ensino superior tradicional incluem cursos técnicos, bootcamps, programas de microcredentials e plataformas de aprendizado online, que oferecem formação mais rápida e focada em habilidades específicas. Esses formatos, muitas vezes mais acessíveis, podem atrair estudantes que buscam inserção rápida no mercado de trabalho ou atualização profissional contínua. A ameaça é crescente, especialmente em áreas ligadas à tecnologia e negócios, onde a aprendizagem prática é valorizada. No entanto, a EAFIT mantém vantagem competitiva ao oferecer uma formação integral, com reconhecimento acadêmico formal, rede de contatos e experiências de pesquisa e intercâmbio, fatores que ainda representam barreiras significativas para a substituição total por formatos alternativos.

#### 4.1.2. Análise SWOT

&emsp; Segundo Rother e Shook (2003), a Análise SWOT é uma ferramenta de planejamento estratégico que organiza visualmente as forças, fraquezas, oportunidades e ameaças de um negócio. Seu objetivo é auxiliar na avaliação do ambiente interno e externo de uma empresa ou projeto, e orientar uma tomada de decisão mais embasada na realidade.

&emsp; Dessa maneira, a aplicação dessa análise é crucial para o mapeamento estratégico da solução em desenvolvimento para a EAFIT. Fornecendo elementos vitais para a idealização e o debate de ideias do projeto, permitindo uma compreensão clara dos desafios e das oportunidades.

<div align="center">

   <sub>Figura 1 - Análise Swot </sub>

   <img src="../assets/analise-swot.png">

   <sup>Fonte: Material produzido pelos autores (2025)</sup>

</div>

&emsp; Na figura acima temos:

##### Forças:

- **Posicionada como uma das melhores universidades da Colômbia** - A Universidad EAFIT possui reconhecimento nacional por sua excelência acadêmica (UNIVERSIDAD EAFIT, 2025), foco na inovação e comprometimento com a formação integral de seus estudantes. É constantemente classificada entre as melhores instituições de ensino superior da Colômbia.

- **Credenciada como instituição de alta qualidade** - A EAFIT foi credenciada pelo Ministério Nacional da Educação da Colômbia como uma universidade de alta qualidade duas vezes seguidas, sendo a primeira universidade colombiana a ter esta recognição. Essa certificação garante que a instituição atende a rigorosos critérios de avaliação institucional, como infraestrutura, corpo docente, produção científica, governança e impacto social, contribuindo para a confiança do público interno e externo.

- **Currículo extenso e diverso, com opções de pós-graduação** - A universidade oferece uma ampla gama de programas acadêmicos em áreas como administração, economia, engenharia, humanidades, direito e ciências aplicadas. Além disso, conta com cerca de 90 opções de cursos de pós-graduação.

##### Fraquezas:

- **Gastos elevados com a manutenção do Campus Vivo** - Embora o Campus Vivo seja um diferencial arquitetônico e ambiental da EAFIT, sua manutenção representa custos operacionais significativos. Isso inclui jardinagem, segurança, manutenção predial e limpeza, o que pode impactar os recursos disponíveis para investimentos em outras áreas estratégicas, como digitalização ou internacionalização.

- **Inexistência de parcerias com universidades de referência na América Latina e no mundo** - Apesar de seu prestígio nacional, a EAFIT ainda apresenta limitações na construção de alianças acadêmicas internacionais robustas, especialmente com instituições de referência global. A ausência de programas de dupla titulação, intercâmbios amplamente reconhecidos e pesquisa conjunta com universidades de renome mundial limita o alcance internacional da instituição.

##### Ameaças:

- **Instabilidade econômica e política regional** - O contexto colombiano, assim como o de outras nações latino-americanas, é frequentemente marcado por flutuações econômicas, tensões sociais e mudanças políticas que podem afetar diretamente o financiamento da educação superior, os programas de intercâmbio, os investimentos em infraestrutura e a própria capacidade de planejamento estratégico das universidades privadas.

- **Competição com outras universidades sul-americanas** - A crescente profissionalização e internacionalização de outras universidades na América Latina, como a Universidad de Los Andes (Colômbia), Pontificia Universidad Católica (Chile), Universidade de São Paulo (Brasil) e Universidad Nacional Autónoma de México (México), impõe um desafio constante. A EAFIT precisa manter-se atualizada, inovadora e conectada globalmente para não perder sua atratividade frente à concorrência (QS, 2025).

##### Oportunidades:

- **Horizonte para a digitalização do atendimento ao aluno** - A universidade possui uma grande oportunidade de melhorar a experiência do estudante por meio da automação e digitalização de processos relacionados à vida acadêmica. Isso inclui sistemas mais inteligentes para acompanhamento de desempenho, integração com orientações pedagógicas, monitoramento psicológico, alertas de risco acadêmico, e acesso facilitado a recursos administrativos e financeiros. A adoção de plataformas tecnológicas modernas pode otimizar a gestão estudantil e fortalecer o engajamento institucional.

#### 4.1.3. Planejamento Geral da Solução
&emsp; Planejamento Geral da Solução é um conceito de organizar o projeto em tópicos com intuito de nunca se perder em relação a esses 6 tópicos: Dados que serão usados, neste caso, para abastecer o modelo preditivo, A solução proposta para ao cliente, tipo de tarefa, para que o produto será usado, benefícios ao escolher o produto e quais críterios e métricas será usada para acompanhar o sucesso da solução. Pode-se fazer uma analogia com um mapa, onde os tópicos citados são os locais para chegar ao produto ideal. A empresa PMBOK Guide, empresas de software e análise de projetos foram os primeiros a utilizar esse método de se guiar conforme o projeto está em andamento.

&emsp; O planejamento geral da solução é uma etapa fundamental em projetos de inteligência artificial e ciência de dados, já que é fácil se perder em um projeto que exige muitos detalhes. Nele são detalhados os dados disponíveis, os objetivos da solução, o tipo de tarefa de aprendizado de máquina mais adequada (como classificação ou regressão), além dos possíveis usos da ferramenta, benefícios esperados e critérios de sucesso do projeto feito.

&emsp; Primeiro, será mostrado a base que todo o projeto se baseará: Os dados. Fornecidos pela EAFIT, eles estão dispostos em tabelas de notas na nova matéria de programção de 775 alunos da instituição entre o primeiro e segundo semestre do ano de 2023. Logo abaixo, terá as explicações do que cada coluna significa:

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

&emsp; Com o modelo preditivo, conseguimos resolver as dores do cliente, mas temos que contextualizar tal problema para ficar o mais claro possível nossos objetivos. A instituição EAFIT colocou uma nova matéria de programação em sua grade e, no primeiro ano, teve muitas notas baixas e vários alunos desistindo da matéria antes de acabar. Para solucionar esse problema, será produzido um modelo preditivo que ajudará os professores a administrar o curso, analisando as notas dos alunos e se há chance de reprovação dos mesmos. Com um sistema capaz de prever desempenhos e até prever se o aluno será reprovado ou não, os professores e coordenadores poderão disponibilizar o melhor suporte para os alunos que estão com dificuldade ou até grande risco de reprovação.



##### Tipo de Tarefa

&emsp; A solução engloba duas tarefas de aprendizado de máquina:

- **Classificação:** Utilizada para prever se o aluno será aprovado ou reprovado, categorizando os casos.

- **Regressão:** Aplicada para estimar as notas futuras com base em padrões de desempenho, frequência, participação e tempo de execução das provas.

&emsp; Mesmo com o modelo em mãos e o problema explicado detalhadamente, sem mostrar a utilidade não será muito produtivo.
&emsp; Com base em dados passados, como notas de quizzes e projetos de alunos de anos anteriores, o sistema preditivo irá ajudar os professores a identificar padrões de notas com o intuito de prever quais terão chances de reprovar a matéria. Assim, os educadores poderão intervir previamente, antes que os alunos atinjam a reprovação. A análise será entregue a partir da semana 5, depois terão atualizações dessa análise entre 3 e 4 semanas. Como sempre terá atualizações sobre as situações dos alunos, o projeto facilitará a tomada de decisões mais informadas e oportunas por parte dos professores, permitindo-lhes identificar com eficiência os alunos em risco de reprovação e oferecer-lhes apoio adicional. Além disso, com o acompanhamento e suporte à esses alunos, o desempenho geral dos alunos irá aumentar, terminando a matéria melhor qualificado e preparado para diversas ocasiões.

&emsp; Com todos os passos passados sendo feitos corretamentes, já é possível definir e observar como o modelo está performando. Primeiramente, a máquina, necessita acertar qual aluno está com dificuldade ou está caminhando para uma situação agravada de reprovação. Outro ponto que pode ser usado como métrica de sucesso é o aumento do suporte dos professores aos alunos e essa alta nos atendimentos resultar em melhoras nas notas. Além disso, o aumento da escolha, por parte dos alunos, de incluir essa matéria em sua grade curricular também é uma métrica de sucesso.

#### 4.1.4. Value Proposition Canvas
&emsp; O Canvas de Proposta de Valor é uma ferramenta visual que ajuda a alinhar, de forma prática e objetiva, o que uma solução oferece com o que o cliente realmente precisa. Desenvolvido por Alexander Osterwalder, Yves Pigneur e Alan Smith, ele organiza a análise em dois blocos complementares: o Perfil do Cliente, que detalha as tarefas atuais do cliente, as dores em relação aquela atividade e os ganhos esperados com a solução, e o Mapa de Valor, com as principais informações sobre o produto ou serviço, os elementos aliviantes de dores e as vantagens que criam de ganho. Nesse sentido, o objetivo é alcançar o "encaixe" entre oferta e demanda: entender claramente o que o cliente tenta realizar, quais obstáculos enfrenta e quais resultados espera, e então descrever como a solução elimina essas dores e potencializa os ganhos.

<div align="center">

   <sub>Figura : Canvas Proposta de Valor </sub>

   <img src="../assets/canva-proposta-de-valor.png">

   <sup>Fonte: Material produzido pelos autores (2025)</sup>

</div>

##### Perfil do Cliente:
&nbsp;&nbsp;&nbsp;&nbsp;
&emsp; **Ganhos:** Professores e coordenação querem entender rapidamente o que impacta as notas para agir cedo e melhorar os resultados. Buscam visão por curso/área e horário, com evidências para orientar intervenções e monitores.

&nbsp;&nbsp;&nbsp;&nbsp;
&emsp; **Dores:** Alunos em risco são identificados tarde, por falta de previsibilidade e pela necessidade de juntar dados de várias fontes. O aumento de turmas piora a falta de visibilidade e dificulta priorizar quem atender.

&nbsp;&nbsp;&nbsp;&nbsp;
&emsp; **Tarefas do Cliente:** Professores intervêm quando o risco já está claro (após notas baixas) e organizam grupos a cada semestre. Precisam de um fluxo simples, online e padronizado para acompanhar evolução, comparar grupos e orientar monitores.

##### Proposta de Valor

&nbsp;&nbsp;&nbsp;&nbsp;
&emsp; **Criadores de Ganho:** Alertas antecipados nas primeiras semanas indicam probabilidade de reprovação por faixas de risco (baixo, médio, alto, muito alto). Um dashboard reúne evolução das notas, motivos do risco e filtros por programa, grupo e horário para ações rápidas e coordenadas.

&nbsp;&nbsp;&nbsp;&nbsp;
&emsp; **Aliviam as Dores:** O sistema prevê próximos resultados e explica o "porquê do risco" (ex.: quizzes pendentes, queda de desempenho, efeitos de horário/programa), reduzindo checagens manuais. É escalável, com execução automática por marcos do semestre ou upload manual, absorvendo o crescimento de alunos sem sobrecarga.

&nbsp;&nbsp;&nbsp;&nbsp;
&emsp; **Produtos e Serviços:** Modelo preditivo que destaca alunos em risco (nota final < 3) e diferencia "aprova", "reprova" e "cancela". Integra notas oficiais, quizzes/talleres, grupos/horários e indicadores de evolução, com privacidade garantida. Entrega inclui dashboard web, manuais (usuário e técnico), capacitação breve e revisão do modelo a cada semestre.

#### 4.1.5. Matriz de Riscos
&emsp; A análise de riscos e oportunidades em um projeto é uma etapa essencial no desenvolvimento de um modelo preditivo, pois permite mitigar possíveis problemas e, ao mesmo tempo, identificar oportunidades que possam alavancar a entrega do MVP. Segundo o PMBOK® Guide (PMI, 2021), o gerenciamento de riscos compreende os processos de planejamento, identificação, análise, resposta, monitoramento e controle de riscos e oportunidades que possam surgir ao longo do ciclo de vida do projeto. Com base nesse entendimento, propõe-se a seguinte divisão em matriz de riscos e matriz de oportunidades:


##### Riscos:

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

##### Oportunidades:

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

&emsp; No desenvolvimento de produtos e serviços — especialmente em projetos de tecnologia e experiência do usuário — o uso de personas é uma prática amplamente adotada para orientar decisões de design. Uma persona é uma representação fictícia, porém plausível, de um usuário-alvo, construída a partir de dados qualitativos e quantitativos sobre seus comportamentos, necessidades, motivações e objetivos. Essa abordagem ajuda as equipes a manterem o foco nas expectativas reais do público, reduzindo suposições e alinhando o projeto às demandas concretas.
&emsp; De acordo com Cooper et al. (2014)[personas], personas funcionam como arquétipos que sintetizam as principais características de determinados segmentos de usuários, permitindo que designers e desenvolvedores fundamentem suas escolhas em evidências, e não em opiniões subjetivas. Ao serem aplicadas em documentos técnicos e estratégicos, elas contribuem para que o produto final seja relevante, funcional e verdadeiramente centrado no usuário.

<div align = "center">

<sub>Figura : Persona 1</sub>

<img src = "../assets/persona1.png">

<sup>Fonte: Material produzido pelos autores (2025)</sup>

</div>

##### Persona: Paola Andrea Vallejo Ramírez

**Perfil**

- Nome: Paola Andrea Vallejo Ramírez
- Gênero: Feminino
- Idade: 41 anos
- Cidade: Medellín - Antioquia, Colômbia
- Posição: Docente universitária e coordenadora de projetos pedagógicos na Universidad EAFIT

**Biografia**

&emsp; Paola nasceu em Medellín, na Colômbia, e cresceu em um ambiente onde a educação era altamente valorizada. Desde pequena, era curiosa e gostava de resolver problemas práticos. Apaixonada por aprender, escolheu seguir a carreira acadêmica e se formou em Engenharia de Software pela Universidade Industrial de Santander. Posteriormente, concluiu um mestrado em Educação e Tecnologias Digitais na Universidad de los Andes.

&emsp; Atualmente, mora em Medellín e leciona disciplinas introdutórias de programação na Universidad EAFIT, onde também lidera iniciativas de inovação educacional. É reconhecida por sua dedicação ao sucesso dos alunos e por seu compromisso com a inclusão e o uso ético da tecnologia na educação. Atua como ponte entre dados educacionais e ações pedagógicas eficazes, sempre buscando formas de aprimorar os resultados acadêmicos.

**Frustrações**

- Dificuldade em acompanhar o progresso individual de cada aluno devido ao grande número de estudantes e ao tempo limitado.
- Falta de ferramentas práticas para identificar alunos em risco antes que a situação se agrave.
- Sensação de que as ações pedagógicas são frequentemente reativas, e não preventivas.
- Necessidade constante de adaptar estratégias sem dados objetivos suficientes para orientar as decisões.

**Motivações**

- Acredita que a educação transforma vidas e que todos os alunos merecem oportunidades reais de sucesso.
- Busca aplicar métodos científicos e baseados em dados para tornar o ensino mais eficaz.
- Quer melhorar a retenção e o desempenho dos estudantes, especialmente os que enfrentam maiores dificuldades, reduzindo a taxa de evasão.
- Valoriza tecnologias que permitam aos professores agir com mais precisão e empatia.

 **Interesses**

- Ferramentas de visualização de dados e dashboards educacionais.
- Avaliação formativa e intervenções pedagógicas personalizadas.
- Inteligência artificial aplicada à educação.
- Equidade de gênero e inclusão no ensino superior.

<div align = "center">

<sub>Figura : Persona 2</sub>

<img src = "../assets/persona2.png">

<sup>Fonte: Material produzido pelos autores (2025)</sup>

</div>

##### Persona: Juan Esteban Gómez Ríos

**Perfil**

- Nome: Juan Esteban Gómez Ríos
- Gênero: Masculino
- Idade: 18 anos
- Cidade: Bello - Antioquia, Colômbia
- Posição: Estudante de primeiro semestre no curso de Engenharia de Sistemas da Universidad EAFIT

**Biografia**

&emsp; Juan nasceu e cresceu em Bello, uma cidade próxima a Medellín. Vem de uma família de classe média-baixa, onde é o primeiro a ingressar em uma universidade particular. Sempre se destacou na escola pública por sua criatividade e curiosidade, especialmente em áreas como matemática e informática, onde aprendeu programação básica por conta própria através de vídeos no YouTube.

&emsp; Ingressar na Universidad EAFIT foi um grande sonho realizado, mas o choque com a metodologia, o volume de conteúdo e a linguagem acadêmica mais formal têm representado grandes desafios. Juan trabalha meio período em uma loja para ajudar nas despesas e, por isso, nem sempre consegue dedicar o tempo ideal aos estudos. Mesmo esforçado, suas notas nos primeiros quizzes e avaliações foram baixas, o que começou a impactar sua motivação.

**Frustrações**

- Sente que estuda muito, mas não vê resultado nas notas.
- Tem dificuldades em organizar o tempo entre trabalho, estudo e tarefas da universidade.
- Acredita que falta suporte ou acompanhamento mais próximo dos professores para lidar com suas dificuldades.
- Não entende bem por que está indo mal: se é falta de base, cansaço ou desorganização.
- Tem receio de reprovar logo no primeiro semestre e decepcionar sua família.

**Motivações**

- Quer ser um exemplo positivo para seus irmãos mais novos e mostrar que é possível vencer pelos estudos.
- Sonha em trabalhar com tecnologia e desenvolvimento de software, talvez até criar sua própria startup.
- Gosta de aprender e se desenvolver, principalmente em temas práticos e aplicados.
- Quer provar para si mesmo que é capaz de se adaptar à universidade e ter sucesso.
- Valoriza professores que explicam com empatia e clareza, e se sente mais seguro quando percebe que está sendo acompanhado.

**Interesses**

- Desenvolvimento web e mobile.
- Jogos digitais e cultura geek.
- Comunidades de aprendizado online (como YouTube, Discord e fóruns de programação).
- Tecnologias acessíveis e que ajudam a estudar de forma independente.
- Bolsas de estudo e oportunidades extracurriculares que possam melhorar sua formação.

<div align = "center">

<sub>Figura : Persona 3</sub>

<img src = "../assets/persona3.png">

<sup>Fonte: Material produzido pelos autores (2025)</sup>

</div>

##### Persona: Ricardo Morales

**Perfil**

- Nome: Dr. Ricardo Morales
- Gênero: Masculino
- Idade: 55 anos
- Cidade: Medellín, Colômbia
- Posição: Diretor da Faculdade de Ciências e Engenharia na Universidad EAFIT

**Biografia**

&emsp; Ricardo nasceu em Bogotá e desde cedo demonstrou paixão por educação e tecnologia. Formou-se em Engenharia de Sistemas na Universidad Nacional da Colômbia e concluiu mestrado e doutorado em Inovação Educacional no MIT. Iniciou sua carreira como professor de algoritmos antes de assumir cargos de liderança acadêmica. Hoje, como diretor, busca integrar soluções baseadas em dados para melhorar o desempenho estudantil e reduzir a evasão.

**Frustrações**

- Possuímos dados históricos, mas não os aplicamos de forma preventiva.
- Intervimos apenas quando a reprovação já é inevitável.
- Parte do corpo docente ainda prioriza intuição em detrimento de evidências.

**Motivações**

- Transformar a EAFIT em referência em learning analytics na América Latina.
- Reduzir a taxa de reprovação em 25% nos próximos 3 anos.
- Criar um modelo replicável para outras disciplinas e instituições.

**Interesses**

- Educação.
- Estatística.

#### 4.1.7. Jornadas do Usuário

&nbsp; O mapeamento das jornadas dos usuários é fundamental para compreender como diferentes atores (professores, gestores e estudantes) interagem com o modelo preditivo e quais são as suas necessidades, emoções e oportunidades em cada etapa. Segundo Cooper et al. (2014), ao representar as experiências e necessidades do usuário em forma de jornada, é possível estruturar de maneira cronológica as atividades, emoções e pontos de contato, possibilitando um desenho de soluções mais eficaz e centrado no usuário. Detalhamos abaixo as jornadas de três personas centrais do projeto: **Paola Andrea Vallejo Ramírez (docente/coordenadora)**, **Dr. Ricardo Morales (diretor)** e **Juan Esteban Gómez Ríos (estudante)**.

---

##### Jornada da Persona 1: Paola Andrea Vallejo Ramírez (Docente/Coordenadora)

&emsp; **Cenário:** Utilização do modelo preditivo para identificar alunos em risco e planejar intervenções pedagógicas eficientes.

- **Atividades:** Analisa notas e frequência manualmente; identifica alunos com baixo desempenho; cria grupos de monitoria; oferece suporte individual ou em grupo; sugere atividades de reforço; acompanha evolução das notas.
- **Necessidades:** Ferramentas que automatizem a análise de dados; visão rápida de desempenho; informações claras sobre fatores de risco; priorização de alunos que precisam de mais ajuda; feedback sobre a eficácia das intervenções.
- **Emoções:** Frustração ao atuar de forma reativa; preocupação sobre eficácia das intervenções; esperança e alívio ao ver melhoras nas notas.
- **Oportunidades:** Alertas proativos sobre alunos em risco; insights sobre motivos do risco; classificação por faixas de risco; relatórios periódicos para medir impacto das ações pedagógicas.

<div align="center">
   <sub>Figura - Jornada da Persona Paola Andrea Vallejo Ramírez</sub>
   <img src="../assets/Paola Andrea Vallejo Ramírez uj.png">
   <sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

---

##### Jornada da Persona 2: Dr. Ricardo Morales (Diretor)

&emsp; **Cenário:** Avaliação estratégica e tomada de decisão sobre a continuidade e expansão do modelo preditivo.

- **Atividades:** Analisa relatórios de desempenho e evasão; define metas e KPIs; recebe relatórios periódicos; participa de reuniões com equipe pedagógica; decide sobre manutenção ou expansão do projeto; apresenta resultados para stakeholders.
- **Necessidades:** Dados claros sobre ROI; métricas de sucesso alinhadas a objetivos institucionais; evidências concretas de que a solução funciona; projeções de impacto da expansão.
- **Emoções:** Inquietação pela falta de dados preventivos; curiosidade e avaliação crítica diante dos relatórios; satisfação com resultados positivos e sensação de liderança.
- **Oportunidades:** Relatórios executivos sobre impacto da solução; dashboards consolidados comparando dados históricos; simulações de impacto em outras disciplinas; manuais de replicabilidade.

<div align="center">
   <sub>Figura - Jornada da Persona Dr. Ricardo Morales</sub>
   <img src="../assets/Dr. Ricardo Morales uj.png">
   <sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

---

##### Jornada da Persona 3: Juan Esteban Gómez Ríos (Estudante)

&emsp; **Cenário:** Experiência como estudante em risco de reprovação e recebimento de suporte baseado no modelo preditivo.

- **Atividades:** Assiste às aulas; recebe notas baixas nos quizzes; sente esforço insuficiente; recebe suporte do professor; aplica orientações recebidas; dedica mais tempo aos estudos.
- **Necessidades:** Clareza sobre expectativas da disciplina; ajuda para entender notas baixas; suporte empático de professores; feedback personalizado; motivação e confiança.
- **Emoções:** Ansiedade e esperança no início; frustração e insegurança ao receber notas baixas; alívio e motivação ao receber suporte; orgulho e confiança ao ver progresso.
- **Oportunidades:** Sistema de boas-vindas com dicas personalizadas; notificações automáticas alertando risco; relatórios com insights para professores; gamificação com medidores de progresso.

<div align="center">
   <sub>Figura - Jornada da Persona Juan Esteban Gómez Ríos</sub>
   <img src="../assets/Juan Esteban Gómez Ríos uj.png">
   <sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

---

&nbsp;A análise conjunta das jornadas de **Paola Andrea Vallejo Ramírez (docente/coordenadora)**, **Dr. Ricardo Morales (diretor)** e **Juan Esteban Gómez Ríos (estudante)** evidencia como o modelo preditivo se conecta de maneira complementar aos diferentes níveis da comunidade acadêmica. Enquanto para o **estudante** o foco está em apoio personalizado, motivação e superação de dificuldades, para a **docente** a ênfase recai sobre ferramentas práticas de análise, priorização de alunos em risco e feedback sobre intervenções. Já o **gestor** necessita de dados consolidados, projeções estratégicas e métricas de impacto que sustentem decisões institucionais.

&nbsp;Assim, percebe-se que as jornadas, apesar de distintas, são interdependentes: a motivação e o progresso do aluno alimentam os indicadores analisados pela professora; esses dados, por sua vez, são consolidados em relatórios que oferecem ao diretor uma visão estratégica da efetividade da solução. Essa correlação cria um **ciclo virtuoso de informação**, no qual cada persona se beneficia de forma diferenciada, mas convergente, reforçando o alinhamento entre **ações pedagógicas, suporte individualizado e decisões estratégicas**.

&nbsp;Portanto, as jornadas não devem ser vistas isoladamente, mas como partes de um ecossistema de inovação educacional, no qual o modelo preditivo atua como elo central entre experiência do aluno, prática docente e gestão institucional.


#### 4.1.8 Política de Privacidade

##### **Modelo de Política de Privacidade:**

&emsp; A Política de Privacidade é um documento que tem como objetivo informar de forma clara e transparente como uma organização realiza a coleta, o uso, o armazenamento e a proteção dos dados pessoais de seus usuários. No Brasil, esse processo deve estar em conformidade com a Lei Geral de Proteção de Dados Pessoais (LGPD), em vigor desde 2020. A LGPD estabelece regras e princípios para o tratamento de dados, garantindo os direitos dos titulares e promovendo práticas seguras, éticas e responsáveis por parte das instituições.

##### **Projeto Latech**

- **Informações Gerais:** Esta política de privacidade informa como o projeto Latech, desenvolvido pelo grupo Throxy, trata os dados pessoais coletados durante o uso da solução. Está em conformidade com a Lei nº 13.709/2018 - LGPD.<br>

- **Dados Coletados**<br>
   1- *Dados fornecidos diretamente:* Gênero, Faixa etária e Programa Acadêmico.<br>
   2- *Dados coletados automaticamente:* Notas dos quizzes, provas e projetos realizados no curso<br>

- **Finalidade do Tratamento:** A finalidade do tratamento é analisar e encontrar alunos que estão com probabilidade de serem reprovados para que sejam introduzidos em um programa de ajuda com o objetivo de aumentar a taxa de aprovação dos alunos.<br>

- **Armazenamento e Retenção**<br>
   1- *Local:* Arquivo Excel<br>
   2- *Prazo:* 10 semanas<br>

- **Compartilhamento de Dados:** Parceiros técnicos, Fornecedores dos dados.<br>

- **Segurança dos Dados:** Todos os dados pessoais coletados são armazenados com técnicas de segurança da informação, incluindo criptografia em repouso (AES-256) e em trânsito (TLS), além de controles de acesso e autenticação. Quando armazenados localmente, os arquivos são protegidos por criptografia de disco e acesso restrito.<br>

- **Direitos dos Titulares:** Acesso, correção, exclusão, revogação de consentimento

- **Solicitações via e-mail:** lgonzalez8@eafit.edu.co

- **Encarregado de Dados (DPO):**<br>
   1- *Nome:* Paola Vallejo<br>
   2- *E-mail:* pvallej3@eafit.edu.co<br>

##### **Política de Privacidade na Colômbia**

&emsp; Na Colômbia, a Lei sobre proteção de dados é a Lei Estatutária 1581 de 2012. Sancionada em 2017, ela visa garantir o direito constitucional à retificação e atualização de dados que cosntem em vases de dados ou arquivos, conforme os artigos 15(direito ao habeas data) e 20(direito à informação) da Constituição Política colombiana. Entrou em vigor em 27 de junho de 2013, por meio do Decreto 1377 de 2013

### 4.2. Compreensão dos Dados
&emsp; Esta seção tem como objetivo compreender todo o processo de entendimento dos dados do projeto. Esse processo representa o primeiro contato dos integrantes do grupo com os dados fornecidos pela empresa parceira. Trata-se de um momento destinado a analisar a estrutura e a composição desses dados, por meio de consultas, aplicação de métodos de estatística descritiva, identificação de colunas numéricas e categóricas, além da realização de etapas de pré-processamento, normalização e limpeza dos dados disponibilizados.

#### 4.2.1. Exploração de dados
Esta etapa inicial marca o primeiro contato com os dados, sendo responsável pela análise preliminar e pela identificação dos tipos de variáveis que compõem a base. A partir dessa exploração, torna-se possível compreender melhor a natureza das informações disponíveis e orientar as próximas etapas de preparação e tratamento.
  A base de dados contém informações de alunos matriculados em um curso de Pensamento Computacional da Universidade EAFIT e apresenta as seguintes features:

<div align = "center">

<sub>Tabela : Classificações das variáveis</sub>

<table align="center">

| Variável | Descrição | Tipo de Variável |
|:-----:|:-----:|:-----:|
| **Período** | Indica o turno do curso (manhã/tarde/noite). | Categórica |
| **Grupo** | Identificação da turma ou grupo de alunos. | Categórica |
| **Horário** | Hora da aula (valor inteiro). | Numérica discreta |
| **Tipo\_Documento** | Tipo de documento de identificação do aluno. | Categórica |
| **Idade** | Idade do aluno em anos | Numérica discreta |
| **Gênero** | Sexo/gênero do aluno. | Categórica |
| **Nome\_Programa\_Acadêmico** | Nome do programa/curso acadêmico do aluno. | Categórica |
| **STEM** | Indica se o curso é da área STEM (Sim/Não). | Categórica binária |
| **Parcial\_1** | Nota do aluno na primeira avaliação parcial. | Numérica contínua |
| **Parcial\_2** | Nota do aluno na segunda avaliação parcial. | Numérica contínua |
| **Projeto\_Parte1** | Nota do primeiro projeto. | Numérica contínua |
| **Projeto\_Parte2** | Nota do segundo projeto. | Numérica contínua |
| **Taller** | Nota obtida em atividades práticas. | Numérica contínua |
| **Quizzes** | Nota agregada dos quizzes. | Numérica contínua |
| **Fecha\_Quiz1** | Data de realização do Quiz 1\. | Temporal (Data) |
| **Quiz1** | Nota obtida no Quiz 1\. | Numérica contínua |
| **TempoQ1** | Tempo gasto no Quiz 1 (em minutos/segundos). | Numérica contínua |
| **Fecha\_Quiz2** | Data de realização do Quiz 2\. | Temporal (Data) |
| **Quiz2** | Nota obtida no Quiz 2\. | Numérica contínua |
| **TempoQ2** | Tempo gasto no Quiz 2\. | Numérica contínua |
| **Fecha\_Quiz3** | Data de realização do Quiz 3\. | Temporal (Data) |
| **Quiz3** | Nota obtida no Quiz 3\. | Numérica contínua |
| **TempoQ3** | Tempo gasto no Quiz 3\. | Numérica contínua |
| **Fecha\_Quiz4** | Data de realização do Quiz 4\. | Temporal (Data) |
| **Quiz4** | Nota obtida no Quiz 4\. | Numérica contínua |
| **TempoQ4** | Tempo gasto no Quiz 4\. | Numérica contínua |
| **Fecha\_Quiz5** | Data de realização do Quiz 5\. | Temporal (Data) |
| **Quiz5** | Nota obtida no Quiz 5\. | Numérica contínua |
| **TempoQ5** | Tempo gasto no Quiz 5\. | Numérica contínua |
| **Fecha\_Quiz6** | Data de realização do Quiz 6\. | Temporal (Data) |
| **Quiz6** | Nota obtida no Quiz 6\. | Numérica contínua |
| **TempoQ6** | Tempo gasto no Quiz 6\. | Numérica contínua |
| **Fecha\_Quiz7** | Data de realização do Quiz 7\. | Temporal (Data) |
| **Quiz7** | Nota obtida no Quiz 7\. | Numérica contínua |
| **TempoQ7** | Tempo gasto no Quiz 7\. | Numérica contínua |
| **Quiz8** | Nota obtida no Quiz 8\. | Numérica contínua |
| **CalcNotaQuiz** | Cálculo agregado da nota de quizzes. | Numérica contínua |
| **MelhoraNotaQuizzes** | Indicador se houve melhora nos quizzes. | Categórica binária |
| **Quanto melhora?** | Valor quantitativo da melhora nas notas. | Numérica contínua |
| **Qualificação\_Oficial** | Nota oficial final do curso. | Numérica contínua |
| **Aprovo** | Indica se o aluno foi aprovado (Sim/Não). | Categórica binária |

</table>

<sup>Fonte: Material produzido pelos autores (2025)</sup>

</div>

#### 4.2.2. Pré-processamento

&emsp; Antes da etapa de modelagem, é essencial realizar um rigoroso pré-processamento dos dados. Segundo Silva, Peres e Boscarioli (2016), esta fase é fundamental para garantir a integridade e a qualidade do dataset, mitigando o risco de conclusões preciptadas ou de baixa performance do modelo. O objetivo deste processo é transformar os dados brutos — marcados por inconsistências, erros de formatação e ruídos — em um conjunto de dados limpo, padronizado e estruturado, prontos para serem aplicados no treinamento do modelo.

&emsp; Para alcançar tal objetivo, foi desenvolvido um conjunto de funções utilitárias, organizadas em um pipeline sequencial. As seções a seguir detalham cada uma dessas funções e a lógica de sua execução:

##### 4.2.2.1. Funções Utilitárias

&emsp; A seguir, são apresentadas as funções desenvolvidas para a limpeza, padronização e tratamento do dataset.

- **Detecção e Padronização de Erros**

&emsp; A análise exploratória inicial identificou a presença de múltiplos tokens de erro provenientes do google planilhas que atrapalham a análise dos dados. A função replace_excel_errors foi criada para resolver este problema, substituindo todas as ocorrências desses tokens pelo valor nulo do NumPy, o numpy.nan:

```python

def replace_excel_errors(df, cols=None):
    df = df.copy()
    if cols is None:
        cols = df.select_dtypes(include="object").columns.tolist()
    for c in cols:
        if c in df.columns:
            df[c] = df[c].replace(list(ERROR_TOKENS), np.nan)
    return df

```

- **Tradução e Padronização de Conteúdo**

&emsp; Para melhorar a interpretação dos dados durante o processo de desenvolvimento do modelo, foi necessário traduzir os nomes das colunas e padronizar os valores categóricos. A função padroniza_df centraliza essas operações. Além de renomear as colunas para o português (conforme rename_map), a função aplica mapeamentos específicos para corrigir os dados com diversas variantes em colunas críticas como Aprovou, Genero e STEM, que continha múltiplas representações para a mesma informação booleana. Essa padronização é vital para a construção do modelo e treinamento dele. Todo esse processo ocorreu da seguinte maneira:


```python

def padroniza_df(df):
    df = df.copy().rename(columns=rename_map)
    df = replace_excel_errors(df)
    if "Nome_Programa_Academico" in df.columns:
        df["Nome_Programa_Academico"] = (
            df["Nome_Programa_Academico"].astype(str).str.strip().replace(MAPA_PROGRAMAS, regex=False)
        )
    if "Aprovou" in df.columns:
        df["Aprovou"] = df["Aprovou"].astype(str).str.strip().replace(MAPA_APROV, regex=False)
    if "Idade" in df.columns:
        df["Idade"] = df["Idade"].astype(str).str.strip().replace(MAPA_IDADE, regex=False)
    if "Genero" in df.columns:
        df["Genero"] = df["Genero"].astype(str).str.strip().replace(MAPA_GENERO, regex=False)
    if "STEM" in df.columns:
        mask = df["STEM"].notna()
        if mask.any():
            df.loc[mask, "STEM"] = df.loc[mask, "STEM"].astype(str).str.strip().replace(MAPA_STEM, regex=False)
    return df

```

- **Normalização de Variáveis Temporais**

&emsp; As colunas que registram o tempo de execução dos quizzes (TempoQ) foram disponibilizado com unidades de tempo e outros caracteres que não são interpretados corretamente pelo modelo, para isso foi desenvolvida a função parse_to_seconds. Utilizando expressões regulares e lógica condicional, função transforma esses dados irregulares na quantidade de segundos correspondente. A função converte_colunas_tempo aplica essa transformação a todas as colunas de tempo relevantes, da seguinte maneira:

```python

_PATTERN_TEMPO = re.compile(
    r"^\s*(?:(\d+)\s*minuto(?:s)?)?\s*(?:(\d+)\s*segundo(?:s)?)?\s*$",
    re.IGNORECASE
)

def parse_to_seconds(val):
    if pd.isna(val):
        return np.nan
    if isinstance(val, (int, float)) and not isinstance(val, bool):
        try:
            return int(val)
        except Exception:
            return np.nan
    if isinstance(val, str):
        s = val.strip()
        try:
            return int(float(s))
        except Exception:
            pass
        s_norm = s.replace(" e ", " ").replace(",", " ")
        m = _PATTERN_TEMPO.match(s_norm)
        if m:
            mins, secs = m.group(1), m.group(2)
            total = (int(mins) * 60 if mins else 0) + (int(secs) if secs else 0)
            return total if (mins or secs) else np.nan
        if ":" in s_norm:
            parts = [p.strip() for p in s_norm.split(":")]
            if len(parts) == 2 and all(p.isdigit() for p in parts):
                mm, ss = map(int, parts)
                return mm * 60 + ss
            if len(parts) == 3 and all(p.isdigit() for p in parts):
                hh, mm, ss = map(int, parts)
                return hh * 3600 + mm * 60 + ss
    return np.nan

def converte_colunas_tempo(df):
    df = df.copy()
    cols_tempo = [c for c in df.columns if re.match(r"^(TempoQ|TiempoQ)\d+$", c)]
    for col in cols_tempo:
        df[col] = df[col].apply(parse_to_seconds)
    return df

```

- **Filtragem de Dados de Alunos Ausentes**

&emsp; Para o objetivo do modelo, os alunos faltantes atrapalham na predição do modelo. A função filtra_alunos_presentes implementa essa regra de negócio. Ela identifica os alunos para os quais todas as colunas de data de  entrega de quizzes são nulas e remove esses registros do dataset. A ausência total de datas de entrega indica que o aluno faltou durante a aplicação das atividades avaliativas. Após a filtragem, as próprias colunas de data são removidas, da seguinte forma:

```python

# Remove os alunos faltantes
def filtra_alunos_presentes(df):
    df = df.copy()
    cols_data = [c for c in df.columns if re.match(r"^(Data_Quiz|Fecha_Quiz)\d+$", c)]
    if not cols_data:
        return df
    df_filtrado = df.dropna(subset=cols_data, how="all")
    df_filtrado = df_filtrado.drop(columns=cols_data)
    return df_filtrado

```

- **Identificação e Tratamento de Outliers**

&emsp; A presença de outliers em variáveis numéricas pode impactar negativamente o desempenho do modelo preditivo. A função remove_outliers foi projetada para identificar e mitigar esses valores extremos. A identificação é feita pelo método de Tukey, que utiliza o Intervalo Interquartil (IQR) para definir limites estatísticos. Para o tratamento, optou-se pela técnica de clipping, que substitui os outliers pelo valor do limite mais próximo (inferior ou superior). Essa abordagem tem a vantagem de reduzir a influência dos valores extremos sem descartar o registro inteiro, preservando as informações contidas nas outras features daquela observação. A função também gera visualizações de boxplots antes e depois do tratamento, permitindo uma validação visual da eficácia do processo.

```python

def remove_outliers(df, n_cols_per_row=3):
    df_numeric = df.select_dtypes(include=["number"])
    df_numeric = df_numeric.drop(columns=["Grupo"], errors="ignore")  # evita erro se não existir

    n_cols = len(df_numeric.columns)
    n_rows = math.ceil(n_cols / n_cols_per_row)

    # Boxplots originais
    fig, axes = plt.subplots(n_rows, n_cols_per_row, figsize=(6*n_cols_per_row, 4*n_rows))
    axes = axes.flatten()
    for i, col in enumerate(df_numeric.columns):
        sns.boxplot(x=df_numeric[col], ax=axes[i])
        axes[i].set_title(f"Boxplot - {col}")
    # remover eixos vazios
    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])
    plt.tight_layout()
    plt.show()

    # Normalizar os outliers (clip)
    for col in df_numeric.columns:
        Q1 = df_numeric[col].quantile(0.25)
        Q3 = df_numeric[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        df_numeric[col] = df_numeric[col].clip(lower, upper)

    # Boxplots limpos
    fig, axes = plt.subplots(n_rows, n_cols_per_row, figsize=(6*n_cols_per_row, 4*n_rows))
    axes = axes.flatten()
    for i, col in enumerate(df_numeric.columns):
        sns.boxplot(x=df_numeric[col], ax=axes[i])
        axes[i].set_title(f"Boxplot cleaned - {col}")
    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])
    plt.tight_layout()
    plt.show()

    return df_numeric

```

- **Codificação de Variáveis Categóricas**

&emsp; Como etapa final, as variáveis categóricas restantes foram transformadas em um formato numérico que pode ser processado pelo modelo, utilizando a técnica de One-Hot Encoding. A implementação foi segregada em duas funções (fit_onehot_encoder e aplica_onehot). O encoder é "treinado" (fit) apenas uma vez no conjunto de dados principal. A transformação (aplica) pode então ser consistentemente aplicada a qualquer novo conjunto de dados (como dados de teste ou validação). A implementação também trata explicitamente valores ausentes, criando uma categoria "MISSING", o que permite ao modelo aprender padrões a partir da própria ausência de dados.

```python

def fit_onehot_encoder(df_cat, cat_cols):
    cat_cols_exist = [c for c in cat_cols if c in df_cat.columns]
    if not cat_cols_exist:
        return {"type": "none", "encoder": None, "columns": [], "cat_cols": []}
    X_fit = replace_excel_errors(df_cat[cat_cols_exist].copy(), cols=cat_cols_exist)
    X_fit = X_fit.fillna("MISSING").astype(str)
    try:
        from sklearn.preprocessing import OneHotEncoder
        try:
            enc = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
        except TypeError:
            enc = OneHotEncoder(sparse=False, handle_unknown="ignore")
        enc.fit(X_fit)
        cols = list(enc.get_feature_names_out(cat_cols_exist))
        return {"type": "sklearn", "encoder": enc, "columns": cols, "cat_cols": cat_cols_exist}
    except Exception:
        dummies = pd.get_dummies(X_fit, prefix=cat_cols_exist, dummy_na=False)
        cols = dummies.columns.tolist()
        return {"type": "pandas", "encoder": cols, "columns": cols, "cat_cols": cat_cols_exist}

def aplica_onehot(df, encoder_info):
    df = df.copy()
    if encoder_info["type"] == "none":
        return df
    cat_cols_exist = encoder_info["cat_cols"]
    X = replace_excel_errors(df[cat_cols_exist].copy(), cols=cat_cols_exist).fillna("MISSING").astype(str)
    if encoder_info["type"] == "sklearn":
        arr = encoder_info["encoder"].transform(X)
        encoded_df = pd.DataFrame(arr, columns=encoder_info["columns"], index=df.index)
        out = pd.concat([df.drop(columns=cat_cols_exist), encoded_df], axis=1)
    else:
        dummies_df = pd.get_dummies(X, prefix=cat_cols_exist, dummy_na=False)
        all_cols = encoder_info["columns"]
        for c in all_cols:
            if c not in dummies_df.columns:
                dummies_df[c] = 0
        dummies_df = dummies_df[all_cols]
        out = pd.concat([df.drop(columns=cat_cols_exist), dummies_df], axis=1)
    bad_cols = [c for c in out.columns if "#ERROR!" in c]
    if bad_cols:
        out = out.drop(columns=bad_cols)
    return out

```

##### 4.2.2.2. Pipeline de Execução do Pré-processamento
 
&emsp; As funções utilitárias foram integradas em um pipeline sequencial para processar os dados brutos. O processo inicia-se com o carregamento dos datasets. Em seguida, a função padroniza_df é aplicada para realizar a tradução, padronização e limpeza inicial. As colunas de tempo são normalizadas para segundos. Após isso, os alunos ausentes são filtrados com base na ausência de entregas. Após a concatenação dos datasets, a função remove_outliers trata os valores extremos nas features numéricas. Por fim, as variáveis categóricas são transformadas via One-Hot Encoding, resultando no dataframe final, pronto para a modelagem.

```python

# 1) Carregar Excel
df1_raw = pd.read_excel(XLSX1_PATH, sheet_name=SHEET_INDEX)
df2_raw = pd.read_excel(XLSX2_PATH, sheet_name=SHEET_INDEX)

# 2) Padronizar valores/nomes
df1 = padroniza_df(df1_raw)
df2 = padroniza_df(df2_raw)

# 3) Converter tempos para segundos
df1 = converte_colunas_tempo(df1)
df2 = converte_colunas_tempo(df2)

# 4) Filtrar apenas alunos com algum quiz e remover colunas de datas
df1_presentes = filtra_alunos_presentes(df1)
df2_presentes = filtra_alunos_presentes(df2)

# 5) Concatenar
df_consolidado = pd.concat([df1_presentes, df2_presentes], ignore_index=True)

# 5.1) Limpar outliers das colunas numéricas
df_numeric_clean = remove_outliers(df_consolidado)  # faz clip nos outliers
# Substituir as colunas numéricas no df_consolidado
df_consolidado[df_numeric_clean.columns] = df_numeric_clean

# 6) Remover linhas com STEM ausente, replicando lógica original
if "STEM" in df_consolidado.columns:
    df_consolidado = df_consolidado.dropna(subset=["STEM"])

# 7) One-Hot
cat_cols = ["Tipo_Documento", "Idade", "Genero", "STEM", "MelhoraNotaQuizzes", "Aprovou"]
encoder_info = fit_onehot_encoder(df_consolidado, cat_cols)
df_onehot = aplica_onehot(df_consolidado, encoder_info)

```

&emsp; Ao final deste pipeline, o dataframe está devidamente processado e preparado para a próxima fase do projeto, a análise de hipóteses formulada conforme descrito na seção 4.2.3.

#### 4.2.3. Hipóteses

&emsp; A etapa de verificação de hipóteses é um pilar no processo de mineração de dados. Conforme destacam Silva, Peres e Boscarioli (2016), a qualidade do resultado da modelagem está diretamente ligada à compreensão das características e da distribuição dos dados de entrada. Nesse contexto, a construção de um modelo preditivo robusto exige que os pressupostos dos algoritmos sejam validados. Muitos modelos, especialmente os paramétricos como a regressão linear, partem da suposição de que as variáveis seguem uma distribuição normal, e ignorar essa premissa pode levar a inferências incorretas e a decisões de negócio equivocadas.

&emsp; A hipótese central investigada nesta análise é se as principais variáveis quantitativas do projeto seguem uma distribuição normal. Esta verificação é crucial, pois o resultado orienta diretamente as etapas seguintes do projeto, incluindo:

1.  A escolha entre testes estatísticos **paramétricos** (que assumem normalidade) e **não-paramétricos** (que não possuem tal premissa).
2.  A necessidade de aplicar **técnicas de transformação** de dados para normalizar variáveis assimétricas.
3.  A seleção de **métodos de escalonamento** e tratamento de *outliers*, visto que modelos baseados em distância (como SVM e K-Means) são sensíveis à escala e à distribuição dos dados.

&emsp; A seguir, detalhamos o teste dessa hipótese para as três variáveis selecionadas.

##### 4.2.3.1. Teste de Normalidade para a variável `CalcNotaQuiz`

* **Hipótese:** A variável `CalcNotaQuiz`, que representa o número de itens adquiridos em cada transação, segue uma distribuição normal. A suposição inicial seria que a maioria das transações se concentraria em torno de uma média, com menos transações contendo muito poucos ou muitos itens.
* **Implementação e Análise:** Para validar essa hipótese, foi aplicado o teste de aderência de Shapiro-Wilk, um método estatístico robusto para verificação de normalidade. No notebook do projeto, o teste foi executado utilizando a biblioteca `scipy.stats`, conforme o código apresentado. O resultado obtido foi um **p-valor de 5.73e-27**.

    ```python
        # Testando normalidade para "CalcNotaQuiz" via Shapiro-Wilk
        from scipy.stats import shapiro

        dados = df_consolidado['CalcNotaQuiz'].dropna()
        stat, p = shapiro(dados)

        print('H0: Os dados seguem uma distribuição normal')
        print('H1: Os dados não seguem uma distribuição normal')
        print("Estatística W:", stat)
        print("p-valor:", p)

        if p > 0.05:
            print("Não rejeitamos H0: os dados seguem uma distribuição normal.")
        else:
            print("Rejeitamos H0: os dados não seguem uma distribuição normal.")

        # Saída:
        # H0: Os dados seguem uma distribuição normal
        # H1: Os dados não seguem uma distribuição normal
        # Estatística W: 0.9158549463812558
        # p-valor: 5.737420736467878e-27
        # Rejeitamos H0: os dados não seguem uma distribuição normal.
    ```

* **Conclusão:** Como o p-valor é significativamente menor que o nível de significância padrão de 0,05, a hipótese nula de normalidade (H₀) é **rejeitada**. Isso indica que há evidência estatística forte para afirmar que os dados de `CalcNotaQuiz` não seguem uma distribuição normal.

##### 4.2.3.2. Teste de Normalidade para a variável `Talleres`

* **Hipótese:** A variável `Talleres`, referente à nota de trabalhos complementares, segue uma distribuição normal. A expectativa seria que as notas se distribuíssem simetricamente em torno de uma média central.
* **Implementação e Análise:** Assim como na variável anterior, o código no notebook aplicou o teste de Shapiro-Wilk sobre os dados da variável `Talleres` (referenciada como `Oficinas` no código). O teste gerou um **p-valor de 3.38e-39**.

    ```python
        # Testando normalidade para "Oficinas" (Talleres) via Shapiro-Wilk
        from scipy.stats import shapiro

        dados = df_consolidado['Oficinas'].dropna()
        stat, p = shapiro(dados)

        print('H0: Os dados seguem uma distribuição normal')
        print('H1: Os dados não seguem uma distribuição normal')
        print("Estatística W:", stat)
        print("p-valor:", p)

        if p > 0.05:
            print("Não rejeitamos H0: os dados seguem uma distribuição normal.")
        else:
            print("Rejeitamos H0: os dados não seguem uma distribuição normal.")

        # Saída:
        # H0: Os dados seguem uma distribuição normal
        # H1: Os dados não seguem uma distribuição normal
        # Estatística W: 0.7847014498757214
        # p-valor: 3.386401173855684e-39
        # Rejeitamos H0: os dados não seguem uma distribuição normal.
    ```

* **Conclusão:** O p-valor extremamente baixo leva à **rejeição** da hipótese nula (H₀). Fica evidente que a distribuição das notas de `Talleres` também desvia significativamente da normalidade.

#### 4.2.3.3. Teste de Normalidade para a variável `Calificación_Oficial`

* **Hipótese:** A variável `Nota_Oficial`, que representa o custo de produção dos produtos, segue uma distribuição normal. A premissa seria que a maioria dos produtos teria um custo próximo da média, com menos produtos sendo extremamente baratos ou caros para produzir.
* **Implementação e Análise:** O mesmo procedimento foi repetido para a variável `Nota_Oficial`. A execução do código de teste de Shapiro-Wilk, conforme documentado no notebook, também resultou em um p-valor muito baixo (inferior a 0,05).

    ```python
        # Testando normalidade para "Nota_Oficial" (Calificación_Oficial) via Shapiro-Wilk
        from scipy.stats import shapiro

        dados = df_consolidado['Nota_Oficial'].dropna()
        stat, p = shapiro(dados)

        print('H0: Os dados seguem uma distribuição normal')
        print('H1: Os dados não seguem uma distribuição normal')
        print("Estatística W:", stat)
        print("p-valor:", p)

        if p > 0.05:
            print("Não rejeitamos H0: os dados seguem uma distribuição normal.")
        else:
            print("Rejeitamos H0: os dados não seguem uma distribuição normal.")
    ```

* **Conclusão:** A execução do teste, assim como nos casos anteriores, resultou em um p-valor muito baixo (inferior a 0,05), levando à **rejeição** da hipótese de normalidade para a `Nota_Oficial`.
* **Conclusão:** Assim como as demais, a hipótese de normalidade para a `Nota_Oficial` é **rejeitada**.

### 4.2.3.4. Implicações dos Resultados

&emsp; A refutação da hipótese de normalidade para todas as três variáveis chave é um resultado de grande impacto para o projeto. Fica claro que a utilização direta de modelos e testes paramétricos seria inadequada e poderia comprometer a validade das conclusões. Dessa forma, a análise dessas hipóteses nos força a tomar decisões mais informadas na próxima fase, como a aplicação de transformações matemáticas (ex: logarítmica) para tentar normalizar os dados ou, alternativamente, a adoção de algoritmos não-paramétricos, que são mais flexíveis quanto à distribuição dos dados de entrada.

### 4.3. Preparação dos Dados e Modelagem

> Aviso de confidencialidade: os dados institucionais utilizados são confidenciais e foram disponibilizados exclusivamente para fins acadêmicos mediante acordo com a Universidad EAFIT. Nenhuma amostra individual, linha ou arquivo bruto será exibido neste documento. As referências a variáveis e procedimentos são descritivas e não expõem conteúdo sensível.

Nesta seção, será apresentado o processo de preparação dos dados para a construção do nosso modelo supervisionado de risco acadêmico. O primeiro passo consiste na escolha das features e suas justificativas, seguido pela organização dos dados em conjuntos de treinamento, validação e teste.

#### 4.3.1. Justificativa das features

&emsp;A partir da análise das colunas disponíveis (Seção 4.2), foram selecionadas features que capturam desempenho, esforço/tempo, evolução e contexto acadêmico, pois estão diretamente relacionadas à probabilidade de aprovação.

&emsp; As avaliações formais — `Parcial_1`, `Parcial_2`, `Projeto_Parte1`, `Projeto_Parte2`, `Oficinas` e `Quizzes` — refletem o aprendizado acumulado do estudante e, por isso, constituem o núcleo das variáveis explicativas. Diferenças entre primeiras e segundas avaliações sinalizam evolução ou retração ao longo do período, oferecendo indícios precoces de risco que podem subsidiar intervenções pedagógicas antes do fechamento das notas.

&emsp; Os quizzes individuais (`Quiz1`–`Quiz8`) adicionam granularidade temporal. A observação de picos e quedas entre semanas permite construir indicadores de estabilidade (como o desvio padrão entre quizzes) e de tendência (como a inclinação de uma regressão simples das notas ao longo do tempo). Tais indicadores ajudam a distinguir perfis consistentes de perfis erráticos, algo crítico para antecipar situações de risco.

&emsp; O tempo de execução de cada quiz (`TempoQ1`–`TempoQ8`, convertido para segundos no pré-processamento) traz um componente de esforço e dificuldade percebida. Tempos anormalmente baixos podem sugerir respostas aleatórias; por outro lado, tempos excessivamente altos podem indicar barreiras de compreensão. Agregações como média, mediana, soma e variabilidade ao longo dos quizzes enriquecem a interpretação conjunta com as notas.

&emsp; As variáveis de evolução declarada, como `MelhoraNotaQuizzes` e `Quanto melhora?`, registram diretamente o progresso entre avaliações, contribuindo para diferenciar estudantes que respondem positivamente a monitorias e atividades de reforço daqueles que mantêm desempenho estável ou declinante.

&emsp; O contexto acadêmico — `Período`, `Grupo`, `Horário`, `Nome_Programa_Academico` e `STEM` — é incorporado para controlar efeitos de turma, turno e curso que impactam padrões de avaliação e disponibilidade de suporte. Essas variáveis serão tratadas por codificação apropriada, mitigando riscos de dominância de categorias e reduzindo a chance de sobreajuste.

&emsp; Aspectos demográficos essenciais, como `Idade` (em faixas) e `Genero`, são considerados com parcimônia e auditados quanto a viés. Caso não agreguem valor preditivo sem riscos éticos, podem ser excluídos da versão final do modelo. Quando presentes, sua utilização é acompanhada de verificações de fairness.

&emsp; Além das variáveis brutas, serão construídos atributos derivados capazes de ampliar a capacidade explicativa: estatísticas agregadas dos quizzes (média, mediana, mínimos e máximos, desvio padrão), tendências temporais, deltas entre avaliações (`Parcial_2 - Parcial_1`, `Projeto_Parte2 - Projeto_Parte1`) e interações relevantes (por exemplo, `STEM × tempo médio`, `Horário × desempenho`, `Oficinas × Quizzes`). Em paralelo, variáveis redundantes ou altamente correlacionadas serão reduzidas, favorecendo um conjunto de atributos mais parcimonioso e interpretável.

#### 4.3.2. Organização dos dados (treinamento, validação e teste)

&emsp; O problema é formulado como classificação binária, tendo `Aprovou` como alvo principal. Em análises complementares, `Nota_Oficial` pode ser modelada como regressão e posteriormente mapeada para aprovação por limiar institucional, permitindo comparar abordagens sem comprometer a interpretação final.

&emsp; Para estimar o desempenho de forma honesta e replicável, será reservado um conjunto de teste de aproximadamente 20% dos registros, estratificado por `Aprovou`, a ser utilizado apenas na avaliação final. Sobre o conjunto restante, emprega-se validação cruzada estratificada (k=5 ou k=10), que fornece métricas estáveis e reduz a variância associada a um único particionamento.

&emsp; Sempre que houver estrutura temporal clara (por exemplo, semestres distintos) ou organização por turmas, será adotada uma estratégia que evite vazamento entre treino e avaliação. Duas alternativas serão consideradas conforme a disponibilidade: separação temporal (por exemplo, utilizar 2023-1 para treino/validação e 2023-2 como teste) ou validação por grupos (GroupKFold) com chaves como `Grupo` e `Horário`. Dessa maneira, amostras muito semelhantes não aparecem simultaneamente em treino e validação.

&emsp; Todo o pré-processamento descrito na Seção 4.2 — padronização de colunas e valores, conversão dos tempos dos quizzes para segundos, filtragem de ausentes, tratamento de outliers por clipping e codificação One-Hot — ocorrerá dentro de cada fold, ajustando encoders e escalonadores exclusivamente no subconjunto de treino e aplicando-os aos subconjuntos de validação e teste. Esse procedimento evita vazamento de informação e preserva a validade das métricas obtidas.

&emsp; Na presença de desbalanceamento entre classes de aprovação, serão avaliadas técnicas como o ajuste de pesos de classe (`class_weight=balanced`) ou oversampling (por exemplo, SMOTE), sempre restritas ao subconjunto de treino. Por fim, serão fixadas sementes aleatórias nos processos de amostragem e modelagem, e os artefatos do pipeline — mapeamentos, encoders, lista final de colunas e escalonadores — serão versionados, garantindo reprodutibilidade e auditabilidade institucional.

### 4.3.3 Métricas relacionadas ao modelo

Métricas são utilizadas para avaliar o desempenho durante o desenvolvimento do modelo preditivo supervisionado.

Em cenários desbalanceados, como este (93% de aprovação e 7% de reprovação), a acurácia por si só pode ser enganosa: um modelo que sempre prevê a classe majoritária (aprovação) pode ter alta acurácia e, ainda assim, pouca utilidade prática. Métricas baseadas na matriz de confusão fornecem uma visão mais detalhada das previsões:

<div align="center">
  <sub>Figura x — Matriz de confusão do modelo Nearest Centroid na etapa 1</sub><br>
  <img src="../assets/matriz_confusão_nearestCentroid.png" alt="Matriz de confusão — Nearest Centroid (Etapa 1)"><br>
  <sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

```
            Previsto: 1     Previsto: 0
Real: 1        VP               FN
Real: 0        FP               VN
```

- Verdadeiro Positivo (VP): o modelo prevê “Reprovou” e a pessoa realmente reprovou.
- Falso Positivo (FP): o modelo prevê “Reprovou”, mas a pessoa não reprovou.
- Verdadeiro Negativo (VN): o modelo prevê “Não reprovou” e a pessoa de fato não reprovou.
- Falso Negativo (FN): o modelo prevê “Não reprovou”, mas a pessoa reprovou.

A classe positiva (“Reprovou”) é minoritária e crítica. Dessa forma, reduzir FN — isto é, evitar deixar de identificar alunos que irão reprovar — é a prioridade.

#### Métricas-chave

##### Recall
- Fórmula: Recall = VP / (VP + FN)
- Definição: proporção de positivos reais corretamente identificados.
- Interpretação: “Entre os que realmente reprovam, quantos o modelo detecta?”
- Observação: o grid search utiliza `scoring='recall'`, indicando que perder um caso de reprovação (FN) é mais custoso do que gerar um alarme a mais (FP). Assim, o modelo prioriza identificar o máximo de casos de reprovação, mesmo que isso aumente o número de alarmes falsos.

##### Precisão
- Fórmula: Precisão = VP / (VP + FP)
- Definição: proporção de positivos previstos que são de fato positivos.
- Interpretação: “Entre os marcados como reprovados, quantos realmente reprovam?”
- Observação: em dados desbalanceados, ao elevar o recall, é comum aumentar FP e reduzir a precisão. A precisão ajuda a controlar a confiabilidade das sinalizações de reprovação.

##### F1-Score
- Fórmula: F1 = 2 × (Precisão × Recall) / (Precisão + Recall)
- Definição: média harmônica entre precisão e recall.
- Interpretação: equilíbrio entre capturar a maioria dos reprovados e manter previsões positivas confiáveis.
- Observação: útil para balancear FN e FP. Como o custo de FN é maior, o recall é priorizado; ainda assim, o F1 é monitorado para evitar colapso da precisão.

---

### 4.3.4 Modelo Candidato — Nearest Centroid

#### Descrição do modelo
O Nearest Centroid (NC) é um classificador simples baseado em distância. Para cada classe, calcula-se o centróide (média dos vetores) no conjunto de treino. Uma nova amostra é atribuída à classe cujo centróide estiver mais próximo, segundo uma métrica de distância.

Foi utilizada busca em grade com validação cruzada (cv=5) para selecionar “metric” e “shrink_threshold”, otimizando por recall, dado o objetivo de reduzir falsos negativos na classe positiva (“Reprovou” = 1). O conjunto é dividido em treino e teste com `random_state=42`. O uso de SMOTE no treino foi considerado (comentado no código) em razão do desbalanceamento.

#### Resultados por pontos no tempo
- Tabela 1 (menos atributos): recall razoável/alto, porém precisão muito baixa — muitas sinalizações incorretas (FP). Com pouca informação, o NC tende a “abrir a rede” para capturar reprovados, mas gera muitos alarmes falsos.
- Tabela 2 (informação intermediária): recall muito alto, precisão ainda modesta; F1 melhora — o modelo segue eficaz em detectar reprovados, mas o custo de FP permanece relevante.
- Tabela 3 (mais atributos): recall alto e leve melhora de precisão e F1 — com mais variáveis, o NC reduz um pouco os FP, mas ainda mantém viés em favor do recall.

#### Ajuste ao desbalanceamento
O problema é desbalanceado (poucos “Reprovou”). O NC, por ser um classificador simples e otimizado por recall, favorece a classe positiva. Isso ajuda a reduzir FN, mas pode reduzir a precisão. O código prevê SMOTE no treino; sua ativação e comparação de métricas é recomendada para verificar possibilidade de ganhar recall mantendo ou melhorando precisão/F1. 

Nota breve sobre SMOTE: técnica que cria exemplos sintéticos da classe minoritária para equilibrar o treino; deve ser aplicada apenas no conjunto de treino para evitar vazamento de informação.

#### Próximos passos para o candidato
- Avaliar o efeito de SMOTE apenas no treino e repetir a seleção de hiperparâmetros.
- Ajustar “shrink_threshold” para maior seletividade (redução de FP).
- Se o objetivo prioriza estritamente recall (minimizar FN), manter o NC é coerente; do contrário, testar modelos com limiar ajustável (regressão logística, árvores/ensembles) a fim de calibrar um ponto de operação com recall-alvo e ganhar precisão (curva Precision–Recall).


#### Conclusão
O Nearest Centroid atende bem ao objetivo de detectar reprovados (alto recall, baixos FN), sobretudo à medida que mais atributos ficam disponíveis no tempo. Entretanto, tende a produzir muitos falsos positivos nas etapas iniciais, reduzindo a precisão e o F1. É um bom ponto de partida orientado a recall em um cenário desbalanceado. Para implantação, recomenda-se ajuste fino e comparação com modelos que permitam melhor equilíbrio entre recall e custo operacional (FP).

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
Escreva, de forma resumida, sobre os principais resultados do seu projeto e faça recomendações formais ao seu parceiro de negócios em relação ao uso desse modelo. Você pode aproveitar este espaço para comentar sobre possíveis materiais extras, como um manual de usuário mais detalhado na seção "Anexos". Não se esqueça também das pessoas que serão potencialmente afetadas pelas decisões do modelo preditivo e elabore recomendações que ajudem seu parceiro a tratá-las de maneira estratégica e ética.

Remova este bloco ao final
```

## <a name="c6"></a>6. Referências

[Contexto da indústria]QS. Rankings released! QS World University Rankings: Latin America & The Caribbean 2025. Disponível em: https://www.qs.com/rankings-released-qs-world-university-rankings-latin-america-the-caribbean-2025/. Acesso em: 9 ago. 2025.

[Númeração de acordo com a ordem alfabética] EAFIT HISTORIA. "Historia de EAFIT". Disponível em: https://www.eafit.edu.co/historia. Acesso em: 11 de agosto de 2025.

[Númeração de acordo com a ordem alfabética] EAFIT NOTICIAS. "La ANDI reconoció a EAFIT por 65 años de impacto social y legado de futuro". Disponível em: https://www.eafit.edu.co/noticias/eafit-es-noticia/ANDI-reconocio-EAFIT-65anios-impacto-social. Acesso em: 11 de ago. de 2025.

[Númeração de acordo com a ordem alfabética] EAFIT HISTORIA NOTICIAS. "EAFIT, hija de la Medellín de los 60". Disponível em: https://www.eafit.edu.co/institucional/historia/noticias/eafit-hija-de-la-medellin-de-los-60. Acesso em: 11 de ago. de 2025.

[Númeração de acordo com a ordem alfabética] ROTHER, Mike; SHOOK, John. Aprendendo a enxergar: Mapeando o fluxo de valor para agregar valor e eliminar o desperdício. Disponível em: https://leanproduction.com.br/livro/aprendendo-a-enxergar/. Acesso em: 11 ago. 2025.

[Númeração de acordo com a ordem alfabética] UNIVERSIDAD EAFIT. "Excelencia y reconocimiento". Disponível em: https://www.eafit.edu.co/informes-de-gestion-y-sostenibilidad/informe-sostenibilidad-2023/excelencia-y-reconocimiento. Acesso em: 11 de ago. de 2025.

[Númeração de acordo com a ordem alfabética] QS QUACQUARELLI SYMONDS. "QS World University Rankings 2025". Disponível em: https://www.topuniversities.com/university-rankings/world-university-rankings/2025. Acesso em: 11 de ago. de 2025.

[personas] <a name="ref[Numeração de acrodo com a ordem alfabética]"></a> [COOPER, Alan; REIMANN, Robert; CRONIN, David; NOESSEL, Christopher. *About Face: The Essentials of Interaction Design*. 4. ed. Indianapolis: Wiley, 2014.](https://www.wiley.com/en-us/About+Face%3A+The+Essentials+of+Interaction+Design%2C+4th+Edition-p-9781118766576)


[Númeração de acordo com a ordem alfabética]. <a name="ref[Numeração de acrodo com a ordem alfabética]"></a> [PMI - Project Management Institute. Um guia do conhecimento em gerenciamento de projetos (Guia PMBOK®): guia do conhecimento em gerenciamento de projetos. 7. ed. Newtown Square, PA: Project Management Institute, 2021.](https://www.academiaplaorc.com.br/wp-content/uploads/2024/07/Guia-PMBOK-7a-Edicao.pdf)

SILVA, L. A. da; PERES, S. M.; BOSCARIOLI, C. **Introdução à mineração de dados**: com aplicações em R. Rio de Janeiro: GEN LTC, 2016

## <a name="attachments"></a>Anexos

### Distribuição normal e teste de hipótese

&ensp;Esta seção investiga se as variáveis quantitativas seguem (ou não) a distribuição normal e discute as implicações dessa avaliação para as etapas subsequentes de modelagem. Em projetos de natureza preditiva voltados a decisões de negócio — como expansão de pontos de venda, segmentação de clientes ou aumento da penetração de produtos — a validade dos resultados depende diretamente da escolha adequada de: (1) testes estatísticos (paramétricos vs. não-paramétricos), (2) técnicas de transformação e tratamento de outliers e (3) métodos de escalonamento capazes de garantir comparabilidade entre atributos de diferentes magnitudes.

&ensp;Nesse sentido, a análise de assimetria, curtose e valores extremos atua como etapa crítica tanto na engenharia de atributos quanto na seleção de algoritmos. Modelos baseados no cálculo de distâncias, que sensíveis à escala (como K-Means, SVM e redes neurais) ou baseados em pressupostos distributivos (como regressões lineares e outros modelos paramétricos) dependem fortemente da adequação das distribuições de entrada para gerar inferências consistentes e decisões confiáveis.

#### Seleção e Caracterização das Variáveis

&ensp;As três variáveis selecionadas para análise foram escolhidas com base em sua possibilidade de impacto e relevância para o treinamento do modelo preditivo.

- **Talleres**: Representa a nota associada a trabalhos complementares aos Quizes e provas.
- **CalcNotaQuiz**: Indica o número de itens adquiridos em cada transação, fundamental para compreender padrões de consumo
- **Nota_Oficial**: Refere-se ao custo de produção dos produtos, essencial para análises de margem e rentabilidade

### Análise e Teste de Normalidade das Variáveis Quantitativas

 A verificação da normalidade dos dados é uma etapa central na análise estatística, pois orienta a escolha entre procedimentos paramétricos e não-paramétricos nas fases seguintes do estudo. Neste trabalho, a questão investigada é se as variáveis quantitativas do conjunto analisado podem ser consideradas como provenientes de uma distribuição normal.

<div align="center">

Hipótese Nula (H₀): Os dados seguem uma distribuição normal.
$H_0: X \sim N(\mu, \sigma^2)$

Hipótese Alternativa (Hₐ): Os dados não seguem uma distribuição normal.
$H_1: X \not\sim N(\mu, \sigma^2)$

</div> </br>

&ensp;A formulação segue a abordagem clássica de testes de hipóteses: a hipótese nula (H₀) assume normalidade, enquanto a hipótese alternativa (Hₐ) sugere sua violação. Essa estrutura possibilita avaliar formalmente a adequação da distribuição de cada variável, constituindo um critério essencial para a definição de métodos estatísticos apropriados nas etapas posteriores da análise.

### Nível de significâcia e critérios de decisão

&ensp;Adotou-se um nível de significância de α = 0,05 (5%), valor amplamente utilizado na literatura científica por proporcionar um equilíbrio adequado entre o risco de cometer erro do tipo I e a potência do teste. A decisão sobre a hipótese nula baseia-se no valor-p: se p-valor ≤ 0,05, rejeita-se H₀, indicando evidência estatística de desvio da normalidade; se p-valor > 0,05, não se rejeita H₀, sugerindo que não há evidência suficiente para concluir que os dados não seguem uma distribuição normal.

### Teste de Normalidade (Aderência)

&ensp;A normalidade das variáveis quantitativas foi avaliada por meio do teste de Shapiro-Wilk, indicado para amostras de tamanho moderado e amplamente utilizado na literatura para essa finalidade. A estatística do teste é definida como:

$$W = \frac{\left( \sum_{i=1}^{n} a_i x_{(i)} \right)^2}{\sum_{i=1}^{n} (x_i - \bar{x})^2}$$

&ensp;Onde $x_{(i)}$ são os valores ordenados da amostra, $\bar{x}$ é a média amostral, $n$ representa o tamanho da amostra e $a_i$ são constantes derivadas das médias, variâncias e covariâncias das estatísticas de ordem de uma amostra de tamanho $n$ proveniente de uma distribuição normal. Seguem os testes feitos no código para a variável `"CalcNotaQuiz"`:

```python
# Testes de normalidade das variáveis "CalcNotaQuiz", "Talleres", "Calificación_Oficial"
# Testando normalidade para "CalcNotaQuiz" via Shapiro-Wilk
from scipy.stats import shapiro

dados = df_consolidado['CalcNotaQuiz'].dropna()

stat, p = shapiro(dados)

print('H0: Os dados seguem uma distribuição normal')
print('H1: Os dados não seguem uma distribuição normal')
print("Estatística W:", stat)
print("p-valor:", p)

if p > 0.05:
    print("Não rejeitamos H0: os dados seguem uma distribuição normal.")
else:
    print("Rejeitamos H0: os dados não seguem uma distribuição normal.")
```
Segue a saída:
```
H0: Os dados seguem uma distribuição normal
H1: Os dados não seguem uma distribuição normal
Estatística W: 0.9158549463812558
p-valor: 5.737420736467878e-27
Rejeitamos H0: os dados não seguem uma distribuição normal.
```
#### Teste de Normalidade para a variável "Talleres"

```python
# Testando normalidade para "Oficinas" (Talleres) via Shapiro-Wilk

from scipy.stats import shapiro

dados = df_consolidado['Oficinas'].dropna()

stat, p = shapiro(dados)

print('H0: Os dados seguem uma distribuição normal')
print('H1: Os dados não seguem uma distribuição normal')
print("Estatística W:", stat)
print("p-valor:", p)

if p > 0.05:
    print("Não rejeitamos H0: os dados seguem uma distribuição normal.")
else:
    print("Rejeitamos H0: os dados não seguem uma distribuição normal.")
```

Segue a saída:
```
H0: Os dados seguem uma distribuição normal
H1: Os dados não seguem uma distribuição normal
Estatística W: 0.7847014498757214
p-valor: 3.386401173855684e-39
Rejeitamos H0: os dados não seguem uma distribuição normal.
```

#### Teste de Normalidade para a variável Calificación_Oficial

```python
# Testando normalidade para "Nota_Oficial" (Calificación_Oficial) via Shapiro-Wilk
from scipy.stats import shapiro

dados = df_consolidado['Nota_Oficial'].dropna()

stat, p = shapiro(dados)

print('H0: Os dados seguem uma distribuição normal')
print('H1: Os dados não seguem uma distribuição normal')
print("Estatística W:", stat)
print("p-valor:", p)


if p > 0.05:
    print("Não rejeitamos H0: os dados seguem uma distribuição normal.")
else:
    print("Rejeitamos H0: os dados não seguem uma distribuição normal.")
```

Segue a saída:
```
# Testando normalidade para "Nota_Oficial" (Calificación_Oficial) via Shapiro-Wilk
from scipy.stats import shapiro

dados = df_consolidado['Nota_Oficial'].dropna()

stat, p = shapiro(dados)

print('H0: Os dados seguem uma distribuição normal')
print('H1: Os dados não seguem uma distribuição normal')
print("Estatística W:", stat)
print("p-valor:", p)


if p > 0.05:
    print("Não rejeitamos H0: os dados seguem uma distribuição normal.")
else:
    print("Rejeitamos H0: os dados não seguem uma distribuição normal.")
```

&ensp; Os resultados indicam que as variáveis `CalcNotaQuiz`, `Talleres`, `Calificación_Oficial` apresentam evidências de não seguirem uma distribuição normal (p < 0.05).

### Visualização por gráficos

&ensp;A fim de complementar a análise, foram construídos histogramas e violin-plots das três variáveis, permitindo uma avaliação visual sobre a distribuição das variáveis.

<div align="center">
  <sub>Figura x - Multiplot da variável CalcNotaQuiz</sub><br>
  <img src="../assets/CalcNotaQuiz.png"><br>
  <sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

<div align="center">
  <sub>Figura x - Multiplot da variável Talleres (Oficinas)</sub><br>
  <img src="../assets/Oficinas.png"><br>
  <sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

<div align="center">
  <sub>Figura x - Multiplot da variável Calificación_Oficial (Nota_Oficial)</sub><br>
  <img src="../assets/Nota_Oficial.png"><br>
  <sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

<div align="center">
  <sub>Figura x - Multiplot das três variáveis</sub><br>
  <img src="../assets/Multiplot_3.png"><br>
  <sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&ensp;A análise visual dos histogramas confirma os resultados dos testes estatísticos, revelando características específicas de cada distribuição. Nota-se que os gráficos das três variáveis possuem uma assimetria acentuada à esquerda, com os dados se concentrando em valores mais altos. Explicando a rejeição da normalidade e a diferença entre a média e a mediana quepode também ser visualizada no violin-plot.

A saber, a curva normal teórica usada como referência para os testes é dada por:

$$
f(x)=\frac{1}{\sigma\sqrt{2\pi}}\,e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

&ensp;em que $\mu$ é a média e $\sigma$ o desvio padrão. A sobreposição dessa curva aos histogramas facilita a visualização dos desvios observados em todas as variáveis.

#### Comparação entre média e mediana

&ensp;No gráfico das três variáveis juntas, podemos ver que a média e a mediana de todas as três variáveis não coincidem, possuindo determinada distância. A variável Nota_Oficial e Oficinas têm a mediana (4,50) ligeiramente maior que a média (4,28 e 4,17, respectivamente), enquanto para CalcNotaQuiz a diferença é ainda menor. A proximidade entre esses dois valores dá uma forte indicação de que as distribuições não são simétricas.

&ensp;Essa observação visual é confirmada pelo cálculo do skewness. O skewness é uma medida numérica que quantifica a assimetria da distribuição. Um valor de zero indica simetria perfeita, enquanto para um valor negativo, a distribuição tem uma cauda mais longa para a esquerda, e em números positivos, a cauda é mais longa para a direita. De acordo com o cálculo, o skewness para Oficinas é -1,16, para Nota_Oficial é -1,02, e para CalcNotaQuiz é -0,93. Todos esses valores são negativos, o que valida a nossa observação visual de que as distribuições são assimétricas à esquerda.

### Escalonamento das variáveis selecionadas

&ensp;O escalonamento de variáveis quantitativas é uma etapa essencial no pré-processamento de dados para modelagem preditiva, sobretudo em algoritmos de machine learning sensíveis à magnitude das variáveis. O objetivo dessa técnica é padronizar as escalas, de modo a evitar que atributos com valores mais elevados exerçam influência desproporcional sobre o processo de aprendizado e prejudiquem o desempenho preditivo do modelo.

&ensp;No contexto da análise de dados da Universidad EAFIT, as três variáveis quantitativas selecionadas foram: CalcNotaQuiz, Talleres e Nota_Oficial. Essas variáveis podem fornecer informações muito importantes, uma vez que as Oficinas (Talleres), e os quizes são atividades que ocorrem com frequência e possuem grande influência na variável Nota_Oficial, que indica se um aluno foi reprovado ou não.

&ensp;O uso adequado do escalonamento possibilita que algoritmos de clustering, classificação e regressão processem os dados de maneira mais equilibrada, favorecendo a convergência dos modelos e aprimorando a precisão das predições. Além disso, contribui para a interpretação dos resultados e para a comparação consistente entre variáveis em análises exploratórias.

#### Métodos de escalonamento escolhidos para cada variável

&ensp;Para o escalonamento da variável "Calificación_Oficial", o método escolhido foi a padronização, pois é menos sensível a outliers significativos e mantém a escala das notas pré-escalonamento (de 0 a 5). Para a variável Talleres, o método escolhido foi a normalização (Min-Max) para manter a escala das notas de 0 a 1, e por fim, para a variável CalcNotaQuiz, o método de escalonamento escolhido foi a padronização, pois além de ser menos sensível a outliers, permite analisar a quantos desvios padrões de distância uma certa nota se encontra da média da amostra.

#### Equações de cada escalonamento

Primeiramente, segue a tabela dos valores a serem utilizados nas equações:

| Variável     | Mínimo    | Máximo      | Média    | Desvio Padrão |
|--------------|-----------|-------------|----------|---------------|
| CalcNotaQuiz         | 0.625000  | 5.000000    | 4.075710 | 0.772738      |
| Talleres             | 0.000000  | 5.000000    | 4.100491 | 1.281169      |
| Calificación_Oficial | 0.500000  | 5.000000    | 4.319476 | 0.768881      |

Seguindo com as equações:

**CalcNotaQuiz (Padronização)**

- Fórmula geral: $Z = (X - \mu) / \sigma$
- Fórmula específica: $Z = (X - 4.075710) / 0.772738$

**Talleres (Normalização)**

- Fórmula geral: $X' = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$
- Fórmula específica: $X' = \frac{X - 0.000000}{5.000000 - 0.000000}$

**Calificación_Oficial (Padronização)**

- Fórmula geral: $Z = (X - \mu) / \sigma$
- Fórmula específica: $Z = (X - 4.319476) / 0.768881$

### Histogramas pós escalonamento

<div align="center">
  <sub>Figura x - Multiplot da variável CalcNotaQuiz pós escalonamento</sub><br>
  <img src="../assets/esc_CalcNotaQuiz.jpg"><br>
  <sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

<div align="center">
  <sub>Figura x - Multiplot da variável Talleres (Oficinas) pós escalonamento</sub><br>
  <img src="../assets/esc_Oficinas.jpg"><br>
  <sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

<div align="center">
  <sub>Figura x - Multiplot da variável Nota_Oficial pós escalonamento</sub><br>
  <img src="../assets/esc_Nota_Oficial.jpg"><br>
  <sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&ensp;Ao comparar com os histogramas pré escalonamento, nota-se que a principal mudança está na escala dos dados limitando-se ao limite superior igual a 1, contribuindo para a atribuição de pesos do modelo preditivo na etapa de treinamento e uma singela suavização dos gráficos.
