import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from activities import TASK_QUEUE_NAME, get_latest_post_ids, get_top_posts
from workflow import TemporalCommunityWorkflow


async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue=TASK_QUEUE_NAME,
        workflows=[TemporalCommunityWorkflow],
        activities=[get_latest_post_ids, get_top_posts],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
