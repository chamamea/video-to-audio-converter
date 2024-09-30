import os
from moviepy.editor import VideoFileClip

def is_valid_video(file_path):
    return os.path.exists(file_path) and file_path.lower().endswith('.mp4')

def convert_video_to_audio(video_path, audio_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)
        video.close()
        audio.close()
        return True
    except Exception as e:
        print(f"Conversion error: {str(e)}")
        return False

def main():
    while True:
        video_path = input("Enter the path to the MP4 file (or 'q' to quit): ")
        
        if video_path.lower() == 'q':
            break

        if not is_valid_video(video_path):
            print("Error: Invalid video file. Please provide a valid MP4 file.")
            continue

        audio_path = os.path.splitext(video_path)[0] + '.mp3'

        print("Converting video to audio...")
        if convert_video_to_audio(video_path, audio_path):
            print(f"Conversion successful. Audio saved as: {audio_path}")
        else:
            print("Conversion failed. Please try again.")

    print("Thank you for using the MP4 to MP3 converter!")

if __name__ == "__main__":
    main()
