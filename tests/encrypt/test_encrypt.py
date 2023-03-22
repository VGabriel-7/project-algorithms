from challenges.challenge_encrypt_message import encrypt_message

import pytest


def test_encrypt_message():
    assert encrypt_message('bcapac', 3) == 'acb_cap'
    assert encrypt_message('bcapac', 9) == 'capacb'
    assert encrypt_message('bcapac', 4) == 'ca_pacb'

    with pytest.raises(
        TypeError, match='tipo inválido para key'
    ):
        encrypt_message(message=42, key='YoungSheldon')
    with pytest.raises(
        TypeError, match='tipo inválido para message'
    ):
        encrypt_message(message=42, key=42)
