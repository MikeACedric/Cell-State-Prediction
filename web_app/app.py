import streamlit as st
import plotly.express as px
from predict import predict_cell_states
from preprocessing import load_and_preprocess

# Load data
adata = load_and_preprocess("../data/sample.h5ad")
adata = predict_cell_states(adata)

st.title("Single-Cell State Prediction")

# Plot results
fig = px.scatter(
    x=adata.obsm["X_pca"][:, 0],
    y=adata.obsm["X_pca"][:, 1],
    color=adata.obs["cell_state"].astype(str),
    title="Predicted Cell States"
)
st.plotly_chart(fig)

st.write("Explore cell states and gene expression changes.")
