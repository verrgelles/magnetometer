import pyvisa


class Device:
    def __init__(self):
        resource_manager = pyvisa.ResourceManager()
        device_id = resource_manager.list_resources()[0]
        self.instance = resource_manager.open_resource(device_id)

    def is_device_available(self) -> bool:
        if self.instance.query("*IDN?") is not None:
            return True
        else:
            return False

    def get_wavelength(self) -> float:
        # in nmeters
        return float(self.instance.query(":SENS:CORR:WAV?"))

    def set_wavelength(self, target_wavelength: float):
        #in nmeters
        self.instance.write(f":SENS:CORR:WAV {target_wavelength}")

    def get_sensor_info(self) -> str:
        # Return (name, serial, calibration, type, subtype, flags)
        # "S140C","220520303","20-MAY-2022",1,18,33
        return self.instance.query(":SYST:SENS:IDN?")

    def get_power(self) -> float:
        return self.instance.query("MEAS[:SCAL][:POW]?")

    def get_power_density(self) -> float:
        return self.instance.query("MEASure[:SCALar]:PDENsity?")

    def get_frequency(self) -> float:
        return self.instance.query("MEAS[:SCAL]:FREQ?")

    def get_data(self) -> float:
        # Returns power in Watts
        return float(self.instance.query(":READ?"))
