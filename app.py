import streamlit as st
from transcribe import transcribe_audio
from audioutils import download_audio

def main():
    st.title("AI Video Highlighter")

    # Input for YouTube URL
    youtube_url = st.text_input("Enter YouTube Video URL:")

    if st.button("Transcribe"):
        if youtube_url:
            with st.spinner("Downloading audio..."):
                audio_path = download_audio(youtube_url)

            if audio_path:
                st.success("Audio downloaded successfully!")

                with st.spinner("Transcribing audio..."):
                    transcription = transcribe_audio(audio_path)

                if transcription:
                    st.success("Transcription completed!")

                    # Display results
                    if "utterances" in transcription.get("results", {}):
                        for utterance in transcription["results"]["utterances"]:
                            st.write(f"**Text:** {utterance['transcript']}")
                            st.write(f"**Start time:** {utterance['start']} seconds")
                            st.write(f"**End time:** {utterance['end']} seconds")
                            st.write(f"**Confidence:** {utterance['confidence']}")
                            st.write("")
                    else:
                        st.write("No utterances found in the response.")
            else:
                st.error("Failed to download audio.")
        else:
            st.error("Please enter a valid YouTube URL.")

if __name__ == "__main__":
    main()
