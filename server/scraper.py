import asyncio
from TikTokApi import TikTokApi

HASHTAG = "stil"

async def main():
    async with TikTokApi() as api:
        await api.create_sessions(num_sessions=1, sleep_after=3, headless=False)

        async for video in api.hashtag(name=HASHTAG).videos(count=10):
            data = video.as_dict
            stats = data.get("stats", {})
            author = data.get("author", {})
            print(f"""
id:       {data.get('id')}
desc:     {data.get('desc', '')[:80]}
likes:    {stats.get('diggCount')}
views:    {stats.get('playCount')}
comments: {stats.get('commentCount')}
shares:   {stats.get('shareCount')}
author:   {author.get('uniqueId')}
""")

if __name__ == "__main__":
    asyncio.run(main())