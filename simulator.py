from classes import *
import debugging
import datetime
import time


class Simulation():

    def __init__(self):
        self.logger = debugging.initialize_debug_services('debug')
        self.logger.debug('Logger initalization completed')
        self.logger.info("""World of cows simulation. © Max Budko, 2022""")
        self.logger.info("""Creating field""")
        self.field = Field(16, 16, self.logger)
        self.logger.info("Created field %s" % self.field)

    def run(self):

        while True:
            self.logger.info("Sending tick")
            try:
                self.field.tick()
                time.sleep(0.2)
            except NotImplementedError as e:
                self.logger.error(e.message)
                self.logger.warning(
                    "Could not proceed tick with error, skipping the rest")
            except ValueError as e:
                self.logger.fatal(e.message)
                self.logger.warning(
                    "Could not proceed programm with fatal error, skipping")
                self.logger.info("Programm quit")
                break


if __name__ == '__main__':
    Simulation().run()
