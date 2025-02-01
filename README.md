# 📊 Dashboard de IDH nos Estados Brasileiros

Este repositório contém um **dashboard interativo** desenvolvido em Python utilizando **Streamlit**, **Pandas** e **Plotly** para visualizar indicadores do **IDH (Índice de Desenvolvimento Humano)** nos estados brasileiros.

## ✨ Funcionalidades
- 📊 **Visualização do IDH Médio** por estado.
- 📈 **Comparativo entre os 5 estados com maior e menor IDH**.
- 💰 **Análise de IDH Renda**: Identifica os estados com menor IDH relacionado à renda.
- 🏥 **IDHM Longevidade**: Gráfico interativo para seleção de estados.
- 👥 **Estados mais populosos**: Top 10 estados com maior população.
- 🎓 **Estados com menor IDH Educação**.

## 🛠 Tecnologias Utilizadas
- **Python**
- **Streamlit**
- **Pandas**
- **Plotly**
- **Seaborn**
- **Matplotlib**

## 📂 Dataset Utilizado

O projeto utiliza o arquivo "Cidades brasileiras.xlsx", que contém dados sobre:

IDH e seus componentes (IDH Renda, IDHM Longevidade, IDHM Educação).

População residente por estado.

Nomes dos estados e municípios.

Os dados são carregados a partir da aba "BRAZIL_CITIES" do arquivo Excel.

## 📁 Crie e Ative um Ambiente Virtual (Opcional)
python -m venv venv  # Criar ambiente virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

## 📁 Instale as depedências
pip install -r requirements.txt

## 📁 Execute o Dashboard
streamlit run dashboard.py
