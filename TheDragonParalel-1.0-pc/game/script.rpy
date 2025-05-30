# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    import os
    import types
    import random

define n = Character("Narrator")

init python: #historey editing
    def history_add(who, what, who_id=None):
        fake_line = types.SimpleNamespace()
        fake_line.who = who
        fake_line.what = what
        fake_line.who_id = who_id
        fake_line.who_args = {}
        fake_line.what_args = {}
        fake_line.window_args = {}
        _history_list.append(fake_line)
    def history_remove():
        if _history_list:
            _history_list.pop()
    def history_remove_text(text, mode=1):
        global _history_list
        if mode == int(1): # Remove entries with specific text in 'what'
            _history_list = [h for h in _history_list if h.what != text]
        elif mode == int(2): # Remove entries with specific text in 'who'
            _history_list = [h for h in _history_list if h.who != text]
    def history_disable():
        config.history = False

init python:
    def check_license(data=None):
        path = os.path.join(config.gamedir, "license.txt")
        if not os.path.isfile(path):
            return "missing"
        with open(path, "r") as f:
            content = f.read().strip()
        if content != "licencs=0":
            if content == "licencs=-1":
                return "bad"
            elif not content.startswith("license=") or data == 1:
                return "tampered"
            result = content[len("license="):].strip()
            if result.isdigit():
                return f"i{int(result)}"
            else:
                return f"s-{str(result)}"
        else:
            return "valid"


# The game starts here.
label start:
    jump game_start
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room   

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    jump game_start

return #Fail-safe
label setup:
    default current_hour = 12
    default current_minute = 0
    default time_selected = False
    init python:
        import time
        import datetime        
    scene black with fade
    "Before we begin..."
    "Please enter the current time."
    show screen time_input_screen
    $ time_selected = False
    while not time_selected:
        $ renpy.pause(0.1, hard=True)
    hide screen time_input_screen
    "Thank you. Your input has been recorded."
    $ now = time.time()
    $ input_time = datetime.datetime.fromtimestamp(now).replace(hour=current_hour, minute=current_minute)
    $ persistent.entered_time_timestamp = time.mktime(input_time.timetuple())
    $ persistent.time_input_real_time = now

    #$ persistent.entered_time = "%02d:%02d" % (current_hour, current_minute)
    scene
    return
label pirate:
    if not persistent.last_licence_status:
        $ license_status = check_license(1)
    else:
        $ license_status = check_license()
    if persistent.last_licence_status == "bad":
        return #Telling the player that they should be puniched.
    $ persistent.last_licence_status = license_status
    #"[license_status]"
    if not persistent.seen_pirate_screen:
        if license_status == "missing":
            scene black with fade
            pause 1.0
            centered "{size=+40}LICENSE VERIFICATION FAILED{/size}\n\nNo license data found.{p=7}{nw}"
            pause 1.5
            centered "You didn't even try.{p=5}{nw}"
            pause 1.2
            centered "You could've typed in random digits. A fake key. A doodle. A whisper of effort.{p=7}{nw}"
            pause 1.5
            centered "But no. You left it blank."
            pause 1.0
            centered "What were you expecting to happen? That the game would look at the empty void and say,\n'Oh yes, clearly this user is a trustworthy sort'?"
            pause 2.0
            centered "You insult me."
            pause 1.5
            centered "I built this entire world for you. Handcrafted every variable, loop, and conditional."
            pause 1.5
            centered "And in return, you couldn't even be bothered to type '1234'."
            pause 1.0
            centered "But fine. We'll continue. Just know that I'm watching you more closely now."
            pause 2.0
            centered "...Very closely."
        else:
            $ persistent.seen_pirate_screen = True
            scene black with fade
            pause 1.0
            centered "{size=+40}WARNING!{/size}\nPiracy detected{p=5}{nw}"
            pause 1.0
            centered "The copy of the game you are playing contains no license key.{p=6}{nw}"
            pause 2.0
            centered "What does it mean to own a story?{p=5}{nw}"
            pause 1.0
            centered "If a game is copied without payment, does its world still exist?{p=7}{nw}"
            pause 1.5
            centered "If no one paid for you... are you still real?{p=5}{nw}"
            centered "...{p=5}{nw}"
            pause 2.0
            centered "If you weren't supposed to be here... does that make you more important?{p=5}{nw}"
            pause 1.5
            centered "Things to ponder...{p=5}{nw}"    
    else:
        if license_status == "valid":
            return
        elif license_status == "tampered":
            return #Telling the player they have fucked up the license.
        elif license_status[0] == "i" or license_status[0] == "s":
            if license_status[0] == "i":
                $ license_status = license_status[1:]
            else:
                $ license_status = license_status[2:]


            $ license_status = license_status[:40] + ("..." if len(license_status) > 40 else "")
            $ funnumber = random.randint(1, 867201)
            centered "Ah. {w=0.5}Interesting."
            centered "You entered [license_status] as your license key."
            centered "Not exactly {i}official{/i}, is it? No DRM signature. No corporate backing. Not even a checksum!"
            centered "You thought you were clever, didn't you?"
            centered "Just smash your fingers against the keyboard and invent a number like [license_status], anbd somehow, magically, the game would thik you are a legitimate user?"
            centered "Well then, [license_status]-wielder, if that even is your {i}real{/i} number..."
            centered "Let's put that so-called license to the test."
            centered "Welcome to the Official Unauthorizatied User Validation Exam™."
            centered "A quick quiz on [license_status]."
            pause 1.0
            if license_status[1:].isdigit():
                $ answer = renpy.input(f"Question 1: What is {license_status} + {funnumber}?")
                if answer.isdigit():
                    if answer == int(license_status) + int(funnumber):
                        centered "My godness, you can count."
                        centered ""
                else:
                    centered "What, no! That is not even a number."
            else:
                return

            
            """Question 1: What is the square root of [license_status]? Round to the nearest feeling.\n
            A) """


        elif license_status[0] == "s":
            $ license_status = license_status[2:]

        return

    