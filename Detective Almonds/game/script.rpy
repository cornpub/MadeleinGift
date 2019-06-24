# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define isabelle = Character("Isabelle")
define kitty = Character("Kitty")
define resetti = Character("Mr.Resetti")
define tom = Character("Tom Nook")
define hazel = Character("Hazel")
define doctor = Character("Doctor")


label start:
    scene frontdesk
    with fade
    show isabellehappy
    isabelle "Hello there, Welcome to our town! You are here for your meeting with the mayor right?"
    "???""Yeah, that's me."
    isabelle "Can I please get the name for the meeting?"
    init python:
        name = renpy.input("Please enter your name")
    define player = Character("[name]")
    isabelle "Okay, [name]... Oh yes, I see you on the list. You can head right in, the mayor is waiting for you."
    "You walk to the mayor's office and you knock on the door."
    "*Knock Knock*"
    isabelle"Mr. Mayor? [name] is waiting for you!"
    "You knock once more to try to get a response."
    "*Knock Knock*"
    hide isabelle
    jump invests
label invests:
    menu:
        "Who should I talk to first?"
        "Isabelle.":
            jump isabelleinvest
        "Kitty.":
            jump kittyinvest
        "Tom Nook.":
            jump tomnookinvest
        "Resetti.":
            jump resettiinvest
        "Hazel.":
            jump hazelinvest
        "The doctor.":
            jump doctorinvest
label isabelleinvest:
    #insert thing here
    jump invests
label kittyinvest:
    #insert thing here
    jump invests
label tomnookinvest:
    #insert thing here
    jump invests
label resettiinvest:
    #insert thing here
    jump invests
label hazelinvest:
    #insert thing here
    jump invests
label doctorinvest:
    #insert thing here
    jump invests
