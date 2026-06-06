import asyncio
from TikTokApi import TikTokApi
from supabase_config import supabase

HASHTAG = "stil"

async def main():
    async with TikTokApi() as api:
        await api.create_sessions(num_sessions=1, sleep_after=3, headless=False)

        async for video in api.hashtag(name=HASHTAG).videos(count=10):
            data = video.as_dict
            stats = data.get("stats", {})

            row = {
                "id": data.get("id"),
                "desc": data.get("desc", "")[:500],
                "hashtags": [t.get("hashtagName") for t in data.get("textExtra", []) if t.get("hashtagName")],
                "mentions": [t.get("userUniqueId") for t in data.get("textExtra", []) if t.get("userUniqueId")],
                "likes": stats.get("diggCount", 0),
                "views": stats.get("playCount", 0),
                "comments": stats.get("commentCount", 0),
                "shares": stats.get("shareCount", 0),
                "collect_count": stats.get("collectCount", 0),
                "author": data.get("author", {}).get("uniqueId", ""),
                "author_id": data.get("author", {}).get("id", ""),
                "author_followers": data.get("authorStats", {}).get("followerCount", 0),
                "author_following": data.get("authorStats", {}).get("followingCount", 0),
                "author_total_likes": data.get("authorStats", {}).get("heartCount", 0),
                "author_video_count": data.get("authorStats", {}).get("videoCount", 0),
                "duration": data.get("video", {}).get("duration", 0),
                "ratio": data.get("video", {}).get("ratio", ""),
                "music_title": data.get("music", {}).get("title", ""),
                "music_author": data.get("music", {}).get("authorName", ""),
                "music_id": data.get("music", {}).get("id", ""),
                "is_duet": data.get("duetInfo", {}).get("duetFromId", "0") != "0",
                "hashtag": HASHTAG,
                "created_at": data.get("createTime"),
            }

            supabase.table("videos").upsert(row).execute()
            print(f"Saved: {row['id']} — {row['likes']} likes — {row['views']} views")

if __name__ == "__main__":
    asyncio.run(main())