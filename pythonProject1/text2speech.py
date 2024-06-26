import os
from deepgram import DeepgramClient, SpeakOptions

# Retrieve the Deepgram API key from environment variables
api_key = os.getenv("DG_API_KEY")
print(f"DG_API_KEY: {api_key}")

# Ensure that the API key is set correctly in your environment variables
if not api_key:
    raise ValueError("Deepgram API key not found. Set DG_API_KEY environment variable.")

# Filename for saving the output speech
filename = "output.wav"


def text2speech(text):
    try:
        # Define the options for the text-to-speech conversion
        SPEAK_OPTIONS = {"text": text}

        # Create a DeepgramClient instance using the API key
        deepgram = DeepgramClient(api_key=api_key)

        # Specify the options for the speech generation
        options = SpeakOptions(
            model="aura-asteria-en",  # Example model provided by Deepgram
            encoding="linear16",  # Audio encoding format
            container="wav"  # Output container format (WAV)
        )

        # Call the save method on the speak property to generate and save the speech
        response = deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)

        # Return the filename where the speech is saved
        return filename

    except Exception as e:
        print(f"Exception: {e}")


# Entry point of the script
if __name__ == "__main__":
    text2speech("this is a test")
