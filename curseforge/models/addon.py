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

from .attachments import Attachment
from .category import Category
from .file import ModFile
from .user import User
from ..enums import Modloader
from ..utils import from_iso_format

if TYPE_CHECKING:
    from ..api import Interface

__all__ = ["Addon"]


class Addon:
    def __init__(self, interface: Interface, data: dict[str, Any]) -> None:
        self.interface = interface
        self.id: int = data['id']
        self.display_name: str = data['name']
        self.name: str = data['slug']
        self.authors = [User(d) for d in data['authors']]
        self.attachments = [Attachment(self, d) for d in data['attachments']]
        self.url: str = data['websiteUrl']
        self.summary: str = data['summary']
        self.featured: bool = data['isFeatured']
        self.created_at = from_iso_format(data['dateCreated'])
        self.released_at = from_iso_format(data['dateReleased'])
        self.modified_at = from_iso_format(data['dateModified'])
        self.modloaders: list[Modloader] = data.get("modLoaders", [])
        self.downloads: int = round(data['downloadCount'])

        self.categories: list[Category] = [interface._store_category(d) for d in data['categories']]

        self._files: dict[int, ModFile] = {k['id']: ModFile(self, k) for k in data['latestFiles']}
        self._default_file_id: int = data['defaultFileId']

    def __repr__(self) -> str:
        return "<Addon id={0.id} display_name={0.display_name!r} categories={0.categories}>".format(self)

    @property
    def default_file(self) -> ModFile:
        return self._files[self._default_file_id]

    @property
    def latest_file(self) -> ModFile:
        return max(self._files.values(), key=lambda i: i.uploaded_at)

    @property
    def files(self) -> list[ModFile]:
        return list(self._files.values())
    
