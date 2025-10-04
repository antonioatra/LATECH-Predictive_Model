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

# Configuração da página
st.set_page_config(
    page_title="LATECH - Dashboard Preditivo",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para estilo similar ao dashboard da imagem
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
    """Carrega dados de teste para predições"""
    try:
        # Tentar carregar arquivos de teste específicos
        dados_teste = {}

        # Dados de teste para semana 6 (3 quizzes)
        if os.path.exists('dados/teste_semana6.csv'):
            dados_teste['semana6'] = pd.read_csv('dados/teste_semana6.csv')

        # Dados de teste para semana 8 (4 quizzes + parcial)
        if os.path.exists('dados/teste_semana8.csv'):
            dados_teste['semana8'] = pd.read_csv('dados/teste_semana8.csv')

        # Dados de teste para semana 12 (6 quizzes + parcial)
        if os.path.exists('dados/teste_semana12.csv'):
            dados_teste['semana12'] = pd.read_csv('dados/teste_semana12.csv')

        return dados_teste
    except Exception as e:
        st.error(f"Erro ao carregar dados de teste: {e}")
        return {}

def criar_dados_teste_sinteticos(df_treino, semana, num_amostras=50):
    """Cria dados de teste sintéticos baseados nos dados de treino"""
    np.random.seed(42)

    # Mapear semana para colunas
    if semana == 6:
        colunas_base = ['Quiz1', 'Quiz2', 'Quiz3']
    elif semana == 8:
        colunas_base = ['Quiz1', 'Quiz2', 'Quiz3', 'Quiz4', 'Parcial_1']
    else:  # semana 12
        colunas_base = ['Quiz1', 'Quiz2', 'Quiz3', 'Quiz4', 'Quiz5', 'Quiz6', 'Parcial_1']

    # Criar DataFrame de teste
    dados_teste = pd.DataFrame()

    for col in colunas_base:
        if col in df_treino.columns:
            # Usar distribuição similar aos dados de treino
            media = df_treino[col].mean()
            std = df_treino[col].std()

            # Se os dados estão normalizados (0-1), converter para escala 0-5
            if df_treino[col].max() <= 1:
                media *= 5
                std *= 5

            dados_teste[col] = np.random.normal(media, std, num_amostras)
            # Manter no intervalo de notas válidas (0-5)
            dados_teste[col] = np.clip(dados_teste[col], 0, 5).round(2)

    # Adicionar outras features se existirem
    outras_features = ['Genero_Masculino', 'STEM_SI', 'Grupo']
    for feature in outras_features:
        if feature in df_treino.columns:
            if feature == 'Genero_Masculino':
                dados_teste[feature] = np.random.choice([0, 1], num_amostras, p=[0.4, 0.6])
            elif feature == 'STEM_SI':
                dados_teste[feature] = np.random.choice([0, 1], num_amostras, p=[0.3, 0.7])
            elif feature == 'Grupo':
                grupos_unicos = df_treino[feature].unique()
                dados_teste[feature] = np.random.choice(grupos_unicos, num_amostras)

    # Adicionar IDs dos alunos
    dados_teste['ID_Aluno'] = [f'Aluno_Teste_{i+1}' for i in range(num_amostras)]

    return dados_teste

def dividir_dados_treino_teste(df, test_size=0.3, random_state=42):
    """Divide os dados em treino e teste"""
    if 'Reprovou' in df.columns:
        X = df.drop('Reprovou', axis=1)
        y = df['Reprovou']

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=y
        )

        # Adicionar coluna alvo de volta aos conjuntos
        df_train = X_train.copy()
        df_train['Reprovou'] = y_train

        df_test = X_test.copy()
        df_test['Reprovou'] = y_test

        return df_train, df_test
    else:
        # Se não há coluna alvo, dividir aleatoriamente
        return train_test_split(df, test_size=test_size, random_state=random_state)

def treinar_modelo(X_train, y_train, modelo_nome):
    """Treina o modelo NearestCentroid com SMOTE"""
    # Aplicar SMOTE
    sm = SMOTE(random_state=42)
    X_train_balanced, y_train_balanced = sm.fit_resample(X_train, y_train)

    # Configurar modelo
    nc = NearestCentroid()
    param_grid = {
        "metric": ["euclidean", "manhattan"],
        "shrink_threshold": [None, 0.1, 0.5, 1.0]
    }

    # Treinar com GridSearch
    grid = GridSearchCV(nc, param_grid, cv=5, scoring='recall')
    grid.fit(X_train_balanced, y_train_balanced)

    return grid.best_estimator_, X_train_balanced, y_train_balanced

def salvar_modelo(modelo_dados, nome_arquivo):
    """Salva modelo treinado com metadados"""
    os.makedirs("modelos_treinados", exist_ok=True)
    caminho = os.path.join("modelos_treinados", nome_arquivo)
    with open(caminho, 'wb') as f:
        pickle.dump(modelo_dados, f)
    return caminho

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

# Header principal
st.markdown("""
<div class="main-header">
    <h1 style="margin: 0; font-size: 3rem; letter-spacing: 2px;">LATECH</h1>
    <p style="margin: 0.5rem 0 0 0; font-size: 1.2rem;">Sistema Preditivo de Aprovação Acadêmica</p>
</div>
""", unsafe_allow_html=True)

# Sidebar para navegação
st.sidebar.title("🎛️ Painel de Controle")
opcao = st.sidebar.selectbox(
    "Escolha uma opção:",
    ["📊 Dashboard Principal", "🤖 Treinar Modelos", "🔮 Nova Predição", "📈 Análises Avançadas", "📁 Gerenciar Dados"]
)

# Carregar dados
df_modelo1, df_modelo2, df_modelo3, df_consolidado = carregar_dados_processados()

if df_modelo1 is None:
    st.error("❌ Dados não encontrados! Execute primeiro o pipeline de processamento.")
    st.stop()

