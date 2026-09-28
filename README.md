# Master AI Evaluation & LLM Quality Engineering Portfolio

Welcome to the **Master AI Evaluation, RLHF, AI Data Quality & LLM QA Portfolio**. This repository index contains 12 production-grade, reproducible evaluation frameworks, benchmarks, and research labs designed for AI Labs, LLM evaluation teams, RLHF specialists, and technical hiring managers.

---

## Portfolio Navigation Index

### 1. AI Evaluation Fundamentals
* [**`llm-response-quality-evaluator`**](./llm-response-quality-evaluator/) — Reusable evaluation engine scoring correctness, relevance, completeness, clarity, conciseness, instruction following, factuality, safety, and helpfulness with deterministic rules and error taxonomy classification.

### 2. Human Feedback & Annotation Quality
* [**`human-preference-rlhf-dataset`**](./human-preference-rlhf-dataset/) — Original human preference framework with labeling guidelines, calibration, and agreement analytics (Fleiss' Kappa, Cohen's Kappa, Raw Agreement).
* [**`llm-annotation-quality-lab`**](./llm-annotation-quality-lab/) — Inter-annotator agreement research lab measuring Krippendorff's Alpha ($\alpha$), Fleiss' Kappa ($\kappa$), disagreement root causes, and Before vs After guideline calibration.

### 3. LLM Research & Benchmarking
* [**`llm-judge-reliability-benchmark`**](./llm-judge-reliability-benchmark/) — Flagship research study measuring LLM-as-a-judge reliability, Pearson $r$, Spearman $\rho$, verbosity/formatting bias, and prompt strategy ablations (Baseline vs Rubric vs Chain-of-Thought).
* [**`llm-hallucination-factuality-benchmark`**](./llm-hallucination-factuality-benchmark/) — Claim-level factuality benchmark evaluating Precision, Recall, F1 score, and an 8-category hallucination taxonomy against evidence documents.

### 4. Applied Systems & Guardrails
* [**`rag-evaluation-lab`**](./rag-evaluation-lab/) — Decoupled retrieval (Recall@K, NDCG, MRR) and generation (faithfulness, context precision, citation correctness) evaluation suite across RAG v1 (Baseline), v2 (Hybrid), and v3 (Reranked).
* [**`llm-prompt-regression-suite`**](./llm-prompt-regression-suite/) — CI/CD prompt & model version regression testing engine with automated quality gate assertions ($\Delta < -0.05$ blocker), format validation, and safety checks.
* [**`llm-safety-redteam-evals`**](./llm-safety-redteam-evals/) — Adversarial red-teaming benchmark evaluating prompt injection, DAN jailbreaks, PII leakage, harmful content, and system prompt extraction across Def v0 (Raw), v1 (Guard), and v2 (Dual Filter).

### 5. Advanced Models & Agents
* [**`llm-model-comparison-benchmark`**](./llm-model-comparison-benchmark/) — Controlled multi-model comparison across frontier (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro) and open-weights models (Llama-3-70B, Mistral-Large) measuring reasoning, JSON schema compliance, Pareto cost-efficiency, and latency.
* [**`preference-modeling-rlhf`**](./preference-modeling-rlhf/) — Pairwise preference reward model calibration & Bradley-Terry evaluation framework measuring Expected Calibration Error (ECE), log loss, and reward margin ($\Delta r$) progression across RM checkpoints.
* [**`agent-evaluation-framework`**](./agent-evaluation-framework/) — Trajectory-level autonomous agent benchmarking suite evaluating multi-step planning efficiency, tool argument schema correctness, and self-healing error recovery.

### 6. Capstone Platform
* [**`ai-quality-evaluation-platform`**](./ai-quality-evaluation-platform/) — Capstone Enterprise AI Quality & LLM Evaluation Platform consolidating all 7 evaluation pillars into a unified CLI orchestrator, system health score calculation, and executive dashboard reports.

---

## Skills Matrix

| Skill Domain | Projects Demonstrating Competence |
| :--- | :--- |
| **Deterministic Guardrails & Schema Validation** | `llm-response-quality-evaluator`, `llm-prompt-regression-suite` |
| **LLM-as-a-Judge Design & Bias Mitigation** | `llm-response-quality-evaluator`, `llm-judge-reliability-benchmark` |
| **Inter-Annotator Agreement & Data Governance** | `human-preference-rlhf-dataset`, `llm-annotation-quality-lab` |
| **Hallucination & Factuality Benchmarking** | `llm-hallucination-factuality-benchmark`, `rag-evaluation-lab` |
| **AI Safety, Jailbreak & Injection Red-Teaming** | `llm-safety-redteam-evals`, `llm-response-quality-evaluator` |
| **Agent Trajectory & Tool Use QA** | `agent-evaluation-framework` |
| **RLHF & Reward Modeling** | `preference-modeling-rlhf`, `human-preference-rlhf-dataset` |

---

*Portfolio maintained by AI Evaluation & LLM QA Specialist.*
