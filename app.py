#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyleft © 2026 Anung <anung@trisakti.ac.id>
# 2026-11-19 13:29
# Distributed under terms of the MIT license.

"""
Template source code tugas kelompok ELA6105
"""

import streamlit as st

st.set_page_config (
    page_title="Kelompok 007",
    page_icon="x",
    layout="wide"
)

st.title("Proyek Kelompok 007")
st.caption("Aplikasi streamlit kelompok 007")

pages = [
    st.Page("page1.py", title="Home", icon="🏠"),
    st.Page("page2.py", title="Data", icon="📊"),
    st.Page("page3.py", title="Visualisasi", icon="📈"),
    st.Page("page4.py", title="Profil", icon="👤")
]

pg = st.navigation (
    pages,
    position = "sidebar",
    expanded = True
)

