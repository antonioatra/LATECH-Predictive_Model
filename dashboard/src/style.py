# Arquivo dedicado a todos os elementos de estilização da aplicação
import streamlit as st

def carregar_css():
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

def highlight_predictions(row):
    colors = []
    for col in row.index:
        if col == 'Predição':
            colors.append('background-color: #fca5a5; color: #7f1d1d;' if row[col] == 'Reprovado' else 'background-color: #86efac; color: #14532d;')
        else:
            colors.append('')
    return colors

def criar_card_metrica(titulo, valor, cor_fundo):
    st.markdown(f"""
    <div class="metric-card" style="background: {cor_fundo};">
        <div class="metric-value">{valor}</div>
        <div class="metric-label">{titulo}</div>
    </div>
    """, unsafe_allow_html=True)

def criar_footer():
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