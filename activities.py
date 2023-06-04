from dataclasses import dataclass
from typing import List

import aiohttp
from temporalio import activity

TASK_QUEUE_NAME = "temporal-community-task-queue"

TEMPORAL_COMMUNITY_URL = "https://community.temporal.io"


@dataclass
class TemporalCommunityPost:
    title: str
    url: str
    views: int


@activity.defn
async def get_latest_post_ids() -> List[str]:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{TEMPORAL_COMMUNITY_URL}/latest.json") as response:
            if not 200 <= response.status < 300:
                raise RuntimeError(f"Status: {response.status}")
            latest_community_data = await response.json()

    topics = latest_community_data["topic_list"]["topics"]

    return [str(topic["id"]) for topic in topics]


@activity.defn
async def get_top_posts(post_ids: List[str]) -> List[TemporalCommunityPost]:
    results: List[TemporalCommunityPost] = []
    async with aiohttp.ClientSession() as session:
        for item_id in post_ids:
            post_url = f"{TEMPORAL_COMMUNITY_URL}/t/{item_id}.json"
            async with session.get(post_url) as response:
                if not 200 <= response.status < 300:
                    raise RuntimeError(f"Status: {response.status}")
                item = await response.json()
                slug = item["slug"]
                url = f"{TEMPORAL_COMMUNITY_URL}/t/{slug}/{item_id}"
                community_post = TemporalCommunityPost(
                    title=item["title"],
                    url=url,
                    views=item["views"],
                )
                results.append(community_post)

    results.sort(key=lambda p: p.views, reverse=True)
    top_ten_posts = results[:10]
    return top_ten_posts
