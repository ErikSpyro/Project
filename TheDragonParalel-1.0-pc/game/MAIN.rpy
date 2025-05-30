#This is the starting room.

define n = Character("Narrator", color="#0a1011")


image waiting_room_1 = "images/WaitingRoom1.png"




label game_start:
    #python:
        #_history_list.append(None, "", "This is a test.")
        #renpy.add_history("TEST", "Thsi is a test.")
    $ history_add("Test", "Hehe, this is a test.")
    scene waiting_room_1 with fade
    voice "voice/Narrator_MAIN_part1.wav"
    n "This is a story about a man named Stanley."
    $ history_remove()
    voice "voice/Narrator_MAIN_part2.wav"
    n "Standly were waiting in a waiting rooom. He do not know what he is waiting for. He simply... wait."
    voice "voice/Narrator_MAIN_part3.wav"
    n "Stanley sits quietly, alone. The room is silent, save for the subtle hum of fluorescent lighting and the distant tick of a clock mounted on a wall too high to see clearly."
    voice "voice/Narrator_MAIN_part4.wav"
    n "No receptionist. No doors opening. No comforting \"we'll be right with you.\" Just the soft, ever-pressing implication that something - anything - might happen."
    n "He could get up. He could leave. But he don't."
    n "He could scream. Or read a magazine. Or tear it in half, just to feel something."
    n "But he don't."
    n "He sit. Obediently. Waiting."
    "What do you do?"
    menu:
        "Wait more":
            n "You continue waiting. Good. That's what you were expected to do."
            n "Compliance is the backbone of a functional society."
            n "You're doing wonderfully."
        "Get up":
            n "Ah. Initiative. Dangerous, but fascinating."
            n "The door, of course, is locked. But you already knew that."
            n "You sit back down, pretending it was a stretch break."
            return
        "Kick magazines":
            return
    