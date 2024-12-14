# YouTube Video and Audio Downloader

This Python script enables users to download videos or extract audio from YouTube using the yt-dlp library and a graphical user interface (GUI) built with CustomTkinter.

The project provides a simple and efficient way to download YouTube content in either video (MP4) or audio (MP3) format. It utilizes the powerful yt-dlp library to handle the downloading process, ensuring high-quality downloads and format conversions.

Key features include:
- Flexible download options for both video and audio
- High-quality video downloads with merged audio and video streams
- Audio extraction and conversion to MP3 format
- User-friendly graphical interface for easy interaction

## Repository Structure

The repository consists of a single Python script:

- `baixar.py`: The main script containing the download functionality and user interface.

## Usage Instructions

### Installation

1. Ensure you have Python 3.6 or later installed on your system.
2. Install the required libraries using pip:

```bash
pip install yt-dlp customtkinter
```

### Getting Started

To use the YouTube downloader:

1. Run the script:

```bash
python baixar.py
```

2. In the GUI window that appears:
   - Enter the URL of the YouTube video you want to download in the "Insira o link:" field.
   - In the "Deseja baixar como video ou audio?" field, type either "video" or "audio" to choose the download type.
   - Click the "Confirmar" button to start the download.

3. The download status will be displayed in the GUI.

### Code Example

Here's how the `download_video_or_audio` function is used within the script:

```python
def Confirmar():
    video_url = campo_link.get()
    choice = campo_format.get()
    download_video_or_audio(video_url, choice)

def download_video_or_audio(url, download_type="video"):
    # Function implementation...
    pass

# GUI setup and main loop
if __name__ == "__main__":
    # GUI initialization code...
    botao_confirmar = ctk.CTkButton(janela, text="Confirmar", command=Confirmar)
    botao_confirmar.pack(pady=(20, 10))
    # More GUI code...
    janela.mainloop()
```

### Troubleshooting

Common issues and solutions:

1. **Problem**: Script fails to download content
   - Error message: "ERROR: Unable to download video"
   - Diagnostic process:
     1. Check your internet connection
     2. Verify the YouTube URL is correct and accessible
     3. Ensure yt-dlp is up to date: `pip install --upgrade yt-dlp`
   - Expected outcome: After updating yt-dlp or correcting the URL, the download should proceed successfully

2. **Problem**: Audio extraction fails
   - Error message: "ERROR: ffprobe/avprobe and ffmpeg/avconv not found. Please install one."
   - Diagnostic process:
     1. Install FFmpeg: Visit https://ffmpeg.org/download.html for installation instructions
     2. Ensure FFmpeg is in your system PATH
   - Expected outcome: After installing FFmpeg, audio extraction should work correctly

### Debugging

To enable debug mode and verbose logging:

1. Modify the `ydl_opts` dictionary in the `download_video_or_audio` function:

```python
ydl_opts = {
    # ... other options ...
    'verbose': True,
    'logger': yt_dlp.utils.YoutubeDLLogger(),
}
```

2. Run the script as usual. You will see detailed debug output in the console.

3. Log files: yt-dlp does not create log files by default. To save logs, you can redirect the output to a file:

```bash
python baixar.py > download_log.txt 2>&1
```

This will create a `download_log.txt` file in the same directory as the script.

### Performance Optimization

- Monitor network speed and CPU usage during downloads
- For batch downloads, consider using yt-dlp's archive feature to avoid re-downloading content
- Use the `--format` option to specify lower quality for faster downloads if needed

## Data Flow

The data flow in this application is as follows:

1. User input (YouTube URL and download type) → GUI
2. GUI → Script (when "Confirmar" button is clicked)
3. Script → yt-dlp library (with configured options)
4. yt-dlp → YouTube servers (request content)
5. YouTube servers → yt-dlp (stream content)
6. yt-dlp → Local storage (save downloaded content)
7. Script → GUI (display download status)

```
[User Input] → [GUI] → [Script] → [yt-dlp] ↔ [YouTube]
                 ↑          ↓
                 └── [Status Output]
                            ↓
                     [Local Storage]
```

Note: The yt-dlp library handles the complexities of interacting with YouTube's servers, managing the download process, and performing any necessary post-processing (such as audio extraction or format conversion).