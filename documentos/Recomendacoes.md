## ✅ Objetivo

Substituir o modelo leve (`Phi-2`) por um mais poderoso, mantendo o sistema **local e funcional**, porém aceitando **maior uso de RAM** e **tempo de resposta mais alto**, em troca de **melhor compreensão textual**.

---

## 🔁 Opções de Modelos Robustos Offline (GGUF)

| Modelo                 | Tamanho  | RAM (Q4)   | Descrição                                            |
| ---------------------- | -------- | ---------- | ---------------------------------------------------- |
| **Mistral-7B**         | \~4.1 GB | \~6 GB     | Rápido, instruído, ótimo desempenho geral            |
| **LLaMA 2 7B**         | \~4.2 GB | \~6–8 GB   | Respostas mais formais, boa compreensão              |
| **OpenHermes Mistral** | \~4.5 GB | \~6 GB     | Tunado para diálogos naturais                        |
| **MythoMax-L2 13B**    | \~7.7 GB | \~10–12 GB | Excelente criatividade/compreensão (requer mais RAM) |

---

## 🧠 Recomendações

Se você deseja **melhor performance e compreensão**, eu recomendo:

### ✅ **Mistral-7B Instruct Q4\_K\_M**

* **Modelo:**
  [`TheBloke/Mistral-7B-Instruct-v0.1-GGUF`](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)

* **Vantagens:**
  Boa velocidade, responde bem a instruções, roda com \~6 GB RAM.

* **Uso (substituir linha do `Llama`):**

```python
llm = Llama(
    model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=4
)
```

---

## 📁 Estrutura do Projeto

```bash
.
├── source.pdf
├── partes_pdf/              # arquivos de partes, .faiss e .pkl
├── models/
│   └── mistral-7b-instruct-v0.1.Q4_K_M.gguf
├── processar_pdf.py         # parte 1
├── responder_pergunta.py    # parte 2 (com LLM mais forte)
```

---

## 🧩 Ajustes na Segunda Parte

Você já pode manter o mesmo script `responder_pergunta.py`, mudando **apenas o modelo carregado**, como mostrado acima.