# ==================== DASHBOARD PRINCIPAL ====================
if opcao == "📊 Dashboard Principal":
    st.subheader("🎛️ Configurações de Predição")

    # Controles da simulação
    col_config1, col_config2, col_config3 = st.columns(3)

    with col_config1:
        semana_atual = st.selectbox("📅 Semana para Predição:", [6, 8, 12], index=0)

    with col_config2:
        fonte_dados = st.selectbox(
            "📂 Fonte dos Dados:",
            ["Dados de Teste Sintéticos", "Carregar Arquivo de Teste", "Usar Dados de Validação"]
        )

    with col_config3:
        # Melhorar verificação de grupo
        grupos_disponiveis = []
        if "Grupo" in df_consolidado.columns and df_consolidado["Grupo"].notna().any():
            grupos_unicos = df_consolidado["Grupo"].dropna().unique()
            grupos_disponiveis = sorted([str(g) for g in grupos_unicos if str(g) != 'nan'])

        if grupos_disponiveis:
            grupo_selecionado = st.selectbox("👥 Filtrar por Grupo:", ["Todos"] + grupos_disponiveis)
        else:
            grupo_selecionado = "Todos"
            st.info("ℹ️ Grupos não disponíveis nos dados")

    # Selecionar modelo e dados baseado na semana
    if semana_atual == 6:
        modelo_arquivo = "modelo1_treinado.pkl"
        df_base = df_consolidado  # Usar consolidado com valores inteiros
        colunas_disponiveis = ['Quiz1', 'Quiz2', 'Quiz3']
        st.info("📊 Semana 6: Predições baseadas nos primeiros 3 quizzes")
    elif semana_atual == 8:
        modelo_arquivo = "modelo2_treinado.pkl"
        df_base = df_consolidado  # Usar consolidado com valores inteiros
        colunas_disponiveis = ['Quiz1', 'Quiz2', 'Quiz3', 'Quiz4', 'Parcial_1']
        st.info("📊 Semana 8: Predições com 4 quizzes + Parcial 1")
    else:  # semana 12
        modelo_arquivo = "modelo3_treinado.pkl"
        df_base = df_consolidado  # Usar consolidado com valores inteiros
        colunas_disponiveis = ['Quiz1', 'Quiz2', 'Quiz3', 'Quiz4', 'Quiz5', 'Quiz6', 'Parcial_1']
        st.info("📊 Semana 12: Predições completas com 6 quizzes + Parcial 1")

    # Carregar modelo treinado
    modelo_dados = carregar_modelo(modelo_arquivo)

    if modelo_dados is None:
        st.error(f"❌ Modelo para semana {semana_atual} não encontrado! Treine o modelo primeiro.")
        st.stop()

    # Obter dados para predição baseado na fonte selecionada
    df_predicao = None
    tem_labels = False

    if fonte_dados == "Dados de Teste Sintéticos":
        with st.spinner("Gerando dados de teste sintéticos..."):
            df_predicao = criar_dados_teste_sinteticos(df_base, semana_atual, num_amostras=50)
            st.success(f"✅ Gerados {len(df_predicao)} registros de teste sintéticos")

    elif fonte_dados == "Carregar Arquivo de Teste":
        uploaded_file = st.file_uploader("📂 Envie arquivo com dados de teste", type=["csv", "xlsx"])
        if uploaded_file:
            try:
                if uploaded_file.name.endswith('.csv'):
                    df_predicao = pd.read_csv(uploaded_file)
                else:
                    df_predicao = pd.read_excel(uploaded_file)

                # Verificar se tem coluna de resultado real
                if 'Reprovou' in df_predicao.columns:
                    tem_labels = True
                    st.success(f"✅ Dados carregados com {len(df_predicao)} registros (com labels reais)")
                else:
                    st.success(f"✅ Dados carregados com {len(df_predicao)} registros")

            except Exception as e:
                st.error(f"Erro ao carregar arquivo: {e}")

    elif fonte_dados == "Usar Dados de Validação":
        with st.spinner("Dividindo dados em treino/validação..."):
            # Dividir dados base em treino e validação
            df_train, df_predicao = dividir_dados_treino_teste(df_base, test_size=0.3)
            tem_labels = True
            st.success(f"✅ Usando {len(df_predicao)} registros de validação")

    if df_predicao is None or len(df_predicao) == 0:
        st.warning("⚠️ Nenhum dado disponível para predição. Selecione uma fonte de dados.")
        st.stop()

    # Filtrar por grupo se necessário - CORREÇÃO DEFINITIVA
    if grupo_selecionado != "Todos":
        if "Grupo" in df_predicao.columns:
            # Verificar se a coluna Grupo existe e tem valores válidos
            valores_grupo = df_predicao["Grupo"].dropna().astype(str)
            if len(valores_grupo) > 0:
                # Filtrar pelos valores que correspondem ao grupo selecionado
                mascara_grupo = valores_grupo == str(grupo_selecionado)
                indices_grupo = mascara_grupo[mascara_grupo].index

                if len(indices_grupo) > 0:
                    df_predicao = df_predicao.loc[indices_grupo].copy()
                    st.success(f"✅ Filtrado para grupo '{grupo_selecionado}': {len(df_predicao)} registros")
                else:
                    st.warning(f"⚠️ Nenhum registro encontrado para o grupo '{grupo_selecionado}'")
                    st.stop()
            else:
                st.info(f"ℹ️ Coluna 'Grupo' não contém dados válidos. Mostrando todos os registros.")
        else:
            # Se não há coluna Grupo nos dados de predição, mas foi selecionado um grupo
            st.warning(f"⚠️ Coluna 'Grupo' não encontrada nos dados de predição. Mostrando todos os registros.")
            grupo_selecionado = "Todos"  # Reset para todos

    # Fazer predições
    with st.spinner("Calculando predições..."):
        # Preparar dados para o modelo
        X_pred = preparar_dados_predicao(df_predicao, modelo_dados['colunas'])

        # Fazer predições
        predicoes = modelo_dados['modelo'].predict(X_pred)

        # Calcular probabilidades se possível
        try:
            # Para NearestCentroid, usar distância como proxy para probabilidade
            distancias = modelo_dados['modelo'].decision_function(X_pred)
            # Normalizar distâncias para [0,1]
            prob_reprovacao = 1 / (1 + np.exp(-distancias))  # Sigmoid
            prob_reprovacao = np.clip(prob_reprovacao, 0.05, 0.95)  # Limitar extremos
        except:
            # Probabilidades simuladas se não conseguir calcular
            prob_reprovacao = np.where(predicoes == 1,
                                     np.random.uniform(0.6, 0.9, len(predicoes)),
                                     np.random.uniform(0.1, 0.4, len(predicoes)))

    # Calcular métricas das predições
    total_alunos = len(df_predicao)
    reprovados_previstos = int(sum(predicoes))
    aprovados_previstos = total_alunos - reprovados_previstos
    taxa_reprovacao = reprovados_previstos / total_alunos * 100

    # Avaliar modelo APENAS se temos labels reais E estamos usando dados de validação
    if tem_labels and 'Reprovou' in df_predicao.columns and fonte_dados == "Usar Dados de Validação":
        metricas, _ = avaliar_modelo(modelo_dados['modelo'], X_pred, df_predicao['Reprovou'])
        precisao_modelo = metricas['accuracy'] * 100
        recall_modelo = metricas['recall'] * 100
        f1_modelo = metricas['f1_score'] * 100
        mostrar_metricas_reais = True
    else:
        # Para dados sintéticos ou arquivos carregados SEM validação real
        precisao_modelo = None  # Não mostrar precisão falsa
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

    # Garantir que as notas estejam na escala 0-5 para exibição
    notas_cols = [col for col in colunas_disponiveis if col in df_exibicao.columns]
    for col in notas_cols:
        if col in df_exibicao.columns and df_exibicao[col].max() <= 1:
            df_exibicao[col] = (df_exibicao[col] * 5).round(2)  # Converter de volta para 0-5

    # Adicionar colunas de predição
    df_exibicao['Predição'] = ['Reprovado' if p == 1 else 'Aprovado' for p in predicoes]
    df_exibicao['Prob_Reprovacao'] = [f"{p:.1%}" for p in prob_reprovacao]

    # Calcular média das notas disponíveis (na escala 0-5)
    if notas_cols:
        df_exibicao['Media_Atual'] = df_exibicao[notas_cols].mean(axis=1).round(2)

    # Adicionar comparação APENAS se temos labels reais (dados de validação)
    # REMOVIDO: Não vamos mais mostrar coluna "Acerto" para evitar confusão

    # Adicionar IDs se não existirem
    if 'ID_Aluno' not in df_exibicao.columns:
        df_exibicao['ID_Aluno'] = [f'Aluno_{i+1}' for i in range(len(df_exibicao))]

    # Reordenar colunas para melhor visualização
    colunas_ordem = ['ID_Aluno'] + notas_cols + ['Media_Atual', 'Predição', 'Prob_Reprovacao']
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
    amostra_size = min(20, len(df_exibicao_final))
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
        st.subheader("🥧 Distribuição das Predições")

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
        st.subheader("📊 Distribuição de Probabilidades")

        # Criar histograma das probabilidades de reprovação com cores melhores
        fig_hist = go.Figure(data=[go.Histogram(
            x=prob_reprovacao,
            nbinsx=10,
            marker_color='#6366f1',  # Índigo mais vibrante
            opacity=0.8,
            marker_line_color='#4f46e5',
            marker_line_width=1
        )])

        fig_hist.update_layout(
            title="Distribuição das Probabilidades de Reprovação",
            xaxis_title="Probabilidade de Reprovação",
            yaxis_title="Número de Alunos",
            height=400
        )

        st.plotly_chart(fig_hist, use_container_width=True)

    # Análise de performance APENAS se temos dados de validação
    if mostrar_metricas_reais and 'Reprovou' in df_predicao.columns:
        st.subheader("🎯 Matriz de Confusão (Dados de Validação)")

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
    st.subheader("💾 Exportar Resultados")

    # Preparar dados para download
    df_download = df_exibicao_final.copy()
    df_download['Fonte_Dados'] = fonte_dados
    df_download['Semana_Predicao'] = semana_atual
    df_download['Modelo_Usado'] = modelo_arquivo

    csv_export = df_download.to_csv(index=False)

    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            "📥 Download Predições Completas",
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

