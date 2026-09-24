#!/usr/bin/env python3
"""Sinh inventory Ansible từ output của Terraform.
Dùng: ansible-playbook -i inventory-tu-terraform.py site.yml"""

import json
import subprocess
import sys


def lay_output_terraform():
    """Đọc terraform output. Nếu không có Terraform thì dùng dữ liệu mẫu."""
    try:
        r = subprocess.run(
            ["terraform", "output", "-json"],
            capture_output=True, text=True, timeout=10,
        )
        if r.returncode == 0 and r.stdout.strip():
            return json.loads(r.stdout)
    except Exception:
        pass
    # Dữ liệu mẫu để lab chạy được khi chưa có Terraform
    return {
        "may_web": {"value": [
            {"ten": "web1", "ip": "127.0.0.1", "cong_ssh": 2201},
            {"ten": "web2", "ip": "127.0.0.1", "cong_ssh": 2202},
        ]},
        "may_db": {"value": [
            {"ten": "db1", "ip": "127.0.0.1", "cong_ssh": 2203},
        ]},
    }


def dung_inventory():
    tf = lay_output_terraform()
    inv = {
        "_meta": {"hostvars": {}},
        "all": {"children": ["web", "db", "ungrouped"]},
        "web": {"hosts": [], "vars": {"vai_tro": "web"}},
        "db": {"hosts": [], "vars": {"vai_tro": "database"}},
    }

    for khoa, nhom in (("may_web", "web"), ("may_db", "db")):
        for may in tf.get(khoa, {}).get("value", []):
            ten = may["ten"]
            inv[nhom]["hosts"].append(ten)
            inv["_meta"]["hostvars"][ten] = {
                "ansible_host": may["ip"],
                "ansible_port": may.get("cong_ssh", 22),
                "ansible_user": "quantri",
                "ansible_ssh_private_key_file": "./khoa_lab",
                "ansible_ssh_common_args":
                    "-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null",
            }
    return inv


if __name__ == "__main__":
    if "--list" in sys.argv:
        print(json.dumps(dung_inventory(), indent=2, ensure_ascii=False))
    elif "--host" in sys.argv:
        print(json.dumps({}))
    else:
        print("Dùng: --list hoặc --host <tên máy>", file=sys.stderr)
        sys.exit(1)
