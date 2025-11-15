from fastapi import FastAPI

# create FastAPI instance named 'app'
app = FastAPI()

# @ decorator connects the function root() to the FastAPI instance 'app'
@app.get("/") 
def root(): 
    # define function root() that returns a JSON response with a message "Hello World".
    return {"message": "Hello World"}