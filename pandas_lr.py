import streamlit as st
import pandas as pd
import numpy as np

meteo_data = np.random.normal(size=1000)
meteo_data = pd.DataFrame(data=None, columns=["Dist_norm"])

meteo_data