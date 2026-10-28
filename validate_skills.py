#!/usr/bin/env python3
"""Validate every skill in this repo: skills/<name>/SKILL.md must have
YAML frontmatter whose name matches the folder, a usable description,
and a substantive body. Run: python3 validate_skills.py"""
import os, re, sys

def check(path):
    errs = []
    text = open(path, encoding="utf-8").read()
    folder = os.path.basename(os.path.dirname(path))
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m: return [f"{path}: missing frontmatter"]
    fm = m.group(1)
    name = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not name: errs.append(f"{path}: no name in frontmatter")
    elif name.group(1) != folder: errs.append(f"{path}: name '{name.group(1)}' != folder '{folder}'")
    if not desc or len(desc.group(1)) < 40: errs.append(f"{path}: description missing or too short")
    body = text[m.end():]
    if len(body) < 600: errs.append(f"{path}: body too short ({len(body)} chars) — a skill needs a real workflow")
    return errs

def main(root="."):
    skills_dir = os.path.join(root, "skills")
    paths = [os.path.join(skills_dir, d, "SKILL.md") for d in sorted(os.listdir(skills_dir))
             if os.path.isfile(os.path.join(skills_dir, d, "SKILL.md"))]
    if not paths: print("no skills found"); return 1
    errs = []
    for p in paths: errs += check(p)
    for p in paths: print(("OK  " if not any(p in e for e in errs) else "FAIL") + "  " + p)
    if errs:
        print("\n".join(errs)); return 1
    print(f"\n{len(paths)} skill(s) valid."); return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
