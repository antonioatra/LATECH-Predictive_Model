# Arquivo direcionado a toda lógica de Machine Learning utilizada na aplicação
import pandas as pd
import numpy as np
import os
import pickle
import streamlit as st
from sklearn.metrics import recall_score, f1_score, confusion_matrix
    
def carregar_modelo(nome_arquivo):
    """Carrega modelo treinado"""
    try:
        caminho = os.path.join("../notebooks/modelos_treinados", nome_arquivo)
        with open(caminho, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

def preparar_dados_predicao(df_dados, colunas_modelo):
    """Prepara dados para predição garantindo que todas as features estejam presentes"""
    X_pred = pd.DataFrame(index=df_dados.index)
    
    colunas_criticas_ausentes = []
    
    for col in colunas_modelo:
        if col in df_dados.columns:
            # Usar dados reais e normalizar se necessário
            valores = df_dados[col].copy()
            if valores.max() > 1 and col.startswith(('Quiz', 'Parcial')):
                valores = valores / 5.0  # Normalizar notas
            X_pred[col] = valores
        else:
            # Registrar colunas críticas ausentes
            if col.startswith(('Quiz', 'Parcial', 'TempoQ')):
                colunas_criticas_ausentes.append(col)
            
            # Valores padrão para features ausentes
            if 'Genero_Masculino' in col:
                X_pred[col] = np.random.choice([0, 1], len(df_dados), p=[0.4, 0.6])
            elif 'STEM_SI' in col:
                X_pred[col] = np.random.choice([0, 1], len(df_dados), p=[0.3, 0.7])
            else:
                X_pred[col] = 0
    
    # Alertar se houver colunas críticas ausentes
    if colunas_criticas_ausentes:
        st.warning(f"⚠️ **Atenção:** Colunas preenchidas com valores padrão (podem afetar predições): {', '.join(colunas_criticas_ausentes)}")
    
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
