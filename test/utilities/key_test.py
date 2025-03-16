from utilities.key import derive_key

def test_derive_key():
     key_result = derive_key(b"password", "salt")

     assert isinstance(key_result, bytes)
     assert key_result != b"password"
     assert len(key_result) == 32