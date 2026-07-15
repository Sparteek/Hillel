import pytest
import requests

def test_gorest():
    response = requests.get(url='https://gorest.'
                                'co.in/public/v2/users')