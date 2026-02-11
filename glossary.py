import json
import re
from pathlib import Path

def load_glossary(path: str = "glossary.json") -> dict[str, str]:
    p = Path(path)
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))

def apply_glossary(text: str, glossary: dict[str, str]) -> str:
    # substitui termos como "API Gateway" por "Gateway de API" (match exato por palavra)
    for src, dst in glossary.items():
        pattern = r"\b" + re.escape(src) + r"\b"
        text = re.sub(pattern, dst, text)
    return text