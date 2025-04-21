import numpy as np
from PIL import Image
import os

# Ensure the images directory exists
if not os.path.exists('images'):
    os.makedirs('images')

# Create the image array (black and white image)
width = 400
height = 500
image_array = np.zeros((height, width), dtype=np.uint8)

# Add some basic shapes to simulate the face and glasses
# This is just a placeholder - we'll replace it with the actual image
image_array[100:400, 50:350] = 200  # face area
image_array[150:200, 100:300] = 100  # glasses area

# Convert numpy array to PIL Image
img = Image.fromarray(image_array)

# Save the image
img.save('images/superman_glasses.jpg', 'JPEG')
print("Image has been saved to images/superman_glasses.jpg") 