# Text‑Model Catalog

> **Deterministic building blocks for probabilistic language models**

---

## Why this project exists

Current large‑language models (LLMs) are *probabilistic*: for a given prompt they return the **most likely** next tokens, not a guaranteed structure. That is powerful for reasoning over noisy, ambiguous, or gigantic contexts—but painful when you need strict, machine‑readable output.

Classical software, databases, and APIs expect *deterministic* data. When an LLM says a product "costs 9.99" but forgets the currency, your pipeline breaks. Humans (also probabilistic!) handle such gaps naturally; classical computers do not.

This library bridges that gap. We curate and distribute production‑grade **Pydantic** models—validated, typed schemas for real‑world entities (invoices, contracts, SKUs, lab results…). Pair them with a helper that retries / corrects LLM output until it fits the model, and you get deterministic JSON you can trust.

---

## What is in the catalog?

* **Domain packs** – `finance`, `commerce`, `legal`, `healthcare`, each a standalone Python package published to PyPI.
* **Pydantic models** – Strict type annotations, field‑level validators, semantic‑versioned releases.
* **JSON‑Schema & Zod exports** – Generated automatically for non‑Python stacks.
* **Example prompts & tests** – Show how to call GPT‑4o / Gemini with function‑calling and validate the result.

---

## Quick start

```bash
pip install text-model-catalog[finance]
```

```python
# invoice_example.py
from openai import OpenAI
from text_model_catalog.finance import Invoice

client = OpenAI()

prompt = """Generate an invoice for 3 units of SKU‑123 at $42.50 each.\nInclude total, VAT 20 %."""

# 1) Call the model with function‑calling / JSON mode (omitted for brevity)
response_json = client.chat.completions.create(...)

# 2) Ground the response
invoice = Invoice.model_validate(response_json)
print(invoice.total)  # deterministic float
```

---

## Design goals

| Goal | How we meet it |
|------|----------------|
| **Determinism** | Every model runs full Pydantic validation and unit tests. |
| **Transparency** | Open‑source (MIT/Apache); CI publishes docs and schemas on every commit. |
| **Extensibility** | Add new domains via pull request + RFC template. |
| **Minimal overhead** | Zero non‑standard runtime deps; pure Python & typing only. |

---

## Contributing

1. **Fork & clone** the repo.
2. `pip install -e .[dev]` – installs `pytest`, `ruff`, and pre‑commit hooks.
3. Add a model under `models/<domain>/` following the **Model Style Guide** (see `/docs/style_guide.md`).
4. Run `pytest` and `ruff check .`.
5. Open a PR; at least one domain CODEOWNER must approve.

Good first issues are tagged `help wanted`.

---

## Funding & sustainability

The project is community‑driven and funded via **GitHub Sponsors** and **Open Collective**. 100 % of funds pay for CI, docs hosting, and (eventually) maintainer time. If your company relies on deterministic LLM output, please consider sponsoring! 🙏

---

## Roadmap (2025‑2026)

- **v0.1 (MVP)** – Invoice, Product, EmploymentContract models • PyPI alpha
- **v0.3** – Model retry helper (`forge.llm_validate`) • Docs site with live JSON‑Schema explorer
- **v1.0** – Healthcare & Legal packs • Governance RFC‑001 finalized • SOC 2 roadmap
- **v1.1+** – Hosted schema registry, model analytics dashboard, paid vertical packs

---

## License

Source code is licensed under **MIT**. See `LICENSE` for details.

---

*Made with 💚 by a community of developers who believe AI should be as reliable as it is powerful.*

