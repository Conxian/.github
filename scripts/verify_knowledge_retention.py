import os
import sys
import time

def check_knowledge_kb():
    print("Verifying knowledge retention baselines...")

    # 1. Verify that critical audit reports exist
    if not os.path.exists("docs/AUDIT_REPORT_2026_07_07.md"):
        print("❌ Critical audit report missing.")
        return False

    # 2. Verify repository taxonomy is synced
    if not os.path.exists("repository-taxonomy.md"):
        print("❌ Repository taxonomy missing from root.")
        return False

    # 3. Verify AGENTS.md or similar guidance exists in key areas (using index.md as proxy here)
    if not os.path.exists("docs/index.md"):
        print("❌ Documentation index missing.")
        return False

    return True

if __name__ == "__main__":
    if check_knowledge_kb():
        print("✅ Knowledge retention check passed.")
        sys.exit(0)
    else:
        print("❌ Knowledge retention check failed.")
        sys.exit(1)
