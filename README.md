[![chucklepy](https://github.com/software-students-spring2025/3-python-package-httprequest/actions/workflows/build.yaml/badge.svg?event=pull_request)](https://github.com/software-students-spring2025/3-python-package-httprequest/actions/workflows/build.yaml)

# Python Package Exercise

# ChucklePy - A Fun Python Package

##  What is ChucklePy?
**ChucklePy** is a fun Python package designed to bring humor to developers’ lives.  
With puns, comedic insults, text amusement, and random fortunes, it keeps coding interesting.  

## Installation
Install ChucklePy directly from PyPI:
```bash
pip install chucklepy
```
Import the package in your code:

```python
from chucklepy import generate_pun, comedic_insult, amuseify_text, random_fortune
```
Usage Examples  
Here’s how you can use ChucklePy in your Python scripts:

- Generate a Pun
```python
pun = generate_pun(category="tech", length="short")
print(pun)
“A SQL query walks into a bar, sees two tables, and asks: 'Can I join you?'”
```
- Generate a Comedic Insult
```python
insult = comedic_insult("Alice", severity=2)
print(insult)
“Alice, your code is like a maze — I've gone in circles three times and I'm still nowhere near an exit!”
```
- Amuseify Text
```python
fun_text = amuseify_text("Hello world!", style="emoji")
print(fun_text)
“Hello👾 world!”
```
- Get a Random Fortune
```python
from chucklepy import random_fortune

fortune = random_fortune(topic="career", mood="sarcastic")
print(fortune)
“Not writing bugs tonight only means writing double the bugs tomorrow.”
```
See more examples in the [example program](https://github.com/software-students-spring2025/3-python-package-httprequest/blob/main/src/chucklepy/example.py).

## PyPI package link
[Visit Website](https://pypi.org/project/chucklepy/0.1.1/)

[Visit and try our fun package]()
## Contributing to ChucklePy  
We love contributions! Here’s how you can set up the project locally!

### Clone the Repository
```bash
git clone https://github.com/software-students-spring2025/3-python-package-httprequest.git
cd src/chuckle
```
### Set Up Virtual Environment  
- Using Pipenv:
```bash
pipenv install --dev
pipenv shell
```
- Run Tests
```bash
pipenv run pytest
pytest tests
```
- Build and Install the Package Locally
```bash 
pipenv run python -m build
pip install dist/chucklepy-*.whl
```
## Team Members  

- Xiaowei Ma [GitHub](https://github.com/WillliamMa)
- Rishi Rana [GitHub](https://github.com/Rishi-Rana1)
- Mandy Mao [GitHub](https://github.com/manrongm)
- Weite Li [Github](https://github.com/YYukin0)

## Running the Project on Any Platform  
- Ensure Python 3.9+ is installed  
- Clone the repository  
- Install dependencies
- Run tests  
- Execute the example script