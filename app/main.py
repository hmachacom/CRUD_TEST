from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from core.database import test_connection
from api.v1 import candidate, hiring_order, job_offer
import logging
# from api.v1 import users_routes

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(title="Talent Human API")


# @app.exception_handler(Exception)
# async def generic_exception_handler(request: Request, exc: Exception):
#     """
#     Handles uncaught exceptions globally, logging the error and returning a
#     standard JSON error response.

#     Args:
#         request: The incoming request that caused the exception.
#         exc: The exception that was raised.

#     """
#     # logger.error("Error not handled on %s: %s", request.url.path, str(exc))
#     logger.error("Unhandled error at %s: %s", request.url.path, type(exc).__name__)


#     return JSONResponse(
#         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#         content={"message": "Error interno del servidor"} 
#     )


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(candidate.router, prefix="/api/v1/candidates", tags=["Candidates"])
app.include_router(job_offer.router, prefix="/api/v1/job_offers", tags=["Job Offers"])
app.include_router(hiring_order.router, prefix="/api/v1/hiring_orders", tags=["Hiring Orders"])

test_connection()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

