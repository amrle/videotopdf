import os
from moviepy.editor import *
from PIL import Image
import imagehash
import img2pdf

# import cv2

# Define output directory.
videoPath = "input.webm"
outputDirectory = "frames/"

# Create the output directory if it non-existant.
if not os.path.exists(outputDirectory):
    os.makedirs(outputDirectory)

# # Get frame count
# cap = cv2.VideoCapture("input.mp4")
# count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# print(count)

movie = video_path
imgdir = 'output_frames'

# clip = VideoFileClip(movie)
# for t in range(0, count):
#     imgpath = os.path.join(imgdir, '{}.png'.format(t))
#     clip.save_frame(imgpath, t)


clip = VideoFileClip(movie)

frame_count = int(clip.duration * clip.fps)
padding = len(str(frame_count))

# Consider using detect_scenes (scene extraction using luminosity)

# print(.sum())

t = 0

hashes = []
images = []

paddedNum = str(t).zfill(padding)
filename = f"frames/{paddedNum}.png" 

# Get initial image.
prev = Image.fromarray(clip.get_frame(0))
prev.save(filename)
images.append(filename)

# Get initial hash.
prev = imagehash.average_hash(prev)
hashes.append(prev)

# For every frame,
for frame in clip.iter_frames():
    
    # Get hamming distance.
    image = Image.fromarray(frame)
    h = imagehash.average_hash(image)
    hamming = h - prev 

    # Thresholding.
    if hamming > 5:

        paddedNum = str(t).zfill(padding)
        filename = f"frames/{paddedNum}.png"
        
        image.save(filename)
        images.append(filename)

        print(f"{paddedNum}  {h}  {hamming}")

        hashes.append(h)
        prev = h
    
    t+=1

# Create PDF
with open("name.pdf","wb") as f:
	f.write(img2pdf.convert(images))



# TODO
# Add Django interface (view and edit slides, pdf bookmarks)
# Command line arguments
# Whisper translation
# OCR
# CV2 for better pre-processing?
# Text detection with Tesseract?
# Use np arrays
# In memory mode

# Segmentation? 

# for frame in clip.iter_frames():
#     # imgpath = os.path.join(imgdir, '{}.png'.format(t))
#     # clip.save_frame(imgpath, t)
#     # t+=1
#     # print(t)
#     print(frame)
     