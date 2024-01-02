# The initial file

When you use this software you need to launch the `initial.py` file via:

```python
python3 initial.py
```

This will create a file, called `settings.py`, which stores your email and your API token: this way, every time you use this software, you won't need to insert them.\
\
Here's how the `initial.py` file works (code reference [here](https://github.com/federico-trotta/crypto_prices_API/blob/main/initial.py)):
- The user inserts the email and the API KEY via CLI.
- The program checks if the `settings.py` file exists in the settings folder, then:
    - If exists, it warns the user that the file already exists. 
    - If it doesn't exist, it creates it and stores the email and the API KEI inserted by the user.


***

Source code here:

```{eval-rst} 
.. automodule:: initial
   :members:
   :undoc-members:
   :show-inheritance:
```