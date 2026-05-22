import faiss
import numpy as np
import pickle

DIM = 384
index = faiss.IndexFlatIP(DIM)
id_map = []

def add(id, vec):
    global id_map
    index.add(np.array([vec]).astype("float32"))
    id_map.append(id)

def search(vec, k=10):
    D, I = index.search(np.array([vec]).astype("float32"), k)
    return I[0]