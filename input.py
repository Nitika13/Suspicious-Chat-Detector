import re
def remove_emojis(message):
  emoji=re.compile('[\U0001F600-\U0001F64F'
        '\U0001F300-\U0001F5FF'
        '\U0001F680-\U0001F6FF'
        '\U0001F700-\U0001F77F'
        '\U0001F780-\U0001F7FF'
        '\U0001F800-\U0001F8FF'
        '\U0001F900-\U0001F9FF'
        '\U0001FA00-\U0001FA6F'
        '\U0001FAD0-\U0001FAD9'
        '\U00002702-\U000027B0'
        '\U0001F004-\U0001F0CF'
        '\U0000203C-\U0000203D'
        '\U00002B50'
        '\U0001F004'
        '\U0001F600-\U0001F64F'
        ']+', flags=re.UNICODE)
  return emoji.sub('', message)

def remove_lrm_messages(messages):
    lrm = '\u200E'
    filtered_messages = [message for message in messages if lrm not in message]
    return filtered_messages



def extract_text_messages(chat):
  text_messages=[]
  pattern=r'^\[[^\]]+\]\s+[^\:]+: *'
  chat=remove_lrm_messages(chat)

  for message in chat:
    message = re.sub(pattern, '', message)
    if not re.match(r'^[^a-zA-Z]*$',message):
      message=remove_emojis(message)
      text_messages.append(message)
  return text_messages
