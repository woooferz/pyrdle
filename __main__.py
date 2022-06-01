from rich.console import Console
from rich.prompt import Prompt
import random
import readline

c = Console()
p = Prompt()

word = None
words = None

with open("words.txt") as f:
    words = f.read().split("\n")
    word = random.choice(words)


# c.print("Hello World!")

# c.print("[#FFFFFF on #404040] W  O  R [/#FFFFFF on #404040][#FFFFFF on #facc25] D [/#FFFFFF on #facc25][#FFFFFF on #59ff61] S [/#FFFFFF on #59ff61]")

c.print("Pyrdle", style="bold")
c.print("By Wooferz", style="italic")

print("\n\n\n")


def render_word(aword: str):
    word1 = aword
    word2 = word

    word1 = word1.upper()
    word2 = word2.upper()

    final = ""

    occ = {}

    for i in word2:
        try:
            occ[i] = occ[i] + 1
        except KeyError:
            occ[i] = 1

    for l1, l2 in zip(word1, word2):
        if l1 == l2:
            occ[l2] -= 1

    for l1, l2 in zip(word1, word2):
        if l1 == l2:
            final = final + "[#FFFFFF on #59ff61] " + \
                l1 + " [/#FFFFFF on #59ff61]"
        elif l1 in word2 and occ[l1] > 0:
            final = final + "[#FFFFFF on #facc25] " + \
                l1 + " [/#FFFFFF on #facc25]"
            occ[l1] -= 1
        else:
            final = final + "[#FFFFFF on #404040] " + \
                l1 + " [/#FFFFFF on #404040]"

    return final, word1 == word2


try:
    for i in range(6):
        # word = input(str(i + 1) + " > ")
        while True:
            aword = input("GUESS > ")
            if (len(aword) != len(word)):
                c.print("Invalid Word Length!")
            else:
                if not aword.lower() in words:
                    c.print("Not a word")

                else:
                    rendered_word, victory = render_word(aword)
                    c.print(rendered_word)

                    if victory:
                        c.print("You Win!")
                        exit()
                    break
except KeyboardInterrupt:
    pass
c.print("You Lose")
c.print("Word was " + word.capitalize())
