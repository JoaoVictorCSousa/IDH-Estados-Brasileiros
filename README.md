# 📊 Dashboard de IDH nos Estados Brasileiros

Este repositório contém um **dashboard interativo** desenvolvido em Python utilizando **Streamlit**, **Pandas** e **Plotly** para visualizar indicadores do **IDH (Índice de Desenvolvimento Humano)** nos estados brasileiros. O objetivo principal é proporcionar uma análise intuitiva e visual dos dados relacionados ao desenvolvimento socioeconômico dos estados do Brasil.

## ✨ Funcionalidades
- 📊 **Visualização do IDH Médio** por estado, permitindo comparar os diferentes estados do Brasil.
- 📈 **Comparativo entre os 5 estados com maior e menor IDH**, destacando diferenças regionais.
- 💰 **Análise de IDH Renda**: Identifica os estados com menor IDH relacionado à renda, mostrando desigualdades econômicas.
- 🏥 **IDHM Longevidade**: Permite visualizar indicadores de longevidade nos estados, com opção de seleção interativa.
- 👥 **Estados mais populosos**: Exibe os 10 estados mais populosos, permitindo entender a distribuição populacional.
- 🎓 **Estados com menor IDH Educação**, mostrando quais estados apresentam piores indicadores educacionais.

## 🛠 Tecnologias Utilizadas
- **Python** - Linguagem principal do projeto.
- **Streamlit** - Para criação da interface interativa do dashboard.
- **Pandas** - Manipulação e tratamento de dados.
- **Plotly** - Visualização interativa de dados.
- **Seaborn** - Estilização de gráficos.
- **Matplotlib** - Suporte para criação de gráficos.

## 📂 Dataset Utilizado
O projeto utiliza o arquivo **"Cidades brasileiras.xlsx"**, que contém dados extraídos de fontes oficiais sobre:
- **IDH e seus componentes** (IDH Renda, IDHM Longevidade, IDHM Educação).
- **População residente por estado**.
- **Nomes dos estados e municípios**.

Os dados são carregados a partir da aba **"BRAZIL_CITIES"** do arquivo Excel e processados para gerar os gráficos interativos no dashboard.

## 🚀 Como Executar o Projeto

### 1️⃣ Clone o Repositório
```sh
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2️⃣ Crie e Ative um Ambiente Virtual (Opcional)
```sh
python -m venv venv  # Criar ambiente virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

### 3️⃣ Instale as Dependências
```sh
pip install -r requirements.txt
```

### 4️⃣ Execute o Dashboard
```sh
streamlit run dashboard.py
```
Isso abrirá o dashboard no navegador e permitirá a interação com os dados.
