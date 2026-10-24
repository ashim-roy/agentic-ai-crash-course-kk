# Agentic AI Crash Course

A hands-on learning project for understanding and building Agentic AI systems using Python and the OpenAI API.

This repository follows a practical, incremental approach: start with basic LLM API calls, then build tool-calling workflows and progressively evolve them into more capable AI agents.

**Repository:** [agentic-ai-crash-course-kk](https://github.com/ashim-roy/agentic-ai-crash-course-kk)

## Goals

- Understand LLM API integration and response handling.
- Track token usage and estimate API costs.
- Implement function/tool calling with Python.
- Build an agent loop that executes tools and feeds results back to an LLM.
- Learn agent state, planning, memory, RAG, and production-readiness concepts.

## Technology Stack

- Python 3
- OpenAI Python SDK
- OpenAI API
- python-dotenv
- Git and GitHub

## Project Structure

```text
agentic-ai-crash-course-kk/
├── .venv/                         # Local Python virtual environment
├── markers/                       # Local task completion markers
├── .env                           # API credentials; never commit
├── .gitignore
├── llm_client.py                  # Reusable LLM client
├── test_llm_client.py             # Tests the reusable client manually
├── task_1_import_setup.py          # Import required libraries
├── task_2_client_initialization.py # Initialize the API client
├── task_3_api_call_explained.py    # First LLM API call
├── task_4_extract_response.py      # Extract the generated answer
├── task_5_token_costs.py           # Token usage and cost estimates
├── task_6_tool_calling.py          # First calculator tool
├── task_7_agent_loop.py            # Execute a tool and return its result
└── task_8_multi_tool_agent.py      # Multi-tool, multi-round agent
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/ashim-roy/agentic-ai-crash-course-kk.git
cd agentic-ai-crash-course-kk
```

### 2. Create and activate a virtual environment

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install openai python-dotenv
```

### 4. Configure the API key

Create a `.env` file in the project root:

```dotenv
OPENAI_API_KEY=your_actual_api_key
# Optional: configure a compatible API endpoint
# OPENAI_API_BASE=https://api.openai.com/v1
```

The application uses the official OpenAI endpoint by default if `OPENAI_API_BASE` is unset.

**Security:** Never commit `.env` or expose your API key in source code, logs, screenshots, or GitHub.

## Completed Labs

### Lab 1: AI Fundamentals

| Task | Topic | What it teaches |
|---|---|---|
| 1 | Import libraries | Use the OpenAI SDK and Python utilities |
| 2 | Client initialization | Load credentials and configure the client |
| 3 | First API call | Send a prompt to a language model |
| 4 | Response extraction | Access the generated text |
| 5 | Token usage and cost | Inspect token counts and estimate request costs |

### Lab 2: Building Tool-Using Agents

| Task | Topic | What it teaches |
|---|---|---|
| 6 | First tool call | Define and execute a calculator function |
| 7 | Agent loop | Send tool results back to the LLM |
| 8 | Multi-tool agent | Select tools and execute multi-round workflows |

## Key Concepts

### Making an LLM request

```python
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": "Explain AI agents"}
    ]
)

answer = response.choices[0].message.content
print(answer)
```

### Inspecting token usage

```python
input_tokens = response.usage.prompt_tokens
output_tokens = response.usage.completion_tokens
total_tokens = response.usage.total_tokens
```

Token-based cost calculations are estimates. Always verify the current pricing for the model you use.

### Understanding the agent loop

The current multi-tool agent demonstrates this workflow:

1. Receive a user request.
2. Ask the LLM to select an appropriate tool.
3. Execute the requested Python function.
4. Return the tool result to the LLM.
5. Repeat until the LLM provides a final answer or the configured round limit is reached.

```text
User Request
     |
     v
     LLM
     |
     v
  Tool Call
     |
     v
Python Execution
     |
     v
 Tool Result
     |
     +------> LLM
                |
                v
           Final Answer
```

The LLM requests tools; the application is responsible for executing them.

## Running the Labs

Execute individual scripts from the project root:

```bash
python task_1_import_setup.py
python task_2_client_initialization.py
python task_3_api_call_explained.py
python task_4_extract_response.py
python task_5_token_costs.py
python test_llm_client.py
python task_6_tool_calling.py
python task_7_agent_loop.py
python task_8_multi_tool_agent.py
```

These scripts make API requests where applicable, so model usage may incur charges.

## Roadmap

- [ ] Improve tool argument validation and error handling.
- [ ] Add API retries, timeouts, and usage tracking.
- [ ] Generalize tool execution into a reusable agent runtime.
- [ ] Add conversation state and memory.
- [ ] Integrate RAG and retrieval tools.
- [ ] Explore planning and multi-agent workflows.
- [ ] Add automated tests and evaluation.
- [ ] Add tracing, observability, and production safeguards.

## Learning Approach

Each task builds on the previous one. Code is intentionally small and progressively more capable, with inline comments explaining important implementation details.

The objective is not just to call an LLM API, but to understand how an application coordinates models, tools, state, and execution to build reliable agentic workflows.

## License

A license has not yet been specified.
