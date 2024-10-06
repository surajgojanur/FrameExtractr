from flask import Flask, render_template, request, send_file
import moviepy.editor as mp
import os
from PIL import Image

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
OUTPUT_FOLDER = 'output/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    # Handle file upload
    video_file = request.files['video']
    frame_rate = int(request.form['frame_rate'])
    output_format = request.form['output_format']
    
    video_path = os.path.join(UPLOAD_FOLDER, video_file.filename)
    video_file.save(video_path)
    
    # Process the video to extract frames
    clip = mp.VideoFileClip(video_path)
    
    frame_folder = os.path.join(OUTPUT_FOLDER, os.path.splitext(video_file.filename)[0])
    os.makedirs(frame_folder, exist_ok=True)
    
    for i, frame in enumerate(clip.iter_frames(fps=frame_rate)):
        image = Image.fromarray(frame)
        image.save(f"{frame_folder}/frame_{i}.{output_format}")
    
    return "Frames extracted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
