# %% 2.1.2
import math


def polar_complex(c: complex):
    arg = math.atan2(c.imag, c.real)
    abs = math.sqrt(c.real**2 + c.imag**2)
    return arg / (2 * math.pi) * 360, abs


c = complex(1, math.sqrt(3))
arg, abs = polar_complex(c)
print(f"{arg=:.2f} degrees, {abs=:.2f}")

# %% 2.2.1

def linspace(a, b, N=100):
    step = (b - a) / (N - 1)
    points = [a + i * step for i in range(N)]
    return points


print(linspace(0.1, 10))

# %% 2.3.2

x = lambda a, b, c: (
    -b / (2 * a) - math.sqrt((b / (2 * a)) ** 2 - c / a),
    -b / (2 * a) + math.sqrt((b / (2 * a)) ** 2 - c / a),
)
print(x(1, 2, 0))

# %% 2.4.1
import random
"""
Rock (r), Paper (p), Scissors (s)
p > r
s > p
r > s
"""

_map = {
    "r": 1,
    "p": 2,
    "s": 3,
}
name_map = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
}

while True:
    human = _map[input("Choose Rock (r), Paper (p) or Scissors (s): ")]
    computer = random.randint(1, 3)
    print(
        f"""
    You chose {name_map[human]}.
    The computer chose {name_map[computer]}.
    """
    )
    if human == computer:
        print("It's a tie!")
    elif (human - computer) in (1, -2):
        print("You won!")
    else:
        print("You lost!")

# %% 2.5.2

def count_word(file_name, target_word):
    with open(file_name, "r") as f:
        text = f.read().replace("\n", " ")

    # Create a list with the words
    alpha_chars = []
    for letter in text:
        if letter.isalpha() or letter in (" "):
            alpha_chars.append(letter.lower())
    text = "".join(alpha_chars)
    words = text.split(" ")

    # Count words
    count = 0
    target_word = target_word.lower()
    for word in words:
        if word == target_word:
            count += 1
    return count


num_occurences = count_word("story.txt", "the")
print(num_occurences)

# %% 2.6.3

"""
space between letters
/ between words
"""
text_to_morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
}

morse_to_text = {v: k for k, v in text_to_morse.items()}


def encode(in_file_name, morse_file_name):
    with open(in_file_name, "r") as f:
        text = f.read()

    out = []
    for c in text:
        out.append(text_to_morse[c.upper()])

    with open(morse_file_name, "w") as f:
        f.write(" ".join(out))


def decode(morse_file_name, decoded_file_name):
    with open(morse_file_name, "r") as f:
        morse = f.read()

    morse = morse.split(" ")
    out = []
    for m in morse:
        c = morse_to_text[m].lower()
        if len(out) >= 2:
            if out[-2] in [".", ",", "?", "!"]:
                c = c.upper()
        elif len(out) == 0:
            c = c.upper()
        out.append(c)

    with open(decoded_file_name, "w") as f:
        f.write("".join(out))


in_file_name = "story.txt"
morse_file_name = "morse_story.txt"
decoded_file_name = "decoded_story.txt"

encode(in_file_name, morse_file_name)
decoded_text = decode(morse_file_name, decoded_file_name)
