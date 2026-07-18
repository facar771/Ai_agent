from fastapi import FastAPI
from pydantic import BaseModel, Field

from core.engine import engine


app = FastAPI(
    title="agent-engine"
)


class RunSkillRequest(BaseModel):
    chat_id: str = Field(...)
    type: str = Field(...)
    text: str | None = Field(default=None)
    file_path: str | None = Field(default=None)
    metadata: dict | None = Field(default=None)


@app.on_event("startup")
def startup():
    engine.initialize()


@app.post("/run-skill")
def run_skill(request: RunSkillRequest):

    result = engine.run(
        request.model_dump()
    )

    return result