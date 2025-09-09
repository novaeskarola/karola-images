#!/usr/bin/env python3
import argparse, os, pathlib

def build_links(user, repo, branch, base="produtos"):
    base_path = pathlib.Path(base)
    if not base_path.exists():
        print(f"Pasta '{base}' não encontrada. Rode o script na raiz do repo.")
        return 1
    for path in base_path.rglob("*"):
        if path.is_file() and not path.name.startswith("."):
            rel = path.as_posix()
            url = f"https://cdn.jsdelivr.net/gh/{user}/{repo}@{branch}/{rel}"
            print(f"{rel} -> {url}")
    return 0

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", required=True, help="Usuário/Org do GitHub")
    ap.add_argument("--repo", required=True, help="Nome do repositório")
    ap.add_argument("--branch", default="main", help="Branch (default: main)")
    args = ap.parse_args()
    raise SystemExit(build_links(args.user, args.repo, args.branch))
