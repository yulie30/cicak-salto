#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyleft © 2026 Anung <anung@trisakti.ac.id>
# 2026-11-19 13:33
# Distributed under terms of the MIT license.

"""

"""
import streamlit as st

st.set_page_config(
    page_title="Page 1",
    layout="wide",
)

st.title("🔐 Selamat Datang")
st.caption("Halaman Selamat Datang")

st.image("WELCOME_BIGDATA.png", use_container_width=True)

st.markdown("---")

st.subheader("📌 Ringkasan Indikator Utama")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Indikator Utama", "IHK", "Inflasi")
with col2:
    st.metric("Nilai Tukar", "Kurs Rupiah", "USD/IDR")
with col3:
    st.metric("Perdagangan", "Nilai Impor", "Juta USD")

st.markdown("---")

