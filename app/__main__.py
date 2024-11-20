import uvicorn
from app.config.config import config

if __name__ == "__main__":
    uvicorn.run(
        "app.factory:create_app",
        factory=True,
        access_log=True,
        reload_dirs=["app"],
        host=config.app.host,
        port=config.app.port,
        reload=config.app.debug,
    )
