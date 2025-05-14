## 📌 **1. Mythomax vs. Phi-2 (usado no notebook anterior)**

### ✔️ **MythoMax:**

* É uma combinação de modelos de linguagem (merge) baseada no Mistral, com foco em compreensão contextual e geração detalhada.
* Tende a produzir **respostas mais longas, elaboradas e com linguagem mais próxima da naturalidade humana**.
* Boa escolha para contextos onde se exige **inferência mais profunda e melhor compreensão de textos complexos** como normas e documentação técnica, por exemplo o **Anexo 17 do SAGE com IEC 61850**.

### ⚠️ **Phi-2 no notebook:**

* É um modelo leve (cerca de 2.7B parâmetros), mais adequado para tarefas locais com restrições de memória (você mencionou uso com 2GB RAM).
* Ele entrega respostas **mais básicas e diretas**, mas pode deixar de explorar nuances de um documento técnico denso como esse.

### ✅ **Conclusão:**

Se você tiver infraestrutura que suporte o **MythoMax (requer GPU com boa RAM e suporte à arquitetura usada)**, **ele sim deve fornecer respostas melhores e mais completas**, especialmente com PDFs técnicos como este.

---

## 🧠 **2. Perguntas iniciais recomendadas no notebook para obter boas respostas**

Essas perguntas servem tanto para o Phi-2 quanto (melhor ainda) para o MythoMax, pois visam fornecer contexto claro e ativo para o modelo:

### 🔹 Sobre estrutura e função

1. **"O que é necessário para configurar a comunicação com um IED no protocolo IEC 61850 segundo o SAGE?"**
2. **"Quais Logical Nodes e CDCs são utilizados para medição de tensão e ângulo no transformador TF5?"**
3. **"Qual o papel da entidade CNF na configuração do SAGE?"**

### 🔹 Sobre mapeamento e implementação

4. **"Como o modelo IEC 61850 é mapeado para a estrutura SCADA do SAGE?"**
5. **"Quais são os principais Data Objects do Logical Node MMXU?"**
6. **"Qual a função da máscara OPMSK e como ela afeta a comunicação com o IED?"**

### 🔹 Sobre arquivos e processo

7. **"Que arquivos são gerados pelo SAGE após o levantamento dos objetos no IED?"**
8. **"O que é o DataSet EXTRA e qual sua função no SAGE?"**

---

## 🧭 Dica Extra:

Se usar o MythoMax com o mesmo pipeline do notebook, você pode:

* Aumentar o `MAX_CONTEXT` para capturar mais contexto de PDF.
* Ajustar `TOP_K` para trazer mais chunks por parte.
* Trabalhar com prompts mais ricos: `"Explique com base na norma e nos conceitos apresentados..."`


