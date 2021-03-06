import os
import numpy
import pandas
import pytest


# convert all numpy warnings into errors so they can be detected in tests
numpy.seterr(all='raise')


@pytest.fixture(scope='session')
def tests_path():
    return os.path.abspath(os.path.dirname(__file__))


@pytest.fixture(scope='session')
def cps_path(tests_path):
    return os.path.join(tests_path, '..', 'cps.csv.gz')


@pytest.fixture(scope='session')
def cps_fullsample(cps_path):
    return pandas.read_csv(cps_path)


@pytest.fixture(scope='session')
def cps_subsample(cps_fullsample):
    # draw smaller cps.csv subsample than in test_cpscsv.py
    return cps_fullsample.sample(frac=0.01, random_state=123456789)
