import torch
import scvi

def initialize_model(adata):
    """Sets up and returns a scVI model"""
    scvi.model.SCVI.setup_anndata(adata)
    model = scvi.model.SCVI(adata)
    return model

if __name__ == "__main__":
    from preprocessing import load_sample_data
    adata = load_sample_data("../data/sample.h5ad")

    model = initialize_model(adata)
    print("Model initialized successfully.")
