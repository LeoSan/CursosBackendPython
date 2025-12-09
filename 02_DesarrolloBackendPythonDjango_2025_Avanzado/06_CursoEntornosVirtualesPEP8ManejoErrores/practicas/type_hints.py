"""Explicaciones y ejemplos de type hints en Python."""

variable = 42  # int
print(f"Variable: {variable}, del tipo: {type(variable)}")

variable = "Texto de prueba"
print(f"Variable: {variable}, del tipo: {type(variable)}")

otra_variable: int = 44
print(f"Variable: {otra_variable}, del tipo: {type(otra_variable)}")

otra_variable = ""

user_id: int | None = None

# variable = valor
# variable: tipo = valor


def suma_clara(a: int, b: int) -> int:
    return a + b


articles: list[dict] = [
    {"title": "Example"},
    {"title": "Example 2"},
]

articles_dos: list[list[str]] = [
    ["articulos", "otros"],
    ["articulos", "otros"],
]

from typing import Any

articles_tres: list[list[Any]] = [
    ["articulos", "otros", 123],
    ["articulos", "otros"],
]

# int, str, list, dict, tuple, Any