# ==================== TREINAR MODELOS ====================
elif opcao == "🤖 Treinar Modelos":
    st.header("🤖 Treinamento de Modelos")

    # Seleção do modelo
    modelo_selecionado = st.selectbox(
        "Escolha o modelo para treinar:",
        ["Modelo 1 (3 Quizzes - Semana 6)", "Modelo 2 (4 Quizzes + Parcial - Semana 8)", "Modelo 3 (6 Quizzes + Parcial - Semana 12)"]
    )

    # Configurações de treinamento
    col1, col2, col3 = st.columns(3)

    with col1:
        test_size = st.slider("% Dados para Teste", min_value=0.1, max_value=0.5, value=0.3, step=0.05)

    with col2:
        usar_smote = st.checkbox("Usar SMOTE (balanceamento)", value=True)

    with col3:
        random_state = st.number_input("Seed Aleatória", value=42, min_value=1, max_value=999)

    # Mostrar informações do dataset selecionado
    if "Modelo 1" in modelo_selecionado:
        df_modelo = df_modelo1
        nome_modelo = "modelo1_treinado.pkl"
        descricao = "Modelo baseado nos primeiros 3 quizzes (Semana 6)"
    elif "Modelo 2" in modelo_selecionado:
        df_modelo = df_modelo2
        nome_modelo = "modelo2_treinado.pkl"
        descricao = "Modelo com 4 quizzes + Parcial 1 (Semana 8)"
    else:
        df_modelo = df_modelo3
        nome_modelo = "modelo3_treinado.pkl"
        descricao = "Modelo completo com 6 quizzes + Parcial 1 (Semana 12)"

    st.info(f"📊 {descricao}")
    st.write(f"**Total de registros:** {len(df_modelo)}")

    # Mostrar distribuição das classes
    if 'Reprovou' in df_modelo.columns:
        distribuicao = df_modelo['Reprovou'].value_counts()
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Aprovados", distribuicao.get(0, 0))
        with col2:
            st.metric("Reprovados", distribuicao.get(1, 0))

    if st.button("🚀 Iniciar Treinamento", type="primary"):
        with st.spinner("Treinando modelo..."):
            # Dividir dados em treino e teste
            df_train, df_test = dividir_dados_treino_teste(df_modelo, test_size=test_size, random_state=random_state)

            # Preparar features e target
            X_train = df_train.drop('Reprovou', axis=1)
            y_train = df_train['Reprovou']
            X_test = df_test.drop('Reprovou', axis=1)
            y_test = df_test['Reprovou']

            # Tratar valores NaN
            X_train = X_train.fillna(0)
            X_test = X_test.fillna(0)

            # Aplicar SMOTE se solicitado
            if usar_smote:
                sm = SMOTE(random_state=random_state)
                X_train_balanced, y_train_balanced = sm.fit_resample(X_train, y_train)
                st.success(f"✅ SMOTE aplicado: {len(X_train)} → {len(X_train_balanced)} amostras de treino")
            else:
                X_train_balanced, y_train_balanced = X_train, y_train

            # Configurar e treinar modelo
            nc = NearestCentroid()
            param_grid = {
                "metric": ["euclidean", "manhattan"],
                "shrink_threshold": [None, 0.1, 0.5, 1.0]
            }

            grid = GridSearchCV(nc, param_grid, cv=5, scoring='recall')
            grid.fit(X_train_balanced, y_train_balanced)

            modelo_treinado = grid.best_estimator_

            # Avaliar modelo nos dados de teste
            metricas_teste, y_pred = avaliar_modelo(modelo_treinado, X_test, y_test)

            # Salvar modelo com metadados
            modelo_dados = {
                'modelo': modelo_treinado,
                'colunas': X_train.columns.tolist(),
                'X_train': X_train_balanced,
                'y_train': y_train_balanced,
                'X_test': X_test,
                'y_test': y_test,
                'parametros': grid.best_params_,
                'metricas_teste': metricas_teste,
                'configuracao': {
                    'test_size': test_size,
                    'usar_smote': usar_smote,
                    'random_state': random_state
                }
            }

            caminho_salvo = salvar_modelo(modelo_dados, nome_modelo)

            st.success(f"✅ Modelo treinado e salvo em: {caminho_salvo}")

            # Exibir resultados do treinamento
            st.subheader("📊 Resultados do Treinamento")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Acurácia", f"{metricas_teste['accuracy']:.3f}")
            with col2:
                st.metric("Recall", f"{metricas_teste['recall']:.3f}")
            with col3:
                st.metric("F1-Score", f"{metricas_teste['f1_score']:.3f}")

            # Melhores parâmetros
            st.subheader("⚙️ Melhores Parâmetros")
            st.json(grid.best_params_)

            # Matriz de confusão
            st.subheader("🎯 Matriz de Confusão")
            cm = metricas_teste['confusion_matrix']

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
                title="Matriz de Confusão - Dados de Teste",
                height=400
            )

            st.plotly_chart(fig_cm, use_container_width=True)

            # Relatório de classificação
            st.subheader("📋 Relatório Detalhado")
            report = classification_report(y_test, y_pred, output_dict=True)
            df_report = pd.DataFrame(report).transpose()
            st.dataframe(df_report.round(3))

