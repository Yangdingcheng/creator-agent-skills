import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from validate_skills import main, check

def test_repo_skills_valid():
    root = os.path.join(os.path.dirname(__file__), "..")
    assert main(root) == 0

def test_bad_skill_detected(tmp_path=None):
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        os.makedirs(os.path.join(td, "skills", "demo"))
        p = os.path.join(td, "skills", "demo", "SKILL.md")
        open(p, "w", encoding="utf-8").write("---\nname: other\ndescription: short\n---\ntiny")
        errs = check(p)
        assert any("!= folder" in e for e in errs) and any("too short" in e for e in errs)

if __name__ == "__main__":
    test_repo_skills_valid(); test_bad_skill_detected(); print("ok")
