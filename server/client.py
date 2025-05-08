import asyncio
from langchain_groq import ChatGroq

from mcp_use import MCPAgent, MCPClient
import os
from dotenv import load_dotenv

async def run_memory_chat():
    """Run a memory chat with the MCP Agent's built-in conversation memory."""
    # Load environment variables from .env file
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    # Config file path 
    config_file = os.path.join(os.path.dirname(__file__), "weather.json")

    print("Initializing Chat...")

    # Create MCP Client and llm
    client = MCPClient(config_file)
    llm = ChatGroq(model_name="qwen-qwq-32b")

    # MCP Agent with memory enabled
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True # Enable built-in conversation memory
    )

    print("\n===== Interactive MCP Client =====")
    print("Type 'exit' to end the conversation.\n") 
    print("Type 'clear' to clear the memory.\n")
    print("===================================\n")


    try :
        # Main chat loop
        while True:
            # Get user input
            user_input = input("\nYou: ")

            # Check for exit condition
            if user_input.lower() in ["exit", "quit"]:
                print("Ending conversation...")
                break

            # Check for memory clearing
            if user_input.lower() == "clear":
                agent.clear_memory()
                print("Conversation history cleared.")
                continue

            # Get response from the agent
            print("\nMCP: ", end="", flush=True)

            try :
                # Run the agent with user input (memory handling is automatic)
                response = await agent.run(user_input)
                print(response)
            except Exception as e:
                print(f"\nError: {e}")

    except KeyboardInterrupt:
        print("\nConversation ended.")

    finally:
        # Cleanup
        if client and client.sessions:
            await client.close_all_sessions()


if __name__ == "__main__":
    asyncio.run(run_memory_chat())