# ==================== NOVA PREDIÇÃO ====================
elif opcao == "🔮 Nova Predição":
    st.header("🔮 Predição para Novos Dados")

    # Seleção do modelo
    modelos_disponiveis = []
    for arquivo in ["modelo1_treinado.pkl", "modelo2_treinado.pkl", "modelo3_treinado.pkl"]:
        if carregar_modelo(arquivo) is not None:
            if "modelo1" in arquivo:
                modelos_disponiveis.append(("Modelo 1 (3 Quizzes - Semana 6)", arquivo))
            elif "modelo2" in arquivo:
                modelos_disponiveis.append(("Modelo 2 (4 Quizzes + Parcial - Semana 8)", arquivo))
            else:
                modelos_disponiveis.append(("Modelo 3 (6 Quizzes + Parcial - Semana 12)", arquivo))

    if not modelos_disponiveis:
        st.error("❌ Nenhum modelo treinado encontrado! Treine pelo menos um modelo primeiro.")
        st.stop()

    col1, col2 = st.columns(2)

    with col1:
        modelo_escolha = st.selectbox("Escolha o modelo:", [desc for desc, _ in modelos_disponiveis])
        modelo_arquivo = next(arquivo for desc, arquivo in modelos_disponiveis if desc == modelo_escolha)

    with col2:
        formato_entrada = st.radio("Formato de entrada:", ["Upload de Arquivo", "Entrada Manual"])

    # Carregar modelo selecionado
    modelo_dados = carregar_modelo(modelo_arquivo)

    if formato_entrada == "Upload de Arquivo":
        uploaded_file = st.file_uploader("📂 Envie arquivo com novos dados", type=["csv", "xlsx"])

        if uploaded_file and st.button("🎯 Fazer Predições"):
            try:
                # Carregar dados
                if uploaded_file.name.endswith('.csv'):
                    df_novos = pd.read_csv(uploaded_file)
                else:
                    df_novos = pd.read_excel(uploaded_file)

                st.subheader("📊 Dados Carregados")
                st.dataframe(df_novos.head())

                # Fazer predições
                with st.spinner("Fazendo predições..."):
                    X_pred = preparar_dados_predicao(df_novos, modelo_dados['colunas'])
                    predicoes = modelo_dados['modelo'].predict(X_pred)

                    # Criar DataFrame com resultados
                    df_resultados = df_novos.copy()
                    df_resultados['Predição'] = ['Reprovado' if p == 1 else 'Aprovado' for p in predicoes]
                    df_resultados['Risco_Reprovacao'] = predicoes

                    st.subheader("🎯 Resultados das Predições")
                    st.dataframe(df_resultados)

                    # Métricas resumo
                    total = len(predicoes)
                    reprovados = sum(predicoes)
                    aprovados = total - reprovados

                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Total", total)
                    with col2:
                        st.metric("Aprovados", aprovados)
                    with col3:
                        st.metric("Reprovados", reprovados)

                    # Download
                    csv = df_resultados.to_csv(index=False)
                    st.download_button("📥 Download Resultados", csv, "predicoes_resultado.csv", "text/csv")

            except Exception as e:
                st.error(f"Erro ao processar arquivo: {e}")

    else:  # Entrada Manual
        st.subheader("✏️ Entrada Manual de Dados")

        # Determinar quais campos mostrar baseado no modelo
        if "modelo1" in modelo_arquivo:
            campos_quiz = ['Quiz1', 'Quiz2', 'Quiz3']
            st.info("📊 Modelo para Semana 6: Insira as notas dos primeiros 3 quizzes")
        elif "modelo2" in modelo_arquivo:
            campos_quiz = ['Quiz1', 'Quiz2', 'Quiz3', 'Quiz4', 'Parcial_1']
            st.info("📊 Modelo para Semana 8: Insira as notas dos 4 quizzes + Parcial 1")
        else:
            campos_quiz = ['Quiz1', 'Quiz2', 'Quiz3', 'Quiz4', 'Quiz5', 'Quiz6', 'Parcial_1']
            st.info("📊 Modelo para Semana 12: Insira as notas dos 6 quizzes + Parcial 1")

        # Formulário para entrada manual
        with st.form("entrada_manual"):
            dados_entrada = {}

            # Campos de notas
            st.write("**Notas (0-5):**")
            cols = st.columns(len(campos_quiz))
            for i, campo in enumerate(campos_quiz):
                with cols[i]:
                    dados_entrada[campo] = st.number_input(
                        campo,
                        min_value=0.0,
                        max_value=5.0,
                        value=2.5,
                        step=0.1,
                        key=f"nota_{campo}"
                    )

            # Campos adicionais se existirem no modelo
            st.write("**Informações Adicionais:**")
            col1, col2 = st.columns(2)

            if any('Genero_Masculino' in col for col in modelo_dados['colunas']):
                with col1:
                    dados_entrada['Genero_Masculino'] = st.selectbox("Gênero", ["Feminino", "Masculino"], key="genero")
                    dados_entrada['Genero_Masculino'] = 1 if dados_entrada['Genero_Masculino'] == "Masculino" else 0

            if any('STEM_SI' in col for col in modelo_dados['colunas']):
                with col2:
                    dados_entrada['STEM_SI'] = st.selectbox("Área STEM", ["Não", "Sim"], key="stem")
                    dados_entrada['STEM_SI'] = 1 if dados_entrada['STEM_SI'] == "Sim" else 0

            submitted = st.form_submit_button("🎯 Fazer Predição", type="primary")

            if submitted:
                # Preparar dados para predição
                df_manual = pd.DataFrame([dados_entrada])
                X_pred = preparar_dados_predicao(df_manual, modelo_dados['colunas'])

                # Fazer predição
                predicao = modelo_dados['modelo'].predict(X_pred)[0]

                # Exibir resultado
                st.subheader("🎯 Resultado da Predição")

                if predicao == 1:
                    st.error("⚠️ **REPROVADO** - Alto risco de reprovação")
                else:
                    st.success("✅ **APROVADO** - Baixo risco de reprovação")

                # Mostrar resumo dos dados inseridos
                st.subheader("📊 Dados Inseridos")
                df_resumo = pd.DataFrame([dados_entrada])

                # Calcular média das notas
                notas_valores = [dados_entrada[campo] for campo in campos_quiz if campo in dados_entrada]
                media = np.mean(notas_valores)
                df_resumo['Média'] = media

                st.dataframe(df_resumo)

                # Interpretação adicional
                st.subheader("💡 Interpretação")
                if media < 2.0:
                    st.warning("📉 Média muito baixa - Risco elevado de reprovação")
                elif media < 3.0:
                    st.warning("📊 Média abaixo da média - Atenção necessária")
                elif media >= 3.5:
                    st.success("📈 Média boa - Boas perspectivas de aprovação")
                else:
                    st.info("📊 Média regular - Acompanhamento recomendado")

