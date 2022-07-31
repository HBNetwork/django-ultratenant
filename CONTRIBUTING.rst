Contributing
=============


Rules to contribute
-------------------

* Clone the code

.. code:: bash

    git clone https://github.com/HBN3tw0rk/django-ultratenant
    cd django-ultratenant
    git checkout develop


* Setup the project

.. code:: bash

    python -m venv .venv
    pip install -r requirements_dev.txt
    pre-commit install
    pytest


* Create a new branch

.. code:: bash

    git checkout -b task/branch-name-you-work-issue


* Create a pull request to the branch *develop*
