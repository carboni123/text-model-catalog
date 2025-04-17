# examples/generate_invoice_openai.py
"""
Demo of OpenAI function‑calling: ask GPT‑4o to return an Invoice,
then validate with Pydantic. Requires `openai` package & environment var
OPENAI_API_KEY.
"""
from text_model_catalog.finance import Invoice
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
system_msg = (
    "You are an invoicing assistant. "
    "Return JSON that matches the Invoice schema exactly."
)

user_prompt = (
    "Create an invoice for 2 units of SKU‑123 at $50 each, "
    "supplier VAT BR123456789, customer VAT US987654321, USD currency."
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": system_msg},
              {"role": "user", "content": user_prompt}],
    tools=[Invoice.openai_schema()]  # Pydantic v2 helper method
)

raw_json = response.choices[0].message.tool_calls[0].args
invoice = Invoice.model_validate(raw_json)
print("🥳 Invoice validated:", invoice.model_dump_json(indent=2))
