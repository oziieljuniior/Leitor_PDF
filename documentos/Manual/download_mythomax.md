# Como configurar o **MythoMax-L2 13B GGUF**

## 1. **Download**

A versão quantizada ideal:

* [`TheBloke/MythoMax-L2-13B-GGUF`](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGUF)

Baixe o arquivo:

```
MythoMax-L2-13B.Q4_K_M.gguf
```

Coloque-o em sua pasta:

```
~./models/MythoMax-L2-13B.Q4_K_M.gguf
```

---

### 2. **Atualizar o carregamento no `responder_pergunta.py`**

Substitua a parte do carregamento do modelo:

```python
from llama_cpp import Llama

llm = Llama(
    model_path="~./models/MythoMax-L2-13B.Q4_K_M.gguf",
    n_ctx=4096,      # MythoMax entende bem prompts longos
    n_threads=6,     # ou mais, se sua CPU suportar
    n_batch=512      # melhora fluidez em respostas longas
)
```

---

### 3. **Ajustar o prompt para aproveitar o modelo**

Esse modelo é muito bom com prompts no estilo "assistente instrutivo". Use este estilo:

```python
prompt = f"""### Instrução:
Você é um assistente com conhecimento profundo em textos técnicos. Responda a pergunta com base no contexto abaixo.

### Contexto:
{contexto}

### Pergunta:
{pergunta}

### Resposta:"""
```

---

### 4. **Atenção ao uso de memória**

| Recurso               | Estimativa                      |
| --------------------- | ------------------------------- |
| MythoMax 13B          | \~10–12 GB de RAM               |
| 500 chunks            | \~300–500 MB (pkl + embeddings) |
| sentence-transformers | \~300 MB                        |

**Tenha ao menos 16 GB de RAM no sistema**, ou 12 GB livres com swap bem configurado para evitar travamentos.

## Ou download em Nuvem

**Aqui, o modelo foi previamente baixado e colocado em uma nuvem drive**. Esse modo não é recomendado pois ele deve consumir memória em nuvem, existem outras maneiras mais eficientes de contornar esse problema. Caso queira, podemos conversar para mais investimentos.

[Link para download direto no google drive - Não recomendado](https://drive.google.com/file/d/1ncmxUnLjH-JF9vKBefHMKO21cib4aUZD/view?usp=sharing)
