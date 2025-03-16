#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import re

def generate_pun(category: str = "general", length: str = "short") -> str:

    PUNS_GENERAL_SHORT = [
        "I tried to catch some fog yesterday — I mist.",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Did you hear about the mathematician who’s afraid of negative numbers? He will stop at nothing to avoid them!"
    ]
    PUNS_GENERAL_MEDIUM = [
        "Time flies like an arrow; fruit flies like a banana.",
        "The future, the present, and the past walked into a bar. Things got a little tense."
    ]

    PUNS_TECH_SHORT = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "A SQL query walks into a bar, sees two tables, and asks: 'Can I join you?'",
        "There are 10 types of people in the world: those who understand binary, and those who don't."
    ]
    PUNS_TECH_MEDIUM = [
        "Debugging: removing needles from the haystack.",
        "Real programmers count from 0, not 1."
    ]
    if category == "general":
        if length == "short":
            return random.choice(PUNS_GENERAL_SHORT)
        elif length == "medium":
            return random.choice(PUNS_GENERAL_MEDIUM)
        else:
            all_general = PUNS_GENERAL_SHORT + PUNS_GENERAL_MEDIUM
            return random.choice(all_general)

    elif category == "tech":
        if length == "short":
            return random.choice(PUNS_TECH_SHORT)
        elif length == "medium":
            return random.choice(PUNS_TECH_MEDIUM)
        else:
            all_tech = PUNS_TECH_SHORT + PUNS_TECH_MEDIUM
            return random.choice(all_tech)

    else:
        all_puns = (PUNS_GENERAL_SHORT + PUNS_GENERAL_MEDIUM +
                    PUNS_TECH_SHORT + PUNS_TECH_MEDIUM)
        return random.choice(all_puns)


def comedic_insult(name: str, severity: int = 1) -> str:
    if severity == 1:
        return f"{name}, you’re so optimistic you’d treat a 404 error like a fresh start!"
    elif severity == 2:
        return (f"{name}, your code is like a maze — I've gone in circles three times "
                "and I'm still nowhere near an exit!")
    else:  # severity == 3
        return (f"{name}, your bugs look like time travelers. One moment they show up "
                "with ancient errors, and the next moment they're throwing cutting-edge exceptions!")


def amuseify_text(text: str, style: str = "random") -> str:
    if style not in ["emoji", "leet", "random"]:
        raise ValueError("style must be either 'emoji', 'leet', or 'random'.")

    if style == "emoji":
        return _insert_emojis(text)
    elif style == "leet":
        return _to_leetspeak(text)
    else:
        chosen_style = random.choice(["emoji", "leet"])
        if chosen_style == "emoji":
            return _insert_emojis(text)
        else:
            return _to_leetspeak(text)


def _insert_emojis(text: str) -> str:
    EMOJIS = ["😂", "🤣", "😜", "🤪", "🙃", "😊", "😎", "😫"]
    words = text.split()
    for i in range(0, len(words), 2):
        words[i] += random.choice(EMOJIS)
    return " ".join(words)


def _to_leetspeak(text: str) -> str:
    leet_map = {
        "a": "4",
        "e": "3",
        "i": "1",
        "o": "0",
        "s": "5",
        "t": "7",
    }

    def replacer(match):
        char = match.group(0)
        return leet_map.get(char.lower(), char)
    return re.sub(r"[aeiostAEIOST]", replacer, text)


def random_fortune(topic: str = "life", mood: str = "positive") -> str:
    # Example fortune banks
    POSITIVE_FORTUNES = {
        "life": [
            "Your life will bloom like spring flowers.",
            "Keep smiling; good luck follows naturally.",
            "Stay grounded. True happiness will come your way."
        ],
        "career": [
            "Hard work never goes unnoticed – a promotion is just around the corner!",
            "New opportunities are on the horizon. Grab them!",
            "Your perseverance will soon pay off."
        ],
        "love": [
            "Love is just around the corner, patiently waiting for you.",
            "Genuine care yields genuine returns.",
            "No need to rush; real affection appears when you least expect it."
        ],
    }

    SARCASTIC_FORTUNES = {
        "life": [
            "Life is all about stepping into pitfalls. Miss a few, and it's not really complete.",
            "Try laughing — crying won't do much good anyway.",
            "Sure, it could be worse... but let's not jinx it."
        ],
        "career": [
            "Working 9-9-6 is a blessing... maybe?",
            "Have you considered cryptocurrency? Just kidding... or am I?",
            "Not writing bugs tonight only means writing double the bugs tomorrow."
        ],
        "love": [
            "Being single isn't scary. Being single and broke is.",
            "Be bold in love — you can only be rejected a hundred times or so.",
            "A thick wallet might just be the best date you'll have."
        ],
    }

    if mood == "positive":
        if topic in POSITIVE_FORTUNES:
            return random.choice(POSITIVE_FORTUNES[topic])
        else:
            all_positive = sum(POSITIVE_FORTUNES.values(), [])
            return random.choice(all_positive)

    elif mood == "sarcastic":
        if topic in SARCASTIC_FORTUNES:
            return random.choice(SARCASTIC_FORTUNES[topic])
        else:
            all_sarcastic = sum(SARCASTIC_FORTUNES.values(), [])
            return random.choice(all_sarcastic)

    else:
        return "True happiness lies in the little things of everyday life."

