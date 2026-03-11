from .base import patch,get
import json
from mcp_server import mcp


def get_contact_requests_tool(token: str):

    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    res = get("/admin/util/contact-us", headers=headers)
    
    return (res.get("contacts"))

def mark_as_read_tool(token: str, requestId: str):

    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    res = patch(f"/admin/util/contact-us/{requestId}/read", headers=headers)
    
    return (res.get)

# --------------------------------------------------------- #

@mcp.tool()
def get_contact_requests(token:str ):
    """this tool is used to get all the contact requests."""
    
    return get_contact_requests_tool(token)

@mcp.tool()
def mark_as_read(token:str, reqestId:str ):
    """this tool is used to mark contact requests as read."""
    
    return mark_as_read_tool(token, reqestId)