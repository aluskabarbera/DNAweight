# Constants
speed_of_light = 299792458  # m/s
ev_to_joules = 0.000000000000000000160217733
joules_to_kg = 0.00000000000000001112650056

# Composición atómica
atomic_composition = {
    "C": {"protons": 6, "neutrons": 6, "quantity": 4},
    "H": {"protons": 1, "neutrons": 0, "quantity": 4},
    "N": {"protons": 7, "neutrons": 7, "quantity": 2},
    "O": {"protons": 8, "neutrons": 8, "quantity": 2}
}

# Quark masses in MeV/c^2
quark_masses = {
    "up": 2.2,
    "down": 4.7
}

# Calcular total de protones y neutrones por cada elemento
protons_by_element = {}
neutrons_by_element = {}

for element, counts in atomic_composition.items():
    total_protons = counts["protons"] * counts["quantity"]
    total_neutrons = counts["neutrons"] * counts["quantity"]
    protons_by_element[element] = total_protons
    neutrons_by_element[element] = total_neutrons

# Mostrar resultados
for element in atomic_composition:
    # Calculate protons and neutrons
    print(f"{element}: {protons_by_element[element]} protons, {neutrons_by_element[element]} neutrons")

    # Calculate quarks up and down
    quarks_up_protons = protons_by_element[element] * 2
    quarks_down_protons = protons_by_element[element] * 1
    print(f"{element}: {quarks_up_protons} quarks up protons, {quarks_down_protons} quarks down protons")

    quarks_up_neutrons = neutrons_by_element[element] * 1
    quarks_down_neutrons = neutrons_by_element[element] * 2
    print(f"{element}: {quarks_up_neutrons} quarks up neutrons, {quarks_down_neutrons} quarks down neutrons")
    
    # Calculate energy in MeV/c^2 
    energy_quarks_up_protons = quarks_up_protons * quark_masses["up"]
    energy_quarks_down_protons = quarks_down_protons * quark_masses["down"]
    print(f"{element}: {energy_quarks_up_protons} MeV/C^2 quarks up protons, {energy_quarks_down_protons} MeV/C^2 quarks down protons")

    energy_quarks_up_neutrons = quarks_up_neutrons * quark_masses["up"]
    energy_quarks_down_neutrons = quarks_down_neutrons * quark_masses["down"]
    print(f"{element}: {energy_quarks_up_neutrons} MeV/C^2 quarks up neutrons, {energy_quarks_down_neutrons} MeV/C^2 quarks down neutrons")

    # Convert MeV/c^2 to eV/c^2
    energy_quarks_up_protons_ev = energy_quarks_up_protons * 1000000
    energy_quarks_down_protons_ev = energy_quarks_down_protons * 1000000
    print(f"{element}: {energy_quarks_up_protons_ev} eV/C^2 quarks up protons, {energy_quarks_down_protons_ev} eV/C^2 quarks down protons")

    energy_quarks_up_neutrons_ev = energy_quarks_up_neutrons * 1000000
    energy_quarks_down_neutrons_ev = energy_quarks_down_neutrons * 1000000
    print(f"{element}: {energy_quarks_down_neutrons_ev} eV/C^2 quarks up neutrons, {energy_quarks_down_neutrons_ev} eV/C^2 quarks down neutrons")

    # Convert eV/c^2 to Joules/c^2
    energy_quarks_up_protons_joules = energy_quarks_up_protons_ev * ev_to_joules
    energy_quarks_down_protons_joules = energy_quarks_down_protons_ev * ev_to_joules
    print(f"{element}: {energy_quarks_up_protons_joules} J/C^2 quarks up protons, {energy_quarks_down_protons_joules} J/C^2 quarks down protons")
    
    energy_quarks_up_neutrons_joules = energy_quarks_up_neutrons_ev * ev_to_joules
    energy_quarks_down_neutrons_joules = energy_quarks_down_neutrons_ev * ev_to_joules
    print(f"{element}: {energy_quarks_up_neutrons_joules} J/C^2 quarks up neutrons, {energy_quarks_down_neutrons_joules} J/C^2 quarks down neutrons")

    # Convert Joules/c^2 to Kg/c^2
    mass_quarks_up_protons_kilograms = energy_quarks_up_protons_joules * joules_to_kg
    mass_quarks_down_protons_kilograms = energy_quarks_down_protons_joules * joules_to_kg
    print(f"{element}: {mass_quarks_up_protons_kilograms} Kg/C^2 quarks up protons, {mass_quarks_down_protons_kilograms} Kg/C^2 quarks down protons")

    mass_quarks_up_neutrons_kilograms = energy_quarks_up_neutrons_joules * joules_to_kg
    mass_quarks_down_neutrons_kilograms = energy_quarks_down_neutrons_joules * joules_to_kg
    print(f"{element}: {mass_quarks_up_neutrons_kilograms} Kg/C^2 quarks up neutrons, {mass_quarks_down_neutrons_kilograms} Kg/C^2 quarks down neutrons")

    # Convert Kg/c^2 to Kg
    mass_quarks_up_protons = mass_quarks_up_protons_kilograms / speed_of_light ** 2
    mass_quarks_down_protons = mass_quarks_down_protons_kilograms / speed_of_light ** 2
    print(f"{element}: {mass_quarks_up_protons} Kg quarks up protons, {mass_quarks_down_protons} Kg quarks down protons")

    mass_quarks_up_neutrons = mass_quarks_up_neutrons_kilograms / speed_of_light ** 2
    mass_quarks_down_neutrons = mass_quarks_down_neutrons_kilograms / speed_of_light ** 2
    print(f"{element}: {mass_quarks_up_neutrons} Kg quarks up neutrons, {mass_quarks_down_neutrons} Kg quarks down neutrons")

    print(" ")

