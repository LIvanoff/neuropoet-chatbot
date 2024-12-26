from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# llm = pipeline("text-generation", model="gpt2")


class PromptRequest(BaseModel):
    prompt: str


@app.post("/generate")
async def generate_text(request: PromptRequest):
    prompt = request.prompt
    # response = llm(prompt, max_length=512, num_return_sequences=1)

    return {"generated_text": "generated_text"}
