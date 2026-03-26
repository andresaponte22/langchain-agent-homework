# Personal Research Assistant Agent

A LangChain-powered research assistant that uses the ReAct pattern to help users look up information on Wikipedia, check the weather, perform calculations, and save notes. Built with LangGraph's `create_react_agent` and Anthropic Claude.

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
   git clone https://github.com/YOUR_USERNAME/langchain-agent-homework.git
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
   ANTHROPIC_API_KEY=your-key-here
   ```

5. Run the agent:
   ```bash
   python agent.py
   ```

## Example Conversation

```
(PASTE A REAL CONVERSATION HERE AFTER TESTING)
```

## Reflection

(WRITE 3-5 SENTENCES HERE)
- What was the most interesting thing you learned?
- What was the hardest part?
- What would you add next if you had more time?
