""" Tests if both the debug and the release builds pass. """

from subprocess import run

import pytest


def build(flags=''):
    run(
        'cargo build ' + flags,
        shell=True,
        check=True
    )


@pytest.mark.timeout(240)
def test_build_debug():
    build()


@pytest.mark.timeout(240)
def test_build_release():
    build('--release')
