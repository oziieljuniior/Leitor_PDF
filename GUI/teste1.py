import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import fitz  # PyMuPDF
import faiss
import numpy as np
import pickle
import textwrap
from sentence_transformers import SentenceTransformer

# Configuração do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Modelo de embeddings
embed_model = SentenceTransformer('paraphrase-albert-small-v2')

# Parâmetros
CHUNK_SIZE = 300
OUTPUT_DIR = "partes_pdf"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Funções principais
def dividir_pdf_em_partes(pdf_path, paginas_por_parte=10):
    doc = fitz.open(pdf_path)
    num_paginas = doc.page_count
    partes = []
    for i in range(0, num_paginas, paginas_por_parte):
        subdoc = fitz.open()
        for j in range(i, min(i + paginas_por_parte, num_paginas)):
            subdoc.insert_pdf(doc, from_page=j, to_page=j)
        parte_path = os.path.join(OUTPUT_DIR, f"parte_{i // paginas_por_parte + 1}.pdf")
        subdoc.save(parte_path)
        partes.append(parte_path)
    return partes

def extrair_texto(pdf_path):
    doc = fitz.open(pdf_path)
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()
    return texto

def chunk_text(text, max_chars=CHUNK_SIZE):
    return textwrap.wrap(text, width=max_chars)

def salvar_index_e_chunks(chunks, nome_base):
    embeddings = embed_model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    faiss.write_index(index, f"{nome_base}.faiss")
    with open(f"{nome_base}_chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

def processar_pdf(pdf_path, status_callback):
    status_callback("Dividindo PDF...")
    partes = dividir_pdf_em_partes(pdf_path)
    for parte in partes:
        status_callback(f"Processando {parte}...")
        texto = extrair_texto(parte)
        chunks = chunk_text(texto)
        base = os.path.splitext(parte)[0]
        salvar_index_e_chunks(chunks, base)
    status_callback("Concluído!")

# Interface
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Processador de PDF com Embeddings")
        self.geometry("500x300")

        self.label = ctk.CTkLabel(self, text="Selecione um arquivo PDF")
        self.label.pack(pady=10)

        self.btn_selecionar = ctk.CTkButton(self, text="Selecionar PDF", command=self.selecionar_pdf)
        self.btn_selecionar.pack(pady=10)

        self.status = ctk.CTkLabel(self, text="Status: Aguardando...")
        self.status.pack(pady=10)

    def selecionar_pdf(self):
        caminho = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
        if caminho:
            self.status.configure(text="Status: Processando...")
            self.update()
            try:
                processar_pdf(caminho, lambda msg: self.status.configure(text=f"Status: {msg}"))
                messagebox.showinfo("Sucesso", "PDF processado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    app = App()
    app.mainloop()
