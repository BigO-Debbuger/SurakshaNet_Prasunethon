import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from composio import Composio

COMPOSIO_API_KEY = "ak_xhEdApPVj-bJ2prIahSo"
composio_client = Composio(api_key=COMPOSIO_API_KEY)

print("="*60)
print("  TESTING GMAIL & SLACK DISPATCH VIA COMPOSIO")
print("="*60)

print("\n1. Checking Connected Accounts...")
try:
    accounts = composio_client.connected_accounts.list().items
    print(f"Connected accounts count: {len(accounts)}")
    for acc in accounts:
        toolkit_name = acc.toolkit.slug if acc.toolkit else 'unknown'
        status = acc.status
        print(f" - Toolkit: {toolkit_name}, Status: {status}, ID: {acc.id}")
except Exception as e:
    print(f"Could not list connections: {e}")

print("\n2. Testing Gmail Send Email...")
try:
    response = composio_client.tools.execute(
        slug="GMAIL_SEND_EMAIL",
        arguments={
            "recipient_email": "parthgochhwal17@gmail.com",
            "to": "parthgochhwal17@gmail.com",
            "subject": "SurakshaNet Alert Test",
            "body": "This is a test security alert from SurakshaNet to verify Gmail integration."
        },
        user_id="default",
        dangerously_skip_version_check=True
    )
    print(f"[SUCCESS] Gmail response: {response}")
except Exception as e:
    print(f"[ERROR] Gmail failed: {e}")

print("\n3. Testing Slack Message...")
try:
    response = composio_client.tools.execute(
        slug="SLACK_CHAT_POST_MESSAGE",
        arguments={
            "channel": "#surakshanet-alerts",
            "text": "*SurakshaNet Test Alert*: Slack integration test."
        },
        user_id="default",
        dangerously_skip_version_check=True
    )
    print(f"[SUCCESS] Slack response: {response}")
except Exception as e:
    print(f"[ERROR] Slack failed: {e}")

print("\n" + "="*60)
