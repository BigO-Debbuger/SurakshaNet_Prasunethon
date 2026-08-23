# setup_auth.py
import sys
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from composio import Composio

# Your API Key
COMPOSIO_API_KEY = "ak_xhEdApPVj-bJ2prIahSo"

# Initialize Composio client
composio_client = Composio(api_key=COMPOSIO_API_KEY)

print("\n" + "="*55)
print("     SURAKSHANET AUTHENTICATION SETUP")
print("="*55)

try:
    # 1. Generate Gmail Connection Link
    print("\n1. Generating GMAIL connection link...")
    gmail_conn = composio_client.connected_accounts.link(user_id="default", auth_config_id='ac_gkgS-z2F7WNk')
    print(f"👉 CLICK HERE TO CONNECT GMAIL:\n   {gmail_conn.redirect_url}")

    # 2. Generate Slack Connection Link
    print("\n2. Generating SLACK connection link...")
    slack_conn = composio_client.connected_accounts.link(user_id="default", auth_config_id='ac_8xbRAYdCT7nd')
    print(f"👉 CLICK HERE TO CONNECT SLACK:\n   {slack_conn.redirect_url}")

    print("\n" + "="*55)
    print(" Instructions:")
    print(" 1. Click both links above to authorize Gmail & Slack.")
    print(" 2. After authorizing, run 'py test_alert.py' to verify.")
    print(" 3. Restart 'py app.py' in your backend terminal.")
    print("="*55 + "\n")

except Exception as e:
    print(f"❌ Error generating links: {e}")
    import traceback
    traceback.print_exc()