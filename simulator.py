from classes import *
import debugging
import datetime

class Simulation():
    
    def __init__(self):
        self.logger = debugging.initialize_debug_services('debug', 'datetime')