from sklearn.metrics import accuracy_score
from predict import predict_cell_states
from preprocessing import load_and_preprocess

def evaluate_model(adata):
    """Evaluates the model against known cell states"""
    ground_truth = adata.obs["known_cell_state"]
    predicted = adata.obs["cell_state"]

    accuracy = accuracy_score(ground_truth, predicted)
    print(f"Prediction Accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    adata = load_and_preprocess("../data/sample.h5ad")
    evaluate_model(adata)
