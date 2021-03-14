from fastapi import FastAPI

from app.rest.rest import router as api_router


def get_application():
    application = FastAPI()

    application.include_router(api_router)

    return application


app = get_application()
