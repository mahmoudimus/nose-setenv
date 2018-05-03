Development Setup
=================
1. install development dependencies
   ```bash
   $ pip install coverage rednose
   ```
2. Install package
   ```bash
   $ pip install -e .
   ```
3. Run tests
   ```bash
   $ nosetests
   ```

Usage
=====

::

  nosetests --set-env-variables="{'blah': 'foo'}"
