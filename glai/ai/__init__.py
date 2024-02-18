from .easy_ai import EasyAI
from glai.ai.llama_ai import LlamaAI


# Making certain symbols available when the package is imported
__all__ = ["EasyAI", "LlamaAI"]
# print(f"Initializing ai package, available classes: {__all__}")
