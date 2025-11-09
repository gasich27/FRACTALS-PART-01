L_SYSTEM_RULES = {
    "plant": {
        "axiom": "X",
        "rules": {"X": "F−[[X]+X]+F[+FX]−X", "F": "FF"},
        "angle": 25
    },
    "dragon": {
        "axiom": "FX",
        "rules": {"X": "X+YF+", "Y": "-FX-Y"},
        "angle": 90
    },
    "fern": {
        "axiom": "X",
        "rules": {"X": "F[+X]F[-X]+X", "F": "FF"},
        "angle": 22
    },
    "bush": {
        "axiom": "X",
        "rules": {"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"},
        "angle": 18
    }
}
