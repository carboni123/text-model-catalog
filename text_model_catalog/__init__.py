# models/__init__.py
from importlib import import_module
import pkgutil

# Automatically expose all sub‑packages (finance, legal, …)
for _, name, _ in pkgutil.walk_packages(__path__):
    import_module(f"{__name__}.{name}")
