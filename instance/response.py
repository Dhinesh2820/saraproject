
def SuccessJson(data):
        return {"status":'true',"response": data}, 200
    
def ErrorJson(data):
        return {"status":'false',"response": data}, 200
        
        
