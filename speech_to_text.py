import sys
from dotenv import load_dotenv
from openai import OpenAI

def transcribe_audio(file_name):
    load_dotenv()
    client = OpenAI()

    # Open the specified audio file
    try:
        with open(file_name, 'rb') as audio_file:
            # Create a transcript from the audio file
            response = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

            # Create a new file name with "transcribed_" prefix
            output_file_name = f"transcribed_{file_name}"

            # Write the transcript to the new file
            with open(output_file_name, 'w') as output_file:
                output_file.write(response.text)

            print(f"Transcription saved to {output_file_name}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <audio_file>")
    else:
        audio_file_name = sys.argv[1]
        transcribe_audio(audio_file_name)