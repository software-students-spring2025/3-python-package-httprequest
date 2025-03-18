import re
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from chucklepy.fun import (
    generate_pun,
    comedic_insult,
    amuseify_text,
    random_fortune
)


def test_generate_pun1():
    assert generate_pun()

def test_generate_pun2():
    assert generate_pun(category="tech", length="medium") != generate_pun(category="tech", length="short")

def test_generate_pun3():
    assert isinstance(generate_pun(), str)


def test_comedic_insult_optimistic():
    assert "optimistic" in comedic_insult("Alice", severity=1)

def test_comedic_insult_maze():
    assert "maze" in comedic_insult("Bob", severity=2)

def test_comedic_insult_time_travelers():
    assert "time travelers" in comedic_insult("Charlie", severity=3)

def test_amuseify_text():
    assert isinstance(amuseify_text("Hello world", style="emoji"), str)

def test_amuseify_text_emoji():
    assert re.search(r"[😂🤣😜🤪🙃😊😎😫🤯😈👾]", amuseify_text("Hello world", style="emoji"))

def test_amuseify_text_leet():
    assert re.search(r"[413705]", amuseify_text("Hello world", style="leet"))

def test_random_fortune():
    assert random_fortune(topic="life", mood="positive") != random_fortune(topic="career", mood="sarcastic")

def test_random_fortune2():
    assert random_fortune(topic="career", mood="sarcastic")

def test_random_fortune3():
    assert isinstance(random_fortune("love", "positive"), str)
