import requests
import json
url = 'https://datos.gob.cl/es/api/3/action/datastore_search?resource_id=e9d62fab-96d3-40e0-8b6f-faf7891cfd4e'  



try: 
    r = requests.get(url)
    result = r.json()
    print(result)
    with open('data.json', 'w') as f:
        json.dump(result, f)
except Exception as e: 
    print(f"Error: {e}")
    
