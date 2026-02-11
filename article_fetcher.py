import requests
from readability import Document
from bs4 import BeautifulSoup

def fetch_article_text(url: str, timeout: int = 20) -> str:
    r = requests.get(url, timeout=timeout, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()

    doc = Document(r.text)
    html = doc.summary()  # conteúdo principal
    soup = BeautifulSoup(html, "lxml")

    text = soup.get_text(separator="\n")
    # limpa linhas vazias
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    return "\n".join(lines)