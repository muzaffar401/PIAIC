from hello_world.main import Greeter

def test_default_greeting():
    assert Greeter().greet() == "Hello, World"

def test_custom_greeting():
    assert Greeter("Muzaffar").greet() == "Hello, Muzaffar"
