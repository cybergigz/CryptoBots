import logging

from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    binance = BinanceFuturesClient("a640756f426f13b8d225a7f8ac9c9fc92f1f22ed6cf0030755171c96ba48345a",
                                   "b2a94a6d7c43946a4e6bd7273335755413a03896785848db633518b551a27893", True)
    bitmex = BitmexClient("", "", True)

    root = Root(binance, bitmex)
    root.mainloop()
