from PIL import Image
"""
PIL, short for Python Imaging Library, was the name of this module when Python's version was 2.4 or so. Throughout its
development, it was renamed to "Pillow", they just never changed the syntax from PIL to Pillow. Its purpose is image
manipulation. The following syntax is used to create a variable. the type of which is "Image" from Pillow, and save an
image's information in it. I'm showcasing a few attributes of the Image object by printing them. The "show" attribute
creates a temporary copy of the image and opens it using the default image player of the computer.
"""
img = Image.open("FB_IMG_15935075530023065.jpg")
print(img.size)
print(img.format)
print(img.format_description)
img.show()

"""
To crop an image using Pillow, we need to define the area that we want to keep by specifying the coordinates of the top
left corner of the rectangle, as well as those of the bottom right corner of the rectangle. To be able to see the
coordinates in an image you need to open it in some kind of editor.
"""

area = (611, 578, 1045, 939)
# We don't need to use a variable for the coordinates, we could just type img_cropped = img.crop(611, 578, 1045, 939)
img_cropped = img.crop(area)
img_cropped.show()
