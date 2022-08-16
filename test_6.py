import pytest



@pytest.mark.parametrize("i,j,total" , [(1,2,3),(4,5,6),(7,8,15)])
def test_param(i,j,total):
    print("----i = ", i, "  J = ", j, "  totyal = ", total)
    assert i+j==total
