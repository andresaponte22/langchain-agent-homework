# Personal Research Assistant Agent

A LangChain-powered research assistant that uses the ReAct pattern to help users look up information on Wikipedia, check the weather, perform calculations, and save notes. Built with LangGraph's `create_react_agent` and OpenAI. 

## Tools Implemented

| Tool | Description |
|------|-------------|
| `get_weather` | Fetches current weather for any city using the wttr.in API. |
| `search_wikipedia` | Searches Wikipedia and returns a summary of the top result. |
| `calculate` | Evaluates math expressions safely using `numexpr` (not `eval()`). |
| `save_note` | Appends a timestamped note to a local `notes.txt` file. |

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/andresaponte22/langchain-agent-homework.git
   cd langchain-agent-homework
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your API key:
   ```
   OPENAI_API_KEY=your-key-here
   ```

5. Run the agent:
   ```bash
   python agent.py
   ```

## Example Conversation

> **You:** Whats the weather in Toronto?
>
> **Assistant:** The current weather in Toronto is 14°C with cloudy conditions. If you need more details or a forecast, just let me know!
>
> **You:** Search Wikipedia for OSPF routing protocol
>
> **Assistant:** Open Shortest Path First (OSPF) is a routing protocol used for Internet Protocol (IP) networks. It employs a link state routing (LSR) algorithm and is categorized as an interior gateway protocol (IGP), functioning within a single autonomous system (AS). OSPF collects link state information from available routers to create a topology map of the network, which is then used to generate a routing table for directing packets based on their destination IP addresses. It supports both IPv4 and IPv6 networks and is commonly utilized in large enterprise networks. OSPF was originally designed in the 1980s, with OSPF version 2 defined in RFC 2328 (1998) and updates for IPv6 specified in OSPF version 3 in RFC 5340 (2008). It also supports the Classless Inter-Domain Routing (CIDR) addressing model. If you need more specific information or details, feel free to ask!
>
> **You:** What is 1024 * 768?
>
> **Assistant:** The result of 1024 x 768 is 786,432. If you have any more calculations or questions, feel free to ask!
>
> **You:** Save a note: Finished testing my LangChain agent
>
> **Assistant:** Your note "Finished testing my LangChain agent" has been saved successfully. If you need anything else, just let me know!
>
> **You:** What did I ask you about earlier?
>
> **Assistant:** Earlier, you asked about the weather in Toronto, the OSPF routing protocol, and you requested a calculation for 1024 x 768. Additionally, you asked me to save a note about finishing testing your LangChain agent. If you need more information on any of these topics, just let me know!
>
> **You:** quit
>
> Goodbye!

## Reflection

**What was the most interesting thing I learned?**

The most interesting thing I learned was how accessible it is to build a functional AI agent using just a CLI and a few Python packages. I am used to interacting with AI through web browsers or desktop apps, so seeing the entire ReAct loop (reasoning, selecting a tool, executing, responding) happen in a terminal was a shift in perspective. It made the underlying mechanics of how AI agents work much more concrete. Understanding that the LLM reads tool docstrings to decide which tool to call was a key insight into how agent decision-making actually works under the hood.

**What was the hardest part?**

I did not encounter any major blockers during this assignment. Most of the architecture is handled by LangChain and LangGraph, so the core agent setup was straightforward once the dependencies were installed. The closest thing to a challenge was making sure the environment was configured correctly (virtual environment, API key in .env, correct package versions), which is more of a software engineering discipline issue than a coding problem. That said, getting comfortable with that setup process is a skill in itself.

**What would I add next if I had more time?**

If I had more time, I would personalize the agent further by giving it a more defined role and personality tailored to my workflow. I would also explore giving it access to local files and directories so it could read, search, and summarize documents on my machine. Beyond that, integrating a vector database for long-term memory across sessions would make it a genuinely useful daily research tool rather than a one-off demo.