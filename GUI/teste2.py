import customtkinter as ctk
from tkinter import filedialog, messagebox
import fitz
import os
import textwrap
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Configuração do tema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

CHUNK_SIZE = 300
OUTPUT_DIR = "partes_pdf"
os.makedirs(OUTPUT_DIR, exist_ok=True)

class PDFProcessor:
    def __init__(self, embed_model_name='paraphrase-albert-small-v2'):
        self.model = SentenceTransformer(embed_model_name)

    def dividir_pdf(self, path, paginas_por_parte=10):
        doc = fitz.open(path)
        partes = []
        for i in range(0, doc.page_count, paginas_por_parte):
            subdoc = fitz.open()
            for j in range(i, min(i + paginas_por_parte, doc.page_count)):
                subdoc.insert_pdf(doc, from_page=j, to_page=j)
            parte_path = os.path.join(OUTPUT_DIR, f"parte_{i // paginas_por_parte + 1}.pdf")
            subdoc.save(parte_path)
            partes.append(parte_path)
        return partes

    def extrair_texto(self, path):
        doc = fitz.open(path)
        return "".join(page.get_text() for page in doc)

    def chunk_text(self, texto):
        return textwrap.wrap(texto, width=CHUNK_SIZE)

    def salvar(self, chunks, nome_base):
        embeddings = self.model.encode(chunks)
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(np.array(embeddings))
        faiss.write_index(index, f"{nome_base}.faiss")
        with open(f"{nome_base}_chunks.pkl", "wb") as f:
            pickle.dump(chunks, f)

    def processar(self, path):
        partes = self.dividir_pdf(path)
        for parte in partes:
            texto = self.extrair_texto(parte)
            chunks = self.chunk_text(texto)
            base = os.path.splitext(parte)[0]
            self.salvar(chunks, base)

class ChatWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Perguntas sobre o Relatório")
        self.geometry("600x500")

        self.historico = ctk.CTkTextbox(self, height=300)
        self.historico.pack(padx=20, pady=10, fill="both", expand=True)
        self.historico.insert("end", "Pergunte algo sobre o relatório carregado...\n")

        entrada_frame = ctk.CTkFrame(self)
        entrada_frame.pack(padx=20, pady=10, fill="x")

        self.entrada = ctk.CTkEntry(entrada_frame, placeholder_text="Digite sua pergunta...")
        self.entrada.pack(side="left", expand=True, fill="x", padx=(0, 10))

        botao = ctk.CTkButton(entrada_frame, text="Enviar", command=self.enviar)
        botao.pack(side="right")

    def enviar(self):
        pergunta = self.entrada.get()
        if pergunta:
            self.historico.insert("end", f"Você: {pergunta}\n")
            self.historico.insert("end", f"Resposta: [resposta gerada aqui]\n\n")
            self.entrada.delete(0, 'end')

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Leitor Inteligente de Relatórios PDF")
        self.geometry("600x400")
        self.processor = PDFProcessor()

        frame = ctk.CTkFrame(self, corner_radius=15)
        frame.pack(pady=40, padx=30, fill="both", expand=True)

        label = ctk.CTkLabel(frame, text="Olá! Sou um leitor de PDF que irá processar seu relatório.", wraplength=520, justify="left")
        label.pack(pady=(20, 10), padx=20, anchor="w")

        for exemplo in [
            "➤ O que este relatório aborda?",
            "➤ Quais são os pontos principais identificados?",
            "➤ Posso obter um resumo do conteúdo?"
        ]:
            ctk.CTkLabel(frame, text=exemplo, anchor="w").pack(padx=20, pady=2, anchor="w")

        self.btn = ctk.CTkButton(frame, text="Selecionar PDF para Processar", command=self.selecionar_pdf)
        self.btn.pack(pady=30)

    def selecionar_pdf(self):
        caminho = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if caminho:
            try:
                self.btn.configure(state="disabled", text="Processando...")
                self.update()
                self.processor.processar(caminho)
                messagebox.showinfo("Sucesso", "PDF processado com sucesso!")
                ChatWindow()
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao processar o PDF:\n{str(e)}")
            finally:
                self.btn.configure(state="normal", text="Selecionar PDF para Processar")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
