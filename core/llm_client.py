# core/llm_client.py

from core.config import settings
from core.budget_guard import budget_guard


class LLMClient:

    def __init__(self):
        self.model = settings.MODEL

    def generate(self, prompt: str, max_output_tokens: int = 300):

        if budget_guard.is_dry_run():
            return {
                "text": "[DRY_RUN] Mock GPT response",
                "usage": {
                    "prompt_tokens": 0,
                    "completion_tokens": 0,
                    "total_tokens": 0,
                    "cost": 0
                }
            }

        if not budget_guard.can_call():
            raise RuntimeError(
                "OpenAI budget limit exceeded"
            )

        # Gerçek OpenAI bağlantısı sonraki aşamada eklenecek.
        # Bu aşamada bilinçli olarak API çağrısı yapılmıyor.

        return {
            "text": "LLM response placeholder",
            "usage": {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0,
                "cost": 0
            }
        }


llm_client = LLMClient()