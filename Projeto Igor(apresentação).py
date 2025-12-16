import streamlit as st
from datetime import datetime

# =====================================================
# CONFIGURAÇÃO DA PÁGINA
# =====================================================
st.set_page_config(
    page_title="Relatório Executivo | Icatu Seguros",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# CSS EXECUTIVO CUSTOMIZADO
# =====================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');

* { font-family: 'Montserrat', sans-serif; }

.main-header {
    background: linear-gradient(135deg, #667eea, #764ba2);
    padding: 2.2rem;
    border-radius: 18px;
    color: white;
    margin-bottom: 2rem;
    box-shadow: 0 12px 30px rgba(0,0,0,0.15);
}

.section-title {
    margin-top: 2.5rem;
    font-weight: 600;
    border-bottom: 3px solid #764ba2;
    padding-bottom: .5rem;
}

.metric-card {
    background: white;
    padding: 1.6rem;
    border-radius: 15px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.06);
    border-left: 6px solid #764ba2;
}

.highlight {
    background: linear-gradient(135deg, #f093fb, #f5576c);
    color: white;
    padding: 1.6rem;
    border-radius: 15px;
}

.advisor-card {
    background: white;
    padding: 1.6rem;
    border-radius: 15px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.06);
    margin-bottom: 1.5rem;
    border-top: 5px solid;
}

.gold { border-top-color: #FFD700; }
.silver { border-top-color: #C0C0C0; }
.bronze { border-top-color: #CD7F32; }

.tag {
    background: #f0f2f6;
    padding: 5px 12px;
    border-radius: 20px;
    font-size: .85rem;
    margin-right: 6px;
}

.footer {
    margin-top: 3rem;
    text-align: center;
    color: #666;
    font-size: .9rem;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# CABEÇALHO
# =====================================================
st.markdown("""
<div class="main-header">
    <h1>📊 Relatório de Produção – Icatu Seguros</h1>
    <p>Período analisado: até 12/12/2025 | Indicador: PA – Prêmio Anual</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# VISÃO GERAL
# =====================================================
st.markdown('<h2 class="section-title">1. Visão Geral da Produção</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h3>PA Total</h3>
        <h1>R$ 1.912.452</h1>
        <p>Produção acumulada no período</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3>Ranking Geral</h3>
        <h1>2ª colocação</h1>
        <p>Posição no ranking anual</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h3>Participação</h3>
        <h1>21%</h1>
        <p>Do total de vendas da operação</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# DESTAQUES
# =====================================================
st.markdown('<h2 class="section-title">2. Destaques de Performance</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="highlight">
        <h3>Maior PA Individual</h3>
        <h1>R$ 80.356</h1>
        <p>Registrado em 29/04/2025</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight" style="background: linear-gradient(135deg, #4facfe, #00f2fe);">
        <h3>Melhor Mês do Ano</h3>
        <h1>Outubro</h1>
        <p>R$ 524.692 em PA</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# TOP ASSESSORES
# =====================================================
st.markdown('<h2 class="section-title">3. Top 3 Assessores em Produção</h2>', unsafe_allow_html=True)

advisors = [
    ("🥇 Johannes Schoof", "Condado", "R$ 126.610", "4", "Igor Sobroza", "gold"),
    ("🥈 Gabriel Correia", "Les Gars", "R$ 71.559", "4", "Igor Sobroza", "silver"),
    ("🥉 Bernardo Cordeiro", "Les Gars", "R$ 64.481", "4", "Igor Sobroza", "bronze"),
]

for name, branch, pa, proposals, specialist, cls in advisors:
    st.markdown(f"""
    <div class="advisor-card {cls}">
        <h3>{name}</h3>
        <span class="tag">Filial: {branch}</span>
        <span class="tag">Propostas: {proposals}</span>
        <h2 style="color:#764ba2;">{pa}</h2>
        <p><strong>Especialista:</strong> {specialist}</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# EVOLUÇÃO ANUAL
# =====================================================
st.markdown('<h2 class="section-title">4. Evolução em Relação ao Ano Anterior</h2>', unsafe_allow_html=True)

st.markdown("""
<p>
A produção da Icatu Seguros apresentou crescimento expressivo em relação ao ano anterior.
</p>
<ul>
<li><strong>PA 2024:</strong> R$ 1.398.937</li>
<li><strong>PA 2025 (até 16/12):</strong> R$ 1.997.761</li>
</ul>
<p>
Isso representa um crescimento absoluto de <strong>R$ 598.824</strong>, equivalente a <strong>42,8%</strong>,
além da evolução no ranking do 4º para o 2º lugar.
</p>
""", unsafe_allow_html=True)

# =====================================================
# CONSIDERAÇÕES FINAIS
# =====================================================
st.markdown('<h2 class="section-title">5. Considerações Finais</h2>', unsafe_allow_html=True)

st.markdown("""
<p>
Os resultados reforçam a Icatu Seguros como parceira estratégica, evidenciando um processo
comercial maduro, escalável e alinhado aos objetivos de crescimento sustentável.
</p>
""", unsafe_allow_html=True)

# =====================================================
# RODAPÉ
# =====================================================
st.markdown(f"""
<div class="footer">
<hr>
<p>Relatório gerado em {datetime.now().strftime("%d/%m/%Y %H:%M")}</p>
<p><strong>Apresentação Executiva • Icatu Seguros</strong></p>
</div>
""", unsafe_allow_html=True)

