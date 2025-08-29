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
```
Descreva a metodologia CRISP-DM e suas etapas de desenvolvimento, citando o referencial teórico. Você deve apenas enunciar os métodos, sem dizer ainda como eles foram aplicados, nem quais resultados foram obtidos.

Remova este bloco ao final
```

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

## <a name="attachments"></a>Anexos

### Distribuição normal e teste de hipótese

&ensp;Esta seção investiga se as variáveis quantitativas seguem (ou não) a distribuição normal e discute as implicações dessa avaliação para as etapas subsequentes de modelagem. Em projetos de natureza preditiva voltados a decisões de negócio — como expansão de pontos de venda, segmentação de clientes ou aumento da penetração de produtos — a validade dos resultados depende diretamente da escolha adequada de: (1) testes estatísticos (paramétricos vs. não-paramétricos), (2) técnicas de transformação e tratamento de outliers e (3) métodos de escalonamento capazes de garantir comparabilidade entre atributos de diferentes magnitudes.

&ensp;Nesse sentido, a análise de assimetria, curtose e valores extremos atua como etapa crítica tanto na engenharia de atributos quanto na seleção de algoritmos. Modelos baseados no cálculo de distâncias, que sensíveis à escala (como K-Means, SVM e redes neurais) ou baseados em pressupostos distributivos (como regressões lineares e outros modelos paramétricos) dependem fortemente da adequação das distribuições de entrada para gerar inferências consistentes e decisões confiáveis.
