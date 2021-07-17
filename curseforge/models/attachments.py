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

import os.path
import urllib.parse
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .addon import Addon
    from ..api import Interface

__all__ = ["Attachment"]


class Downloadable:
    def __init__(self, interface: Interface, url: str) -> None:
        self.url = url
        self.interface = interface
        self._filename = os.path.basename(urllib.parse.urlparse(url).path)

    def read(self) -> bytes:
        with self.interface._session.get(self.url) as g:  # type: ignore
            g.raise_for_status()
            return g.content

    def save(self, fname: str | None = None):
        fname = (fname or self._filename).format(self)
        data = self.read()
        with open(fname, 'wb') as f:
            f.write(data)


class AttachmentBase:
    id: int
    addon: Addon
    description: str
    default: bool
    title: str


class Attachment(AttachmentBase, Downloadable):
    def __init__(self, addon: Addon, data: dict[str, Any]) -> None:
        super().__init__(addon.interface, data['url'])
        self.addon = addon
        self.id = data['id']
        self.description = data['description']
        self.default = data['isDefault']
        self.title = data['title']

    def __repr__(self) -> str:
        return "<Attachment id={0.id} title={0.title!r}>".format(self)
