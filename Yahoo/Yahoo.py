import os

import pandas as pd
from pandas import *
import plotly.graph_objects as go


class YahooStock:
    '''
    Read yahoo stock information and process it.
    '''

    def plotFile(self, path: str):
        '''
        Read a yahoo file with stock information, plot all columns. Return a figure. Intended to call show() on this figure later.
        :param path: str: path to file.
        :return:
        '''
        dataFrame: DataFrame = pd.read_csv(path)
        column_header: DataFrame = dataFrame.loc[:, dataFrame.columns != 'Date']
        fig: Figure = go.Figure()
        for header in column_header:
            fig.add_trace(go.Scatter(x=dataFrame['Date'], y=dataFrame[header], name=header, mode='lines'))

        fig.update_layout(yaxis_type="log", title=f"{path.split('/')[:-1]} price")
        return fig

    def getPaths(selfs, configPath: str = '/home/khoa/Documents/plotting.python/config.json', extension:str = ".csv"):
        '''
        Read config file for the path of yahoo data, then file fully qualified paths to those files.
        :param configPath:
        :param extension:
        :return:
        '''
        paths:[]=[]
        with json.loads(configPath) as configDict:
            fileList: [] = []
            for path, name, fileNames in os.walk(configDict["paths"]["data"] + configDict["paths"]["yahooData"]):
                for file in fileNames:
                    if extension in file:
                        paths.append(os.path.join(r, file))
        return paths

