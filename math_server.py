from typing import Union
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="MathServer")


@mcp.tool()
def add(a: float, b: float) -> float:
    """Return a + b."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Return a - b."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Return a * b."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> Union[float, str]:
    """Return a / b or an error message when dividing by zero."""
    if b == 0:
        return "error: division by zero"
    return a / b


if __name__ == "__main__":
    # start server on stdio
    mcp.run(transport="stdio")
