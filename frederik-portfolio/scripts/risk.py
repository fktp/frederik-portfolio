"""Deterministic policy: sensitive code/config > app code > copy/styles."""
import subprocess
import sys

def risk_level(paths):
    if any(p.startswith((".github/", "scripts/")) or p.endswith((".csproj", "packages.lock.json", "global.json", "staticwebapp.config.json")) for p in paths):
        return "HIGH"
    if any(p.endswith((".cs", ".razor", ".js")) for p in paths):
        return "MEDIUM"
    return "LOW"

if __name__ == "__main__":
    paths = subprocess.check_output(["git", "diff", "--name-only", sys.argv[1], sys.argv[2]], text=True).splitlines()
    level = risk_level(paths)
    print(f"## Risk level: {level}\n")
    print({"HIGH": "Kræver ekstra menneskeligt review af pipeline, dependencies eller sikkerhedskonfiguration.", "MEDIUM": "Kræver funktionelt review og kontrol af preview.", "LOW": "Kontrollér tekst, layout og links i preview."}[level])
    for path in paths:
        print(f"- `{path.replace('`', '')}`")
