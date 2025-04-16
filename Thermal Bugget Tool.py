# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 09:27:59 2025

@author: mbaigorria
"""

# thermal_budget.py

import json
import numpy as np

# Constantes
SIGMA = 5.670374419e-8  # W/m²·K⁴


def load_input(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)


def compute_thermal_balance(surface):
    area = surface['area']
    alpha = surface['alpha']
    epsilon = surface['epsilon']
    power_diss = surface.get('power_dissipated', 0)
    q_solar = surface.get('solar_irradiance', 1361)  # W/m², default sun constant

    # Potencia absorbida por radiación solar
    absorbed_power = alpha * q_solar * area

    # Potencia total a disipar
    total_power = absorbed_power + power_diss

    # Temperatura de equilibrio (aproximada)
    T_eq = (total_power / (epsilon * SIGMA * area)) ** 0.25

    return {
        'absorbed_power': absorbed_power,
        'power_dissipated': power_diss,
        'total_power': total_power,
        'T_equilibrium_K': T_eq,
        'T_equilibrium_C': T_eq - 273.15
    }


def main():
    data = load_input('example_input.json')
    results = []

    for surface in data['surfaces']:
        name = surface.get('name', 'Unnamed surface')
        result = compute_thermal_balance(surface)
        print(f"\n{name}")
        for k, v in result.items():
            print(f"  {k}: {v:.2f}")
        results.append({"name": name, **result})


if __name__ == '__main__':
    main()