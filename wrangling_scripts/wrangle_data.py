import pandas as pd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def generateWeatherTable():
    df = pd.read_csv('data/weatherAUS.csv')
    dfTemperature = df[['MinTemp', 'MaxTemp']]
    dfDates = df["Date"].str.split("-", n = 2, expand = True)
    dfWeather = pd.concat([dfDates, dfTemperature], axis=1).rename(columns={0: 'Year', 1:'Month', 2:'Day'})
    dfWeather = dfWeather.dropna()
    return dfWeather
	
def AusWeatherByMonths(df) :
    return df.groupby(['Month']).mean().rename(index={'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August','09': 'September', '10': 'October', '11': 'November', '12': 'December'})
	
def AusWeatherByYear(df):
    return df.groupby(['Year']).mean()

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots arable land from 1990 to 2015 in top 10 economies 
    # as a line chart

    df = generateWeatherTable()
    dfWatherMonths = AusWeatherByMonths(df)
    dfWatherYear = AusWeatherByYear(df)
	
    graph_one = []
    graph_one.append(
      go.Scatter(
      x = list(dfWatherMonths.index),
      y = list(dfWatherMonths["MinTemp"]),
      mode = 'lines'
      )
    )

    layout_one = dict(title = 'Minimum Temperature per Month',
                xaxis = dict(title = 'Months'),
                yaxis = dict(title = 'Temperature'),
                )

# second chart plots ararble land for 2015 as a bar chart    
    graph_two = []

    graph_two.append(
      go.Scatter(
      x = list(dfWatherMonths.index),
      y = list(dfWatherMonths["MaxTemp"]),
	  mode = 'lines'
      )
    )

    layout_two = dict(title = 'Maximum Temperature per Month',
                xaxis = dict(title = 'Months',),
                yaxis = dict(title = 'Temperature'),
                )


# third chart plots percent of population that is rural from 1990 to 2015
    graph_three = []
    graph_three.append(
      go.Scatter(
      x = list(dfWatherYear.index),
      y = list(dfWatherYear["MinTemp"]),
	  mode = 'lines'
      )
    )

    layout_three = dict(title = 'Minimum Temperature per Year',
                xaxis = dict(title = 'Years'),
                yaxis = dict(title = 'Temperature')
                       )
    
# fourth chart shows rural population vs arable land
    graph_four = []
    
    graph_four.append(
      go.Scatter(
      x = list(dfWatherYear.index),
      y = list(dfWatherYear["MaxTemp"]),
	  mode = 'lines'
      )
    )

    layout_four = dict(title = 'Maximum Temperature per Year',
                xaxis = dict(title = 'Years'),
                yaxis = dict(title = 'Temperature'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures