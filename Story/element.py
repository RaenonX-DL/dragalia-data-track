class ElementType:
    FIRE = "F"
    WATER = "W"
    WIND = "N"
    LIGHT = "L"
    DARK = "D"

    TO_PROCESS = (
        (FIRE, "火", "#FF0000"),
        (WATER, "水", "#3366FF"),
        (WIND, "風", "#339966"),
        (LIGHT, "光", "#FF6600"),
        (DARK, "暗", "#512DA8")
    )

    @staticmethod
    def cast(s: str):
        allowed_const = (ElementType.FIRE, ElementType.WATER, ElementType.WIND, ElementType.LIGHT, ElementType.DARK)

        for c in allowed_const:
            if c == s:
                return c

        raise ValueError(f"Unknown element type: {s}")
