from utils import arrs


from utils import arrs

def test_get():
    result = arrs.get([1, 2, 3], 1, "test")
    assert result == 2, f"Expected 2, but got {result}"



def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
