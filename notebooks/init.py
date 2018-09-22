import IPython.display
import pyspark
import pyspark.sql.functions as F
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker

# Show a bit more of content
pd.set_option('display.max_colwidth', 100)

def display(object, n=10):
    if type(object) == pyspark.sql.dataframe.DataFrame:
        IPython.display.display(convert_to_pandas(object, n))
    else:
        IPython.display.display(object)


def convert_to_pandas(df, n):
    # Unbork decimal types
    for column in df.columns:
        if isinstance(df.schema[column].dataType, pyspark.sql.types.DecimalType):
            df = df.withColumn(column, F.expr(column).cast("int"))

    return df.limit(n).toPandas()

@ticker.FuncFormatter
def log_formatter(x, pos):
    return "$10^{%s}$" % x

def plot(self, x=None, y=None, kind="scatter", hue=None, n=100000, logx=False, logy=False, norm_hist=False):
    df = convert_to_pandas(self.cache(), n)

    if kind == "scatter":
        grid = sns.scatterplot(x=x, y=y, hue=hue, data=df)
    elif kind == "line":
        grid = sns.lineplot(x=x, y=y, hue=hue, data=df)
    elif kind == "hist":
        series = df[x]
        if logx:
            series = np.log10(series[series > 0.0])
        
        grid = sns.distplot(series, kde=False,  norm_hist=norm_hist)
        if logx:
            grid.xaxis.set_major_formatter(log_formatter)
    else:
        raise ValueError("kind should be one of: scatter, line, hist")

    if logx and not kind == "hist":
        grid.set(xscale="log")
    if logy:
        grid.set(yscale="log")

    return grid

# Horrible, horrible monkey patching
pyspark.sql.dataframe.DataFrame.plot = plot
