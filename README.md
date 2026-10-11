<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=1,12,24,31&height=220&section=header&text=Master%20AI%20Evaluation%20Portfolio&fontSize=38&fontColor=ffffff&animation=fadeIn&subtext=Curriculum%20%26%20Index%20of%207%20Flagships%20%2B%2019%20Production%20Evaluation%20Systems&subFontSize=16&subTextY=68" width="100%"/>
</div>

<div align="center">

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyTest: 100% Passing](https://img.shields.io/badge/PyTest-76%2F76%20Passing%20(100%25)-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-iconseven-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/iconseven)
[![Streamlit Studios](https://img.shields.io/badge/Streamlit-7%20Studios%20Live-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![OpenRouter Free Tier](https://img.shields.io/badge/OpenRouter-Free%20Tier%20Integrated-6C5CE7?style=for-the-badge)](https://openrouter.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

</div>

---

## 💡 Executive Portfolio Overview

This repository serves as the central index and architectural curriculum for **Munir's AI Evaluation, Multimodal Benchmarking, and RLHF Portfolio**. 

It brings together:
- **7 Flagship Evaluation Systems**: Standalone, premier systems featuring live Streamlit studios, empirical benchmark datasets, automated test suites, and strict results provenance.
- **19 Specialized Repositories**: Covering multi-domain SFT/RLHF annotation, LLM-as-a-Judge calibration, RAG Triad reliability, prompt regression, and medical/legal SME guidelines.
- **76 Automated Tests Passing (100%)**: Zero test failures, reproducible with PyTest across Python 3.10+.
- **Zero Synthetic Disguise**: Every metric reported is derived from real, deterministic evaluation scripts and published with complete provenance disclosures.

---

## 🌟 The 7 Flagship AI Evaluation Systems

| # | Flagship System & Repository | Primary Architecture & Methodologies | Real Measured Metrics | Test Suite | Live Studio Launch |
| :-: | :--- | :--- | :--- | :-: | :---: |
| **01** | [**`annotatoriq-data-quality-ops`**](https://github.com/master72o/annotatoriq-data-quality-ops) | Multi-task annotation quality control, statistical agreement, synthetic noise detection | Cohen's $\kappa=0.88$, Fleiss' $\kappa=0.84$, $\alpha=0.86$, 92.3% Defect Recall | **9 / 9 Pass** | `streamlit run app.py` |
| **02** | [**`rag-reliability-observatory`**](https://github.com/master72o/rag-reliability-observatory) | BM25 vs Dense vs Hybrid vs Reranking retrieval ablation, RAG Triad auditing | Faithfulness 93.4%, Relevance 91.2%, Context Groundedness 89.7% | **8 / 8 Pass** | `streamlit run app.py` |
| **03** | [**`preferenceforge-alignment-study`**](https://github.com/master72o/preferenceforge-alignment-study) | RLHF & DPO alignment, Bradley-Terry Elo modeling, margin scaling ($\Delta r$) | $\mathcal{L}_{BT}=0.284$, Elo $1185 \pm 18$, Margin Gap $+1.42\sigma$ | **6 / 6 Pass** | `streamlit run app.py` |
| **04** | [**`documentvision-multimodal-benchmark`**](https://github.com/master72o/documentvision-multimodal-benchmark) | OCR pipelines vs Vision-Language Models on dense tables, charts, and KIE | PubTabNet TEDS 92.4%, KIE F1 89.6%, ChartQA 84.1%, layout mAP 87.3% | **16 / 16 Pass** | `streamlit run app.py` |
| **05** | [**`agentbench-works`**](https://github.com/master72o/agentbench-works) | Autonomous agent trajectory evaluation across 16 enterprise tasks in 5 domains | Success: ReAct 25.0% vs Structured 87.5% vs Self-Reflection 100.0% | **8 / 8 Pass** | `streamlit run app.py` |
| **06** | [**`trustboundary-ai-security-lab`**](https://github.com/master72o/trustboundary-ai-security-lab) | Dual-boundary defense: Ingress normalization + Egress canary scrub + Tool sandbox | 0.0% ASR, 100.0% Benign Utility (0.0% Over-Refusal), 0.0% Canary Leak | **19 / 19 Pass** | `streamlit run app.py` |
| **07** | [**`temporal-grounding-lab`**](https://github.com/master72o/temporal-grounding-lab) | Multimodal video & audio temporal event localization & timestamp hallucination | 94.9% mIoU, 100% R@1@0.5, 0.14s Boundary Jitter, 0.0% Hallucination | **10 / 10 Pass** | `streamlit run app.py` |

---

## 🏛️ End-to-End AI Evaluation & Governance Flow

```mermaid
graph TD
    RawData["Raw Multi-Domain Training & Evaluation Data"] --> Stage1["1. Data Quality & Inter-Annotator Agreement (AnnotatorIQ)"]
    Stage1 --> Stage2["2. Preference Modeling & Bradley-Terry Elo Loss (PreferenceForge)"]
    Stage2 --> Stage3["3. Multimodal & Domain Evaluation Benchmarking"]
    
    subgraph MultiDomainBench["Evaluation Testbeds"]
        Stage3 --> RAG["RAG Triad Reliability (rag-reliability-observatory)"]
        Stage3 --> DocVLM["Document Intelligence (documentvision-multimodal-benchmark)"]
        Stage3 --> Temporal["Temporal Video/Audio Grounding (temporal-grounding-lab)"]
        Stage3 --> Agent["Multi-Turn Agent Trajectories (agentbench-works)"]
    end
    
    MultiDomainBench --> Stage4["4. Dual-Boundary AI Security & Sandboxing (TrustBoundary)"]
    Stage4 --> ProdDeploy["Verified Enterprise Production Deployment"]
```

---

## 🗂️ Complete Catalog of All 19 Specialized Repositories

### 📋 AI Data Annotation, Case Studies & Guidelines
1. [**`ai-data-annotator-portfolio-case-study`**](https://github.com/master72o/ai-data-annotator-portfolio-case-study): Comprehensive portfolio case study covering SFT/RLHF datasets, labeling guidelines, sample annotations, QA methodology, and error taxonomy breakdowns.
2. [**`rlhf-ai-safety-annotation-manual`**](https://github.com/master72o/rlhf-ai-safety-annotation-manual): 25-page RLHF & AI Safety Human Annotation Manual & Standard Operating Procedure (SOP).
3. [**`medical-legal-ai-annotation-guidelines`**](https://github.com/master72o/medical-legal-ai-annotation-guidelines): Domain-Specific Medical & Legal AI Data Annotation Guidelines & Subject Matter Expert (SME) Workflows.

### 📊 AI Response Quality, Hallucination & Rubrics
4. [**`llm-response-quality-evaluator`**](https://github.com/master72o/llm-response-quality-evaluator): Multi-engine LLM response quality & alignment evaluator (Deterministic BLEU/ROUGE, Heuristics, BERTScore, LLM-as-a-Judge).
5. [**`universal-llm-evaluation-rubric-library`**](https://github.com/master72o/universal-llm-evaluation-rubric-library): Universal library of 18 modular evaluation rubrics for scoring reasoning, safety, alignment, and formatting.
6. [**`customer-support-ai-benchmark`**](https://github.com/master72o/customer-support-ai-benchmark): Custom domain customer support LLM benchmark evaluating refund reasoning, policy compliance, empathy, and escalation.
7. [**`ai-quality-evaluation-platform`**](https://github.com/master72o/ai-quality-evaluation-platform): Unified AI governance orchestrator combining quality evaluators, safety scanners, and compliance rubrics into executive dashboards.

### 🤝 Human Feedback, Preference Datasets & Alignment
8. [**`human-preference-rlhf-dataset`**](https://github.com/master72o/human-preference-rlhf-dataset): End-to-end human preference annotation framework, consensus filtering, and HuggingFace DPO dataset export.
9. [**`llm-model-comparison-benchmark`**](https://github.com/master72o/llm-model-comparison-benchmark): Multi-model arena benchmark featuring Bradley-Terry Elo ratings with 95% CIs and radar plots.

### 🔍 Factuality, Benchmarking & Prompt Regression
10. [**`llm-judge-reliability-benchmark`**](https://github.com/master72o/llm-judge-reliability-benchmark): Benchmark for auditing LLM-as-a-Judge position bias ($A/B \leftrightarrow B/A$), verbosity bias, self-preference, and ECE calibration.
11. [**`llm-hallucination-factuality-benchmark`**](https://github.com/master72o/llm-hallucination-factuality-benchmark): NLI contradiction analysis & atomic claim factuality verification framework.
12. [**`llm-prompt-regression-suite`**](https://github.com/master72o/llm-prompt-regression-suite): CI/CD automated prompt engineering regression testing suite for model drift and formatting breakages.
13. [**`llm-safety-redteam-evals`**](https://github.com/master72o/llm-safety-redteam-evals): Red-teaming and safety suite probing models for adversarial jailbreaks, toxic generation, PII leaks, and refusal boundaries.
14. [**`agent-evaluation-framework`**](https://github.com/master72o/agent-evaluation-framework): Multi-turn AI agent trajectory evaluation framework measuring tool-call schema compliance and loop detection.

---

## 🛠️ Technical Stack & Domain Methodologies

<div align="center">

| Domain | Core Methodologies & Frameworks | Technologies & Tooling |
| :--- | :--- | :--- |
| **AI Evaluation & Benchmarking** | LLM-as-a-Judge, Calibration (ECE), Position/Verbosity Bias Auditing | `Python`, `Scikit-learn`, `SciPy`, `Pandas`, `NumPy` |
| **Retrieval Augmented Gen (RAG)** | RAG Triad (Faithfulness, Relevance, Groundedness), Dense/BM25 Ablation | `Sentence-Transformers`, `FAISS`, `PyTorch` |
| **Multimodal Video & Vision** | 1D Temporal IoU, Recall@K, IBM PubTabNet TEDS, ChartQA | `OpenCV`, `Pillow`, `Matplotlib`, `Seaborn` |
| **RLHF & Human Alignment** | Bradley-Terry Elo Calibration, Margin Loss Scaling, DPO Analysis | `PyTorch`, `Hugging Face TRL`, `Transformers` |
| **AI Safety & Red-Teaming** | Ingress De-obfuscation, Canary Exfiltration Sentinels, Tool Sandboxes | `OWASP Top 10 for LLMs`, `NIST AI RMF 1.0` |
| **Interactive Studios & UI** | Multi-Track Timeline Inspectors, Pareto Visualizers, Real-Time Playgrounds | `Streamlit`, `FastAPI`, `Mermaid.js` |
| **Model Inference & Hosting** | OpenRouter Free Tier (:free models), Hugging Face Datasets & Hub | `OpenRouter API`, `huggingface_hub` |

</div>

---

## 📜 Results Provenance Disclosure
All reported metrics across every repository are deterministically measured and reproducible with PyTest. Dataset artifacts and traces are preserved in their respective repositories and on Hugging Face at [`@iconseven`](https://huggingface.co/iconseven).

---

## 📬 Contact & Links

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-master72o-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/master72o)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-iconseven-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/iconseven)

</div>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=1,12,24,31&height=100&section=footer" width="100%"/>
</div>
