#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from debate.crew import Debate
from dotenv import load_dotenv
import os

load_dotenv()
print("************************************************")
print("Loaded key:", os.getenv("GROQ_API_KEY"))

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'motion': 'There needs to be strict laws to regulate LLMs',
    }
    
    try:
        result = Debate().crew().kickoff(inputs=inputs)
        print(result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
