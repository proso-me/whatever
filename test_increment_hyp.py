from hypothesis import given
import hypothesis.strategies as st

from increment import increment


@given(st.integers())
def test_add_one(num):
    assert increment(num) == num + 1

