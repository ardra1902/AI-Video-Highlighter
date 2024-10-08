
# AI Video Highlighter.

This Streamlit application allows you to input a YouTube video URL, download the audio from the video, and transcribe the audio using Deepgram's API. The transcription includes highlighted sentences with start times, end times, and confidence scores.

![App Screenshot](https://raw.githubusercontent.com/ardra1902/AI-Video-Highlighter/main/AIVSS.png)

## Features

- Download audio from a YouTube video URL.
- Transcribe the audio using Deepgram's API.
- Display transcribed sentences with start time, end time, and confidence scores.


### Installation


**Clone the repository:**
   ```bash
   git clone https://github.com/ardra1902/AI-Video-Highlighter
   cd AI-Video-Highlighter
```


## Requirements

Make sure you have the following dependencies installed. You can install them using the provided `requirements.txt` file.

- `streamlit`
- `requests`
- `python-dotenv`
- `yt-dlp`               
- `pydub`
- `pytube`
  
To install the dependencies, use the following command:

```bash
pip install -r requirements.txt
```

**Obtain a Deepgram API Key:**

  - Sign up for an account at [Deepgram](https://console.deepgram.com/login).

  - Go to your [Deepgram dashboard](https://console.deepgram.com/project/6eaf47f0-2e1f-4c53-b78a-15adeed07e8c/keys) and generate a new API key.




## Usage


**Configure Environment Variables**

Create the .env file in the root directory of the project with the following content:
```bash
API_KEY="your_deepgram_api_key"
```
**Run the Streamlit App:**

Start the Streamlit application by running the following command:
```bash
streamlit run main.py
```

 **Input YouTube URL**:
   - Open the Streamlit app in your browser.
   - Paste the YouTube URL into the provided text input field.
   - Click on transcribe to start the transcription process.

 **View Results**:
   - The app will display the transcript with start/end times, text excerpts, and confidence scores.




## Example Output

The output will be an array of objects, each containing:
- **Text**: The transcribed text.
- **Start Time**: Start time of the text excerpt in seconds.
- **End Time**: End time of the text excerpt in seconds.
- **Confidence**: The confidence score of the transcription segment.


## Troubleshooting


**Import Errors:** Verify that all required packages are installed using pip list.


## Contributions

Contributions are welcome! Please fork the repository and create a pull request with your feature additions or bug fixes.


## Feedback


If you have any feedback, please reach out to me at ardrakakkarath@gmail.com

Feel free to star ⭐ this repository if you find it helpful!
