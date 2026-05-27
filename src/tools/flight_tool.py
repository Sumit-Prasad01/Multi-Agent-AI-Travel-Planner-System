import requests
from src.config import settings


def search_flights(query : str, limit : int =  5) -> str:

    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": settings.AVIATIONSTACK_API_KEY,
        "limit": 5
    }

    response = requests.get(url, params)

    data = response.json()

    flights = []

    if "data" in data:

        for flight in data["data"][:5]:

            airline = flight.get("airline", {}).get("name", "Unknown")

            departure = flight.get(
                "departure", {}
            ).get("airport", "Unknown")

            arrival = flight.get(
                "arrival", {}
            ).get("airport", "Unknown")

            status = flight.get("flight_status", "Unknown")

            flights.append(
                f"""
                    Airline: {airline}
                    Departure: {departure}
                    Arrival: {arrival}
                    Status: {status}
                """
            )

    return "\n".join(flights)