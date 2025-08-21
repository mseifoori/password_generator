import random
import string
import nltk
from typing import List, Optional


nltk.download('words')


def main():
    pass


def pin_password_generator(length: int = 8) -> str:
    """Generates a password using only numbers.

    :param length: Length of the password. Defaults to 8.
    :type length: int, optional
    :return: Pin generated password.
    :rtype: str
    """
    return ''.join([random.choice(string.digits) for _ in range(length)])


def words_password_generator(
    length: int = 4,
    capitalization: bool = False,
    all_capitalized: bool = False,
    separator: str = ', ',
    vocabulary: Optional[List[str]] = False
) -> str:
    """Generates a password using words.

    :param length: Length of the password. Defaults to 4.
    :type length: int, optional
    :param capitalization: When True, the first letter of each word is capitalized. Defaults to False.
    :type capitalization: bool, optional
    :param all_capitalized: When True, all letters are capitalized. Defaults to False.
    :type all_capitalized: bool, optional
    :param separator: Separator between words. Defaults to ', '.
    :type separator: str, optional
    :param vocabulary: List of words to use. If None, the default vocabulary is used. Defaults to None.
    :type vocabulary: Optional[List[str]], optional
    :return: Words generated password.
    :rtype: str
    """
    if vocabulary:
        password: str = separator.join([random.choice(vocabulary) for _ in range(length)])
    else:
        password: str = separator.join([random.choice(nltk.corpus.words.words()) for _ in range(length)])
        
    if capitalization:
        return separator.join([word.capitalize() for word in password.split(separator)])
    elif all_capitalized:
        return password.capitalize()
    else:
        return password
    
    
def random_password_generator(
    length: int = 8,
    include_letters: bool = True,
    include_numbers: bool = True,
    include_characters: bool = True,
) -> str:
    """Generates a random password.

    :param length: Length of the password. Defaults to 8.
    :type length: int, optional
    :param include_letters: When True, letters are included. Defaults to True.
    :type include_letters: bool, optional
    :param include_numbers: When True, numbers are included. Defaults to True.
    :type include_numbers: bool, optional
    :param include_characters: When True, characters are included. Defaults to True.
    :type include_characters: bool, optional
    :return: Random password.
    :rtype: str
    """
    password_structure: List = []
    if include_letters:
        password_structure.append(string.ascii_letters)
    if include_numbers:
        password_structure.append(string.digits)
    if include_characters:
        password_structure.append(string.punctuation)
        
    password: str = ''.join([random.choice(''.join(password_structure)) for _ in range(length)])
    
    return password


def memorable_password_generator(num: int = 1) -> str:
    """Generates a memorable password.

    :param num: Number of words to include in the password. Defaults to 1.
    :type num: int, optional
    :return: Memorable password.
    :rtype: str
    """
    random_password: str = random_password_generator(length=4, include_letters=False)
    memorable_words: List = [random.choice(nltk.corpus.words.words()) for _ in range(num)]
    pre_password: List = list(random_password) + memorable_words
    random.shuffle(pre_password)
    
    return ''.join(pre_password)


if __name__ == '__main__':
    main()
