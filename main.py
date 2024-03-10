from fastapi import FastAPI

app = FastAPI()

@app.get('/home')
def home():
    return "Hello World"

@app.get("/about")
def about():
    return "This is about page"

@app.get("/contact")
def contact():
    return "This is contact us page"