from os import write
from typing import Sequence
import streamlit as st

for i in range(len(st.secrets["things_i_like"])):
  st.write(print(i+7))
