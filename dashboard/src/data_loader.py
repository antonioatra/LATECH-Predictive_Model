# Arquivo direcionado a toda a lógica de carregamento de dados da aplicação
import pandas as pd
import streamlit as st
import os

def carregar_dados_processados():
    """Carrega dados já processados salvos"""
    try:
        df_modelo1 = pd.read_csv('../notebooks/dados/dados_modelo1.csv')
        df_modelo2 = pd.read_csv('../notebooks/dados/dados_modelo2.csv')
        df_modelo3 = pd.read_csv('../notebooks/dados/dados_modelo3.csv')
        df_consolidado = pd.read_csv('../notebooks/dados/dados_consolidado.csv')
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
            "semana6": "../notebooks/dados/teste_semana6.csv",
            "semana8": "../notebooks/dados/teste_semana8.csv",
            "semana12": "../notebooks/dados/teste_semana12.csv"
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