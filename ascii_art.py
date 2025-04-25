from PIL import Image

ASCII_CHARS = "@%#*+=-:. "
def scale(img, new_width=100):
    w, h = img.size
    ratio = h / w / 1.65
    return img.resize((new_width, int(new_width * ratio)))

def to_grayscale(img): return img.convert("L")

def pixel_to_ascii(img):
    pixels = img.getdata()
    return ''.join([ASCII_CHARS[p // 25] for p in pixels])

path = input("🖼️ Path to image: ")
img = scale(to_grayscale(Image.open(path)))
ascii_img = pixel_to_ascii(img)
width = img.width
print("\n".join([ascii_img[i:i+width] for i in range(0, len(ascii_img), width)]))