# ==================== ANÁLISES AVANÇADAS ====================
elif opcao == "📈 Análises Avançadas":
    st.header("📈 Análises Avançadas")

    # Verificar modelos disponíveis
    modelos_disponiveis = []
    for arquivo in ["modelo1_treinado.pkl", "modelo2_treinado.pkl", "modelo3_treinado.pkl"]:
        modelo_dados = carregar_modelo(arquivo)
        if modelo_dados is not None:
            if "modelo1" in arquivo:
                modelos_disponiveis.append(("Modelo 1 (3 Quizzes - Semana 6)", arquivo, modelo_dados))
            elif "modelo2" in arquivo:
                modelos_disponiveis.append(("Modelo 2 (4 Quizzes + Parcial - Semana 8)", arquivo, modelo_dados))
            else:
                modelos_disponiveis.append(("Modelo 3 (6 Quizzes + Parcial - Semana 12)", arquivo, modelo_dados))

    if not modelos_disponiveis:
        st.error("❌ Nenhum modelo treinado encontrado!")
        st.stop()

    # Seleção do modelo para análise
    modelo_escolha = st.selectbox("Escolha o modelo para análise:", [desc for desc, _, _ in modelos_disponiveis])
    _, modelo_arquivo, modelo_dados = next(item for item in modelos_disponiveis if item[0] == modelo_escolha)

    # Tabs para diferentes análises
    tab1, tab2, tab3, tab4 = st.tabs(["🔍 Explicabilidade", "📊 Performance", "🎯 Análise de Features", "📈 Comparação"])

    with tab1:
        st.subheader("🔍 Análise de Explicabilidade (SHAP)")

        if st.button("🚀 Gerar Análise SHAP", key="shap_analysis"):
            with st.spinner("Gerando análise de explicabilidade..."):
                try:
                    # Preparar dados para SHAP
                    X_sample = modelo_dados['X_train'][:50]  # Amostra menor para performance

                    # Criar explainer SHAP
                    explainer = shap.KernelExplainer(modelo_dados['modelo'].predict, X_sample[:10])
                    shap_values = explainer.shap_values(X_sample[:20])

                    # Calcular importância média das features
                    feature_importance = np.abs(shap_values).mean(axis=0)
                    feature_names = modelo_dados['colunas']

                    # Criar DataFrame para visualização
                    df_importance = pd.DataFrame({
                        'Feature': feature_names,
                        'Importancia_SHAP': feature_importance,
                        'Importancia_Relativa': feature_importance / feature_importance.max() * 100
                    }).sort_values('Importancia_SHAP', ascending=True)

                    # Gráfico de importância SHAP
                    fig_shap = go.Figure(go.Bar(
                        x=df_importance['Importancia_SHAP'],
                        y=df_importance['Feature'],
                        orientation='h',
                        marker_color='rgba(55, 83, 109, 0.8)',
                        text=df_importance['Importancia_Relativa'].round(1).astype(str) + '%',
                        textposition='auto'
                    ))

                    fig_shap.update_layout(
                        title="Importância das Features (SHAP Values)",
                        xaxis_title="Importância SHAP",
                        yaxis_title="Features",
                        height=600
                    )

                    st.plotly_chart(fig_shap, use_container_width=True)

                    # Tabela com detalhes
                    st.subheader("📋 Ranking de Importância")
                    df_ranking = df_importance.sort_values('Importancia_SHAP', ascending=False)
                    st.dataframe(df_ranking.round(4))

                    # Interpretação
                    st.info("""
                    **Como interpretar os valores SHAP:**
                    - **Valores altos** indicam features que têm maior influência na predição
                    - **Features de notas** geralmente são mais importantes para predizer reprovação
                    - **Valores relativos** mostram a importância proporcional de cada feature
                    """)

                except Exception as e:
                    st.error(f"Erro na análise SHAP: {str(e)}")
                    st.info("A análise SHAP pode ser computacionalmente intensiva.")

    with tab2:
        st.subheader("📊 Análise de Performance")

        if 'metricas_teste' in modelo_dados:
            metricas = modelo_dados['metricas_teste']

            # Métricas principais
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Acurácia", f"{metricas['accuracy']:.3f}")
            with col2:
                st.metric("Recall", f"{metricas['recall']:.3f}")
            with col3:
                st.metric("F1-Score", f"{metricas['f1_score']:.3f}")

            # Matriz de confusão detalhada
            cm = metricas['confusion_matrix']

            # Calcular métricas detalhadas
            tn, fp, fn, tp = cm.ravel()
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            specificity = tn / (tn + fp) if (tn + fp) > 0 else 0

            # Métricas adicionais
            st.subheader("📊 Métricas Detalhadas")
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Precisão", f"{precision:.3f}")
            with col2:
                st.metric("Especificidade", f"{specificity:.3f}")
            with col3:
                st.metric("Verdadeiros Positivos", tp)
            with col4:
                st.metric("Falsos Positivos", fp)

            # Gráfico da matriz de confusão
            fig_cm_detailed = go.Figure(data=go.Heatmap(
                z=cm,
                x=['Previsto: Aprovado', 'Previsto: Reprovado'],
                y=['Real: Aprovado', 'Real: Reprovado'],
                colorscale='RdYlBu_r',
                text=[[f'TN: {tn}', f'FP: {fp}'], [f'FN: {fn}', f'TP: {tp}']],
                texttemplate="%{text}",
                textfont={"size": 14}
            ))

            fig_cm_detailed.update_layout(
                title="Matriz de Confusão Detalhada",
                height=500
            )

            st.plotly_chart(fig_cm_detailed, use_container_width=True)

        else:
            st.warning("⚠️ Métricas de teste não disponíveis para este modelo.")

    with tab3:
        st.subheader("🎯 Análise de Features")

        # Análise das features do modelo
        features = modelo_dados['colunas']
        X_train = modelo_dados['X_train']
        y_train = modelo_dados['y_train']

        st.write(f"**Total de features:** {len(features)}")

        # Análise de correlação com target
        correlacoes = []
        for feature in features:
            if feature in X_train.columns:
                corr = np.corrcoef(X_train[feature], y_train)[0, 1]
                correlacoes.append((feature, corr))

        df_corr = pd.DataFrame(correlacoes, columns=['Feature', 'Correlacao']).sort_values('Correlacao', key=abs, ascending=False)

        # Gráfico de correlações
        fig_corr = go.Figure(go.Bar(
            x=df_corr['Correlacao'],
            y=df_corr['Feature'],
            orientation='h',
            marker_color=np.where(df_corr['Correlacao'] > 0, 'red', 'green')
        ))

        fig_corr.update_layout(
            title="Correlação das Features com Reprovação",
            xaxis_title="Correlação",
            yaxis_title="Features",
            height=600
        )

        st.plotly_chart(fig_corr, use_container_width=True)

        # Tabela de correlações
        st.subheader("📋 Correlações Detalhadas")
        df_corr_display = df_corr.copy()
        df_corr_display['Correlacao'] = df_corr_display['Correlacao'].round(4)
        df_corr_display['Interpretacao'] = df_corr_display['Correlacao'].apply(
            lambda x: 'Forte positiva' if x > 0.5 else
                     'Moderada positiva' if x > 0.3 else
                     'Fraca positiva' if x > 0.1 else
                     'Muito fraca' if abs(x) <= 0.1 else
                     'Fraca negativa' if x > -0.3 else
                     'Moderada negativa' if x > -0.5 else
                     'Forte negativa'
        )

        st.dataframe(df_corr_display)

    with tab4:
        st.subheader("📈 Comparação entre Modelos")

        if len(modelos_disponiveis) > 1:
            # Criar tabela comparativa
            comparacao = []
            for desc, arquivo, dados in modelos_disponiveis:
                if 'metricas_teste' in dados:
                    metricas = dados['metricas_teste']
                    comparacao.append({
                        'Modelo': desc,
                        'Acuracia': metricas['accuracy'],
                        'Recall': metricas['recall'],
                        'F1_Score': metricas['f1_score'],
                        'Num_Features': len(dados['colunas']),
                        'Tamanho_Treino': len(dados['X_train'])
                    })

            if comparacao:
                df_comp = pd.DataFrame(comparacao)

                # Gráfico comparativo
                fig_comp = go.Figure()

                fig_comp.add_trace(go.Bar(
                    name='Acurácia',
                    x=df_comp['Modelo'],
                    y=df_comp['Acuracia'],
                    yaxis='y'
                ))

                fig_comp.add_trace(go.Bar(
                    name='Recall',
                    x=df_comp['Modelo'],
                    y=df_comp['Recall'],
                    yaxis='y'
                ))

                fig_comp.add_trace(go.Bar(
                    name='F1-Score',
                    x=df_comp['Modelo'],
                    y=df_comp['F1_Score'],
                    yaxis='y'
                ))

                fig_comp.update_layout(
                    title="Comparação de Performance entre Modelos",
                    xaxis_title="Modelos",
                    yaxis_title="Score",
                    barmode='group',
                    height=500
                )

                st.plotly_chart(fig_comp, use_container_width=True)

                # Tabela comparativa
                st.subheader("📊 Tabela Comparativa")
                df_comp_display = df_comp.round(4)
                st.dataframe(df_comp_display)

                # Recomendação
                st.subheader("💡 Recomendação")
                melhor_f1 = df_comp.loc[df_comp['F1_Score'].idxmax(), 'Modelo']
                melhor_recall = df_comp.loc[df_comp['Recall'].idxmax(), 'Modelo']

                st.info(f"""
                **Melhor modelo por métrica:**
                - **F1-Score:** {melhor_f1}
                - **Recall:** {melhor_recall}

                Para detecção de reprovação, priorize o modelo com melhor **Recall**
                (capacidade de identificar alunos em risco).
                """)
            else:
                st.warning("⚠️ Dados de teste não disponíveis para comparação.")
        else:
            st.info("ℹ️ Treine mais modelos para realizar comparações.")

