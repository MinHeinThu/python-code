from rembg import remove
from PIL import Image

with open("/Users/loomenes/projects/python-code/1200px-Sunflower_from_Silesia2.jpg", "rb") as image:
    input_data =  image.read()

# Remove the background using AI
output_data = remove(input_data)

# Save the new image with transparent background
with open("photo_no_bg.png", "wb") as output_file:
    output_file.write(output_data)

print("Background removed and saved as photo_no_bg.png")