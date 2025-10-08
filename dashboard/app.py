# Arquivo destinado a junção da estilização com a lógica de predição e carregamento de dados
import streamlit as st
from PIL import Image
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import src.data_loader as dl
import src.model as ml
import src.style as stl
import src.plotting as plot

# Configuração da página
st.set_page_config(
    page_icon="../assets/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Logo 
img = Image.open("../assets/logo.png")
img = img.resize((1400, 500))  # largura, altura
st.image(img)

# Carregar o CSS da página
stl.carregar_css()

# # Carregamento dos dados
# df_modelo1, df_modelo2, df_modelo3, df_consolidado = dl.carregar_dados_processados()

# # Preventiva caso os dados nao sejam carregados
# if df_modelo1 is None:
#     st.er("Dados não encontrados! Execute primeiro o pipeline de processamento. | ¡Datos no encontrados! Ejecute primero el canal de procesamiento.")
#     st.stop()

# Interface
# Seção de configurações da predição
st.subheader("Configuración de predicción | Configurações de Predição")
col_config1, col_config2, col_config3 = st.columns(3)

with col_config1:
    semana_atual = st.selectbox("📅 Semana de predicción | Semana para Predição:", [6, 8, 12], index=0)
    
with col_config2:
    fonte_dados = st.selectbox(
        "📂 Fuente de datos | Fonte dos Dados:", 
        ["Cargar datos de predicción | Carregar dados da predição"]
    )

# Selecionar modelo e dados baseado na semana
if semana_atual == 6:
    modelo_arquivo = "modelo1_treinado.pkl"
    df_base = df_consolidado  # Usar consolidado com valores inteiros
    colunas_disponiveis = ['Genero_Masculino','STEM_SI',  'Quiz1', 'Quiz2', 'Quiz3', 'TempoQ1', 'TempoQ2', 'TempoQ3']
    st.info("📊 Semana 6: Predicciones basadas en los primeros 3 cuestionarios | Semana 6: Predições baseadas nos primeiros 3 quizzes")
elif semana_atual == 8:
    modelo_arquivo = "modelo2_treinado.pkl"
    df_base = df_consolidado  # Usar consolidado com valores inteiros
    colunas_disponiveis = ['Genero_Masculino','STEM_SI', 'Quiz1', 'Quiz2', 'Quiz3','Quiz4', 'TempoQ1', 'TempoQ2', 'TempoQ3','TempoQ4', 'Parcial_1']
    st.info("📊 Semana 8: Predicciones con 4 cuestionarios + Parcial 1 | Semana 8: Predições com 4 quizzes + Parcial 1")
else:  # semana 12
    modelo_arquivo = "modelo3_treinado.pkl"
    df_base = df_consolidado  # Usar consolidado com valores inteiros
    colunas_disponiveis = ['Genero_Masculino','STEM_SI', 'Quiz1', 'Quiz2', 'Quiz3','Quiz4','Quiz5', 'Quiz6', 'TempoQ1', 'TempoQ2', 'TempoQ3','TempoQ4', 'TempoQ5', 'TempoQ6','Parcial_1' ]
    st.info("📊 Semana 12: Predicciones completas con 6 cuestionarios + 1 parcial | Semana 12: Predições completas com 6 quizzes + Parcial 1")

# Carregar modelo treinado
modelo_dados = ml.carregar_modelo(modelo_arquivo)

if modelo_dados is None:
    st.error(f"Semana actual: {semana_atual} | Semana atual: {semana_atual}")
    st.error(f"Plantilla para la semana {semana_atual} ¡No encontrado! Entrena el modelo primero. | Modelo para semana {semana_atual} não encontrado! Treine o modelo primeiro.")
    st.stop()

# Obter dados para predição baseado na fonte selecionada
df_predicao = None
tem_labels = False

        
if fonte_dados == "Cargar datos de predicción | Carregar dados da predição":
    uploaded_file = st.file_uploader("Enviar archivo con datos de prueba | Envie arquivo com dados de teste", type=["csv"])
    if uploaded_file:
        try:
            if uploaded_file.name.endswith('.csv'):
                df_predicao = pd.read_csv(uploaded_file)
            else:
                df_predicao = pd.read_excel(uploaded_file)
            
            # ========== VALIDAÇÃO DE COLUNAS (NOVO) ==========
            # Identificar colunas obrigatórias (notas/quizzes)
            colunas_obrigatorias = [col for col in colunas_disponiveis 
                                    if col.startswith(('Quiz', 'Parcial', 'TempoQ'))]
            
            # Verificar colunas faltantes
            colunas_faltantes = set(colunas_obrigatorias) - set(df_predicao.columns)
            
            if colunas_faltantes:
                st.error(f"❌ **¡Archivo inválido! | Arquivo inválido!**")
                st.error(f"**Faltan columnas obligatorias | Colunas obrigatórias ausentes:** {', '.join(sorted(colunas_faltantes))}")
                st.info(f"**Columnas esperadas para la semana | Colunas esperadas para Semana {semana_atual}:** {', '.join(colunas_disponiveis)}")
                st.warning("Corrija el archivo CSV y vuelva a intentarlo. | Por favor, corrija o arquivo CSV e tente novamente.")
                st.stop()  # Para a execução
            
            # Verificar se tem coluna de resultado real
            if 'Reprovou' in df_predicao.columns:
                tem_labels = True
                st.success(f"✅ Datos cargados con {len(df_predicao)} registros (con etiquetas reales)")
                st.success(f"✅ Dados carregados com {len(df_predicao)} registros (com labels reais)")
            else:
                st.success(f"✅ Datos cargados con {len(df_predicao)} registros")
                st.success(f"✅ Dados carregados com {len(df_predicao)} registros")
            
            # Mostrar colunas encontradas
            with st.expander("🔍 Ver columnas detectadas en el archivo | Ver colunas detectadas no arquivo"):
                st.write(f"**Colunas encontradas:** {', '.join(df_predicao.columns.tolist())}")
                
        except Exception as e:
            st.error(f"❌ Error al cargar el archivo | Erro ao carregar arquivo: {e}")
            st.stop()
            

if df_predicao is None or len(df_predicao) == 0:
    st.warning("No hay datos disponibles para la predicción. Seleccione una fuente de datos. | Nenhum dado disponível para predição. Selecione uma fonte de dados.")
    st.stop()

with col_config3:
    # Melhorar verificação de grupo
    grupos_disponiveis = []
    if "Grupo" in df_predicao.columns and df_predicao["Grupo"].notna().any():
        grupos_unicos = df_predicao["Grupo"].unique()
        grupos_disponiveis = sorted([str(g) for g in grupos_unicos if str(g) != 'nan'])
        
    if grupos_disponiveis:
        grupo_selecionado = st.selectbox("👥 Filtrar por Grupo:", ["Todos"] + grupos_disponiveis)
    else:
        grupo_selecionado = "Todos"
        st.info("ℹ️ Grupos no disponibles en los datos | Grupos não disponíveis nos dados")

# Filtrar por grupo se necessário 
if grupo_selecionado != "Todos":
    if "Grupo" in df_predicao.columns:
        # Converter para string para evitar problemas de tipos
        df_predicao["Grupo"] = df_predicao["Grupo"].astype(str)
        
        # Filtrar apenas os registros do grupo selecionado
        df_predicao = df_predicao[df_predicao["Grupo"] == grupo_selecionado].copy()
        
        if len(df_predicao) == 0:
            st.warning(f"No se encontraron registros para el grupo | Nenhum registro encontrado para o grupo '{grupo_selecionado}'")
            st.stop()
        else:
            st.success(f"Filtrado por grupo '{grupo_selecionado}': {len(df_predicao)} registros")
    else:
        st.info("ℹ️ No se encontró la columna 'Grupo' en los datos cargados. Se muestran todos los registros. | Coluna 'Grupo' não encontrada nos dados carregados. Mostrando todos os registros.")

# Fazer predições
with st.spinner("Calculando predicciones | Calculando predições..."):
    # Preparar dados para o modelo
    X_pred = ml.preparar_dados_predicao(df_predicao, modelo_dados['colunas'])
    
    # Fazer predições
    predicoes = modelo_dados['modelo'].predict(X_pred)
    

# Calcular métricas das predições
total_alunos = len(df_predicao)
reprovados_previstos = int(sum(predicoes))
aprovados_previstos = total_alunos - reprovados_previstos
taxa_reprovacao = reprovados_previstos / total_alunos * 100

if tem_labels and 'Reprovou' in df_predicao.columns and fonte_dados == "Usar Dados de Validação":
    metricas, _ = ml.avaliar_modelo(modelo_dados['modelo'], X_pred, df_predicao['Reprovou'])
    precisao_modelo = metricas['accuracy'] * 100
    recall_modelo = metricas['recall'] * 100
    f1_modelo = metricas['f1_score'] * 100
    mostrar_metricas_reais = True
else:
    # Para dados sintéticos ou arquivos carregados SEM validação real
    precisao_modelo = None  
    recall_modelo = None
    f1_modelo = None
    mostrar_metricas_reais = False

# Cards de métricas
col1, col2, col3, col4 = st.columns(4)

with col1:
    stl.criar_card_metrica(
        titulo="Total de estudiantes analizados | Total de Alunos Analisados", 
        valor=f"{total_alunos}",
        cor_fundo="linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%)"
    )

with col2:
    stl.criar_card_metrica(
        titulo=f"Rechazo esperado | Reprovação Prevista ({taxa_reprovacao:.1f}%)", 
        valor=f"{reprovados_previstos}",
        cor_fundo="linear-gradient(135deg, #ef4444 0%, #dc2626 100%)"
    )

with col3:
    stl.criar_card_metrica(
        titulo="Aprobación esperada | Aprovação Prevista", 
        valor=f"{aprovados_previstos}",
        cor_fundo="linear-gradient(135deg, #10b981 0%, #059669 100%)"
    )

with col4:
    if mostrar_metricas_reais:
        stl.criar_card_metrica(
            titulo="Precisión del pronóstico |Precisão da Previsão",
            valor=f"{precisao_modelo:.0f}%",
            cor_fundo="linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%)"
        )
    else:
        stl.criar_card_metrica(
            titulo="Precisión del pronóstico | Precisão da Previsão",
            valor="N/A",
            cor_fundo="linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%)"
        )

st.markdown("<br>", unsafe_allow_html=True)

# Tabela com predições
st.subheader(f"📋 Predicciones detalladas - Semana | Predições Detalhadas - Semana {semana_atual}")

# Preparar tabela para exibição
df_exibicao = df_predicao.copy()

# Filtrar apenas colunas de notas (Quiz e Parcial)
notas_cols = [col for col in colunas_disponiveis if col in df_exibicao.columns and col.startswith(('Quiz', 'Parcial'))]

# Converter apenas colunas de notas de 0-1 para 0-5
for col in notas_cols:
    if df_exibicao[col].max() <= 1:
        df_exibicao[col] = (df_exibicao[col] * 5).round(2)

# Calcular média apenas das notas
if notas_cols:
    df_exibicao['Media_Atual'] = df_exibicao[notas_cols].mean(axis=1).round(2)

# Adicionar colunas de predição
df_exibicao['Predição'] = ['Reprobado | Reprovado' if p == 1 else 'Aprobado | Aprovado' for p in predicoes]


# Adicionar IDs se não existirem
if 'ID_Aluno' not in df_exibicao.columns:
    df_exibicao['ID_Aluno'] = [f'Aluno_{i+1}' for i in range(len(df_exibicao))]

# Reordenar colunas para melhor visualização
colunas_ordem = ['ID_Aluno'] + notas_cols + ['Media_Atual', 'Predição']

colunas_finais = [col for col in colunas_ordem if col in df_exibicao.columns]
df_exibicao_final = df_exibicao[colunas_finais]

# Mostrar apenas uma amostra para melhor visualização
amostra_size = len(df_exibicao_final)
df_amostra = df_exibicao_final.head(amostra_size).rename(columns={'ID_Aluno': 'ID_Alumno', 'Predição': 'Predicción'})

st.dataframe(
    df_amostra.style.apply(stl.highlight_predictions, axis=1),
    use_container_width=True,
    height=500
)

if len(df_exibicao_final) > amostra_size:
    st.info(f"Mostrando {amostra_size} de los {len(df_exibicao_final)} registros. Use el botón de descarga para ver todos. | Mostrando {amostra_size} de {len(df_exibicao_final)} registros. Use o download para ver todos.")

# Gráficos de análise
col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribuição das Predições")
    
    # Gráfico de pizza com cores mais vibrantes
    fig_pizza = plot.criar_grafico_pizza(aprovados_previstos, reprovados_previstos, semana_atual)
    
    st.plotly_chart(fig_pizza, use_container_width=True)

with col2:
    st.subheader("Distribuição da Média das Notas")
    
    # 1. Chama a função de plotting para criar a figura e obter as médias
    fig_histograma, media_aprov, media_reprov = plot.criar_histograma_medias(df_exibicao)
    
    # 2. O app.py exibe o gráfico que foi retornado
    st.plotly_chart(fig_histograma, use_container_width=True)
     
    # 3. O app.py exibe as métricas que foram retornadas
    col_a, col_b = st.columns(2)
    with col_a: 
        st.metric("📗 Media Aprobados | Média Aprovados", f"{media_aprov:.2f}")
    with col_b: 
        st.metric("📕 Media Reprobados | Média Reprovados", f"{media_reprov:.2f}")

stl.criar_footer()
 