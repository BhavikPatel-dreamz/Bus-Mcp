# QuickBus Admin MCP Server

This server provides a Model Context Protocol (MCP) interface for administrative operations within the QuickBus ecosystem. It enables LLM-powered agents to manage core logistics including buses, routes, trips, and personnel.

## Features

- **Resource Management**: Complete CRUD operations for buses and trips.
- **Logistics Mapping**: Define routes with multiple stops, distances, and travel times.
- **Personnel Oversight**: Manage employee records for drivers and conductors.
- **Communication**: Access and manage customer contact requests.
- **Secure Access**: Token-based authentication for all administrative tools.

## Project Structure

```text
DD-QuickBus-Admin-MCP/
├── main.py                # Server entry point and tool registration
├── mcp_server.py          # FastMCP instance configuration
├── tools/                 # Tool implementation logic
│   ├── base.py            # API communication helpers
│   ├── busTools.py        # Bus management tools
│   ├── routesTools.py     # Route definition tools
│   ├── tripTools.py       # Trip scheduling tools
│   └── ...                # Other administrative tools
└── schemas/               # Pydantic models for data validation
```

## Setup and Installation

### Prerequisites

- Python 3.10 or higher.
- [uv](https://docs.astral.sh/uv/) package manager.

### Configuration

Create a `.env` file in this directory:

```env
BASE_URL=https://api.your-quickbus-instance.com
```

### Installation

```bash
uv sync
```

## Running the Server

### Direct Execution
```bash
uv run python main.py
```

### Using FastMCP Inspector
For testing and debugging tool interfaces:
```bash
uv run fastmcp dev inspector main.py
```

## Tool Reference

### Authentication
- `login(email, password)`: Authenticates an admin and returns a Bearer token.

### Bus Operations
- `get_all_buses(token)`
- `add_bus(data: AddBusInput)`
- `update_bus(data: UpdateBusInput)`
- `delete_bus(token, busId)`

### Route and Trip Management
- `get_all_routes(token)`
- `add_route(data: AddRouteInput)`
- `get_all_trips(token)`
- `add_trip(...)`: Schedule a new trip.
- `find_available_resources(...)`: Check for available buses and drivers for a specific schedule.

### Personnel and Support
- `get_all_employee(token)`
- `get_contact_requests(token)`
- `mark_as_read(token, requestId)`

## Usage Workflow

1.  **Authenticate**: Use `login` to obtain an administrative token.
2.  **Initialize Resources**: Use `add_bus` and `add_route` to set up the system.
3.  **Schedule**: Use `find_available_resources` to verify availability before calling `add_trip`.
4.  **Monitor**: Use `get_all_trips` and `get_contact_requests` for ongoing operations.
