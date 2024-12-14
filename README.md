# YouTube Video and Audio Downloader

This Python script enables users to download videos or extract audio from YouTube using the yt-dlp library.

The project provides a simple and efficient way to download YouTube content in either video (MP4) or audio (MP3) format. It utilizes the powerful yt-dlp library to handle the downloading process, ensuring high-quality downloads and format conversions.

Key features include:
- Flexible download options for both video and audio
- High-quality video downloads with merged audio and video streams
- Audio extraction and conversion to MP3 format
- User-friendly command-line interface for easy interaction

## Repository Structure

The repository consists of a single Python script:

- `baixar.py`: The main script containing the download functionality and user interface.

## Usage Instructions

### Installation

1. Ensure you have Python 3.6 or later installed on your system.
2. Install the required library using pip:

```bash
pip install yt-dlp
```

### Getting Started

To use the YouTube downloader:

1. Run the script:

```bash
python baixar.py
```

2. When prompted, enter the URL of the YouTube video you want to download.
3. Choose whether you want to download the content as 'video' or 'audio'.

### Code Example

Here's how you can use the `download_video_or_audio` function in your own Python scripts:

```python
from baixar import download_video_or_audio

# Download a video
download_video_or_audio("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "video")

# Download audio only
download_video_or_audio("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "audio")
```

### Configuration Options

The script uses default configuration options for both video and audio downloads. You can modify these options in the `download_video_or_audio` function:

- For audio downloads:
  - Format: 'bestaudio/best'
  - Preferred codec: 'mp3'
  - Preferred quality: '192'

- For video downloads:
  - Format: 'bestvideo+bestaudio/best'
  - Merge output format: 'mp4'
  - Final format: 'mp4'

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

The data flow in this application is straightforward:

1. User input (YouTube URL and download type) → Script
2. Script → yt-dlp library (with configured options)
3. yt-dlp → YouTube servers (request content)
4. YouTube servers → yt-dlp (stream content)
5. yt-dlp → Local storage (save downloaded content)
6. Script → User (display download status)

```
[User Input] → [Script] → [yt-dlp] ↔ [YouTube]
                   ↓
            [Local Storage]
                   ↓
             [Status Output]
```

Note: The yt-dlp library handles the complexities of interacting with YouTube's servers, managing the download process, and performing any necessary post-processing (such as audio extraction or format conversion).