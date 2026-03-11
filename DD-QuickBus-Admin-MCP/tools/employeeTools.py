from .base import get,delete,put,post
import json
from mcp_server import mcp
from typing import Literal


def get_all_employee_tool(token):
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    res = get("/emp/getemps", headers=headers)
    
    return json.dumps(res.get("emps"))

def add_employee_tool(token,name,phone,city,role):
    payload={
        "name":name, 
        "phone":phone, 
        "city":city, 
        "role":role
        }
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    res = post(f"/emp/create", payload=payload ,headers=headers)
    
    return json.dumps(res)

def delete_employee_tool(token,empsID):
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    res = delete(f"/emp/delete/{empsID}", headers=headers)
    
    return json.dumps(res)  

def update_employee_tool(token,empsID,name,phone,city,role):
    
    payload = {
        "_id" : empsID,
        "name":name, 
        "phone":phone, 
        "city":city, 
        "role":role
    }
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    res = put(f"/emp/update", payload=payload ,headers=headers)
    
    return json.dumps(res)

# --------------------------------------------------------- #

@mcp.tool()
def get_all_employee(token: str):
    """this tool return all the employees in system, it requires token which is generated ny login tool."""
    
    return get_all_employee_tool(token)

@mcp.tool()
def add_employee(token:str,name:str,phone:str,city:str,role:Literal["driver", "conductor"]):
    """this tool add the employee in the system."""
    
    return add_employee_tool(token,name,phone,city,role)

@mcp.tool()
def update_employee(token:str,empsID:str,name:str,phone :str,city:str,role:Literal["driver", "conductor"]):
    """ this tool update the empoyee in existing system.
     
        This API requires the complete employee object.
        
        All fields must be provided, even if they are not being changed.
        
        role is from "driver,condustor".
        
        If a field is not intended to be updated, 
        its current (existing) value must be sent.
        
        The `_id` field identifies the bus.
        A valid authentication token is required.
    """
    
    return update_employee_tool(token,empsID,name,phone,city,role)

@mcp.tool()
def delete_employee(token:str , empsID:str):
    """this tool delete the employee based on provided empsID."""
    
    return delete_employee_tool(token,empsID)