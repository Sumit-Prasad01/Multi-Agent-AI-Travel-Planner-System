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
from src.config import settings

llm = ChatGroq(
    model = settings.MODEL,
    temperature = 0.7
)


# State
class TravelState(TypedDict):

    messages: Annotated[list[AnyMessage], operator.add]
    user_query: str
    flight_results: str
    hotel_results: str
    itinerary: str
    llm_calls : int



# Flight Agent
def flight_agent(state : TravelState):
    query = state["user_query"]
    flight_data = search_flights(query)

    return {
        "flight_results" : flight_data,
        "messages" : [
            AIMessage(content = f"Flight results fetched")
        ],
        "llm_calls" : state.get("llm_calls", 0) + 1

    }


# Hotel Agent
def hotel_agent(state : TravelState):
    query = f"Best hotels for {state["user_query"]}"
    hotel_results = tavily_search(query)
    
    return {
        "hotel_results" : hotel_results,
        "messages" : [
            AIMessage(content = f"Hotel information fetched")
        ],
        "llm_calls" : state.get("llm_calls", 0) + 1
    }


# Itinerary
def itinerary_agent(state : TravelState):
    prompt = f"""
            Create a travel itinerary.
            User Query:
            {state['user_query']}

            Flight Results:
            {state['flight_results']}

            Hotel Results:
            {state['hotel_results']}
        """
    
    response = llm.invoke([
        SystemMessage(
            content = "You are an expert travell planner"
        ),
        HumanMessage(content = prompt)
    ])


    return {
        "itinerary" : response.content,
        "messages" : [response],
        "llm_calls" : state.get("llm_calls", 0) + 1
    }


# Final Response Agent
def final_agent(state : TravelState):
    final_prompt = f"""
            Generate final travel response.

            Flights:
            {state['flight_results']}

            Hotels:
            {state['hotel_results']}

            Itinerary:
            {state['itinerary']}
        """
    
    response = llm.invoke([
        HumanMessage(content = final_prompt)
    ])

    return {
        "messages" : [response],
        "llm_calls" : state.get("llm_calls", 0) + 1
    }