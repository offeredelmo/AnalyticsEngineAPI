import os
from dotenv import load_dotenv
import uvicorn
load_dotenv(".env")

port = int(os.getenv('PORT', 3000))

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port = port , reload=True)