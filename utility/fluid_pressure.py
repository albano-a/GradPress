def fluid_pressure():
    """
    This function defines a dictionary of fluid pressures.
    Each key in the dictionary represents a type of fluid, and the value is another dictionary.
    This nested dictionary contains the name of the fluid and its pressure gradient in various units.
    """
    fluid_pressure = {
        "dry_gas_zero": {"name":"Dry gas zero","gradient":{"psi/ft":0.0,"psi/m":0.0,"kgf/cm2/m":0.0,"bar/m":0.0}},
        "dry_gas": {"name":"Dry gas","gradient":{"psi/ft":0.0,"psi/m":0.0,"kgf/cm2/m":0.0,"bar/m":0.0}},
        "wet_gas": {"name":"Wet gas","gradient":{"psi/ft":0.140,"psi/m":0.459,"kgf/cm2/m":0.030,"bar/m":0.032}},
        "oil_limit": {"name":"Oil limit","gradient":{"psi/ft":0.300,"psi/m":0.984,"kgf/cm2/m":0.069,"bar/m":0.069}},
        "oil_60": {"name":"Oil 60°","gradient":{"psi/ft":0.387,"psi/m":1.270,"kgf/cm2/m":0.089,"bar/m":0.087}},
        "oil_20": {"name":"Oil 20° (heavy)","gradient":{"psi/ft":0.404,"psi/m":1.325,"kgf/cm2/m":0.093,"bar/m":0.091}},
        "fresh_water": {"name":"Fresh water","gradient":{"psi/ft":0.433,"psi/m":1.421,"kgf/cm2/m":0.100,"bar/m":0.098}},
        "sea_water": {"name":"Sea Water","gradient":{"psi/ft":0.444,"psi/m":1.457,"kgf/cm2/m":0.102,"bar/m":0.101}},
        "salt_sat_water": {"name":"Salt sat. Water","gradient":{"psi/ft":0.520,"psi/m":1.706,"kgf/cm2/m":0.120,"bar/m":0.118}},
        "salt_max": {"name":"Salt sat. Water Max","gradient":{"psi/ft":100.000,"psi/m":100.000,"kgf/cm2/m":100.000,"bar/m":100.000}}
    }
    return fluid_pressure

# REF: Ryder & Kennedy, 2011