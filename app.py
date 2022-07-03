from fastapi import FastAPI
app = FastAPI()

# DEMO DATA...
trades = {
    1:{ 
        "assetClass":"fixed income",
        "end": "15-08-2022",
        "maxPrice":"$45,000",
        "start":"4-3-2021",
        "tradeType":"Bond",
        "trader":"HDFC bank",
        "counterparty":"abc",
        "instrumentId":1,
        "instrumentName":"pqr"
    },
    2:{
        "assetClass":"Equity",
        "end": "24-12-2022",
        "maxPrice":"$10,000",
        "start":"11-12-2020",
        "tradeType":"Stocks",
        "trader":"Goldman Sachs",
        "counterparty":"XYZ",
        "instrumentId":2,
        "instrumentName":"XYZ"
    },
    3:{
        "assetClass":"real estate",
        "end": "08-08-2022",
        "maxPrice":"$67,999",
        "start":"5-5-2020",
        "tradeType":"Property",
        "trader":"Sun valley",
        "counterparty":"abc",
        "instrumentId":3,
        "instrumentName":"real estate"
    }
}
@app.get("/")
def home():
    return {"Welcome"}

@app.get("/list-trades")
def list_trades():
    return trades;
@app.get("/single-trade/{id}")
def single_trade(id:int):
    return trades[id];
@app.get("/search-by-counterparty")
def search_by_counterparty(cp:str):
    for id in trades:
        if(trades[id]["counterparty"]==cp):
            return trades[id]
    return {"Data":"not found"}

@app.get("/search-by-instrumentId")
def search_by_counterparty(iid:int):
    for id in trades:
        if(trades[id]["instrumentId"]==iid):
            return trades[id]
    return {"Data":"not found"}

@app.get("/search-by-instrumentName")
def search_by_counterparty(iN:str):
    for id in trades:
        if(trades[id]["instrumentName"]==iN):
            return trades[id]
    return {"Data":"not found"}
    
@app.get("/search-by-trader")
def search_by_counterparty(trd:str):
    for id in trades:
        if(trades[id]["trader"]==trd):
            return trades[id]
    return {"Data":"not found"}