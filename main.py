book = "books/frankenstein.txt"

def main():
  with open(book) as f:
    file_contents = f.read()
    number_of_words = countNumberOfWords(file_contents)
    count_of_characters = countAlphabeticCharacters(file_contents)

    print(f"--- Begin report of {book} ---")
    print(f"{number_of_words} words found in the document")
    for character, count in count_of_characters.items():
      print(f"The '{character}' character was found {count} times")

def countNumberOfWords(book_string: str):
  book_words = book_string.split()

  return len(book_words)

def countCharacters(book_string: str):
  book_characters = list(book_string)
  character_dict = {}

  for character in book_characters:
    lower_cased_character = character.lower()

    if lower_cased_character in character_dict:
      character_dict[lower_cased_character] += 1
    else:
      character_dict[lower_cased_character] = 1

  return character_dict

def countAlphabeticCharacters(book_string: str):
  book_characters = list(book_string)
  character_dict = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
  }

  for character in book_characters:
    lower_cased_character = character.lower()

    if lower_cased_character in character_dict:
      character_dict[lower_cased_character] += 1

  return character_dict

main()
