# 📚 Chatbot Local para PDFs com IA (Offline)

Este projeto implementa um **chatbot inteligente offline** que:

- Lê e processa arquivos PDF extensos.
- Divide automaticamente o conteúdo em partes otimizadas.
- Gera embeddings e indexação vetorial com FAISS.
- Responde perguntas sobre o conteúdo dos PDFs utilizando modelos de linguagem locais via `llama-cpp`.

---

## ✅ Funcionalidades

- 📖 Leitura e extração de texto de PDFs grandes.
- 🔁 Divisão automática em partes menores para economia de memória RAM.
- 🧠 Embeddings com `sentence-transformers`.
- 🔍 Busca distribuída com FAISS.
- 🗣️ Geração de respostas com LLM local, como `Phi-2`.

---

## 🛠 Requisitos

- Python 3.8 ou superior
- RAM mínima: **4 GB livres**
- Instalação das dependências:

```bash
pip install -r requirements.txt
````

---

## 📁 Estrutura de Diretórios

Com base no projeto atual:

```
.
├── documentos/
│   └── SAGE_ManCfg_Anx17_61850 1.pdf    # PDF original
├── models/
│   └── phi-2.Q4_K_M.gguf                # Modelo LLM local
├── outputs/
│   └── source.pdf                       # PDF convertido ou de trabalho
├── pyproject/
│   ├── partes_pdf/
│   │   ├── parte_1.pdf → parte_6.pdf     # PDFs divididos
│   │   ├── parte_1.faiss → parte_6.faiss # Índices vetoriais FAISS
│   │   ├── parte_1_chunks.pkl → parte_6_chunks.pkl # Trechos de texto
│   └── source.ipynb                     # Notebook de controle
├── poetry.lock
├── pyproject.toml
├── README.md
├── requirements.txt
└── saida.txt                            # Estrutura exportada
```

---

## ▶️ Como Usar

### 1. Processar o PDF:

```bash
python processar_pdf.py
```

Isso irá:

* Dividir o PDF em partes.
* Criar os embeddings de texto.
* Salvar índices `.faiss` e trechos `.pkl`.

### 2. Realizar perguntas:

```bash
python responder_pergunta.py
```

Digite uma pergunta sobre o conteúdo do PDF e o chatbot retornará a resposta com base nos trechos relevantes.

---

## 📚 Modelos Recomendados

| Nome       | RAM sugerida | Link                                                                                               |
| ---------- | ------------ | -------------------------------------------------------------------------------------------------- |
| Phi-2      | 3–4 GB       | [https://huggingface.co/TheBloke/Phi-2-GGUF](https://huggingface.co/TheBloke/Phi-2-GGUF)           |
| TinyLLaMA  | 2 GB         | [https://huggingface.co/TheBloke/TinyLlama](https://huggingface.co/TheBloke/TinyLlama)             |
| Mistral 7B | 6–8 GB       | [https://huggingface.co/TheBloke/Mistral-7B-GGUF](https://huggingface.co/TheBloke/Mistral-7B-GGUF) |

Coloque os arquivos `.gguf` em `./models/`.

---

## 💡 Melhorias Futuras

* [ ] 🔎 Ranking global entre partes para priorização de contexto.
* [ ] 🧠 Fine-tuning local com PDFs específicos.
* [ ] 💬 Interface com Gradio ou Streamlit.
* [ ] 🗂 Cache de embeddings por documento.
* [ ] 📦 Empacotamento via `PyInstaller` ou `Docker`.

---

## 🔐 Licença

Uso educacional e pessoal. Consulte as licenças dos modelos utilizados.

---

## 🙌 Autor

Desenvolvido por **Oziel Ramos** com suporte do ChatGPT-4.

