Pytest Implicit Namespace Packages Demo
=======================================

This repo is intended to demonstrate an issue with Pytest when using
implicit namespace packages. See [How do I Pytest a project using
PEP 420 namespace packages?][so-50174130] on Stack Overflow for the
question that inspired this and `test_modulename()` in
`project/util/thing_testme.py` for more details on why the test fails.


Requirements
------------

* Python ≥ 3.4
* Python 3 [`virtualenv`] available from your command line.


Running the Tests
-----------------

Run `./Test` in the top-level directory (or, if you modify the
path appropriately, from any directory).

Adding `-C` as the first argument will force a clean rebuild (wiping
and reinstalling the virtualenv).

All other arguments will be passed on to `pytest`.

If you have difficulty with the configuration:
* Run `./Test -C` to ensure your virtualenv is being configured
  correctly.
* Try removing `.build/` and sourcing the activate script with
  `. activate --python=python3`. Without the `-q` added by `Test` this
  will produce more verbose output that may indicate the problem.
* If you wish to use a specific version of Python, remove `.build/`,
  source `. activate --python=/path/to/my/python` and subequently run
  `./Test` without `-C` so that it uses the environment that you set up.


[`virtualenv`]: https://pypi.org/project/virtualenv/
[so-50174130]: https://stackoverflow.com/q/50174130/107294
