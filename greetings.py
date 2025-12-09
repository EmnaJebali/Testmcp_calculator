from mcp.server.fastmcp import FastMCP

mcp=FastMCP(
    name="Greetings_server"
)

@mcp.tool()
def say_hello(name: str) ->str:
    """
    a simple function that returns a greeting message.
    """
    return f"Hello {name}, welcome to greetings server!"

if __name__ == "__main__":
    mcp.run(transport="stdio")