import faiss
import numpy as np
import os

# Embedding dimension for all-MiniLM-L6-v2
DIMENSION = 384

# Folder to store FAISS index
INDEX_FOLDER = "app/vector_db"
INDEX_PATH = os.path.join(INDEX_FOLDER, "faiss.index")

# Create folder if it doesn't exist
os.makedirs(INDEX_FOLDER, exist_ok=True)

# Create an empty FAISS index
index = faiss.IndexFlatL2(DIMENSION)


def save_index():
    """
    Save the FAISS index to disk.
    """
    os.makedirs(INDEX_FOLDER, exist_ok=True)
    faiss.write_index(index, INDEX_PATH)


def load_index():
    """
    Load the FAISS index if it exists.
    If the file is corrupted or missing,
    create a new empty index.
    """
    global index

    if os.path.exists(INDEX_PATH):
        try:
            index = faiss.read_index(INDEX_PATH)
            print("FAISS index loaded successfully.")
            print(f"Total vectors in FAISS: {index.ntotal}")

        except Exception as e:
            print("Corrupted FAISS index found.")
            print(e)
            print("Creating a new FAISS index...")
            index = faiss.IndexFlatL2(DIMENSION)

    else:
        print("No existing FAISS index found. Creating a new one...")
        index = faiss.IndexFlatL2(DIMENSION)
        print(f"Total vectors in FAISS: {index.ntotal}")


def add_vector(embedding):
    """
    Add a new embedding vector to FAISS.
    """
    global index

    vector = np.array([embedding]).astype("float32")

    index.add(vector)

    save_index()


def search_vector(embedding, top_k=5):
    """
    Search the most similar vectors.
    """
    global index

    vector = np.array([embedding]).astype("float32")

    distances, indices = index.search(vector, top_k)

    return distances, indices