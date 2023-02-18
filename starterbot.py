import os
import slack
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

txt = 'DADDY JEFF'

for i in range(100):
    client.chat_postMessage(channel='#a', text=txt)
