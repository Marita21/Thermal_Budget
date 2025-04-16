# 🔧 Thermal Budget Tool

This Python script estimates the thermal balance of radiating surfaces exposed to solar irradiance and internal dissipation. It calculates absorbed power, total power to be dissipated, and equilibrium temperature using Stefan-Boltzmann's law.

---

## 📂 Files Included

- `Thermal Bugget Tool.py`: Main Python script that processes surface data and prints thermal balance results.
- `example_input.json`: Sample input file containing surface properties for analysis.

---

## 📌 How It Works

Each surface is defined by:
- **Area** (m²)
- **Absorptivity** (α)
- **Emissivity** (ε)
- **Solar Irradiance** (W/m²)
- **Internal Power Dissipation** (W)

The script computes:
- Absorbed solar power
- Total power to radiate
- Equilibrium temperature (in Kelvin and Celsius)

The model assumes surfaces radiate to deep space (ideal sink).

---

## ▶️ How to Run

1. Make sure you have Python 3 and `numpy` installed:
```bash
pip install numpy
```

2. Run the script:
```bash
python "Thermal Bugget Tool.py"
```

---

## 📄 Input Format (`example_input.json`)

```json
{
  "surfaces": [
    {
      "name": "Aluminum Panel",
      "area": 1.0,
      "alpha": 0.3,
      "epsilon": 0.8,
      "solar_irradiance": 1361,
      "power_dissipated": 50
    },
    {
      "name": "Radiator Surface",
      "area": 0.5,
      "alpha": 0.1,
      "epsilon": 0.9,
      "solar_irradiance": 500,
      "power_dissipated": 10
    }
  ]
}
```

---

## 📊 Sample Output

```
Aluminum Panel
  absorbed_power: 408.30
  power_dissipated: 50.00
  total_power: 458.30
  T_equilibrium_K: 317.04
  T_equilibrium_C: 43.89

Radiator Surface
  absorbed_power: 25.00
  power_dissipated: 10.00
  total_power: 35.00
  T_equilibrium_K: 192.45
  T_equilibrium_C: -80.70
```

---

## 👩‍💻 Author

**Mariela Baigorria**  
Thermal Engineer | Space Systems | Python Developer  
[github.com/Marita21](https://github.com/Marita21)

---

## 📜 License

MIT License

