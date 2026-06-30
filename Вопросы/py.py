import os, re, sys

TXT_FILE = "input.txt"
OUTPUT_DIR = "."

def read_names(txt_path: str):
    try:
        with open(txt_path, encoding="utf-8") as f:
            txt = f.read()
    except FileNotFoundError:
        print(f"❌ Файл {txt_path!r} не найден.", file=sys.stderr)
        return []
    return re.findall(r"\[\[(.*?)\]\]", txt)

def create_md(names, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    for name in set(names):
        safe_name = re.sub(r"[<>:\"/\\|?*\x00-\x1F]", "_", name).strip()
        if not safe_name:
            continue
        path = os.path.join(out_dir, f"{safe_name}.md")
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write("")  # пусто
            print(f"✅ Создан {path}")
        else:
            print(f"⚪ Уже существует {path}")

def main():
    names = read_names(TXT_FILE)
    if not names:
        sys.exit(1)
    create_md(names, OUTPUT_DIR)

if __name__ == "__main__":
    main()