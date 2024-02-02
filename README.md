# SoEasyData
快速获取数据

## 安装

```
pip install SoEasyData
```

## 获取机器学习数据

```python
# 导入模块
>>> from SoEasyData import GetMLData
>>> df, _ = GetMLData(45027)
>>> print(df.head())
>>> print(_)
>>> df, _ = GetMLData(31)
>>> print(df.head())
>>> print(_)
```

## 获取R数据集

```python
>>> from SoEasyData import GetRData
>>> df, _ = GetRData("women", "datasets")
>>> print(df.head())
>>> print(_)
>>> df, _ = GetRData("Arrests", "carData")
>>> print(df.head())
>>> print(_)
```

## 获取Stata数据集

```python
>>> from SoEasyData import GetStataData
>>> df = GetStataData("auto")
>>> print(df.head())
>>> df = GetStataData("sat")
>>> print(df.head())
```

## 获取Statsmodel自带数据集

```python
>>> from SoEasyData import GetStatsmodelData
>>> df, _ = GetStatsmodelData("anes96")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("cancer")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("ccard")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("china_smoking")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("co2")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("committee")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("copper")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("cpunish")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("danish_data")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("elnino")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("engel")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("fair")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("fertility")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("grunfeld")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("heart")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("interest_inflation")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("longley")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("macrodata")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("modechoice")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("nile")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("randhie")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("scotland")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("spector")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("stackloss")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("star98")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("statecrime")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("strikes")
>>> print(df.head())
>>> df, _ = GetStatsmodelData("sunspots")
>>> print(df.head())
```

## 获取Seaborn自带数据集

```python
>>> from SoEasyData import GetSeabornData
>>> df = GetSeabornData("anagrams")
>>> print(df.head())
>>> df = GetSeabornData("anscombe")
>>> print(df.head())
>>> df = GetSeabornData("attention")
>>> print(df.head())
>>> df = GetSeabornData("brain_networks")
>>> print(df.head())
>>> df = GetSeabornData("car_crashes")
>>> print(df.head())
>>> df = GetSeabornData("diamonds")
>>> print(df.head())
>>> df = GetSeabornData("dots")
>>> print(df.head())
>>> df = GetSeabornData("dowjones")
>>> print(df.head())
>>> df = GetSeabornData("exercise")
>>> print(df.head())
>>> df = GetSeabornData("flights")
>>> print(df.head())
>>> df = GetSeabornData("fmri")
>>> print(df.head())
>>> df = GetSeabornData("geyser")
>>> print(df.head())
>>> df = GetSeabornData("glue")
>>> print(df.head())
>>> df = GetSeabornData("healthexp")
>>> print(df.head())
>>> df = GetSeabornData("iris")
>>> print(df.head())
>>> df = GetSeabornData("mpg")
>>> print(df.head())
>>> df = GetSeabornData("penguins")
>>> print(df.head())
>>> df = GetSeabornData("planets")
>>> print(df.head())
>>> df = GetSeabornData("seaice")
>>> print(df.head())
>>> df = GetSeabornData("taxis")
>>> print(df.head())
>>> df = GetSeabornData("tips")
>>> print(df.head())
>>> df = GetSeabornData("titanic")
>>> print(df.head())
```

