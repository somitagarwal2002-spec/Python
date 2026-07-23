from pathlib import Path
from PyPDF2 import PdfReader
from gtts import gTTS
import pygame

PDF_FILE = "Day 91/atomic_habits_book.pdf"
OUTPUT_MP3 = "Day 91/audiobook.mp3"


def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)
    return "\n".join(text)


def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang="en")
    tts.save(output_file)


def play_audio(audio_file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


if __name__ == "__main__":
    pdf = Path(PDF_FILE)
    if not pdf.exists():
        print(f"Place your PDF in the project folder as '{PDF_FILE}'.")
        raise SystemExit

    print("Extracting text...")
    text = extract_text(pdf)

    print("Generating audiobook...")
    text_to_speech(text, OUTPUT_MP3)

    print("Playing audiobook...")
    play_audio(OUTPUT_MP3)

    print("Done!")
