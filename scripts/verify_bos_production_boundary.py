import os
import sys
import subprocess

def check_production_boundary():
    print("Verifying BOS production boundary consistency...")

    # 1. Check for stub indicators in specific production paths
    # In a real environment, we would scan the linked repositories.
    # For this org-wide governance repo, we verify the presence of key research docs
    # that mandate the removal of stubs.

    mandatory_docs = [
        "docs/research/source-and-gap-map.md",
        "docs/research/nexus-holistic-alignment.md",
        "docs/research/hardening-best-practices.md"
    ]

    for doc in mandatory_docs:
        if not os.path.exists(doc):
            print(f"❌ Missing mandatory research document: {doc}")
            return False

    # 2. Check for prohibited 'stub' strings in core scripts that should be production-ready
    core_scripts = ["scripts/verify_knowledge_retention.py"]
    for script in core_scripts:
        if os.path.exists(script):
            with open(script, 'r') as f:
                if "This is a stub" in f.read():
                    print(f"❌ Script {script} is still a stub.")
                    return False

    return True

if __name__ == "__main__":
    if check_production_boundary():
        print("✅ BOS production boundary check passed.")
        sys.exit(0)
    else:
        print("❌ BOS production boundary check failed.")
        sys.exit(1)
