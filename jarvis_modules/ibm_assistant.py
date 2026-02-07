import os
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

IBM_ASSISTANT_API_KEY = os.getenv('IBM_ASSISTANT_API_KEY', 'YOUR_ASSISTANT_API_KEY')
IBM_ASSISTANT_URL = os.getenv('IBM_ASSISTANT_URL', 'YOUR_ASSISTANT_URL')
IBM_ASSISTANT_ID = os.getenv('IBM_ASSISTANT_ID', 'YOUR_ASSISTANT_ID')

def talkibm(tm):
    authenticator = IAMAuthenticator(IBM_ASSISTANT_API_KEY)
    assistant = AssistantV2(version='2021-07-27', authenticator=authenticator)
    assistant.set_service_url(IBM_ASSISTANT_URL)
    session = assistant.create_session(assistant_id=IBM_ASSISTANT_ID).get_result()
    session_id = session['session_id']
    response = assistant.message(
        assistant_id=IBM_ASSISTANT_ID,
        session_id=session_id,
        input={'message_type': 'text', 'text': tm}
    ).get_result()
    try:
        return response['output']['generic'][0]['text']
    except Exception:
        return "I didn't understand that."
