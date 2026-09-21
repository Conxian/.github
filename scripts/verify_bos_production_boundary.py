import os
import sys

def check_production_boundary():
    print("Verifying BOS production boundary consistency...")

    # 1. Verify mandatory research documents exist
    mandatory_docs = [
        "docs/research/source-and-gap-map.md",
        "docs/research/nexus-holistic-alignment.md",
        "docs/research/hardening-best-practices.md"
    ]

    for doc in mandatory_docs:
        if not os.path.exists(doc):
            print(f"❌ Missing mandatory research document: {doc}")
            return False

    # 2. Verify core verification scripts are production-ready and non-stub
    core_scripts = [
        "scripts/verify_knowledge_retention.py",
        "scripts/verify_bos_production_boundary.py",
        "scripts/verify_tracked_artifacts.py",
        "scripts/verify_compose_env_templates.py",
        "scripts/verify_submodule_secret_filenames.py"
    ]

    placeholder_phrases = ["this is a stub", "add actual logic", "add real logic"]

    for script in core_scripts:
        if not os.path.exists(script):
            print(f"❌ Core verification script missing: {script}")
            return False

        with open(script, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for line_idx, line in enumerate(lines, 1):
            # Skip checking the checking logic itself
            if "placeholder_phrases" in line or "skip checking" in line.lower():
                continue

            line_lower = line.lower()
            for phrase in placeholder_phrases:
                if phrase in line_lower:
                    print(f"❌ Script {script}:{line_idx} contains placeholder phrase: '{phrase}'")
                    return False

    return True

if __name__ == "__main__":
    if check_production_boundary():
        print("✅ BOS production boundary check passed.")
        sys.exit(0)
    else:
        print("❌ BOS production boundary check failed.")
        sys.exit(1)
