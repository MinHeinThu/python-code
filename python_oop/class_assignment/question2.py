# Name: Min Hein Thu
# ID: 67111391
# Course: Object Oriented Programming

class Device:
    def __init__(self, device_name):
        self.device_name = device_name

    def power_on(self):
        print(f"{self.device_name} power ON")

    def power_off(self):
        print(f"{self.device_name} power OFF")

class Sensor:
    def __init__(self, sensor_type):
        self.sensor_type = sensor_type

    def detect(self):
        print(f"{self.sensor_type} detected")

class SmartLight(Device):
    def __init__(self, device_name, brightness):
        super().__init__(device_name)
        self.brightness = brightness

    def power_on(self):
        print(f"{self.device_name} ON | Brightnesss: {self.brightness}%")

    def power_off(self):
        print(f"{self.device_name} OFF")

class SmartThermostat(Device,Sensor):
    def __init__(self, device_name, sensor_type, temperature):
        Device.__init__(self, device_name)
        Sensor.__init__(self,sensor_type)
        self.temperture = temperature

    def set_temperature(self, value):
        print(f"{self.device_name} ON | Temperature Set: {value}°C")
        self.temperature = value
        return

    def detect(self):
        print(f"{self.sensor_type} Detected: Temperature Change!")

light1 = SmartLight("Living room bulb", 80)
light1.power_on()
light1.power_off()

device1 = SmartThermostat("Nest", "Temperature sensor" ,26)
device1.set_temperature(24)
device1.detect()
device1.power_off()
device1.power_on()

devices = [light1, device1]
def turn_on_off(devices,on_off):
    if on_off == "ON":
        print("Turning ON all devices...")
        for device in devices:
            device.power_on()
    if on_off == "OFF":
        print("Turning OFF all devices...")
        for device in devices:
            device.power_off()
turn_on_off(devices, "ON")
turn_on_off(devices, "OFF")
