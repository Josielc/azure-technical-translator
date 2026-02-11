import argparse
from translator import translate_text
from article_fetcher import fetch_article_text
from glossary import load_glossary, apply_glossary

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", help="Texto para traduzir")
    parser.add_argument("--url", help="URL do artigo para traduzir")
    parser.add_argument("--to", default="pt", help="Idioma de destino (ex: pt, en, es)")
    parser.add_argument("--glossary", default="glossary.json", help="Arquivo de glossário")
    args = parser.parse_args()

    if not args.text and not args.url:
        raise SystemExit("Use --text OU --url")

    glossary = load_glossary(args.glossary)

    if args.url:
        source = fetch_article_text(args.url)
    else:
        source = args.text

    translated = translate_text(source, args.to)
    translated = apply_glossary(translated, glossary)

    print(translated)

if __name__ == "__main__":
    main()
