from .base import post
from mcp_server import mcp


import validators


def validate_credentials(payload):
    email = (payload.get('email'))
    password = (payload.get('password'))

    if not validators.email(email):
        return f"{email} is not a valid email please try again"

    if ( len(password) < 6):
        return "Password must be at least 6 characters"
    
    return True
    
def login_tool(email, password):

    payload = {
        "email" : str(email),
        "password" : str(password)
    }

    valid = validate_credentials(payload)

    if(valid == True):
        return post("/login", payload)
    
    return valid

@mcp.tool()
def login(email: str, password: str):
    """this tool log in the user into the system and return token that is required for all the tasks 
    this is the default tool for the system """
    
    return login_tool(email, password)