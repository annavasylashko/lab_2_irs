# Inf. search systems - Lab2 (search engines)

## Task

[Link to task](./SearchEnginesAssignment2.pdf)

[Link to starter code](http://web.stanford.edu/class/archive/cs/cs106a/cs106a.1212/assn/bajillion)

## Student

Name: Anna Vasylashko

Group: KP-21mp

## Extra/Optional tasks:

1. Ranking system (number of occurencies)
2. Stop-word elimination
3. Word stemming (using *ntlk* library)
4. Hyperlinks to resulting files on search results

## Instructions

Installing dependencies:

```zsh
pip3 install -r requirements.txt
```

Run tests

```zsh
python3 -m doctest -v common_elements.py searchengine.py extension.py
```

Run console search application

```zsh
python3 searchengine.py <bbcnews/small> -s
```

**Run server:**

```zsh
python3 extension_server.py
```

