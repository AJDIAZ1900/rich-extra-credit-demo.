
Emoji (Python) — Extra Credit Demo
==================================

What this is
------------
A tiny demo of the ``emoji`` module for adding emoji to Python output and converting shortcodes
like ``:fire:`` into real emoji 🔥.

Why I chose it
--------------
It’s not in the standard library, installs in one command, and makes CLI output more expressive
and user-friendly in seconds.

Install
-------
Requires Python 3.

.. code-block:: bash

   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

Run the examples
----------------
Basic prints:

.. code-block:: bash

   python hello_emoji.py

Shortcodes → emoji:

.. code-block:: bash

   python emojize_demo.py

Flags & skin tones:

.. code-block:: bash

   python extras_demo.py

Uninstall (optional)
--------------------
.. code-block:: bash

   pip uninstall emoji

Notes
-----
- This module is NOT part of the Python standard library.
- Tested on macOS with Python 3.
