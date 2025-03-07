import scanpy as sc

def load_sample_data():
    """Loads a small built-in scRNA-seq dataset from Scanpy for testing."""
    adata = sc.datasets.pbmc3k()  # Loads a sample 3,000-cell PBMC dataset
    sc.pp.filter_cells(adata, min_genes=200)
    sc.pp.filter_genes(adata, min_cells=3)
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)

    return adata

if __name__ == "__main__":
    adata = load_sample_data()
    print(f"Processed dataset shape: {adata.shape}")
    adata.write("data/sample.h5ad")  # Save for consistency


# import scanpy as sc

# def load_and_preprocess(file_path):
#     """Loads and preprocesses scRNA-seq data"""
#     adata = sc.read_h5ad(file_path)

#     # Quality control: filter low-quality cells & genes
#     sc.pp.filter_cells(adata, min_genes=200)
#     sc.pp.filter_genes(adata, min_cells=3)

#     # Normalize and log-transform
#     sc.pp.normalize_total(adata, target_sum=1e4)
#     sc.pp.log1p(adata)

#     return adata

# if __name__ == "__main__":
#     adata = load_and_preprocess("../data/sample.h5ad")
#     print(f"Processed data shape: {adata.shape}")
