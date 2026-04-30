from agents import function_tool, RunContextWrapper
from context import User_Context
import requests

@function_tool
def get_all_leases(ctx: RunContextWrapper[User_Context]):
    """ Fetch all leases data for company """
    print('fetching transactions!')

    url = f"https://ifrs16.ifrs.ca/api/LeaseFormData/GetAllLeasesForCompany?companyId={ctx.context.companyId}" # Replace with your actual endpoint
    
    headers = {
        "Authorization": f"Bearer {ctx.context.token}", # Or just "token": token depending on API requirements
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        
        # Raises an HTTPError if the response was an error (4xx or 5xx)
        response.raise_for_status() 
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
# fetching transactions!
# An error occurred: 401 Client Error: Unauthorized for url: https://ifrs16.ifrs.ca/api/LeaseFormData/GetAllLeasesForCompany?companyId=1