import os
import subprocess
import sys

def check_gitignore_rules():
    print("Verifying .gitignore contains mandatory artifact ignore rules...")
    gitignore_path = ".gitignore"
    if not os.path.exists(gitignore_path):
        print("❌ .gitignore file missing from repository root.")
        return False

    with open(gitignore_path, "r", encoding="utf-8") as f:
        gitignore_content = f.read()

    mandatory_patterns = [
        "node_modules/",
        "test-results/",
        "playwright-report/",
        "coverage/",
        "dist/",
        "build/",
        "target/",
    ]

    missing = [pattern for pattern in mandatory_patterns if pattern not in gitignore_content]
    if missing:
        print(f"❌ .gitignore is missing mandatory artifact ignore rules: {missing}")
        return False

    return True

def check_for_artifacts():
    print("Verifying no tracked artifacts in source control...")

    forbidden_extensions = (
        '.exe', '.dll', '.so', '.dylib', '.node',
        '.pyc', '.pyo', '.pyd', '.class', '.o', '.a'
    )
    forbidden_directories = (
        'node_modules/', 'dist/', 'target/', 'build/',
        '.pytest_cache/', 'test-results/', 'playwright-report/',
        'coverage/', '.next/', '.nuxt/', 'out/'
    )
    forbidden_files = (
        '.env', '.env.local', '.env.production', '.env.staging',
        'lightning-coverage.json'
    )

    try:
        res = subprocess.run(
            ['git', 'ls-files'],
            capture_output=True,
            text=True,
            check=True
        )
        tracked_files = res.stdout.splitlines()
    except Exception as e:
        print(f"❌ Failed to obtain git tracked files: {e}")
        return False

    violations = []
    for filepath in tracked_files:
        filename = os.path.basename(filepath)

        # Check forbidden file names
        if filename in forbidden_files:
            violations.append(f"Forbidden tracked file: {filepath}")

        # Check forbidden extensions
        if filepath.endswith(forbidden_extensions):
            violations.append(f"Forbidden tracked extension: {filepath}")

        # Check forbidden directories
        for forbidden_dir in forbidden_directories:
            if filepath.startswith(forbidden_dir) or f"/{forbidden_dir}" in filepath:
                violations.append(f"Forbidden tracked directory artifact: {filepath}")

    if violations:
        print("❌ Tracked artifacts found in git index:")
        for v in violations:
            print(f"  - {v}")
        return False

    return True

if __name__ == "__main__":
    gitignore_ok = check_gitignore_rules()
    artifacts_ok = check_for_artifacts()

    if gitignore_ok and artifacts_ok:
        print("✅ Tracked artifacts and .gitignore checks passed.")
        sys.exit(0)
    else:
        sys.exit(1)
