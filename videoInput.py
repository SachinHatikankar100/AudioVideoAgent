import sys
print(sys.executable)
from pathlib import Path

from agno.agent import Agent
from agno.media import Video
from agno.media import Audio
from agno.team.team import Team
from agno.models.google import Gemini
from agno.models.groq import Groq
import os
from moviepy import VideoFileClip
import requests
import json
import asyncio
from shazamio import Shazam
from dotenv import load_dotenv
load_dotenv()


video_agent = Agent(
    model=Gemini(id="gemini-2.0-flash-lite"),
    markdown=True,
    #role="Summarize this video"
)
video_path = Path(os.getenv("VIDEO_PATH"))
video_bytes = video_path.read_bytes()


def convert_video_to_audio_moviepy(video_file, output_ext="mp3"):
    """Converts video to audio using MoviePy (uses ffmpeg)"""
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"{filename}.{output_ext}")

if __name__ == "__main__":
    # Actual file path
    video_path = os.getenv("VIDEO_PATH")
    convert_video_to_audio_moviepy(video_path)

# Path to your local audio file
local_file_path = os.getenv("AUDIO_PATH")

artist, title = None, None 
try:
# Open and read the file
    with open(local_file_path, 'rb') as audio_file:
        files = {'file': audio_file}
        data = {
            'return': 'apple_music,spotify',
            'api_token': os.getenv("AUDD_API_KEY")
        }
        result = requests.post('https://api.audd.io/', data=data, files=files)
        response = json.loads(result.text)
        print(result.text)
        artist = response['result']['artist']
        title = response['result']['title']
except:
    print("Running the Shazam logic as Audd has given up!")
    async def main():
        shazam = Shazam()
        result = await shazam.recognize(os.getenv("AUDIO_PATH"))  # Replace with your file name

        if result.get("track"):
            title = result["track"]["title"]
            artist = result["track"]["subtitle"]
            print(f"Title : {title}")
            print(f"Artist: {artist}")
            return artist, title

        else:
            print("No track recognized.")

    artist, title= asyncio.run(main())


audio_agent = Agent(
    model=Gemini(id="gemini-2.0-flash-lite"),
    markdown=True,
    role=f"artist is {artist} and the title is {title}"
)

# Please download a sample audio file to test this Agent and upload using:
audio_path = Path(os.getenv("AUDIO_PATH"))
audio_bytes = audio_path.read_bytes()

#audio_agent.print_response("Tell me about this audio", audio=[Audio(content=audio_bytes)], stream=True)

#video_agent.print_response("Summarize this video?", videos=[Video(content=video_bytes)])

audio_video_agent = Team(

    name="Audio Video Team",
    mode="route",
    model=Gemini(id="gemini-2.0-flash"),
    members=[audio_agent, video_agent],
    markdown=True,
    description="Audio Video Agent",
    instructions=[
        "You are a agent which will describe what is happening in the video. Describe if the health has deteriorated or improved. If improved describe his muscles and overall gym progress in details. The artist name and the title is given so now me list of 5 songs from the same artist"
    ],
    show_members_responses=True,
    session_state={"artist": artist, "title": title},
    # Enable state in messages
    add_state_in_messages=True,
)

audio_video_agent.print_response(
    audio=[Audio(content=audio_bytes)], 
    videos=[Video(content=video_bytes)],
    stream=False
)


