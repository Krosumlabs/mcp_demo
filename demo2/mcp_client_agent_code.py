import asyncio

from dotenv import load_dotenv

# Groq LLM
from langchain_groq import ChatGroq

# MCP Client
from langchain_mcp_adapters.client import MultiServerMCPClient

# LangGraph
from langgraph.prebuilt import ToolNode, tools_condition,create_react_agent


# Load .env file
load_dotenv()

async def main():
    # connect to remote mcp server
    client = MultiServerMCPClient({"remote_calculator":{"transport":"http","url":"http://localhost:8000/mcp"}})
    tools = await client.get_tools()
    print("\nAvailable MCP Tools:")
    for tool in tools:
        print("-", tool.name)
    llm = ChatGroq(model="qwen/qwen3.6-27b")
    agent = create_react_agent(model=llm,tools = tools)
    result = await agent.ainvoke({"messages":[{"role":"user","content": "add 10 and 20 use the available tools"}]})
    print(result["messages"][-1].content)

if __name__ == '__main__':
	asyncio.run(main())



