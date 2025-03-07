import torch
import numpy as np
from model import initialize_model
from preprocessing import load_and_preprocess

def predict_cell_states(adata):
    """Predicts future cell states using trained model"""
    model = initialize_model(adata)
    model.load("../models/trained_scVI_model.pth")
    latent_embeddings = model.get_latents()

    # Example: KMeans clustering for cell states
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=5, random_state=42)
    adata.obs["cell_state"] = kmeans.fit_predict(latent_embeddings)

    print("Predictions completed.")
    return adata

if __name__ == "__main__":
    adata = load_and_preprocess("../data/sample.h5ad")
    adata = predict_cell_states(adata)
