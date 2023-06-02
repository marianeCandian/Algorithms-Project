from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(1, 2)

    with pytest.raises(TypeError):
        encrypt_message("message", "a")

    assert_one = encrypt_message("message", 9)
    assert assert_one == "egassem"

    assert_two = encrypt_message("message", 3)
    assert assert_two == "sem_egas"

    assert_three = encrypt_message("message", 4)
    assert assert_three == "ega_ssem"
