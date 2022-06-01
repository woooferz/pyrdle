from rich.console import Console
from rich.prompt import Prompt

c = Console()
p = Prompt()

word = "world"

c.print("Hello World!")

c.print("[#FFFFFF on #404040] W  O  R [/#FFFFFF on #404040][#FFFFFF on #facc25] D [/#FFFFFF on #facc25][#FFFFFF on #59ff61] S [/#FFFFFF on #59ff61]")


def render_word(aword: str):
    word1 = aword
    word2 = word

    word1 = word1.upper()
    word2 = word2.upper()

    c.print(word1, word2, sep=", ")


for i in range(6):
   # word = input(str(i + 1) + " > ")
    aword = p.ask(str(i) + " > ")
    if (len(aword) != len(word)):
        c.print("Invalid Word!")
        exit()
    c.print(render_word(aword))
