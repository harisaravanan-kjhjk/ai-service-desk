from services.ai_service import ask_llm
from agents.prompts import prompts
def fall_back_llm(schema,corrupted_output,source):
    prompt=prompts[source].format(schema=schema,corrupted_output=corrupted_output)
    return ask_llm(prompt)
