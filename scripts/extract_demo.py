
import json
import sys
import re
from pathlib import Path

def extract_fields(transcript):

    data = {
        "account_id": "",
        "company_name": "",
        "business_hours": {"days":"", "start":"", "end":"", "timezone":""},
        "office_address": "",
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": {},
        "non_emergency_routing_rules": {},
        "call_transfer_rules": {"timeout_seconds":60,"retries":2},
        "integration_constraints": [],
        "after_hours_flow_summary":"",
        "office_hours_flow_summary":"",
        "questions_or_unknowns":[],
        "notes":"Extracted from demo transcript"
    }

    company = re.search(r'company name is ([A-Za-z0-9 ]+)', transcript, re.I)
    if company:
        data["company_name"] = company.group(1).strip()

    if "sprinkler" in transcript.lower():
        data["services_supported"].append("sprinkler service")

    if "fire alarm" in transcript.lower():
        data["services_supported"].append("fire alarm service")

    if "emergency" in transcript.lower():
        data["emergency_definition"].append("caller mentions emergency")

    if not data["company_name"]:
        data["questions_or_unknowns"].append("company name not mentioned")

    return data


def main():

    transcript_file = sys.argv[1]
    account_id = sys.argv[2]
    output_dir = Path(sys.argv[3])

    transcript = open(transcript_file).read()

    data = extract_fields(transcript)
    data["account_id"] = account_id

    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_dir/"account_memo.json","w") as f:
        json.dump(data,f,indent=2)

    print("Demo extraction complete")


if __name__ == "__main__":
    main()
