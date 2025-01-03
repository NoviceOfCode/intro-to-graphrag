# Description: This file contains the configuration for the Neo4j and OpenAI clients.
# Environment variables for NEO4J_URI (usually `bolt://localhost:7687` ), NEO4J_PASSWORD, NEO4J_USERNAME, and OPENAI_API_KEY should be set.
# The OpenAI API key can be obtained from the OpenAI website.
# The Neo4j URI, username, and password can be obtained from the Neo4j Desktop or Aura console.
import os
from dotenv import load_dotenv

# def get_neo4j_uri():
#     load_dotenv()
#     uri = os.environ.get("NEO4J_URI")
#     if not uri:
#         raise ValueError("NEO4J_URI environment variable not set.")
#     return uri
#
# def get_neo4j_username():
#     load_dotenv()
#     username = os.environ.get("NEO4J_USERNAME")
#     if not username:
#         raise ValueError("NEO4J_USERNAME environment variable not set.")
#     return username
#
# def get_neo4j_password():
#     load_dotenv()
#     password = os.environ.get("NEO4J_PASSWORD")
#     if not password:
#         raise ValueError("NEO4J_PASSWORD environment variable not set.")
#     return password
#
# def get_openai_client():
#     load_dotenv()
#     api_key = os.environ.get("OPENAI_API_KEY")
#     if not api_key:
#         raise ValueError("OPENAI_API_KEY environment variable not set.")
#     return OpenAI(api_key=api_key)

import os
from dotenv import load_dotenv
from neo4j import GraphDatabase
from openai import OpenAI

load_dotenv()
# Create a Neo4j driver instance
neo4j_driver = GraphDatabase.driver(os.environ.get("NEO4J_URI"),
    auth=(os.environ.get("NEO4J_USERNAME"), os.environ.get("NEO4J_PASSWORD")),
)

# Create an OpenAI client instance
open_ai_client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)