"""
The MIT License (MIT)

Copyright (c) 2021 XuaTheGrate

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
from __future__ import annotations

from typing import Any

__all__ = ["Category"]


class Category:
    __slots__ = ('id', 'name', 'game_id')

    def __init__(self, data: dict[str, Any]) -> None:
        self.id: int = data['categoryId']
        self.name: str = data['name']
        self.game_id: int = data['gameId']

    def __repr__(self) -> str:
        return "<Category {0.name!r}: {0.id}>".format(self)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Category) and self.game_id == other.game_id and self.id == other.id

    def __hash__(self) -> int:
        return hash((self.id, self.game_id))
