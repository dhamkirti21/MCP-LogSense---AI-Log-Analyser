from mcp.server.fastmcp import FastMCP
from .tools import recent_logs, recent_anomalies, system_metrics

mcp = FastMCP("AI Log Analyzer MCP")

@mcp.tool()
def get_recent_logs(limit: int = 10):
    return recent_logs(limit)

@mcp.tool()
def get_recent_anomalies(limit: int = 5):
    return recent_anomalies(limit)

@mcp.tool()
def get_system_metrics():
    return system_metrics()

if __name__ == "__main__":
    mcp.run()