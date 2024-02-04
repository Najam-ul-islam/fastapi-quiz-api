import uvicorn

from api.app import create_app
from api.config import settings
from typing import Any

api: Any = create_app(settings)

if __name__ == "__main__":
    # uvicorn.run("asgi:api", host="0.0.0.0", port=8000, reload=True)
    uvicorn.run("asgi:api", host="0.0.0.0", port=8080, reload=True)
