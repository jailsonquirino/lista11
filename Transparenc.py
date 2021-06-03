import sys
from PIL import Image


if __name__ == "__main__":
  print(f'argumentos: {len(sys.argv)}')
  for i, arg in enumerate(sys.argv):
    print(f"argument {i}: {arg}")

img = Image.open(sys.argv[1])
#converter
imgpng = img.convert('RGBA')

#lista pixels
pixels = list(imgpng.getdata())

for i, p in enumerate(pixels):
    pixels[i] = (p[0], p[1], p[2], int(sys.argv[3]))

#imagem nova
outputImg = Image.new('RGBA', img.size)
outputImg.putdata(pixels)
outputImg.save(sys.argv[2])
