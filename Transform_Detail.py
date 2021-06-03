import sys
from PIL import Image, ImageFilter


if __name__ == "__main__":
  print(f'argumentos: {len(sys.argv)}')
  for i, arg in enumerate(sys.argv):
    print(f"argument {i}: {arg}")


original = Image.open(sys.argv[1])

detail = original.filter(ImageFilter.DETAIL)

detail.save(sys.argv[2])