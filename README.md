# MCP Sample Project

## Overview
This repository demonstrates the implementation of a Model-Controller-Prompt (MCP) system, showcasing how to build and interact with MCP servers and clients. The project includes a weather service example that illustrates the integration of external APIs with LLM-powered agents.

## Architecture

### MCP Communication Flow
1. **Client-Server Interaction**
   - The MCP client (`client.py`) initiates communication with the MCP server
   - Uses LangChain and Groq LLM for natural language processing
   - Maintains conversation memory for context-aware interactions

2. **Server Implementation**
   - Built using FastMCP framework
   - Exposes tools and resources for client consumption
   - Example weather service demonstrates API integration with National Weather Service

3. **LLM Integration**
   - Uses Groq's Qwen model for natural language understanding
   - Processes user queries and determines appropriate tool usage
   - Manages conversation context and memory

## Getting Started

### Prerequisites
- Python 3.x
- UV package manager
- Docker (optional, for containerized deployment)

### Installation
1. Clone the repository
2. Install dependencies using UV:
   ```bash
   uv pip install -r requirements.txt
   ```

### Running the Code

#### Basic MCP Server
```bash
# Start the weather MCP server
uv run mcp dev server/weather.py

# Install MCP server to Claude Desktop
uv run mcp install server/weather.py
```

#### MCP Client
```bash
# Run the interactive MCP client
uv run server/client.py
```

#### Docker Deployment
```bash
# Build and run using Docker
cd mcpserver
docker build -t mcp-server .
docker run -p 8000:8000 mcp-server
```

## Features
- Interactive chat interface with memory support
- Weather alerts retrieval for US states
- Docker containerization support
- Configurable MCP server implementation

## More to Explore

### MCP Resources
- [MCP Documentation](https://docs.mcp.dev)
- [FastMCP Framework](https://github.com/fastmcp/fastmcp)
- [MCP Best Practices](https://docs.mcp.dev/best-practices)

### MCP Prompts
- Example prompts and conversation patterns
- Tool usage patterns
- Memory management strategies

### Advanced Topics
- Custom tool development
- Resource management
- Error handling and recovery
- Performance optimization

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
[Add your license information here]
