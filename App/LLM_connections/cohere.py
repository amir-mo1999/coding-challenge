"""Connection to the Cohere API"""

import cohere
import os

co = cohere.Client(os.environ.get("COHERE_AI_API_KEY"))
