from single.city_signal import CitySignal
from single.highway_signal import HighwaySignal
from Controler.controller import SignalController
from app_logger import logger



logger.info(f"Traffic Simulation Started....")
controller=SignalController()

no_vehicle=int(input("Enter number of vehicles"))

city_signal=CitySignal(no_vehicle)
controller.operate(city_signal)

highway_signal=HighwaySignal(no_vehicle)
controller.operate(highway_signal)

logger.info(f"Traffic Simulation Completed....")


