"""
Personal Research Assistant Agent
Built with LangChain + LangGraph using the ReAct pattern.
Uses OpenAI GPT as the LLM backbone.
"""

import os
import datetime
import requests
import numexpr
import wikipedia
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

# ──────────────────────────────────────────────
# 1. ENVIRONMENT SETUP
# ──────────────────────────────────────────────
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Create a .env file with your key.")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=api_key,
)

# ──────────────────────────────────────────────
# 2. CUSTOM TOOLS
# ──────────────────────────────────────────────

@tool
def get_weather(city: str) -> str:
    """
    Get the current weather for a city.
    Use this when the user asks about weather, temperature, or forecast
    for any location. Pass the city name as a string.
    Example input: "Toronto"
    """
    try:
        response = requests.get(
            f"https://wttr.in/{city}?format=3",
            timeout=10,
            headers={"User-Agent": "langchain-agent-homework"}
        )
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        return f"Error fetching weather for '{city}': {e}"


@tool
def search_wikipedia(query: str) -> str:
    """
    Search Wikipedia and return a summary of the top result.
    Use this when the user asks to look up a topic, wants a definition,
    or needs factual background information on any subject.
    Example input: "quantum computing"
    """
    try:
        results = wikipedia.search(query, results=1)
        if not results:
            return f"No Wikipedia results found for '{query}'."
        page = wikipedia.page(results[0], auto_suggest=False)
        # Return first 1500 chars to keep context manageable
        summary = page.summary[:1500]
        return f"**{page.title}**\n{summary}"
    except wikipedia.DisambiguationError as e:
        return f"Disambiguation: multiple matches found. Options include: {', '.join(e.options[:5])}"
    except wikipedia.PageError:
        return f"No Wikipedia page found for '{query}'."
    except Exception as e:
        return f"Wikipedia error: {e}"


@tool
def calculate(expression: str) -> str:
    """
    Evaluate a mathematical expression and return the result.
    Use this when the user asks to compute, calculate, or do any math.
    Supports standard operations: +, -, *, /, **, %, sqrt(), abs(), etc.
    Example input: "347 * 29 + 12"
    """
    try:
        result = numexpr.evaluate(expression).item()
        return f"{expression} = {result}"
    except Exception as e:
        return f"Error evaluating '{expression}': {e}"


@tool
def save_note(note: str) -> str:
    """
    Save a note to a local file called notes.txt.
    Use this when the user asks to save, write down, or remember something.
    The note will be appended with a timestamp.
    Example input: "Today I learned about LangChain agents."
    """
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("notes.txt", "a") as f:
            f.write(f"[{timestamp}] {note}\n")
        return f"Note saved successfully at {timestamp}."
    except Exception as e:
        return f"Error saving note: {e}"


# ──────────────────────────────────────────────
# 3. SYSTEM PROMPT
# ──────────────────────────────────────────────

SYSTEM_PROMPT = """You are a Personal Research Assistant. Your job is to help users
look up information, perform calculations, check the weather, and save notes.

Guidelines:
- Always explain your reasoning before using a tool.
- If a query requires multiple steps, break it down and use tools one at a time.
- If a tool returns an error, let the user know and suggest an alternative.
- Be concise but thorough in your responses.
- When saving notes, confirm what was saved.
"""

# ──────────────────────────────────────────────
# 4. AGENT CREATION
# ──────────────────────────────────────────────

tools = [get_weather, search_wikipedia, calculate, save_note]

agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt=SYSTEM_PROMPT,
)

# ──────────────────────────────────────────────
# 5. CONVERSATION LOOP WITH MEMORY
# ──────────────────────────────────────────────

def main():
    print("=" * 50)
    print("  Personal Research Assistant")
    print("  Type 'quit' or 'exit' to end the session.")
    print("=" * 50)

    # Conversation history persists across turns (memory)
    conversation_history = []

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        # Append the new user message to the running history
        conversation_history.append(HumanMessage(content=user_input))

        try:
            # Invoke the agent with the full conversation history
            response = agent.invoke({"messages": conversation_history})

            # Extract the last AI message from the response
            ai_messages = response["messages"]
            # The last message in the returned list is the final AI reply
            last_ai_message = ai_messages[-1]
            assistant_reply = last_ai_message.content

            # Append the AI response to history for memory
            conversation_history.append(last_ai_message)

            print(f"\nAssistant: {assistant_reply}")

        except Exception as e:
            print(f"\n[Error] Something went wrong: {e}")
            print("Please try rephrasing your question.")


if __name__ == "__main__":
    main()
