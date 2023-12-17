import requests
import json
from typing import Any, Dict, List, Optional

def get_millennium_falcon_info() -> Optional[Dict[str, Any]]:
    base_url: str = "https://swapi.dev/api/starships/"
    search_params: Dict[str, str] = {"search": "Millennium Falcon"}

    response: requests.Response = requests.get(base_url, params=search_params)
    data: Dict[str, Any] = response.json()

    if "results" in data and data["results"]:
        falcon: Dict[str, Any] = data["results"][0]
        pilot_urls: List[str] = falcon.get("pilots", [])

        falcon_info: Dict[str, Any] = {
            "name": falcon["name"],
            "max_speed": falcon["max_atmosphering_speed"],
            "class": falcon["starship_class"],
            "pilots": []
        }

        for pilot_url in pilot_urls:
            pilot_response: requests.Response = requests.get(pilot_url)
            pilot_data: Dict[str, Any] = pilot_response.json()

            pilot_info: Dict[str, Any] = {
                "name": pilot_data["name"],
                "height": pilot_data["height"],
                "weight": pilot_data["mass"],
                "homeworld": pilot_data["homeworld"],
                "homeworld_url": pilot_data["homeworld"]
            }

            falcon_info["pilots"].append(pilot_info)

        return falcon_info

    return None

if __name__ == "__main__":
    millennium_falcon_info: Optional[Dict[str, Any]] = get_millennium_falcon_info()

    if millennium_falcon_info:
        print(json.dumps(millennium_falcon_info, indent=2))

        with open("millennium_falcon_info.json", "w") as json_file:
            json.dump(millennium_falcon_info, json_file, indent=2)