# The main file

## Structure of the main file
After the first usage, always invoke the main file via:

```python
python3 main.py
```

Here's what it does:
1. It imports the email and the API token from the `settings.py` file.
2. It prints a welcome message reporting the version of the software.
3. It tries to authenticate the user.
4. With a `while` loop, it has a menù that gives the user to choose between three options:
    - **Option 1**: the user can visualize the price of one crypto in a currency of their choice. Also, the user can choose to store the value of the crypto in a CVS file with the current date.
    - **Option 2**: the user can visualize the difference between today's and yesterday's price of a crypto.
    - **Option 0**: it closes the program by breaking the loop.

## Using the main file
The main file is built as a menu with two options:
- Option 1 writes the current value of a crypto and stores its value in the CVS, if the user wants-
- Option 2 prints the difference in the value of a crypto between today and yesterday.


***
Let's see the actual code:

```{literalinclude} ../main.py
```
