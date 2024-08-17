from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    price :float
    brand : Optional[str] = None

inventory = {
    1: {
        "name" : "Milk" ,
        "price" : 3.99, 
        "brand" : "Regular"
    }
}


'''
@app.get("/get-item/{item_id}/{name}")
def get_item(item_id: int , name: str ):
    return inventory[item_id]
'''

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description= "The ID of the item you would like to view")):
    return inventory[item_id]

@app.get("/get-by-name/")
def get_item(Test : int , name : Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]["name"]== name:
            return inventory[item_id]
    return{"Data" : "Not Found"}
    
@app.post("/create-item/{item_id}")
def create_item(item_id : int , item: Item):
    if item_id in inventory:
        return{"Error" : "Item ID already exists. "}
    
    inventory[item_id] = {"name" : item.name , "brand" : item.brand , "price": item.price}
    return inventory[item_id]

