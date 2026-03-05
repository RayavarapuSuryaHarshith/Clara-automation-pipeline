
import json
import sys
from pathlib import Path

def main():

    v1_file = Path(sys.argv[1])
    onboarding_updates = Path(sys.argv[2])
    output_dir = Path(sys.argv[3])

    v1 = json.load(open(v1_file))
    updates = json.load(open(onboarding_updates))

    v2 = v1.copy()

    changes = []

    for key,val in updates.items():
        if key in v2 and v2[key] != val:
            changes.append(f"{key} updated")
            v2[key] = val

    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_dir/"account_memo.json","w") as f:
        json.dump(v2,f,indent=2)

    with open(output_dir/"changes.md","w") as f:
        f.write("# Changes\n")
        for c in changes:
            f.write(f"- {c}\n")

    print("Patch applied")


if __name__ == "__main__":
    main()
