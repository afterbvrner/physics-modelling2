avogadro = 6.02214076 * 10**23
R = 8.31446261815324
delta_map = {
    "elastic scattering": 0.1,
    "radiation capture": 10 ** 6,
    "photonuclear reactions": 10 ** -3,
    "weak interaction": 10 ** -20
}


def barn_to_cm(barn: float):
    return barn * 10 ** -24


def length(interaction_type: str, n: float):
    return 1/(barn_to_cm(delta_map[interaction_type]) * n)


def amount_of_solid(p: float, M: float):
    return p / 1000 / M * avogadro


def amount_of_gas(P: float, t: float):
    return 0.001 / (R * t / P)


if __name__ == '__main__':
    print("{:e}".format(length("weak interaction", amount_of_gas(101325, 273.15))), "см")
