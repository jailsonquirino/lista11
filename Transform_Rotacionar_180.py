import sys
from PIL import Image


if __name__ == "__main__":
  print(f'argumentos: {len(sys.argv)}')
  for i, arg in enumerate(sys.argv):
    print(f"argument {i}: {arg}")


original = Image.open(sys.argv[1])

Rotacionar1 = original.transpose(Image.ROTATE_180)

Rotacionar1.save(sys.argv[2])