from src.llm import LLM
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse, Response
import logging
import uvicorn


logger = logging.getLogger(__name__)

llm: LLM = LLM()

app = FastAPI()
logger.info("FastAPI initialized")


@app.post("/initialize/")
async def initialize(request: Request) -> Response:
    body = await request.json()
    model = body.get("model", "Phi2")
    max_total_tokens = body.get("max_total_tokens", 300)
    quantization = body.get("quantization", "q8")
    llm.initialize(model, max_total_tokens, quantization)

    return Response(status_code=200, content="LLM initialized")


@app.post("/generate/")
async def generate(request: Request) -> StreamingResponse:
    body = await request.json()
    prompt = body.get("prompt")

    if not llm.is_initialized():
        raise HTTPException(status_code=500, detail="LLM is not initialized")

    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")

    response_generator = llm(prompt)
    return StreamingResponse(response_generator, media_type="text/event-stream")


def run():
    uvicorn.run(app, host="0.0.0.0", port=9000)


if __name__ == "__main__":
    run()
