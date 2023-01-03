from typing import List, Optional

from .fib_crust import object_interface


class ObjectInterface:
    def __init__(self, number: List[int], numbers: List[List[int]]) -> None:
        self.number: List[int] = number
        self.numbers: List[List[int]] = numbers
        self.number_results: Optional[List[int]] = None
        self.numbers_results: Optional[List[List[int]]] = None

    # Pass self to the rust func
    def process(self) -> None:
        object_interface(self)
