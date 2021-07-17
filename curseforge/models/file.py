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

from typing import Any, TYPE_CHECKING

from .attachments import Downloadable
from ..utils import from_iso_format

if TYPE_CHECKING:
    from ..api import Interface
    from .addon import Addon

__all__ = ['File', 'ModFile']


class File(Downloadable):
    def __init__(self, interface: Interface, data: dict[str, Any]) -> None:
        super().__init__(interface, data['downloadUrl'])
        self.id: int = data['id']
        self._filename = data['fileName']
        self.versions: list[str] = data['gameVersion']
        self.uploaded_at = from_iso_format(data['fileDate'])
        self.fingerprint: str = data['packageFingerprint']

    @property
    def default_filename(self) -> str:
        return self._filename

class ModFile(File):
    def __init__(self, addon: Addon, data: dict[str, Any]) -> None:
        super().__init__(addon.interface, data)
        self.addon = addon
        self.dependencies: list[Addon] = []  # todo

    def __repr__(self) -> str:
        return "<File {0.default_filename!r}: {0.id}>".format(self)

    def save(self, fname: str | None = None, *, optional_dependencies: bool=True):
        super().save(fname=fname)
        
        for dep in self.dependencies:
            ...  # todo
