"""
This is a big comment
😆
"""

def run():
  print("This function runs the program")
  phrase = "this is a phrase as a string"
  phrase = phrase.upper().lower().capitalize()
  phrase = phrase.replace(" ","😀")
  phrase = phrase[::-1]
  print(phrase)


# This is simple a comment
if __name__ == "__main__":
  run()