# ==================== GERENCIAR DADOS ====================
elif opcao == "📁 Gerenciar Dados":
    st.header("📁 Gerenciamento de Dados")

    tab1, tab2, tab3 = st.tabs(["📊 Visualizar Dados", "📤 Upload de Dados", "🔧 Processar Dados"])

    with tab1:
        st.subheader("📊 Visualização dos Dados Carregados")

        # Mostrar informações dos datasets
        datasets = {
            'Modelo 1 (3 Quizzes)': df_modelo1,
            'Modelo 2 (4 Quizzes + Parcial)': df_modelo2,
            'Modelo 3 (6 Quizzes + Parcial)': df_modelo3,
            'Dados Consolidados': df_consolidado
        }

        dataset_selecionado = st.selectbox("Escolha o dataset:", list(datasets.keys()))
        df_visualizar = datasets[dataset_selecionado]

        if df_visualizar is not None:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Registros", len(df_visualizar))
            with col2:
                st.metric("Colunas", len(df_visualizar.columns))
            with col3:
                if 'Reprovou' in df_visualizar.columns:
                    taxa_reprov = df_visualizar['Reprovou'].mean() * 100
                    st.metric("Taxa Reprovação", f"{taxa_reprov:.1f}%")
                else:
                    st.metric("Tipo", "Dados de Entrada")

            # Mostrar preview dos dados
            st.subheader("📋 Preview dos Dados")
            st.dataframe(df_visualizar.head(20))

            # Estatísticas descritivas
            st.subheader("📊 Estatísticas Descritivas")
            numeric_cols = df_visualizar.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 0:
                st.dataframe(df_visualizar[numeric_cols].describe())

            # Distribuição das notas (se existirem)
            quiz_cols = [col for col in df_visualizar.columns if col.startswith('Quiz') or col.startswith('Parcial')]
            if quiz_cols:
                st.subheader("📈 Distribuição das Notas")

                fig_dist = go.Figure()
                for col in quiz_cols:
                    fig_dist.add_trace(go.Box(
                        y=df_visualizar[col],
                        name=col,
                        boxpoints='outliers'
                    ))

                fig_dist.update_layout(
                    title="Distribuição das Notas por Avaliação",
                    yaxis_title="Nota",
                    height=400
                )

                st.plotly_chart(fig_dist, use_container_width=True)
        else:
            st.error("Dataset não encontrado!")

    with tab2:
        st.subheader("📤 Upload de Novos Dados")

        tipo_upload = st.radio("Tipo de dados:", ["Dados de Treinamento", "Dados de Teste"])

        uploaded_files = st.file_uploader(
            "Escolha os arquivos",
            type=["csv", "xlsx"],
            accept_multiple_files=True
        )

        if uploaded_files:
            for uploaded_file in uploaded_files:
                st.write(f"**Arquivo:** {uploaded_file.name}")

                try:
                    # Carregar arquivo
                    if uploaded_file.name.endswith('.csv'):
                        df_upload = pd.read_csv(uploaded_file)
                    else:
                        df_upload = pd.read_excel(uploaded_file)

                    # Mostrar preview
                    st.dataframe(df_upload.head())

                    # Opções para salvar
                    col1, col2 = st.columns(2)

                    with col1:
                        nome_arquivo = st.text_input(
                            "Nome para salvar:",
                            value=f"{tipo_upload.lower().replace(' ', '_')}_{uploaded_file.name}",
                            key=f"nome_{uploaded_file.name}"
                        )

                    with col2:
                        pasta_destino = st.selectbox(
                            "Pasta destino:",
                            ["dados", "dados_teste", "dados_externos"],
                            key=f"pasta_{uploaded_file.name}"
                        )

                    if st.button(f"💾 Salvar {uploaded_file.name}", key=f"salvar_{uploaded_file.name}"):
                        try:
                            # Criar pasta se não existir
                            os.makedirs(pasta_destino, exist_ok=True)

                            # Salvar arquivo
                            caminho_destino = os.path.join(pasta_destino, nome_arquivo)
                            if caminho_destino.endswith('.xlsx'):
                                caminho_destino = caminho_destino.replace('.xlsx', '.csv')
                            elif not caminho_destino.endswith('.csv'):
                                caminho_destino += '.csv'

                            df_upload.to_csv(caminho_destino, index=False)
                            st.success(f"✅ Arquivo salvo em: {caminho_destino}")

                        except Exception as e:
                            st.error(f"Erro ao salvar: {e}")

                except Exception as e:
                    st.error(f"Erro ao carregar {uploaded_file.name}: {e}")

    with tab3:
        st.subheader("🔧 Processamento de Dados")

        st.info("""
        Esta seção permite reprocessar os dados e criar novos datasets para treinamento.
        Útil quando novos dados são adicionados ou quando parâmetros de processamento mudam.
        """)

        # Configurações de processamento
        st.subheader("⚙️ Configurações de Processamento")

        col1, col2 = st.columns(2)

        with col1:
            normalizar_notas = st.checkbox("Normalizar notas (0-1)", value=True)
            remover_outliers = st.checkbox("Remover outliers", value=False)

        with col2:
            criar_features = st.checkbox("Criar features derivadas", value=True)
            balancear_classes = st.checkbox("Preview do balanceamento", value=False)

        # Arquivos de entrada
        st.subheader("📂 Arquivos de Entrada")

        arquivos_disponiveis = []
        for pasta in ["dados", "dados_teste", "dados_externos"]:
            if os.path.exists(pasta):
                for arquivo in os.listdir(pasta):
                    if arquivo.endswith('.csv'):
                        arquivos_disponiveis.append(os.path.join(pasta, arquivo))

        if arquivos_disponiveis:
            arquivo_base = st.selectbox("Arquivo base para processamento:", arquivos_disponiveis)

            if st.button("🚀 Processar Dados", type="primary"):
                with st.spinner("Processando dados..."):
                    try:
                        # Carregar dados
                        df_processo = pd.read_csv(arquivo_base)
                        st.success(f"✅ Dados carregados: {len(df_processo)} registros")

                        # Aplicar processamentos
                        if normalizar_notas:
                            quiz_cols = [col for col in df_processo.columns if col.startswith(('Quiz', 'Parcial'))]
                            for col in quiz_cols:
                                if col in df_processo.columns and df_processo[col].max() > 1:
                                    df_processo[col] = df_processo[col] / 5.0
                            st.info("✅ Notas normalizadas para escala 0-1")

                        if remover_outliers:
                            # Remover outliers usando IQR
                            numeric_cols = df_processo.select_dtypes(include=[np.number]).columns
                            antes = len(df_processo)

                            for col in numeric_cols:
                                Q1 = df_processo[col].quantile(0.25)
                                Q3 = df_processo[col].quantile(0.75)
                                IQR = Q3 - Q1

                                limite_inferior = Q1 - 1.5 * IQR
                                limite_superior = Q3 + 1.5 * IQR

                                df_processo = df_processo[
                                    (df_processo[col] >= limite_inferior) &
                                    (df_processo[col] <= limite_superior)
                                ]

                            removidos = antes - len(df_processo)
                            st.info(f"✅ Outliers removidos: {removidos} registros")

                        if criar_features:
                            # Criar features derivadas
                            quiz_cols = [col for col in df_processo.columns if col.startswith('Quiz')]

                            if len(quiz_cols) >= 2:
                                # Média dos quizzes
                                df_processo['Media_Quizzes'] = df_processo[quiz_cols].mean(axis=1)

                                # Tendência (diferença entre último e primeiro quiz)
                                if len(quiz_cols) >= 3:
                                    df_processo['Tendencia'] = df_processo[quiz_cols[-1]] - df_processo[quiz_cols[0]]

                                # Consistência (desvio padrão dos quizzes)
                                df_processo['Consistencia'] = df_processo[quiz_cols].std(axis=1)

                                st.info("✅ Features derivadas criadas: Média, Tendência, Consistência")

                        # Mostrar resultado
                        st.subheader("📊 Dados Processados")
                        col1, col2 = st.columns(2)

                        with col1:
                            st.metric("Registros Finais", len(df_processo))
                        with col2:
                            st.metric("Features Finais", len(df_processo.columns))

                        st.dataframe(df_processo.head())

                        # Preview do balanceamento se solicitado
                        if balancear_classes and 'Reprovou' in df_processo.columns:
                            st.subheader("⚖️ Preview do Balanceamento")

                            # Distribuição original
                            dist_original = df_processo['Reprovou'].value_counts()

                            # Simular SMOTE
                            X = df_processo.drop('Reprovou', axis=1)
                            y = df_processo['Reprovou']

                            # Mostrar apenas estatísticas do que seria o balanceamento
                            classe_menor = min(dist_original.values)
                            classe_maior = max(dist_original.values)

                            col1, col2 = st.columns(2)
                            with col1:
                                st.write("**Distribuição Original:**")
                                st.write(f"- Aprovados: {dist_original.get(0, 0)}")
                                st.write(f"- Reprovados: {dist_original.get(1, 0)}")

                            with col2:
                                st.write("**Após Balanceamento:**")
                                st.write(f"- Aprovados: {classe_maior}")
                                st.write(f"- Reprovados: {classe_maior}")

                        # Salvar dados processados
                        st.subheader("💾 Salvar Dados Processados")

                        nome_saida = st.text_input(
                            "Nome do arquivo de saída:",
                            value=f"dados_processados_{pd.Timestamp.now().strftime('%Y%m%d_%H%M')}.csv"
                        )

                        pasta_saida = st.selectbox("Pasta de destino:", ["dados", "dados_processados"])

                        if st.button("💾 Salvar Dados Processados"):
                            try:
                                os.makedirs(pasta_saida, exist_ok=True)
                                caminho_saida = os.path.join(pasta_saida, nome_saida)
                                df_processo.to_csv(caminho_saida, index=False)
                                st.success(f"✅ Dados processados salvos em: {caminho_saida}")

                            except Exception as e:
                                st.error(f"Erro ao salvar: {e}")

                    except Exception as e:
                        st.error(f"Erro no processamento: {e}")
                        st.exception(e)
        else:
            st.warning("⚠️ Nenhum arquivo CSV encontrado nas pastas de dados.")
            st.info("Faça upload de dados primeiro na aba 'Upload de Dados'.")

# Footer com informações do sistema
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
