from fastapi import FastAPI

app = FastAPI(
    title="SecureOPShip API",
    description="A demonstration API for DevSecOps and CI/CD automation.",
    version="1.0.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    """Return the API welcome message."""
    return {"message": "SecureOPShip API is running"}


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Return the API health status."""
    return {"status": "healthy"}