import os

from dotenv import load_dotenv


load_dotenv()


INFURA_API_KEY = os.getenv("INFURA_API_KEY")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
