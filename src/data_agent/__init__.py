import os
import sys

# Add the parent directory to the path to import agents, utils, etc.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from agents.data_agent import data_agent
from langchain_core.messages import HumanMessage


def main() -> None:
    """Main entry point for the data agent."""
    print("Welcome to the Data Agent!")
    print("This agent can help you with SQL queries and ETL operations.")
    print("-" * 60)

    while True:
        user_input = input("\nEnter your query (or 'quit' to exit): ").strip()

        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Thank you for using the Data Agent. Goodbye!")
            break

        if not user_input:
            print("Please enter a valid query.")
            continue

        try:
            print("\nProcessing your query...")
            response = data_agent.invoke(
                {
                    "messages": [HumanMessage(content=user_input)],
                    "route_response": ""
                }
            )

            # Extract and display the final answer from messages
            if response.get("messages"):
                final_message = response["messages"][-1]
                print("\nAgent Response:")
                print("-" * 60)
                print(final_message.content if hasattr(final_message, 'content') else final_message)
                print("-" * 60)

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            import traceback
            traceback.print_exc()


__all__ = ["main"]
