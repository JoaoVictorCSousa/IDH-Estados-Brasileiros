import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Configure the style for a more vibrant look
st.set_page_config(page_title='Dashboard de Estados Brasileiros com menor IDH', layout='wide')
sns.set_palette("summer") 
# Create a file uploader in Streamlit
st.title('🎒💸💊 Relação de IDH nos Estados Brasileiros 🎒💸💊')
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f5f5dc;
    }
    h1 {
        color: #2a9d8f;
        text-align: center;
    }
    .stDataFrame, .st-bar-chart, .stPlotlyChart {
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0px 4px 15px rgba(0, 128, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Carregar o arquivo Excel
file_path = 'Cidades brasileiras.xlsx'  # Substitua pelo caminho do arquivo
data = pd.read_excel(file_path, sheet_name='BRAZIL_CITIES')

# Processar os dados
# Certifique-se de que os nomes das colunas estejam corretos
data_grouped = data.groupby('ESTADO')['IDH'].mean().reset_index()
data_grouped = data_grouped.rename(columns={'IDH': 'IDH Médio'})

fig = px.bar(
    data_grouped,
    x='ESTADO',
    y='IDH Médio',
    title='Distribuição do IDH Médio por Estado',
    labels={'IDH Médio': 'IDH Médio', 'Estado': 'Estados'},
    color='IDH Médio',  # Adiciona uma escala de cores
    color_continuous_scale='Viridis'
)

# Exibir no Streamlit
st.title('Gráfico de Barras: IDH por Estado')
st.plotly_chart(fig)

# Processar os dados: calcular a média de IDH_Renda por estado
data_grouped = data.groupby('ESTADO')['IDH_Renda'].mean().reset_index()
data_grouped = data_grouped.rename(columns={'IDH_Renda': 'IDH de Renda Médio'})

# Selecionar os 5 estados com menor IDH de Renda Médio
top_5_lowest_idh_renda = data_grouped.nsmallest(5, 'IDH de Renda Médio')


# Calcular a média de IDH por estado
data_grouped = data.groupby('ESTADO')['IDH'].mean().reset_index()
data_grouped = data_grouped.rename(columns={'IDH': 'IDH Médio'})

# Selecionar os 5 estados com maior e menor IDH Médio
top_5_highest_idh = data_grouped.nlargest(5, 'IDH Médio')
top_5_lowest_idh = data_grouped.nsmallest(5, 'IDH Médio')

# Resetar índices para alinhamento nos gráficos
top_5_highest_idh.reset_index(drop=True, inplace=True)
top_5_lowest_idh.reset_index(drop=True, inplace=True)

# Criar gráficos lado a lado para cada par
fig = go.Figure()

for i in range(5):
    # Adicionar barras do estado com maior IDH
    fig.add_trace(go.Bar(
        x=[f"Melhor Estado ({top_5_highest_idh.loc[i, 'ESTADO']})"],
        y=[top_5_highest_idh.loc[i, 'IDH Médio']],
        name=f"Melhor: {top_5_highest_idh.loc[i, 'ESTADO']}",
        marker_color='green'
    ))

    # Adicionar barras do estado com menor IDH
    fig.add_trace(go.Bar(
        x=[f"Pior Estado ({top_5_lowest_idh.loc[i, 'ESTADO']})"],
        y=[top_5_lowest_idh.loc[i, 'IDH Médio']],
        name=f"Pior: {top_5_lowest_idh.loc[i, 'ESTADO']}",
        marker_color='red'
    ))

# Atualizar layout do gráfico
fig.update_layout(
    title='Comparação entre Estados com os Melhores e Piores IDHs',
    barmode='group',
    xaxis_title='Estados',
    yaxis_title='IDH Médio',
    legend_title='Categoria',
    template='plotly_white'
)

# Exibir no Streamlit
st.title('Comparação de IDH por Estados: Top 5 Melhores x Top 5 Piores')
st.plotly_chart(fig)

# Agrupar por estado e calcular a média de IDHM_Longevidade
data_grouped = data.groupby('ESTADO')['IDHM_Longevidade'].mean().reset_index()
data_grouped = data_grouped.rename(columns={'IDHM_Longevidade': 'IDHM Longevidade Médio'})

# Interface para filtrar os estados (começando sem nenhum estado selecionado)
st.title('Gráfico Interativo de IDHM Longevidade')
selected_states = st.multiselect(
    'Adicione estados para visualizar:',
    options=data_grouped['ESTADO'].unique(),
    default=[]  # Nenhum estado selecionado por padrão
)

# Filtrar os dados com base na seleção
filtered_data = data_grouped[data_grouped['ESTADO'].isin(selected_states)]

# Verificar se há estados selecionados
if not selected_states:
    st.warning('Nenhum estado selecionado. Por favor, adicione estados ao filtro.')
else:
    # Criar o gráfico
    fig = px.bar(
        filtered_data,
        x='ESTADO',
        y='IDHM Longevidade Médio',
        title='IDHM Longevidade por Estado',
        labels={'IDHM Longevidade Médio': 'IDHM Longevidade Médio', 'Estado': 'Estado'},
        color='IDHM Longevidade Médio',  # Adiciona uma escala de cores
        color_continuous_scale='Viridis'
    )

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)

# Agrupar por estado e somar a população residente
data_grouped = data.groupby('ESTADO')['POPULAÇÃO RESIDENTE'].sum().reset_index()
data_grouped = data_grouped.rename(columns={'POPULAÇÃO RESIDENTE': 'População Residente Total'})

# Filtrar os 10 estados mais populosos
top_10_states = data_grouped.nlargest(10, 'População Residente Total')

# Criar o gráfico
fig = px.bar(
    top_10_states,
    x='ESTADO',
    y='População Residente Total',
    title='Top 10 Estados Mais Populosos',
    labels={'População Residente Total': 'População Residente', 'ESTADO': 'Estado'},
    color='População Residente Total',  # Adiciona uma escala de cores
    color_continuous_scale='Viridis'
)

# Exibir o gráfico no Streamlit
st.title('Gráfico dos Estados Mais Populosos')
st.plotly_chart(fig)

# Agrupar por estado e calcular a média do IDHM Educação
data_grouped = data.groupby('ESTADO')['IDHM_Educacao'].mean().reset_index()
data_grouped = data_grouped.rename(columns={'IDHM_Educacao': 'Média IDH Educação'})

# Filtrar os 10 estados com menor IDH Educação
bottom_10_states = data_grouped.nsmallest(10, 'Média IDH Educação')

# Criar o gráfico
fig = px.bar(
    bottom_10_states,
    x='ESTADO',
    y='Média IDH Educação',
    title='10 Estados com Menor IDH Educação',
    labels={'Média IDH Educação': 'Média IDH Educação', 'ESTADO': 'Estado'},
    color='Média IDH Educação',  # Adiciona uma escala de cores
    color_continuous_scale='Reds'
)

# Exibir o gráfico no Streamlit
st.title('Gráfico dos Estados com Menor IDH Educação')
st.plotly_chart(fig)