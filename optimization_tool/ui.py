import streamlit as st
from streamlit_katex import st_katex

def display_latex_with_tooltip(component, latex_code):
    """Display a UI component with a tooltip showing its LaTeX representation."""
    st_katex(f"{latex_code}", key=component)
