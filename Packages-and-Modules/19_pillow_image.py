from PIL import Image, ImageOps

# Create a simple image, then save a grayscale copy.
image = Image.new("RGB", (300, 180), color="white")
image.save("sample_image.png")
gray = ImageOps.grayscale(image)
gray.save("sample_image_grayscale.png")
print("Created sample_image.png and sample_image_grayscale.png")
