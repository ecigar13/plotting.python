import logging
from os import path
from utils import runCommand
from Yahoo.YahooPlotter import YahooPlotter
from Cboe.CboePlotter import CboePlotter

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'config/logging.config')
logging.config.fileConfig(log_file_path)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    cboePlotter: CboePlotter = CboePlotter()
    files: [] = cboePlotter.get_paths()
    graphs: [] = []
    for file in files:
        graphs.append(cboePlotter.plot_file(file))
    logger.info(f"We have {len(graphs)} graphs")
    for graph in graphs:
        graph.show()

    yahooStock: YahooPlotter = YahooPlotter()
    files: [] = yahooStock.get_paths()
    graphs: [] = []
    for file in files:
        graphs.append(yahooStock.plot_file(file))
    logger.info(f"We have {len(graphs)} graphs")
    for graph in graphs:
        graph.show()
