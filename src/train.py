import torch
from model import initialize_model
from preprocessing import load_and_preprocess

def train_model(adata, epochs=100, batch_size=128):
    """Trains scVI model"""
    model = initialize_model(adata)
    model.train(max_epochs=epochs, batch_size=batch_size)
    model.save("../models/trained_scVI_model.pth")
    print("Model training completed and saved.")

if __name__ == "__main__":
    adata = load_and_preprocess("../data/sample.h5ad")
    train_model(adata)
