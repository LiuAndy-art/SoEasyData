import seaborn as sns
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def GetSeabornData(dataname):
    """
    这是一个获取Seaborn自带数据集函数的文档字符串。

    参数:
    dataname (str): 数据集名称{"anagrams", "anscombe", "attention", "brain_networks", "car_crashes", "diamonds", "dots", "dowjones", "exercise", "flights", "fmri", "geyser", "glue", "healthexp", "iris", "mpg", "penguins", "planets", "seaice", "taxis", "tips", "titanic"}。

    返回:
    dataframe对象。

    示例:
    ===============================================================================0
    导入模块
    >>> import sys
    >>> sys.path.append(r"D:\document\statistics\TidyStatsProject")
    >>> from SoEasyData import GetSeabornData
    ===============================================================================1
    测试各种数据获取
    ===============================================================================2
    >>> df = GetSeabornData("anagrams")
    >>> print(df.head())
    ===============================================================================3
    >>> df = GetSeabornData("anscombe")
    >>> print(df.head())
    ===============================================================================4
    >>> df = GetSeabornData("attention")
    >>> print(df.head())
    ===============================================================================5
    >>> df = GetSeabornData("brain_networks")
    >>> print(df.head())
    ===============================================================================6
    >>> df = GetSeabornData("car_crashes")
    >>> print(df.head())
    ===============================================================================7
    >>> df = GetSeabornData("diamonds")
    >>> print(df.head())
    ===============================================================================8
    >>> df = GetSeabornData("dots")
    >>> print(df.head())
    ===============================================================================9
    >>> df = GetSeabornData("dowjones")
    >>> print(df.head())
    ===============================================================================10
    >>> df = GetSeabornData("exercise")
    >>> print(df.head())
    ===============================================================================11
    >>> df = GetSeabornData("flights")
    >>> print(df.head())
    ===============================================================================12
    >>> df = GetSeabornData("fmri")
    >>> print(df.head())
    ===============================================================================13
    >>> df = GetSeabornData("geyser")
    >>> print(df.head())
    ===============================================================================14
    >>> df = GetSeabornData("glue")
    >>> print(df.head())
    ===============================================================================15
    >>> df = GetSeabornData("healthexp")
    >>> print(df.head())
    ===============================================================================16
    >>> df = GetSeabornData("iris")
    >>> print(df.head())
    ===============================================================================17
    >>> df = GetSeabornData("mpg")
    >>> print(df.head())
    ===============================================================================18
    >>> df = GetSeabornData("penguins")
    >>> print(df.head())
    ===============================================================================19
    >>> df = GetSeabornData("planets")
    >>> print(df.head())
    ===============================================================================20
    >>> df = GetSeabornData("seaice")
    >>> print(df.head())
    ===============================================================================21
    >>> df = GetSeabornData("taxis")
    >>> print(df.head())
    ===============================================================================22
    >>> df = GetSeabornData("tips")
    >>> print(df.head())
    ===============================================================================23
    >>> df = GetSeabornData("titanic")
    >>> print(df.head())
    ===============================================================================24
    """
    df = sns.load_dataset(dataname)
    return df
