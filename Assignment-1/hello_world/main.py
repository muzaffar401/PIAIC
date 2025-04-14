from dataclasses import dataclass

@dataclass
class Greeter:
    name: str = "World"

    def greet(self):
        return f"Hello, {self.name}"

if __name__ == "__main__":
    print(Greeter().greet())
