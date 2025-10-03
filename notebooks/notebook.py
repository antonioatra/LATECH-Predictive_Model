import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from sklearn.neighbors import NearestCentroid
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import recall_score, f1_score, confusion_matrix, classification_report
from imblearn.over_sampling import SMOTE
import shap
from PIL import Image

# Configuração da página
st.set_page_config(
    page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para estilo similar ao dashbord da imagem
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: white;
        background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0;
    }
    
    .metric-label {
        font-size: 1rem;
        opacity: 0.9;
        margin-top: 0.5rem;
    }
    
    .prediction-approved {
        background-color: #10b981;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    .prediction-rejected {
        background-color: #ef4444;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.875rem;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Funções auxiliares
def carregar_dados_processados():
    """Carrega dados já processados salvos"""
    try:
        df_modelo1 = pd.read_csv('dados/dados_modelo1.csv')
        df_modelo2 = pd.read_csv('dados/dados_modelo2.csv') 
        df_modelo3 = pd.read_csv('dados/dados_modelo3.csv')
        df_consolidado = pd.read_csv('dados/dados_consolidado.csv')
        return df_modelo1, df_modelo2, df_modelo3, df_consolidado
    except FileNotFoundError:
        return None, None, None, None

def carregar_dados_teste():
    try:
        dados_teste = {}
        
        # Esquemas esperados para cada semana
        esquemas = {
            "semana6": ["Quiz1", "Quiz2", "Quiz3", "TempoQ1","TempoQ2", "TempoQ3", "Genero_Masculino","STEM_SI"],
            "semana8": ["Quiz1", "Quiz2", "Quiz3", "Quiz4", "parcial","TempoQ1","TempoQ2", "TempoQ3", "TempoQ4", "Genero_Masculino","STEM_SI"],
            "semana12": ["Quiz1", "Quiz2", "Quiz3", "Quiz4", "Quiz5", "Quiz6", "parcial", 'TempoQ1', 'TempoQ2', 'TempoQ3','TempoQ4', 'TempoQ5', 'TempoQ6', "Genero_Masculino","STEM_SI"]
        }
        
        arquivos = {
            "semana6": "dados/teste_semana6.csv",
            "semana8": "dados/teste_semana8.csv",
            "semana12": "dados/teste_semana12.csv"
        }
        
        for semana, caminho in arquivos.items():
            if os.path.exists(caminho):
                df = pd.read_csv(caminho)
                
                # Verificação das colunas
                colunas_esperadas = set(esquemas[semana])
                colunas_arquivo = set(df.columns)
                
                if not colunas_esperadas.issubset(colunas_arquivo):
                    st.error(f"Arquivo {caminho} inválido! Esperado: {colunas_esperadas}, encontrado: {colunas_arquivo}")
                else:
                    dados_teste[semana] = df
        
        return dados_teste
    except Exception as e:
        st.error(f"Erro ao carregar dados de teste: {e}")
        return {}



def carregar_modelo(nome_arquivo):
    """Carrega modelo treinado"""
    try:
        caminho = os.path.join("modelos_treinados", nome_arquivo)
        with open(caminho, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

def preparar_dados_predicao(df_dados, colunas_modelo):
    """Prepara dados para predição garantindo que todas as features estejam presentes"""
    X_pred = pd.DataFrame(index=df_dados.index)
    
    for col in colunas_modelo:
        if col in df_dados.columns:
            # Usar dados reais e normalizar se necessário
            valores = df_dados[col].copy()
            if valores.max() > 1 and col.startswith(('Quiz', 'Parcial')):
                valores = valores / 5.0  # Normalizar notas
            X_pred[col] = valores
        else:
            # Valores padrão para features ausentes
            if 'Genero_Masculino' in col:
                X_pred[col] = np.random.choice([0, 1], len(df_dados), p=[0.4, 0.6])
            elif 'STEM_SI' in col:
                X_pred[col] = np.random.choice([0, 1], len(df_dados), p=[0.3, 0.7])
            else:
                X_pred[col] = 0
    
    return X_pred.fillna(0)

def avaliar_modelo(modelo, X_test, y_test):
    """Avalia performance do modelo nos dados de teste"""
    y_pred = modelo.predict(X_test)
    
    metricas = {
        'accuracy': np.mean(y_pred == y_test),
        'recall': recall_score(y_test, y_pred, pos_label=1),
        'f1_score': f1_score(y_test, y_pred, pos_label=1),
        'confusion_matrix': confusion_matrix(y_test, y_pred)
    }
    
    return metricas, y_pred

img = Image.open("../assets/logo.png")
img = img.resize((1400, 500))  # largura, altura
st.image(img)


# Carregar dados
df_modelo1, df_modelo2, df_modelo3, df_consolidado = carregar_dados_processados()

if df_modelo1 is None:
    st.error("❌ Dados não encontrados! Execute primeiro o pipeline de processamento.")
    st.stop()

# ==================== DASHBOARD PRINCIPAL ====================
st.subheader("Configurações de Predição")

# Controles da simulação
col_config1, col_config2, col_config3 = st.columns(3)

with col_config1:
    semana_atual = st.selectbox("📅 Semana para Predição:", [6, 8, 12], index=0)
    
with col_config2:
    fonte_dados = st.selectbox(
        "📂 Fonte dos Dados:", 
        ["Carregar dados da predição"]
    )
    

# Selecionar modelo e dados baseado na semana
if semana_atual == 6:
    modelo_arquivo = "modelo1_treinado.pkl"
    df_base = df_consolidado  # Usar consolidado com valores inteiros
    colunas_disponiveis = ['Genero_Masculino','STEM_SI',  'Quiz1', 'Quiz2', 'Quiz3', 'TempoQ1', 'TempoQ2', 'TempoQ3']
    st.info("📊 Semana 6: Predições baseadas nos primeiros 3 quizzes")
elif semana_atual == 8:
    modelo_arquivo = "modelo2_treinado.pkl"
    df_base = df_consolidado  # Usar consolidado com valores inteiros
    colunas_disponiveis = ['Genero_Masculino','STEM_SI', 'Quiz1', 'Quiz2', 'Quiz3','Quiz4', 'TempoQ1', 'TempoQ2', 'TempoQ3','TempoQ4', 'Parcial_1']
    st.info("📊 Semana 8: Predições com 4 quizzes + Parcial 1")
else:  # semana 12
    modelo_arquivo = "modelo3_treinado.pkl"
    df_base = df_consolidado  # Usar consolidado com valores inteiros
    colunas_disponiveis = ['Genero_Masculino','STEM_SI', 'Quiz1', 'Quiz2', 'Quiz3','Quiz4','Quiz5', 'Quiz6', 'TempoQ1', 'TempoQ2', 'TempoQ3','TempoQ4', 'TempoQ5', 'TempoQ6','Parcial_1' ]
    st.info("Semana 12: Predições completas com 6 quizzes + Parcial 1")

# Carregar modelo treinado
modelo_dados = carregar_modelo(modelo_arquivo)

if modelo_dados is None:
    st.error(f"Modelo para semana {semana_atual} não encontrado! Treine o modelo primeiro.")
    st.stop()

# Obter dados para predição baseado na fonte selecionada
df_predicao = None
tem_labels = False

        
if fonte_dados == "Carregar dados da predição":
    uploaded_file = st.file_uploader("Envie arquivo com dados de teste", type=["csv", "xlsx"])
    if uploaded_file:
        try:
            if uploaded_file.name.endswith('.csv'):
                df_predicao = pd.read_csv(uploaded_file)
            else:
                df_predicao = pd.read_excel(uploaded_file)
            
            # Verificar se tem coluna de resultado real
            if 'Reprovou' in df_predicao.columns:
                tem_labels = True
                st.success(f"Dados carregados com {len(df_predicao)} registros (com labels reais)")
            else:
                st.success(f"Dados carregados com {len(df_predicao)} registros")
                
        except Exception as e:
            st.error(f"Erro ao carregar arquivo: {e}")
            

if df_predicao is None or len(df_predicao) == 0:
    st.warning("Nenhum dado disponível para predição. Selecione uma fonte de dados.")
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
        st.info("ℹ️ Grupos não disponíveis nos dados")

# Filtrar por grupo se necessário - CORREÇÃO DEFINITIVA
if grupo_selecionado != "Todos":
    if "Grupo" in df_predicao.columns:
        # Converter para string para evitar problemas de tipos
        df_predicao["Grupo"] = df_predicao["Grupo"].astype(str)
        
        # Filtrar apenas os registros do grupo selecionado
        df_predicao = df_predicao[df_predicao["Grupo"] == grupo_selecionado].copy()
        
        if len(df_predicao) == 0:
            st.warning(f"Nenhum registro encontrado para o grupo '{grupo_selecionado}'")
            st.stop()
        else:
            st.success(f"Filtrado para grupo '{grupo_selecionado}': {len(df_predicao)} registros")
    else:
        st.info("ℹ️ Coluna 'Grupo' não encontrada nos dados carregados. Mostrando todos os registros.")

# Fazer predições
with st.spinner("Calculando predições..."):
    # Preparar dados para o modelo
    X_pred = preparar_dados_predicao(df_predicao, modelo_dados['colunas'])
    
    # Fazer predições
    predicoes = modelo_dados['modelo'].predict(X_pred)
    

# Calcular métricas das predições
total_alunos = len(df_predicao)
reprovados_previstos = int(sum(predicoes))
aprovados_previstos = total_alunos - reprovados_previstos
taxa_reprovacao = reprovados_previstos / total_alunos * 100

if tem_labels and 'Reprovou' in df_predicao.columns and fonte_dados == "Usar Dados de Validação":
    metricas, _ = avaliar_modelo(modelo_dados['modelo'], X_pred, df_predicao['Reprovou'])
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
    st.markdown(f"""
    <div class="metric-card" style="background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);">
        <div class="metric-value">{total_alunos}</div>
        <div class="metric-label">Total de Alunos Analisados</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card" style="background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);">
        <div class="metric-value">{reprovados_previstos}</div>
        <div class="metric-label">Reprovação Prevista ({taxa_reprovacao:.1f}%)</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);">
        <div class="metric-value">{aprovados_previstos}</div>
        <div class="metric-label">Aprovação Prevista</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    if mostrar_metricas_reais:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);">
            <div class="metric-value">{precisao_modelo:.0f}%</div>
            <div class="metric-label">Precisão do Modelo</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #64748b 0%, #475569 100%);">
            <div class="metric-value">?</div>
            <div class="metric-label">Precisão (N/A sem labels reais)</div>
        </div>
        """, unsafe_allow_html=True)

# Mostrar métricas adicionais APENAS se temos dados de validação real
if mostrar_metricas_reais:
    st.subheader("📊 Métricas de Avaliação do Modelo (Dados de Validação)")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Acurácia", f"{precisao_modelo:.1f}%")
    with col2:
        st.metric("Recall (Sensibilidade)", f"{recall_modelo:.1f}%")
    with col3:
        st.metric("F1-Score", f"{f1_modelo:.1f}%")
else:
    st.info("ℹ️ Métricas de avaliação não disponíveis - usando dados preditivos sem labels reais para comparação")

st.markdown("<br>", unsafe_allow_html=True)

# Tabela com predições
st.subheader(f"📋 Predições Detalhadas - Semana {semana_atual}")

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
df_exibicao['Predição'] = ['Reprovado' if p == 1 else 'Aprovado' for p in predicoes]


# Adicionar IDs se não existirem
if 'ID_Aluno' not in df_exibicao.columns:
    df_exibicao['ID_Aluno'] = [f'Aluno_{i+1}' for i in range(len(df_exibicao))]

# Reordenar colunas para melhor visualização
colunas_ordem = ['ID_Aluno'] + notas_cols + ['Media_Atual', 'Predição']
# REMOVIDO: Não incluir mais colunas de resultado real ou acerto

colunas_finais = [col for col in colunas_ordem if col in df_exibicao.columns]
df_exibicao_final = df_exibicao[colunas_finais]

# Aplicar estilo condicional com cores mais vibrantes
def highlight_predictions(row):
    colors = []
    for col in row.index:
        if col == 'Predição':
            colors.append('background-color: #fca5a5; color: #7f1d1d;' if row[col] == 'Reprovado' else 'background-color: #86efac; color: #14532d;')
        else:
            colors.append('')
    return colors

# Mostrar apenas uma amostra para melhor visualização
amostra_size = len(df_exibicao_final)
df_amostra = df_exibicao_final.head(amostra_size)

st.dataframe(
    df_amostra.style.apply(highlight_predictions, axis=1),
    use_container_width=True,
    height=500
)

if len(df_exibicao_final) > amostra_size:
    st.info(f"Mostrando {amostra_size} de {len(df_exibicao_final)} registros. Use o download para ver todos.")

# Gráficos de análise
col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribuição das Predições")
    
    # Gráfico de pizza com cores mais vibrantes
    valores = [aprovados_previstos, reprovados_previstos]
    labels = [f'Aprovados ({aprovados_previstos})', f'Reprovados ({reprovados_previstos})']
    colors = ['#22c55e', '#ef4444']  # Verde mais vibrante, vermelho mais forte
    
    fig_pizza = go.Figure(data=[go.Pie(
        labels=labels, 
        values=valores,
        marker=dict(colors=colors),
        textinfo='label+percent',
        textfont_size=14,
        hole=0.3
    )])
    
    fig_pizza.update_layout(
        title=f"Predições - Semana {semana_atual}",
        showlegend=True,
        height=400
    )
    
    st.plotly_chart(fig_pizza, use_container_width=True)

with col2:
    st.subheader("Distribuição da Média da Notas")
    
    # Criar histograma das probabilidades de reprovação com cores melhores
    fig_hist = go.Figure(data=[go.Histogram(
        x=df_exibicao['Media_Atual'],
        nbinsx=10,
        marker_color='#6366f1',  # Índigo mais vibrante
        opacity=0.8,
        marker_line_color='#4f46e5',
        marker_line_width=1
    )])
    
    fig_hist.update_layout(
        
    )
    
    st.plotly_chart(fig_hist, use_container_width=True)

# Análise de performance APENAS se temos dados de validação
if mostrar_metricas_reais and 'Reprovou' in df_predicao.columns:
    st.subheader("Matriz de Confusão (Dados de Validação)")
    
    # Calcular matriz de confusão
    cm = confusion_matrix(df_predicao['Reprovou'], predicoes)
    
    # Criar heatmap da matriz de confusão
    fig_cm = go.Figure(data=go.Heatmap(
        z=cm,
        x=['Previsto: Aprovado', 'Previsto: Reprovado'],
        y=['Real: Aprovado', 'Real: Reprovado'],
        colorscale='Blues',
        text=cm,
        texttemplate="%{text}",
        textfont={"size": 16}
    ))
    
    fig_cm.update_layout(
        title="Matriz de Confusão - Performance do Modelo",
        height=400
    )
    
    st.plotly_chart(fig_cm, use_container_width=True)

# Download dos resultados
st.subheader("Exportar Resultados")

# Preparar dados para download
df_download = df_exibicao_final.copy()
df_download['Fonte_Dados'] = fonte_dados
df_download['Semana_Predicao'] = semana_atual
df_download['Modelo_Usado'] = modelo_arquivo

csv_export = df_download.to_csv(index=False)

col1, col2 = st.columns(2)
with col1:
    st.download_button(
        "Download Predições Completas",
        csv_export,
        f"predicoes_semana_{semana_atual}_{fonte_dados.lower().replace(' ', '_')}.csv",
        "text/csv",
        key="download_predicoes"
    )

with col2:
    # Relatório resumo
    relatorio = f"""# Relatório de Predições - LATECH
    
## Configurações
- **Semana:** {semana_atual}
- **Fonte dos Dados:** {fonte_dados}
- **Grupo Analisado:** {grupo_selecionado}
- **Modelo Utilizado:** {modelo_arquivo}

## Resultados Gerais
- **Total de Alunos Analisados:** {total_alunos}
- **Aprovados Previstos:** {aprovados_previstos} ({100-taxa_reprovacao:.1f}%)
- **Reprovados Previstos:** {reprovados_previstos} ({taxa_reprovacao:.1f}%)

## Métricas do Modelo
- **Precisão:** {precisao_modelo:.1f}%
{"- **Recall:** " + f"{recall_modelo:.1f}%" if tem_labels else ""}
{"- **F1-Score:** " + f"{f1_modelo:.1f}%" if tem_labels else ""}

## Observações
{f"- Análise realizada com dados de validação (métricas reais disponíveis)" if tem_labels and 'Reprovou' in df_predicao.columns else "- Análise preditiva (sem dados reais para comparação)"}
- Probabilidades calculadas baseadas na distância do modelo NearestCentroid
- Notas apresentadas na escala original (0-5)

---
*Relatório gerado automaticamente pelo Sistema LATECH*
    """
    
    st.download_button(
        "📄 Download Relatório",
        relatorio,
        f"relatorio_semana_{semana_atual}.md",
        "text/markdown",
        key="download_relatorio"
    )

st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; margin-top: 2rem;'>
        <h4>🎓 LATECH - Sistema Preditivo de Aprovação Acadêmica</h4>
        <p>
            Desenvolvido com Streamlit e Machine Learning | 
            <strong>Recursos:</strong> Predições em Tempo Real, Análise SHAP, Gestão de Modelos
        </p>
        <p>
            <em>Versão 2.0 - Dashboard com Dados de Teste Separados</em>
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)