# QuickBus User MCP Server

This server provides a Model Context Protocol (MCP) interface for customer-facing operations within the QuickBus ecosystem. It enables LLM-powered agents to assist users with bus discovery, seat selection, and ticket management.

## Features

- **Bus Discovery**: Search for available trips between cities on specific dates.
- **Seat Management**: Real-time checking of available and booked seats for any trip.
- **Booking Lifecycle**: End-to-end ticket creation and cancellation.
- **Ticket Management**: Retrieve booking history and specific ticket details.
- **OTP Authentication**: Secure user validation via email-based One-Time Passwords.

## Project Structure

```text
DD-QuickBus-User-MCP/
├── main.py                # Server entry point and tool registration
└── tools/                 # Tool implementation logic
    ├── base.py            # API communication helpers
    ├── search_bus.py      # Discovery logic
    ├── seats.py           # Seat availability logic
    ├── create_ticket.py   # Booking logic
    └── login.py           # OTP and validation logic
```

## Setup and Installation

### Prerequisites

- Python 3.14 or higher (optimized for latest runtime).
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

### User Authentication
- `auth(email)`: Requests an OTP for the specified email address.
- `validate(email, otp)`: Validates the OTP and returns a session token.

### Discovery
- `search_bus(from_city, to_city, date)`: Returns a list of available trips.
- `get_available_seats(tripId, from_city, to_city, traveldate, token)`: Fetches current seat maps.

### Booking Operations
- `create_ticket(...)`: Books seats for a list of passengers on a specific trip.
- `cancle_ticket(ticketId, token)`: Cancels an existing booking.

### Account Management
- `get_tickets(token)`: Lists all tickets associated with the user.
- `get_ticket_details(ticketId, token)`: Provides comprehensive details for a specific booking.

## Usage Workflow

1.  **Search**: Use `search_bus` to find trips matching user criteria.
2.  **Authentication**: Use `auth` and `validate` to secure a user session.
3.  **Seat Selection**: Check availability using `get_available_seats`.
4.  **Booking**: Finalize the transaction with `create_ticket`.
