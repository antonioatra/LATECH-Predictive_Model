# Arquivo direcionado a criação de gráficos do dashboard
import plotly.graph_objects as go
import pandas as pd

def criar_grafico_pizza(aprovados, reprovados, semana):
    """Cria e retorna uma figura Plotly de gráfico de pizza."""
    valores = [aprovados, reprovados]
    labels = [f'Aprobados ({aprovados})', f'Reprobados ({reprovados})']
    colors = ['#22c55e', '#ef4444']
    
    fig = go.Figure(data=[go.Pie(
        labels=labels, 
        values=valores,
        marker=dict(colors=colors),
        textinfo='label+percent',
        textfont_size=14,
        hole=0.3
    )])
    
    fig.update_layout(
        title=f"Predicciones - Semana {semana} | Predições - Semana {semana}",
        showlegend=True,
        height=400
    )
    return fig

def criar_histograma_medias(df_resultados):
    # 1. Separar médias e calcular estatísticas (lógica interna da função)
    medias_aprovados = df_resultados[df_resultados['Predição'] == 'Aprobado | Aprovado']['Media_Atual']
    medias_reprovados = df_resultados[df_resultados['Predição'] == 'Reprobado | Reprovado']['Media_Atual']
    
    media_aprovados_calc = medias_aprovados.mean() if len(medias_aprovados) > 0 else 0
    media_reprovados_calc = medias_reprovados.mean() if len(medias_reprovados) > 0 else 0

    # 2. Criar a figura do histograma
    fig_hist = go.Figure()
    
    fig_hist.add_trace(go.Histogram(
        x=medias_aprovados, name=f'Aprobados | Aprovados (media: {media_aprovados_calc:.2f})',
        nbinsx=15, marker_color='#22c55e', opacity=0.7,
        marker_line_color='#16a34a', marker_line_width=1
    ))
    
    fig_hist.add_trace(go.Histogram(
        x=medias_reprovados, name=f'Reprobados | Reprovados (media: {media_reprovados_calc:.2f})',
        nbinsx=15, marker_color='#ef4444', opacity=0.7,
        marker_line_color='#dc2626', marker_line_width=1
    ))
    
    fig_hist.add_vline(
        x=media_aprovados_calc, line_dash="dash", line_color="#16a34a", line_width=2,
        annotation_text=f"Mediade los Aprobados: {media_aprovados_calc:.2f} | Média Aprovados: {media_aprovados_calc:.2f}", annotation_position="top"
    )
    
    fig_hist.add_vline(
        x=media_reprovados_calc, line_dash="dash", line_color="#dc2626", line_width=2,
        annotation_text=f"Mediade los Reprobados: {media_reprovados_calc:.2f} | Média Reprovados: {media_reprovados_calc:.2f}", annotation_position="bottom"
    )
    
    fig_hist.update_layout(
        barmode='overlay', xaxis_title="Media de las Notas | Média das Notas", yaxis_title="Número de Alunos | Quantidade de Alunos",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=400, hovermode='x unified'
    )
    
    # 3. Retornar os resultados
    return fig_hist, media_aprovados_calc, media_reprovados_calc