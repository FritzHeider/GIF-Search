import requests

params = {
    "q": query_term,
    "Key": "2T9JR8K6HMUC"
}
response = requests.get(
    'https://api.tenor.com/v1/search',
    params=params)
    