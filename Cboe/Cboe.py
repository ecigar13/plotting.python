import json
import logging
import logging.config
import os
import pandas as pd
from pandas import *
import plotly.graph_objects as go

logging.config.fileConfig("../config/logging.config")
logger = logging.getLogger(__name__)


class YahooStock:
    '''
    Read yahoo stock information and process it.
    '''

    def plot_file(self, path: str):
        '''
        Read a yahoo file with stock information, plot all columns. Return a figure. Intended to call show() on this figure later.
        :param path: str: path to file.
        :return:
        '''
        dataFrame: DataFrame = pd.read_csv(path, skiprows=1)
        column_header: DataFrame = dataFrame.loc[:, dataFrame.columns != 'Date']
        fig: Figure = go.Figure()
        for header in column_header:
            logger.debug(f"Plotting {header}")
            fig.add_trace(
                go.Scatter(x=dataFrame['Date'], y=dataFrame[header], name=header, mode='lines'))

        fig.update_layout(yaxis_type="log", title=f"{path.split('/')[-1]} price")
        return fig

    def get_paths(self, config_path: str = '../config/config.json', extension: str = ".csv"):
        '''
        Read config file for the path of yahoo data, then file fully qualified paths to those files.
        :param configPath:
        :param extension:
        :return: []: list of paths to read.
        '''
        paths: [] = []
        with open(config_path) as json_file:
            config_dict: dict = json.load(json_file)
            readable_extensions: [] = config_dict['readableFileExtensions']['cboe']
            dir: str = os.path.abspath(
                os.path.join("..", config_dict["paths"]["data"],
                             config_dict["paths"]['cboe']["data"]))
            logger.info(f"Searching in {dir}")
            for root, folders, files in os.walk(dir):
                for file in files:
                    if any(extension in file for extension in readable_extensions):
                        logger.debug(f"Found file {os.path.join(root, file)}")
                        paths.append(os.path.join(root, file))

        logger.info(f"Found {len(paths)} data files")
        return paths


if __name__ == "__main__":
    cboePlotter: YahooStock = YahooStock()
    files: [] = cboePlotter.get_paths()
    graphs: [] = []
    for file in files:
        graphs.append(cboePlotter.plot_file(file))
    logger.info(f"We have {len(graphs)} graphs")
    for graph in graphs:
        graph.show()
