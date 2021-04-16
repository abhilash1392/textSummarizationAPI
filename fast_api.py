# Importing the libraries 

import uvicorn
from fastapi import FastAPI,Form,Request
from model_summarization import summary_text

app = FastAPI()

@app.get('/')
def welcome():
    return {'welcome':'Welcome to Text Summary Model'}

@app.post('/predict')
async def get_text(data: str = Form(...)):

    text_data = str(data)

    summary_answer = summary_text(text_data)
    
    return {'summary_text':f'{summary_answer}'}


if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.0", port=8000)

