import asyncio
from shazamio import Shazam

async def main():
    shazam = Shazam()
    result = await shazam.recognize("C:/Users/Sachi/OneDrive/Desktop/Projects/sample-video-gym.mp3")  # Replace with your file name

    if result.get("track"):
        title = result["track"]["title"]
        artist = result["track"]["subtitle"]
        url = result["track"]["url"]
        print(f"🎵 Title : {title}")
        print(f"🎤 Artist: {artist}")
        print(f"🔗 Link  : {url}")
    else:
        print("No track recognized.")

asyncio.run(main())