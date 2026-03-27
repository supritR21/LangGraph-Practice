# LangGraph Practice

A hands-on Python practice repository for building LangGraph-based agents, tool-calling workflows, memory-enabled conversations, and human-in-the-loop interactions.

## Overview

This repo contains multiple standalone scripts exploring LangGraph concepts:

- Basic ReAct weather agents
- Tool-calling with Tavily search
- Stateful conversations with checkpointers
- Human interruption/resume patterns
- State replay and history inspection

## Tech Stack

- Python 3.12+
- LangGraph
- LangChain
- OpenAI / Groq model integrations
- Tavily search integration
- python-dotenv

## Project Structure

```text
LangGraph-Practice/
	agent1.py
	agent2.py
	main.py
	test.py
	practice2/
		p1.py
		p2.py
		p3.py
		p4.py
		p5.py
		p6.py
		graph.png
		graph1.png
		graph3.png
	pyproject.toml
	uv.lock
	.python-version
	README.md
```

## Installation

### Option A: Using uv (recommended)

```bash
uv sync
```

### Option B: Using pip + venv

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

pip install -U pip
pip install -e .
```

## Environment Variables

Create a `.env` file in project root with the keys required by the scripts you run:

```env
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key
GROQ_API_KEY=your_groq_key
```

## Run Scripts

Run any script directly:

```bash
python agent1.py
python agent2.py
python practice2/p1.py
python practice2/p2.py
python practice2/p3.py
python practice2/p4.py
python practice2/p5.py
python practice2/p6.py
```

## Script Guide

### Top-level

- `agent1.py`
	- Weather assistant with Groq model fallback to mock model.
	- Uses `create_react_agent` and a custom weather tool.

- `agent2.py`
	- ReAct weather agent with structured output (`WeatherResponse`).

- `main.py`
	- Simple starter script (`Hello from langgraphproject!`).

- `test.py`
	- Direct external inference API test script.

### practice2 modules

- `p1.py`
	- Minimal chatbot graph with one node.
	- Interactive terminal chat loop.

- `p2.py`
	- Tool-calling loop with a custom `BasicToolNode` and routing logic.

- `p3.py`
	- Adds `MemorySaver` checkpointing and thread-based conversation memory.

- `p4.py`
	- Human-in-the-loop using `interrupt()` and `Command(resume=...)`.

- `p5.py`
	- Human validation step that updates graph state (`name`, `birthday`) through tool-driven state updates.

- `p6.py`
	- Memory history inspection and replay from a saved checkpoint.

## Key Concepts Covered

- `StateGraph` construction
- Message accumulation with `add_messages`
- Tool binding and conditional routing
- Persistent thread memory with checkpointers
- Interrupt/resume flow for human assistance
- Graph state history replay

## Notes

- Scripts are learning-oriented and mostly independent of each other.
- Some scripts use OpenAI models, others use Groq models.
- Generated graph images in `practice2/` are visualization outputs.

## Troubleshooting

- API/auth errors:
	- Verify `.env` keys and billing/access for the selected provider.

- Missing module errors:
	- Ensure environment is activated and dependencies are installed from `pyproject.toml`.

- Tool call errors:
	- Confirm `TAVILY_API_KEY` is set when running tool-enabled scripts.

## Author

Suprit Raj
