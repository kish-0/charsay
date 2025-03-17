# Charsay

**Character Say** - A simple Python package that generates ASCII art of characters saying a given string. Currently, it supports Simpsons characters.

## Features

- **Simpsons Characters**: Supports Bart, Homer, Marge, Lisa, and Maggie.
- **Customizable Text**: Add your own text for the characters to say.
- **ASCII Art**: Each character is represented in ASCII art form, inspired by existing Simpsons designs.
- **I'm Feeling Lucky**: Initialize `character = Charactersay()` and call the `character.imfeelinglucky()` to get fortune cookie messages.

## Installation

To install this package, you can clone the repository and run it locally. Or it can be installed using pip from PyPI.


## Usage

Here's a basic example of how to use the package:
```python.
from charsay import Charactersay   #import Charactersay() class
```
'horizontal_length' can be any int or float (raises ValueError if otherwise)
'horizontal_length' is an optional parameter (default=60) with a minimum possible value 15 (raises ValueError if otherwise)
```python.
from charsay import Charactersay   #import Charactersay() class
character = Charactersay(horizontal_length=x) # initializing object 
```
'object.string' is the string you want characters to say
```python.
character.string = "Hello, world!"
```
#### Example usage:

```python.
from charsay import Charactersay
character = Charactersay(horizontal_length=50)
character.string = 'English? Who needs that? I’m never going to England.'

character.homer()
```

## Available Functions
These methods take no arguments. They only need to be called, and will print the 'object.string' assigned earlier ('Hello, world!' if no string was assigned)
```python.
from charsay import Charactersay
character = Charactersay()

character.homer() 
character.marge()
character.bart()
character.lisa()
character.maggie()
character.imfeelinglucky() 
    #-->Generates a random character saying a random fortune-quote (ignores 'obj'.string)
```

## Contributing

Contributions are welcome! Feel free to add more characters or improve existing ones.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The Simpsons characters are copyrighted by Disney. This project uses ASCII art designs inspired by these characters for non-commercial purposes.
- ASCII art designs are not original and are based on existing Simpsons designs.

## Legal Note

Please be aware that using Simpsons characters without permission may infringe on Disney's copyright. This project is intended for personal, non-commercial use. If you plan to use this project commercially, you should seek permission from Disney or ensure your use falls under fair use provisions.
