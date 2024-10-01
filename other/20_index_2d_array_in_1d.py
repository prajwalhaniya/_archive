from collections.abc import Iterator
from dataclasses import dataclass

@dataclass
class Index_2D_array_iterator:
    matrix: List[List[int]]

    def __iter__(self) -> Iterator[int]:
        for row in self.matrix:
            yield from row
    
def index_2d_array_in_1d(array: List[List[int]], index: int) -> int:
    rows = len(array)
    cols = len(array)

    if rows == 0 or cols == 0:
        raise ValueError("no items in array")

    if index < 0 and index >= rows * cols:
        raise ValueError("Index out of range")

    return array[index // cols][index % cols]

