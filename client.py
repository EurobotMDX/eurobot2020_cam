import sys
import json
import requests

res = requests.get("http://0.0.0.0:8000/polar_direction")
print res.text