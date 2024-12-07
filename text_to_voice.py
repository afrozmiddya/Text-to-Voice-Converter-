from gtts import gTTS
import os

def text_to_speech(text, language='en', output_file='output.mp3', save_location=''):
    
    full_path = os.path.join(save_location, output_file)
    
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)
    
    # Save the audio file
    tts.save(full_path)
    
    print(f"Audio saved as {full_path}")
    

def get_save_location():
    locations = [
        os.path.expanduser("~/Desktop"),
        os.path.expanduser("~/Documents"),
        os.path.expanduser("~/Downloads"),
        os.path.expanduser("~/Music"),
        "."  # Current directory
    ]
    
    print("Choose a location to save the audio file:")
    for i, location in enumerate(locations, 1):
        print(f"{i}. {location}")
    
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(locations):
                return locations[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Example usage
if __name__ == "__main__":
    sample_text = input("Enter the text to convert to speech: ")
    save_location = get_save_location()
    text_to_speech(sample_text, save_location=save_location)
