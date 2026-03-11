# QuickBus MCP Servers

This repository contains two Model Context Protocol (MCP) servers designed to interface with the QuickBus backend API. These servers enable LLM-powered applications to perform administrative tasks and user booking operations through standardized tool interfaces.

## Overview

The project is structured into two specialized MCP servers:

1.  **[DD-QuickBus-Admin-MCP](./DD-QuickBus-Admin-MCP/)**: Provides administrative tools for managing buses, routes, trips, employees, and contact requests.
2.  **[DD-QuickBus-User-MCP](./DD-QuickBus-User-MCP/)**: Provides customer-facing functionality including bus search, seat availability checks, ticket booking, and history management.

## Tech Stack

- **Language**: Python 3.10+
- **Framework**: [FastMCP](https://github.com/jlowin/fastmcp)
- **Dependency Management**: [uv](https://docs.astral.sh/uv/)
- **Communication**: Requests (HTTP/JSON API)
- **Validation**: Pydantic and Validators

## Project Structure

```text
Bus-Mcp/
├── DD-QuickBus-Admin-MCP/     # Administrative Tools
│   ├── main.py                # Server entry point
│   ├── tools/                 # Tool implementations
│   └── schemas/               # Pydantic data models
└── DD-QuickBus-User-MCP/      # Customer Booking Tools
    ├── main.py                # Server entry point
    └── tools/                 # Tool implementations
```

## Installation and Setup

### Prerequisites

- Python 3.10 or higher.
- [uv](https://docs.astral.sh/uv/) package manager (recommended for seamless dependency handling).

### 1. Environment Configuration

Define the backend API location by creating a `.env` file in each server directory.

**`DD-QuickBus-Admin-MCP/.env` and `DD-QuickBus-User-MCP/.env`**:
```env
BASE_URL=https://your-api-url.com
```

### 2. Dependency Installation

Navigate to each directory and synchronize the environment:

```bash
# Admin MCP Setup
cd DD-QuickBus-Admin-MCP
uv sync

# User MCP Setup
cd ../DD-QuickBus-User-MCP
uv sync
```

---

## Testing and Inspection

The FastMCP Inspector is a powerful tool for testing tool definitions and verifying API responses in a web-based interface before integrating with an LLM.

### Running the Inspector

To launch the inspector for either server, use the following command from the respective directory:

```bash
# Launch Admin Inspector
cd DD-QuickBus-Admin-MCP
uv run fastmcp dev inspector main.py

# Launch User Inspector
cd DD-QuickBus-User-MCP
uv run fastmcp dev inspector main.py
```

The inspector will provide a local URL (typically `http://localhost:3000`) where you can manually trigger tools and inspect the JSON payloads.

---

## LLM Client Configuration

To use these servers in an MCP-compatible LLM client (such as Claude Desktop), add the following configurations to your client's settings file.

### Claude Desktop Configuration

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "quickbus-admin": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/Bus-Mcp/DD-QuickBus-Admin-MCP",
        "run",
        "python",
        "main.py"
      ],
      "env": {
        "BASE_URL": "https://your-api-url.com"
      }
    },
    "quickbus-user": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/Bus-Mcp/DD-QuickBus-User-MCP",
        "run",
        "python",
        "main.py"
      ],
      "env": {
        "BASE_URL": "https://your-api-url.com"
      }
    }
  }
}
```

*Note: Replace `/absolute/path/to/` with the actual path on your system.*

---

## Tool Summary

### Administrative Tools (DD-Admin-MCP)
- **Authentication**: `login`
- **Bus Management**: `get_all_buses`, `add_bus`, `update_bus`, `delete_bus`
- **Route Management**: `get_all_routes`, `add_route`
- **Trip Management**: `get_all_trips`, `add_trip`, `update_trip`, `delete_trips`
- **System Management**: `get_employees`, `get_contact_requests`

### Customer Tools (DD-Booking-MCP)
- **Search and Discovery**: `search_bus`, `get_available_seats`
- **Booking Lifecycle**: `create_ticket`, `cancle_ticket`
- **Authentication (OTP)**: `auth`, `validate`
- **Account Management**: `get_tickets`, `get_ticket_details`

