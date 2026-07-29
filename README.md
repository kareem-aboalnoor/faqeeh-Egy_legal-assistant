# 🚀 [Tips Hindawi](https://www.tipshindawi.com/) Challenge (June–July) 2026

> 🏆 This repository is my official submission for the [ **Tips Hindawi** ](https://www.tipshindawi.com/) **Challenge (June–July) 2026**.

## 👤 Participant

| Field            | Value                                |
| ---------------- | ------------------------------------ |
| Full Name        | Kareem Aboalnoor Abdalaal Mohamed    |
| Project Name     | Faqeeh AI - Egyptian Legal Assistant |
| GitHub Username  | kareem-aboalnoor                     |
| Challenge Batch  | June–July 2026                       |
| Training Program | Large Language Models (LLMs) Program |
| Organization     | [**Edrak for Ai**](https://edrak4ai.com/en) |

---

# 📖 Project Overview

**Faqeeh AI** is a smart legal assistant dedicated exclusively to Egyptian law. Its primary goal is to help users understand Egyptian laws simply and easily using Artificial Intelligence.

The idea for the project stems from the fact that many people have everyday legal inquiries but struggle to understand complex legal texts or access reliable legal information quickly. Therefore, our objective was to provide a tool that helps users grasp their initial legal standing and explains laws in plain language, whether they use formal Arabic or the everyday Egyptian dialect.

⚠️ **Disclaimer:** It is important to clarify that Faqeeh AI is *not* a replacement for a professional lawyer. It is a tool designed to increase legal awareness and provide initial legal explanations. For complex cases or specialized legal opinions, consulting a qualified attorney remains strictly necessary.
---

# ✨ Features

* 🧠 **Specialized LLM Fine-Tuning**: Powered by Qwen2.5 (7B) fine-tuned specifically on Egyptian legal data to master the tone, structure, and terminology of formal legal reasoning.
* 🔍 **State-of-the-Art RAG Pipeline**: Utilizes FAISS combined with the powerful `BAAI/bge-m3` embedding model to search legal corpora with high precision.
* 🎯 **CrossEncoder Reranking**: Integrates `BAAI/bge-reranker-v2-m3` to rigorously filter and re-rank the retrieved documents, passing only the absolute most relevant top 3 legal articles to the model.
* 🛡️ **Multi-Layered Guardrails & Validation**: Implements dynamic query classification to instantly block non-legal questions (e.g., medical, sports, programming) and enforces a strict Arabic-only output validation by mathematically scanning unicode ranges.
* 🗣️ **Query Reformulation & Ambiguity Check**: Automatically translates colloquial Egyptian queries (e.g., *"صاحب الشغل طردني من غير مبرر، حقي إيه؟"*) into formal legal search terms, and checks for query ambiguity before proceeding.
* ⚡ **Streaming & Memory**: Maintains context through a custom `ConversationMemory` class and streams responses ChatGPT-style via a threaded FastAPI + ngrok backend.

---

# 🛠️ Technologies Used

* **Core LLM**: Qwen2.5-7B (Fine-Tuned, `float16`)
* **Backend**: FastAPI, Uvicorn, PyTorch, pyngrok, Threading
* **Frontend**: Streamlit, Requests
* **RAG & Embeddings**: FAISS, `BAAI/bge-m3`
* **Reranking**: `BAAI/bge-reranker-v2-m3` (Sentence-Transformers)
* **Data Sources**: `dataflare/egypt-legal-corpus` (RAG)

### 📚 Fine-Tuning Datasets
To achieve a highly dynamic model, we merged four different datasets for the fine-tuning process:
1. `tarekys5/egyptian_legal_v2`
2. `fr3on/eg-legal-qa`
3. `fr3on/eg-legal-instruction-following`
4. `Omar-youssef/QA_LAW_Egyptian_dataset`

**Why did we use four datasets for Fine-Tuning?**
Because each dataset added a unique value. One contained direct Q&A, another focused on instruction-following styles, and the third provided diverse examples. By merging them, the model learned various patterns of legal questions and answers instead of relying on a single source or format, making it incredibly robust.

---

# ⚙️ Installation

To run this project, you need to set up both the backend (on Kaggle) and the frontend (Local).

**1. Backend (Kaggle)**
1. Obtain your free Auth Token from the [ngrok website](https://dashboard.ngrok.com/).
2. Open the notebook located at `notebooks/02_faqeeh_legal_assistant_api.ipynb` in Kaggle.
3. Paste your `ngrok` auth token in the final cell where indicated.
4. Run all cells to start the FastAPI server. 
5. **Important:** Wait for the notebook to output a `Public URL` (e.g., `https://xxxx.ngrok-free.app`), and copy it.

**2. Frontend (Local Deployment)**
1. Clone this repository to your local machine.
2. Navigate to the `Deployment` directory and install the requirements:
   - `pip install -r requirements.txt`
3. Open the `app.py` file in a code editor and replace the `API_URL` variable with the **Public URL** you copied from Kaggle (add `/ask_stream` at the end of it).
4. Run the Streamlit app:
   - `streamlit run app.py`

---
# 🚀 Usage

Once the Streamlit interface is running, simply type your legal question in formal Arabic or Egyptian dialect. The system will internally rephrase the query, search the FAISS database, rerank the best articles, and stream a structured legal response citing specific laws.

**Note on Fine-Tuning:**
If you wish to re-fine-tune the model from scratch or train it on new data, please use the provided fine-tuning notebook on Google Colab located at: `notebooks/01_fine_tuning.ipynb`.

---

# 📸 Demo

Watch **Faqeeh AI** in action as it seamlessly answers everyday legal questions across different domains (Family Law, Labor Law, and Contracts) in real-time, providing highly accurate legal reasoning based on retrieved Egyptian laws:

<video src="assets/demo.mp4" width="100%" controls>
  Your browser does not support the video tag.
</video>

---

# 📈 Results

* **Training Success**: The Qwen2.5 7B model was successfully fine-tuned with a final loss of **0.78**, demonstrating excellent convergence and deep understanding of Egyptian legal text.
* **Significant Hallucination Reduction**: Successfully minimized the common issue of LLM hallucination. By using the CrossEncoder reranker, the model is strictly guided by the retrieved facts, ensuring that responses are highly accurate and grounded in actual Egyptian laws.
* **Seamless Dialect Processing**: Effectively bridged the gap between everyday colloquial Egyptian Arabic and complex formal legal texts, enabling ordinary citizens to receive professional legal advice without needing to understand complex legal jargon.

---

# 🔮 Future Improvements

* 📱 **Mobile Application Development**: Building a dedicated mobile app to provide a seamless and user-friendly experience for quick access to legal answers on the go.
* 📚 **Knowledge Base Expansion**: Expanding the RAG database to include the newest Egyptian legislations, laws, and recent Cassation Court rulings.
* 🔄 **Automated Database Updates**: Implementing a mechanism for periodic, automated updates of legal documents to ensure the assistant always provides up-to-date legal advice.
* 🎙️ **Voice Search Support**: Integrating voice recognition tailored to the Egyptian dialect, allowing users to speak their legal queries naturally instead of typing.
* ⚡ **Latency Optimization**: Reducing response times and improving generation speed through backend infrastructure enhancements and dedicated GPU hosting.
---

# 📚 About the Challenge

This project was developed as part of the [**Tips Hindawi**](https://www.tipshindawi.com/) **Challenge (June–July) 2026**.

[Tips Hindawi](https://www.tipshindawi.com/) is the internships department of [**Edrak for Ai**](https://edrak4ai.com/en), and the challenge encourages participants to build real-world projects, apply practical skills, and showcase their work through GitHub.

For more information about the challenge, training programs, and upcoming batches, visit the official [Tips Hindawi](https://www.tipshindawi.com/) website.

---

# 📄 License

This project is shared for educational and portfolio purposes.
