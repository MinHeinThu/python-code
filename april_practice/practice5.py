
# with open("note.txt", "a") as file:
#     file.write("Ask if you have not sure what you need to do\n")

# with open("note.txt", "r") as original:
#     content = original.readlines()
#     print(content)

with open("note.txt", "w") as original:
    original.write("Meeting at 10AM\n")
    original.write("Project deadline: Friday\n")
    original.write("Check emails\n")

with open("note.txt", "r") as original:
    content = original.readlines()
    print(content)


    
# import os

# if os.path.exists("music.jpg"):
#     with open("music.jpg", "rb") as image:
#         image_data = image.read()
# else:
#     print("Error: 'music.jpg' does not exist in the current directory.")
#     print("Current directory:", os.getcwd())

try:
    with open("/Users/loomenes/projects/python-code/april_practice/music.jpg", "rb") as music_image:
        image_data = music_image.read()
except FileNotFoundError:
    print("File doesn't exist")

try:
    with open("/Users/loomenes/projects/python-code/1200px-Sunflower_from_Silesia2.jpg", "rb") as image:
        sunflower = image.read()
    with open("photo_copy.jpg", "wb") as image2:
        image2.write(sunflower)
    print("Image copied successfully!")
except FileNotFoundError:
    print("File doesn't exist")


# import os

# print("Current folder:", os.getcwd())  # This shows where Python is looking

