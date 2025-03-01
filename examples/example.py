import logging
from runpod_ariadne import Client
from runpod_ariadne.custom_fields import GpuTypeFields
from runpod_ariadne.custom_queries import Query
import dotenv
import os

async def main():
    dotenv.load_dotenv()
    client = Client(url=f"https://api.runpod.io/graphql?api_key={os.getenv('RUNPOD_API_KEY')}")
    response = await client.query(Query.gpu_types().fields(GpuTypeFields.display_name), operation_name="gpuTypes")
    print(response)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
