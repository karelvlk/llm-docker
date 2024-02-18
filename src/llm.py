from glai import EasyAI
from typing import Generator
import logging

logger = logging.getLogger(__name__)


class LLM:
    def __init__(self):
        self.llm = None
        self.initialized = False

    def __call__(self, user_prompt: str) -> Generator[str, None, None]:
        return self.llm.generate(user_prompt)

    def is_initialized(self) -> bool:
        return self.initialized

    def initialize(
        self, model: str = "Phi2", max_total_tokens: int = 300, quantization: str = "q8"
    ) -> EasyAI:
        try:
            eai = EasyAI()
            eai.load_model_db()
            eai.find_model_data(model_name=model, quantization=quantization)
            eai.load_ai(max_total_tokens=max_total_tokens)
            self.llm = eai
            self.initialized = True

        except Exception as e:
            logger.error(f"Initialization of LLM failed with error: {e}")

        return None
