import reversenum

def test_reverse():
    result = reversenum.reverse(105)
    assert result == 501

def test_negreverse():
    result = reversenum.reverse(-639)
    assert result == -936

def test_bitreverse():
    result = reversenum.reverse(2**32)
    assert result == 0

def test_samereverse():
    result = reversenum.reverse(5)
    assert result == 5
