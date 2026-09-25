from mcp.server.fastmcp import FastMCP

# Create MCP server

mcp = FastMCP("Remote Calc server",stateless_http = True,json_response  = True)

# Tool-1
@mcp.tool()
def calc(a: int,b: int) ->int:
 """Add two numbers"""
 return a+b

# Tool-2
@mcp.tool()
def get_server_info() ->str:
 """ Get Information about this remote MCP server"""
 return "Remote MCP calculate server is running"


# Start MCP server 
if __name__ == '__main__':
	mcp.run(transport = "streamable-http")

# http://localhost:8000/mcp
