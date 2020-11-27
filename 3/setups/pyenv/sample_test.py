from contextlib import contextmanager
import sample
import pytest


@contextmanager
def does_not_raise():
    yield
# Copy/pasta from https://docs.pytest.org/en/stable/example/parametrize.html#paramexamples 
@pytest.mark.parametrize(
    "example_input,expectation,",
    [
        (3, does_not_raise()),
        (2, does_not_raise()),
        (1, does_not_raise()),
        (0, pytest.raises(ZeroDivisionError)),
    ])
def test_answer(example_input: int, expectation: Exception):
    """Test how much I know division."""
    with expectation:
        assert (6 / example_input) is not None


@pytest.mark.parametrize(
    "have,want",
    [
        (-1,0),
        (2,3),
        (3,4),
    ],
)
def test_func(have: int,want:int):
    assert want == sample.func(have)


@pytest.fixture(params=[
{
    "input": 12,
    "want": 1,
},
{
    "input": 6,
    "want":2,
},
{
    "input":3,
    "want":3,
}
])
def test_divisor(test):
    assert sample.divisor(test.input) == test.want
