import os
import operator
import psycopg
from typing import TypedDict, Annotated

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.postgres import PostgresSaver
from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
    AnyMessage,
    AIMessage
)
from langchain_groq import ChatGroq

from src.tools.tavily_tool import tavily_search
from src.tools.flight_tool import search_flights