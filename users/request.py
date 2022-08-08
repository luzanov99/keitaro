
import requests
from requests.auth import HTTPBasicAuth
import os

def keitaro(kl_id='Today', start_date=None, end_date=None):
    url = os.environ.get("KEITARO_URL")
    headers = {'Api-Key': os.environ.get("API_KEY")}
    #print(os.environ.get("KEITARO_URL"))
    result = list()
    if start_date == "--" or start_date is None:
        if end_date == "--" or end_date is None:
            req = requests.post(url, headers=headers, json=
            {"range": {
                    "interval": str(kl_id)
                        },
                "metrics": ["conversions", "clicks","sub_id_6"]
            })
    else:
        start_list = start_date.split('-')
        end_list = end_date.split('-')
        if len(start_list[0]) >0 and len(start_list[1]) >0 and len(start_list[2]) >0:
            if len(end_list[0]) >0 and len(end_list[1]) >0 and len(end_list[2]) >0:
                req = requests.post(url, headers=headers, json=
                {"range": {
                        "from":str(start_date),
                        "to" :str(end_date)
                            },
                    "metrics": ["conversions", "clicks","sub_id_6"]
                })
            else :
                return result
        else:
            return result
    response = req.json()
    for i in response["rows"]:
        bayer = [i["sub_id_6"], i["clicks"], i["conversions"]]
        result.append(bayer)
    return result
