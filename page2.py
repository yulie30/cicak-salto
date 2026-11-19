#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyleft © 2026 Anung <anung@trisakti.ac.id>
# 2026-11-19 13:35
# Distributed under terms of the MIT license.

"""

"""
import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(
    layout="wide",
    page_title="Dashboard Data Ekonomi Indonesia"
)

FILE_PATH = "bigdata_kelompok.csv"

@st.cache_data
def load_data():
    return pd.read_csv(FILE_PATH)

df = load_data()

st.write(df)

