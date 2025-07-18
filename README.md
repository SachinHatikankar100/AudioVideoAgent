# Audio Video Agent:

This project showcases a custom-built **Audio-Video Agent** developed using Python and [Agno](https://docs.agno.com/introduction)—a GenAI framework for processing video, audio, and text. 

> 📌 **Goal:** Automatically summarize a video **and** identify the audio track (song) playing in it—then recommend similar songs from the same artist. 

I used a **personal gym progress reel** to demonstrate this workflow in action.

✨Key Features<br/>
🎬 Real-time Video Understanding with Google Gemini 2.0 Flash Lite via Agno<br/>
🎧 Audio Extraction using Python’s moviepy<br/>
🔍 Music Recognition (Artist & Title) via the AUDD API and Shazamio<br/>
🤝 Fused Context Input (video + audio) to generate a richer summary<br/>
🎵 Music Recommendations based on the detected artist<br/>
📂 Supports .mp4 format (Instagram reels, fitness clips, etc.)<br/>


<br/>

# Why I Built This
<p>While Agno enables powerful video summarization, it doesn't natively handle multi-modal input (audio + video) in a way that reflects the full context of real-life content like reels or workout clips.</p>

So, I extended the pipeline to:

- Extract and analyze the audio separately
- Pass both audio and video context to the Gemini agent
- Enable richer, more relevant summaries
- Recommend similar tracks from the same artist
- Ideal for content creators, editors, fitness influencers, or GenAI demos.

<br/>

# Run the agent

`python videoInput.py`


<br/>

# Output

<img width="1133" height="450" alt="image" src="https://github.com/user-attachments/assets/c92dd7bf-043f-45e3-b7f0-f402dba13a05" />


<br/>

# The script will:

✅ Extract audio from your .mp4 video<br/>
✅ Identify the background music (artist + title)<br/>
✅ Generate a visual + audio-aware summary using Gemini<br/>
✅ Suggest other songs by the same artist<br/>

<br/>

# Demo Use Case: Gym Progress Reel

- I tested this using my own gym progress video, which had a background music track. Here's what it did:
- Summarized the visual content (e.g., flexing, lifting, form)
- Detected the song “Shooting Stars” by Bag Raiders
- Recommended other tracks from the same artist
- Produced a complete multi-modal summary ready for social media captions or analytics

<br/>

# Tech Stack

- Agno	GenAI framework (Gemini agent)
- Gemini 2.0	Flash Lite model for video summarization
- MoviePy	Audio extraction from video
- AUDD API	Music recognition (title, artist)
- Shazamio	Alternate music recognition option
- Python	Orchestration (asyncio, dotenv, requests)


<br/>

# About Me  
👋 Hi, I'm Sachin Hatikankan – an RPA Engineer transitioning into AI/ML & Generative AI.

🧠 Passionate about building practical GenAI tools for creators and enterprises

💼 Currently seeking roles in Data Science, AI/ML Engineering, Applied GenAI

🔗 Let’s connect: [LinkedIn – Sachin Hatikankan](https://www.linkedin.com/in/sachin-hatikankan-b5673ab4/)

⭐ If you liked this project, consider starring the repo and reaching out!
