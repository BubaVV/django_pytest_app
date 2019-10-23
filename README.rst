Simple Django app which show cases the integration with pytest, tox, travis-ci
and selenium. Using tox, you can run tests separately:

    ``tox -e selenium``

    ``tox -e not_selenium``

In Ubuntu, don't forget to do ``# apt install firefox-geckodriver``

.. image:: https://travis-ci.org/diefenbach/django_pytest_app.svg?branch=master
   :target: https://travis-ci.org/diefenbach/django_pytest_app
