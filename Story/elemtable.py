"""
Desired elemental table

[div align=center][color=#3366FF][font=微軟正黑體][size=4]【風】[/size][/font][/color][/div]
[div][table width=95% cellspacing=1 cellpadding=1 border=2 align=center]
[tr]
[td align=center][img=https://gamepedia.cursecdn.com/dragalialost_gamepedia_en/5/57/210028_01.png width=60][/td]
[/tr]
[tr]
[td align=center][font=微軟正黑體][size=4]連結[/size][/font][/td]
[/tr]
[/table][/div]
"""
from typing import List, Tuple
from itertools import zip_longest

from data import NULL_SENTINEL
from config import ICON_WIDTH

__all__ = ["generate_elem_table"]


def grouper(iterable, n, fill_value=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fill_value)


def generate_elem_table(elem_name_col: (str, str), data: List[Tuple[str, str]]) -> List[str]:
    ret = []

    # Append header
    name, color = elem_name_col
    ret.append(f"[div align=center][color={color}][font=微軟正黑體][size=4]【{name}】[/size][/font][/color][/div]\n")

    # Append table head
    ret.append("[div][table width=95% cellspacing=1 cellpadding=1 border=2 align=center]\n")

    # Append table data
    if data:
        grouped = grouper(data, 5)
        for group in grouped:
            ret.extend(_generate_tr_td(group))
    else:
        ret.append("[tr]\n")
        ret.append(f"[td align=center][img={NULL_SENTINEL} width={ICON_WIDTH}][/td]\n")
        ret.append("[/tr][tr]\n")
        ret.append(f"[td align=center][font=微軟正黑體][size=4]連結[/size][/font][/td]\n")
        ret.append("[/tr]\n")

    # Append table tail
    ret.append("[/table][/div]\n")

    return ret


def _generate_tr_td(data: List[Tuple[str, str]]):
    tr_img = []
    tr_link = []

    for img, link in filter(lambda x: x is not None, data):
        tr_img.append(f"[td align=center][img={img} width={ICON_WIDTH}][/td]\n")
        tr_link.append(f"[td align=center][font=微軟正黑體][size=4][url={link}]連結[/url][/size][/font][/td]\n")

    ret = ["[tr]\n"]
    ret.extend(tr_img)
    ret.append("[/tr][tr]\n")
    ret.extend(tr_link)
    ret.append("[/tr]\n")

    return ret
