from bw_migrations.utils import rescale_object, get_uncertainty_type
import pytest


def test_get_uncertainty_type():
    assert get_uncertainty_type({"uncertainty type": 1}) == 1
    assert get_uncertainty_type({"uncertainty_type": 2}) == 2
    assert get_uncertainty_type({"uncertainty_type_id": 3}) == 3
    assert get_uncertainty_type({"foo": "bar"}) == 0


def test_rescale_object_number_error():
    with pytest.raises(ValueError):
        rescale_object({}, "nope")


def test_rescale_object_dist_error():
    with pytest.raises(ValueError):
        rescale_object({"uncertainty type": 42}, 7)


def test_rescale_object_formula():
    given = {"uncertainty type": 0, "formula": "hi mom", "amount": 7}
    expected = {"uncertainty type": 0, "formula": "(hi mom) * 7", "amount": 49}
    assert rescale_object(given, 7) == expected


def test_no_uncertainty():
    given = {"uncertainty type": 0, "amount": 42}
    expected = {"uncertainty type": 0, "amount": 21}
    assert rescale_object(given, 0.5) == expected


def test_no_uncertainty_with_loc():
    given = {"uncertainty type": 0, "amount": 42, "loc": "dummy"}
    expected = {"uncertainty type": 0, "amount": 21, "loc": 21}
    assert rescale_object(given, 0.5) == expected


def test_unknown_uncertainty():
    given = {"uncertainty type": 1, "amount": 42}
    expected = {"uncertainty type": 1, "amount": 21}
    assert rescale_object(given, 0.5) == expected


def test_unknown_uncertainty_with_loc():
    given = {"uncertainty type": 1, "amount": 42, "loc": "dummy"}
    expected = {"uncertainty type": 1, "amount": 21, "loc": 21}
    assert rescale_object(given, 0.5) == expected


def test_normal_uncertainty():
    given = {"uncertainty type": 3, "amount": 2, "scale": 4}
    expected = {"uncertainty type": 3, "amount": 3, "loc": 3, "scale": 6}
    assert rescale_object(given, 1.5) == expected


def test_lognormal_uncertainty():
    given = {"uncertainty type": 2, "amount": 2, "loc": 2, "scale": 4}
    expected = {"uncertainty type": 2, "amount": 3, "loc": 3, "scale": 4}
    assert rescale_object(given, 1.5) == expected


def test_uniform_uncertainty():
    given = {"uncertainty type": 4, "amount": 2, "minimum": 0, "maximum": 4}
    expected = {"uncertainty type": 4, "amount": 3, "minimum": 0, "maximum": 6}
    assert rescale_object(given, 1.5) == expected


def test_uniform_uncertainty_flip_sign():
    given = {"uncertainty type": 4, "amount": 2, "minimum": 0, "maximum": 4}
    expected = {"uncertainty type": 4, "amount": -3, "minimum": -6, "maximum": 0}
    assert rescale_object(given, -1.5) == expected


def test_uniform_uncertainty_flip_sign_already_negative():
    given = {"uncertainty type": 4, "amount": -2, "minimum": -4, "maximum": 0}
    expected = {"uncertainty type": 4, "amount": 3, "minimum": 0, "maximum": 6}
    assert rescale_object(given, -1.5) == expected


def test_uniform_uncertainty_no_amount_field():
    given = {"uncertainty type": 4, "minimum": 0, "maximum": 4}
    expected = {"uncertainty type": 4, "minimum": 0, "maximum": 6}
    assert rescale_object(given, 1.5) == expected


def test_triangular_uncertainty():
    given = {"uncertainty type": 5, "amount": 2, "minimum": 0, "maximum": 4}
    expected = {
        "uncertainty type": 5,
        "amount": 3,
        "minimum": 0,
        "maximum": 6,
        "loc": 3,
    }
    assert rescale_object(given, 1.5) == expected


def test_triangular_uncertainty_flip_sign():
    given = {"uncertainty type": 5, "amount": 2, "minimum": 0, "maximum": 4}
    expected = {
        "uncertainty type": 5,
        "amount": -3,
        "minimum": -6,
        "maximum": 0,
        "loc": -3,
    }
    assert rescale_object(given, -1.5) == expected


def test_triangular_uncertainty_flip_sign_already_negative():
    given = {"uncertainty type": 5, "amount": -2, "minimum": -4, "maximum": 0}
    expected = {
        "uncertainty type": 5,
        "amount": 3,
        "minimum": 0,
        "maximum": 6,
        "loc": 3,
    }
    assert rescale_object(given, -1.5) == expected
