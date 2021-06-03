import sys
from PIL import Image


if __name__ == "__main__":
  print(f'argumentos: {len(sys.argv)}')
  for i, arg in enumerate(sys.argv):
    print(f"argument {i}: {arg}")


original = Image.open(sys.argv[1])

Horizontal = original.transpose(Image.FLIP_LEFT_RIGHT)

Horizontal.save(sys.argv[2])