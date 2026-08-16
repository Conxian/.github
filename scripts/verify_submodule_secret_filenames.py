import fnmatch
import os
import subprocess
import sys

def check_secrets():
    print("Verifying no secret filenames in submodules and repository index...")

    secret_patterns = [
        ".env",
        ".env.local",
        ".env.production",
        ".env.staging",
        ".env.development",
        "*.pem",
        "*.key",
        "id_rsa",
        "id_rsa.pub",
        "id_ed25519",
        "*.p12",
        "*.pfx",
        "*.asc",
        "credentials.json",
        "service_account.json",
        "service-account*.json",
        "*.keystore"
    ]

    allowed_suffixes = (
        ".example",
        ".template",
        ".sample",
        ".dist"
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
        print(f"❌ Failed to obtain tracked files: {e}")
        return False

    violations = []
    for filepath in tracked_files:
        filename = os.path.basename(filepath)

        # Skip allowed template/example versions of files
        if any(filename.endswith(suffix) for suffix in allowed_suffixes):
            continue

        for pattern in secret_patterns:
            if fnmatch.fnmatch(filename, pattern):
                violations.append(f"Potentially sensitive file tracked: {filepath} (matched pattern '{pattern}')")

    # Check for git submodules if .gitmodules exists
    if os.path.exists(".gitmodules"):
        try:
            sub_res = subprocess.run(
                ['git', 'submodule', 'status', '--recursive'],
                capture_output=True,
                text=True,
                check=True
            )
            submodules = sub_res.stdout.splitlines()
            print(f"Verified {len(submodules)} git submodule(s).")
        except Exception as e:
            print(f"⚠️ Warning: Could not inspect git submodules: {e}")

    if violations:
        print("❌ Sensitive secret file patterns detected in source control:")
        for v in violations:
            print(f"  - {v}")
        return False

    return True

if __name__ == "__main__":
    if check_secrets():
        print("✅ Submodule secrets check passed.")
        sys.exit(0)
    else:
        sys.exit(1)
