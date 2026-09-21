import os
import re
import subprocess
import sys

def check_env_templates():
    print("Verifying docker-compose env templates and environment security...")

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

    compose_files = [f for f in tracked_files if re.match(r'^.*docker-compose.*\.ya?ml$', f, re.IGNORECASE)]
    env_templates = [f for f in tracked_files if re.match(r'^.*\.env.*\.(example|template|sample|dist)$', f, re.IGNORECASE)]

    findings = []

    # Verify compose files for risky mounts or hardcoded keys
    dangerous_mounts = [
        "/var/run/docker.sock",
        "/etc/shadow",
        "/etc/passwd",
        "/root",
        "~/.ssh"
    ]

    for cfile in compose_files:
        if os.path.exists(cfile):
            with open(cfile, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            for mount in dangerous_mounts:
                if mount in content:
                    findings.append(f"Dangerous host mount '{mount}' found in compose file: {cfile}")

            # Check for hardcoded credentials (e.g. PASSWORD=secret_123)
            matches = re.findall(r'(?i)(PASSWORD|SECRET|API_KEY|PRIVATE_KEY)\s*=\s*([^\s"${}]+)', content)
            for param_name, param_val in matches:
                if param_val.lower() not in ['changeme', 'placeholder', 'dummy', 'your_key_here', 'your_password_here', 'null', 'none']:
                    findings.append(f"Hardcoded configuration value for '{param_name}' in compose file: {cfile}")

    # Verify template files do not leak raw values
    for tfile in env_templates:
        if os.path.exists(tfile):
            with open(tfile, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()

            for line_no, line in enumerate(lines, 1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                if '=' in line:
                    param_name, param_val = line.split('=', 1)
                    param_name = param_name.strip()
                    param_val = param_val.strip()

                    # High risk keywords
                    if re.search(r'(?i)(PRIVATE_KEY|TOKEN|SECRET|PASSWORD|JWT_SECRET)', param_name):
                        # If value looks like a real long key/hash without template indicators
                        if len(param_val) > 20 and not re.search(r'(?i)(your|placeholder|change|example|dummy|<.*>|\${.*})', param_val):
                            findings.append(f"Unmasked template variable '{param_name}' in {tfile}:{line_no}")

    if findings:
        print("❌ Environment template / Docker Compose security check failed:")
        for item in findings:
            print(f"  - {item}")
        return False

    print(f"Verified {len(compose_files)} Docker Compose file(s) and {len(env_templates)} Environment Template file(s).")
    return True

if __name__ == "__main__":
    if check_env_templates():
        print("✅ docker-compose env templates check passed.")
        sys.exit(0)
    else:
        print("❌ docker-compose env templates check failed.")
        sys.exit(1)
