from polygon import RESTClient

def retrieve(ticker: str) ->
    client = RESTClient()
    aggs = client.get_aggs(
        ticker,
        1,
        "day"
    )