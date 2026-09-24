import importlib


def test_package_is_importable() -> None:
    package = importlib.import_module("customer_propensity")

    assert package is not None
