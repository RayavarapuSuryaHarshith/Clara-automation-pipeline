
import json
import sys
from pathlib import Path

def generate_agent_spec(memo):

    spec = {
        "agent_name": memo.get("company_name","Clara Agent"),
        "voice_style":"professional and calm",
        "version":"v1",
        "variables":{
            "timezone": memo["business_hours"]["timezone"],
            "business_hours": memo["business_hours"],
            "address": memo["office_address"]
        },
        "system_prompt": f"""You are Clara, the automated call assistant for {memo.get('company_name','the company')}.

Business Hours Flow:
1. Greet caller
2. Ask reason for call
3. Collect name and phone number
4. Transfer to service desk
5. If transfer fails apologize and promise callback
6. Ask if they need anything else
7. Close call

After Hours Flow:
1. Greet caller
2. Ask if issue is emergency
3. If emergency collect name, phone, and address immediately
4. Attempt dispatch transfer
5. If transfer fails assure quick follow‑up
6. If non‑emergency collect request for next business day
""" ,
        "call_transfer_protocol":{
            "timeout":60,
            "retries":2
        },
        "fallback_protocol":"If transfer fails apologize and assure follow-up."
    }

    return spec


def main():

    memo_file = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    memo = json.load(open(memo_file))

    spec = generate_agent_spec(memo)

    with open(output_dir/"agent_spec.json","w") as f:
        json.dump(spec,f,indent=2)

    print("Agent spec generated")


if __name__ == "__main__":
    main()
