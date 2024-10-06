# Video to Frames Converter

This project is a simple web application that converts videos into frames at customizable frame rates (24, 30, 60) and outputs them in either PNG or JPEG format. The supported video formats for input are MP4 and MKV.

## Features

- Upload MP4 and MKV videos
- Choose frame rate: 24, 30, or 60 FPS
- Extract frames in PNG or JPEG format
- Simple and easy-to-use interface

## Requirements

- Python 3.x
- Flask
- MoviePy
- Pillow (for image handling)
- FFmpeg (for video processing)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/video-to-frames-converter.git
    cd video-to-frames-converter
    ```

2. **Install the required packages:**
    Make sure you have `pip` installed. Then, run the following command:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install FFmpeg:**
    - Download and install FFmpeg from [FFmpeg official website](https://ffmpeg.org/download.html).
    - Add the FFmpeg path to your system's environment variables.

4. **Run the application:**
    ```bash
    python app.py
    ```

5. **Access the application:**
   Open your browser and go to `http://127.0.0.1:5000/` to use the app.


## Usage

- Upload a video in MP4 or MKV format.
- Select the desired frame rate (24, 30, or 60 FPS).
- Choose the output format (PNG or JPEG).
- Submit and download the extracted frames.

## License

This project is licensed under the MIT License. Feel free to contribute or modify as needed.

