Rich (Python) — Extra Credit Demo
=================================

What this is
------------
A tiny demo of the `rich` module for prettier console output (colors, tables, progress bars).

Why I chose it
--------------
It’s beginner-friendly, not in the standard library, and instantly makes CLI output easier to read.

Install
-------
Requires Python 3.  
Create a virtual environment (recommended):

.. code-block:: bash

   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

If you don't want a venv:

.. code-block:: bash

   pip install -r requirements.txt

Run the examples
----------------
Basic styled text:

.. code-block:: bash

   python app.py

Table demo:

.. code-block:: bash

   python table_demo.py

Progress bar:

.. code-block:: bash

   python progress_demo.py

Uninstall (optional)
--------------------
If you used a venv, just deactivate and delete the folder:

.. code-block:: bash

   deactivate
   rm -rf .venv

If you installed globally and want to remove it:

.. code-block:: bash

   pip uninstall rich

Notes
-----
- This module is NOT part of the standard library.
- Tested on macOS with Python 3.
