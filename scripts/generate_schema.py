# scripts/generate_schema.py
"""
Regenerate JSON‑Schema & Zod outputs:
$ python scripts/generate_schema.py finance.Invoice
"""
import importlib
import sys
from pathlib import Path

def export(schema_path: str):
    module_path, cls_name = schema_path.rsplit(".", 1)
    cls = getattr(importlib.import_module(module_path), cls_name)
    schema = cls.model_json_schema()
    out = Path("schemas") / f"{cls_name}.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(schema.json(indent=2))
    print("Wrote", out)

if __name__ == "__main__":
    export(sys.argv[1])
