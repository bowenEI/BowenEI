---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "索引和选择"
linktitle: "索引和选择"
date: 2022-02-19T11:14:00+08:00
type: book
summary: ""
weight: 30
---

<!--more-->


```python
import pandas as pd
import numpy as np
```

## 概述

**pandas** 索引和选择的操作主要是以下五种：

| 操作               | 语法            | Result    |
| ------------------ | --------------- | --------- |
| 选择列             | `df[col]`       | Series    |
| 通过标签选择行     | `df.loc[label]` | Series    |
| 通过整数下标选择行 | `df.iloc[loc]`  | Series    |
| 行切片             | `df[5:10]`      | DataFrame |
| 通过布尔向量切片   | `df[bool_vec]`  | DataFrame |


```python
df = pd.DataFrame(np.random.randn(4, 5), index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D', 'E'])
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>2.251822</td>
      <td>0.508078</td>
      <td>0.296828</td>
      <td>-1.223630</td>
      <td>0.523225</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1.169537</td>
      <td>1.378697</td>
      <td>0.956192</td>
      <td>-0.761983</td>
      <td>1.206156</td>
    </tr>
    <tr>
      <th>c</th>
      <td>-1.071012</td>
      <td>0.117104</td>
      <td>-1.068820</td>
      <td>0.443776</td>
      <td>-1.185699</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.276478</td>
      <td>0.013506</td>
      <td>-0.207837</td>
      <td>-0.295314</td>
      <td>0.402572</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['B']
```




    a    0.508078
    b    1.378697
    c    0.117104
    d    0.013506
    Name: B, dtype: float64




```python
df[['B', 'C']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0.508078</td>
      <td>0.296828</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1.378697</td>
      <td>0.956192</td>
    </tr>
    <tr>
      <th>c</th>
      <td>0.117104</td>
      <td>-1.068820</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.013506</td>
      <td>-0.207837</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc['d']
```




    A    0.276478
    B    0.013506
    C   -0.207837
    D   -0.295314
    E    0.402572
    Name: d, dtype: float64




```python
df.iloc[0]
```




    A    2.251822
    B    0.508078
    C    0.296828
    D   -1.223630
    E    0.523225
    Name: a, dtype: float64




```python
df[:-1]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>2.251822</td>
      <td>0.508078</td>
      <td>0.296828</td>
      <td>-1.223630</td>
      <td>0.523225</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1.169537</td>
      <td>1.378697</td>
      <td>0.956192</td>
      <td>-0.761983</td>
      <td>1.206156</td>
    </tr>
    <tr>
      <th>c</th>
      <td>-1.071012</td>
      <td>0.117104</td>
      <td>-1.068820</td>
      <td>0.443776</td>
      <td>-1.185699</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[:2] > 0
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>b</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df < 0] = 0
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>2.251822</td>
      <td>0.508078</td>
      <td>0.296828</td>
      <td>0.000000</td>
      <td>0.523225</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1.169537</td>
      <td>1.378697</td>
      <td>0.956192</td>
      <td>0.000000</td>
      <td>1.206156</td>
    </tr>
    <tr>
      <th>c</th>
      <td>0.000000</td>
      <td>0.117104</td>
      <td>0.000000</td>
      <td>0.443776</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.276478</td>
      <td>0.013506</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.402572</td>
    </tr>
  </tbody>
</table>
</div>



## 使用 [] 进行索引

使用 `[]` 进行索引，实际上就是选择低维切片。对于 Series 对象和 DataFrame 对象，`[]` 返回的类型不同。

| 对象类型  | 调用方法         | 返回值类型                 |
| --------- | ---------------- | -------------------------- |
| Series    | `series[label]`  | 标量值                     |
| DataFrame | `frame[colname]` | 对应 `colname` 的 `Series` |


```python
dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4),
                  index=dates, columns=['A', 'B', 'C', 'D'])
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>-0.245083</td>
      <td>-1.422116</td>
      <td>0.607832</td>
      <td>1.303857</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>0.596950</td>
      <td>-0.232929</td>
      <td>-1.116721</td>
      <td>-1.387045</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.096937</td>
      <td>-1.016238</td>
      <td>0.547761</td>
      <td>-0.629623</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-0.538159</td>
      <td>1.512869</td>
      <td>0.694778</td>
      <td>0.561185</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>-1.338459</td>
      <td>1.352126</td>
      <td>1.203392</td>
      <td>-0.431008</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-0.525117</td>
      <td>0.735395</td>
      <td>0.562011</td>
      <td>-0.133187</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-0.076509</td>
      <td>0.542937</td>
      <td>0.047262</td>
      <td>0.512984</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>-1.047306</td>
      <td>0.812662</td>
      <td>1.716307</td>
      <td>-0.060350</td>
    </tr>
  </tbody>
</table>
</div>




```python
s = df['A']
s
```




    2000-01-01   -0.245083
    2000-01-02    0.596950
    2000-01-03   -0.096937
    2000-01-04   -0.538159
    2000-01-05   -1.338459
    2000-01-06   -0.525117
    2000-01-07   -0.076509
    2000-01-08   -1.047306
    Freq: D, Name: A, dtype: float64




```python
s[dates[5]]
```




    -0.5251169095699432



交换 `A` 和 `B` 两列：


```python
df[['B', 'A']] = df[['A', 'B']]
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>-1.422116</td>
      <td>-0.245083</td>
      <td>0.607832</td>
      <td>1.303857</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-0.232929</td>
      <td>0.596950</td>
      <td>-1.116721</td>
      <td>-1.387045</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-1.016238</td>
      <td>-0.096937</td>
      <td>0.547761</td>
      <td>-0.629623</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>1.512869</td>
      <td>-0.538159</td>
      <td>0.694778</td>
      <td>0.561185</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>1.352126</td>
      <td>-1.338459</td>
      <td>1.203392</td>
      <td>-0.431008</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.735395</td>
      <td>-0.525117</td>
      <td>0.562011</td>
      <td>-0.133187</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>0.542937</td>
      <td>-0.076509</td>
      <td>0.047262</td>
      <td>0.512984</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.812662</td>
      <td>-1.047306</td>
      <td>1.716307</td>
      <td>-0.060350</td>
    </tr>
  </tbody>
</table>
</div>



注意，如果使用了 `loc` 或者 `iloc`，**pandas** 会先对齐所有 `axes`。这不会修改 `df`，因为列对齐在赋值之前。


```python
df.loc[:, ['B', 'A']] = df[['A', 'B']]
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>-1.422116</td>
      <td>-0.245083</td>
      <td>0.607832</td>
      <td>1.303857</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-0.232929</td>
      <td>0.596950</td>
      <td>-1.116721</td>
      <td>-1.387045</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-1.016238</td>
      <td>-0.096937</td>
      <td>0.547761</td>
      <td>-0.629623</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>1.512869</td>
      <td>-0.538159</td>
      <td>0.694778</td>
      <td>0.561185</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>1.352126</td>
      <td>-1.338459</td>
      <td>1.203392</td>
      <td>-0.431008</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.735395</td>
      <td>-0.525117</td>
      <td>0.562011</td>
      <td>-0.133187</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>0.542937</td>
      <td>-0.076509</td>
      <td>0.047262</td>
      <td>0.512984</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.812662</td>
      <td>-1.047306</td>
      <td>1.716307</td>
      <td>-0.060350</td>
    </tr>
  </tbody>
</table>
</div>



可以强转成 `ndarray` 数组来实现这一操作：


```python
df.loc[:, ['B', 'A']] = df[['A', 'B']].to_numpy()
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>-0.245083</td>
      <td>-1.422116</td>
      <td>0.607832</td>
      <td>1.303857</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>0.596950</td>
      <td>-0.232929</td>
      <td>-1.116721</td>
      <td>-1.387045</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.096937</td>
      <td>-1.016238</td>
      <td>0.547761</td>
      <td>-0.629623</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-0.538159</td>
      <td>1.512869</td>
      <td>0.694778</td>
      <td>0.561185</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>-1.338459</td>
      <td>1.352126</td>
      <td>1.203392</td>
      <td>-0.431008</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-0.525117</td>
      <td>0.735395</td>
      <td>0.562011</td>
      <td>-0.133187</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-0.076509</td>
      <td>0.542937</td>
      <td>0.047262</td>
      <td>0.512984</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>-1.047306</td>
      <td>0.812662</td>
      <td>1.716307</td>
      <td>-0.060350</td>
    </tr>
  </tbody>
</table>
</div>



### 切片

切片的规则和 **Python** 以及 **NumPy** 中的切片规则，一样。这里用 `[]` 运算符说明切片的语义。


```python
s = pd.Series(np.random.randn(7), index=list('abcdefg'))
s
```




    a   -0.430408
    b    1.192773
    c    0.110207
    d    0.252352
    e   -0.126190
    f    0.684152
    g   -0.330652
    dtype: float64




```python
s[:5]
```




    a   -0.430408
    b    1.192773
    c    0.110207
    d    0.252352
    e   -0.126190
    dtype: float64




```python
s[::2]
```




    a   -0.430408
    c    0.110207
    e   -0.126190
    g   -0.330652
    dtype: float64




```python
s[::-1]
```




    g   -0.330652
    f    0.684152
    e   -0.126190
    d    0.252352
    c    0.110207
    b    1.192773
    a   -0.430408
    dtype: float64




```python
s[:3] = 0
s
```




    a    0.000000
    b    0.000000
    c    0.000000
    d    0.252352
    e   -0.126190
    f    0.684152
    g   -0.330652
    dtype: float64




```python
df = pd.DataFrame(np.random.randn(3, 4), index=list('abc'), columns=list('ABCD'))
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0.967130</td>
      <td>0.642469</td>
      <td>-0.327055</td>
      <td>-0.760568</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0.435906</td>
      <td>-0.498920</td>
      <td>0.411437</td>
      <td>-1.726552</td>
    </tr>
    <tr>
      <th>c</th>
      <td>0.793539</td>
      <td>-0.507760</td>
      <td>0.167797</td>
      <td>-1.432030</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[:2]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0.967130</td>
      <td>0.642469</td>
      <td>-0.327055</td>
      <td>-0.760568</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0.435906</td>
      <td>-0.498920</td>
      <td>0.411437</td>
      <td>-1.726552</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[::-1]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>c</th>
      <td>0.793539</td>
      <td>-0.507760</td>
      <td>0.167797</td>
      <td>-1.432030</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0.435906</td>
      <td>-0.498920</td>
      <td>0.411437</td>
      <td>-1.726552</td>
    </tr>
    <tr>
      <th>a</th>
      <td>0.967130</td>
      <td>0.642469</td>
      <td>-0.327055</td>
      <td>-0.760568</td>
    </tr>
  </tbody>
</table>
</div>



## 通过属性索引


```python
s = pd.Series([1, 2, 3], index=list('abc'))
s
```


```python
s.b
```




    2




```python
df = pd.DataFrame(np.random.randn(3, 4), index=list('abc'), columns=list('ABCD'))
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0.967130</td>
      <td>0.642469</td>
      <td>-0.327055</td>
      <td>-0.760568</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0.435906</td>
      <td>-0.498920</td>
      <td>0.411437</td>
      <td>-1.726552</td>
    </tr>
    <tr>
      <th>c</th>
      <td>0.793539</td>
      <td>-0.507760</td>
      <td>0.167797</td>
      <td>-1.432030</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.A
```




    a    0.967130
    b    0.435906
    c    0.793539
    Name: A, dtype: float64




```python
df.A = list(range(len(df.index)))
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0</td>
      <td>0.642469</td>
      <td>-0.327055</td>
      <td>-0.760568</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1</td>
      <td>-0.498920</td>
      <td>0.411437</td>
      <td>-1.726552</td>
    </tr>
    <tr>
      <th>c</th>
      <td>2</td>
      <td>-0.507760</td>
      <td>0.167797</td>
      <td>-1.432030</td>
    </tr>
  </tbody>
</table>
</div>



采用访问属性的方法必须确保该属性存在。如果要创建新的一列，仍然需要通过 `[]`。否则，会出现 `UserWanring` 的警告。


```python
df['E'] = list(range(len(df.index)))
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0</td>
      <td>0.642469</td>
      <td>-0.327055</td>
      <td>-0.760568</td>
      <td>0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1</td>
      <td>-0.498920</td>
      <td>0.411437</td>
      <td>-1.726552</td>
      <td>1</td>
    </tr>
    <tr>
      <th>c</th>
      <td>2</td>
      <td>-0.507760</td>
      <td>0.167797</td>
      <td>-1.432030</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



## 通过标签索引

使用 `loc` 方法可以使用标签对行进行索引。


```python
s = pd.Series(np.random.randn(6), index=list('abcdef'))
s
```




    a   -1.373748
    b    0.505333
    c    0.929577
    d    0.336673
    e    1.074367
    f   -1.375100
    dtype: float64




```python
s.loc['b']
```




    0.5053325199102856



标签支持冒号表达式，进行切片运算。


```python
s.loc['c':]
```




    c    0.929577
    d    0.336673
    e    1.074367
    f   -1.375100
    dtype: float64




```python
df = pd.DataFrame(np.random.randn(6, 4), index=list('abcdef'), columns=list('ABCD'))
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>-0.100191</td>
      <td>-0.129401</td>
      <td>0.976985</td>
      <td>1.839616</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1.158153</td>
      <td>0.662432</td>
      <td>1.278219</td>
      <td>-0.159460</td>
    </tr>
    <tr>
      <th>c</th>
      <td>0.650541</td>
      <td>-0.073285</td>
      <td>-1.377789</td>
      <td>0.122472</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.442271</td>
      <td>0.452595</td>
      <td>-1.274344</td>
      <td>-0.494543</td>
    </tr>
    <tr>
      <th>e</th>
      <td>0.536770</td>
      <td>-0.597499</td>
      <td>0.897752</td>
      <td>1.104886</td>
    </tr>
    <tr>
      <th>f</th>
      <td>1.488848</td>
      <td>1.195444</td>
      <td>1.394976</td>
      <td>1.760736</td>
    </tr>
  </tbody>
</table>
</div>



DataFrame 对象可以行列同时索引。


```python
df.loc[['a', 'b', 'd'], ['A', 'C']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>-0.100191</td>
      <td>0.976985</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1.158153</td>
      <td>1.278219</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.442271</td>
      <td>-1.274344</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc['d':, 'A':'C']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>d</th>
      <td>0.442271</td>
      <td>0.452595</td>
      <td>-1.274344</td>
    </tr>
    <tr>
      <th>e</th>
      <td>0.536770</td>
      <td>-0.597499</td>
      <td>0.897752</td>
    </tr>
    <tr>
      <th>f</th>
      <td>1.488848</td>
      <td>1.195444</td>
      <td>1.394976</td>
    </tr>
  </tbody>
</table>
</div>



注意：下面的切片不是下标切片，而是标签切片。因此，`3:5` 表示标签 `3` 和 `5` 之间的所有标签。`3` 和 `5` 之间还有一个标签 `2`，因此返回结果为：


```python
s = pd.Series(list('abcdef'), index=[0, 3, 2, 5, 4, 2])
s.loc[3:5]
```




    3    b
    2    c
    5    d
    dtype: object



## 通过下标位置索引

使用 `iloc` 方法可以通过下标位置进行索引。


```python
s = pd.Series(np.random.randn(5), index=list(range(0, 10, 2)))
s
```




    0   -0.235442
    2    1.504205
    4    0.917704
    6   -0.268698
    8    0.045323
    dtype: float64




```python
s.iloc[:3]
```




    0   -0.235442
    2    1.504205
    4    0.917704
    dtype: float64




```python
s.iloc[-1]
```




    0.04532252934053265




```python
df = pd.DataFrame(np.random.randn(6, 4),
                   index=list(range(0, 12, 2)),
                   columns=list(range(0, 8, 2)))
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>2</th>
      <th>4</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.342468</td>
      <td>0.198276</td>
      <td>-1.195844</td>
      <td>0.451696</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.025717</td>
      <td>0.077352</td>
      <td>-0.123052</td>
      <td>1.313708</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.137973</td>
      <td>0.373148</td>
      <td>-0.220029</td>
      <td>-0.683300</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.554065</td>
      <td>-0.518741</td>
      <td>-0.839679</td>
      <td>-0.599059</td>
    </tr>
    <tr>
      <th>8</th>
      <td>-0.585208</td>
      <td>1.001620</td>
      <td>0.162317</td>
      <td>-1.386377</td>
    </tr>
    <tr>
      <th>10</th>
      <td>-0.229306</td>
      <td>1.202411</td>
      <td>-0.456811</td>
      <td>0.110556</td>
    </tr>
  </tbody>
</table>
</div>



DataFrame 对象可以行列同时索引。


```python
df.iloc[:3]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>2</th>
      <th>4</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.342468</td>
      <td>0.198276</td>
      <td>-1.195844</td>
      <td>0.451696</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.025717</td>
      <td>0.077352</td>
      <td>-0.123052</td>
      <td>1.313708</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.137973</td>
      <td>0.373148</td>
      <td>-0.220029</td>
      <td>-0.683300</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[1:5, 2:4]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>4</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>-0.123052</td>
      <td>1.313708</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.220029</td>
      <td>-0.683300</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.839679</td>
      <td>-0.599059</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.162317</td>
      <td>-1.386377</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[[1, 3, 5], [1, 3]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>0.077352</td>
      <td>1.313708</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.518741</td>
      <td>-0.599059</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.202411</td>
      <td>0.110556</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[1:3, :]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>2</th>
      <th>4</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>-0.025717</td>
      <td>0.077352</td>
      <td>-0.123052</td>
      <td>1.313708</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.137973</td>
      <td>0.373148</td>
      <td>-0.220029</td>
      <td>-0.683300</td>
    </tr>
  </tbody>
</table>
</div>



可以超出索引范围，但是可能会返回空 DataFrame。


```python
df.iloc[:, 4:]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
    </tr>
    <tr>
      <th>2</th>
    </tr>
    <tr>
      <th>4</th>
    </tr>
    <tr>
      <th>6</th>
    </tr>
    <tr>
      <th>8</th>
    </tr>
    <tr>
      <th>10</th>
    </tr>
  </tbody>
</table>
</div>



## 选择接受可调用对象

`[]`、`loc` 和 `iloc` 都接受可调用对象进行索引。


```python
df = pd.DataFrame(np.random.randn(6, 4),
                   index=list('abcdef'),
                   columns=list('ABCD'))
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.444943</td>
      <td>-0.907930</td>
      <td>1.038214</td>
      <td>-2.246870</td>
    </tr>
    <tr>
      <th>b</th>
      <td>-1.602533</td>
      <td>-1.085308</td>
      <td>-1.039485</td>
      <td>0.574455</td>
    </tr>
    <tr>
      <th>c</th>
      <td>-0.705120</td>
      <td>0.563562</td>
      <td>1.281975</td>
      <td>1.127445</td>
    </tr>
    <tr>
      <th>d</th>
      <td>-1.860152</td>
      <td>-1.679263</td>
      <td>-1.071518</td>
      <td>0.127717</td>
    </tr>
    <tr>
      <th>e</th>
      <td>0.472768</td>
      <td>-0.563109</td>
      <td>-0.331930</td>
      <td>-1.279404</td>
    </tr>
    <tr>
      <th>f</th>
      <td>0.759632</td>
      <td>0.306537</td>
      <td>-0.342015</td>
      <td>-1.121230</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[lambda df: df['A'] > 0, :]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.444943</td>
      <td>-0.907930</td>
      <td>1.038214</td>
      <td>-2.246870</td>
    </tr>
    <tr>
      <th>e</th>
      <td>0.472768</td>
      <td>-0.563109</td>
      <td>-0.331930</td>
      <td>-1.279404</td>
    </tr>
    <tr>
      <th>f</th>
      <td>0.759632</td>
      <td>0.306537</td>
      <td>-0.342015</td>
      <td>-1.121230</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[:, lambda df: ['A', 'B']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.444943</td>
      <td>-0.907930</td>
    </tr>
    <tr>
      <th>b</th>
      <td>-1.602533</td>
      <td>-1.085308</td>
    </tr>
    <tr>
      <th>c</th>
      <td>-0.705120</td>
      <td>0.563562</td>
    </tr>
    <tr>
      <th>d</th>
      <td>-1.860152</td>
      <td>-1.679263</td>
    </tr>
    <tr>
      <th>e</th>
      <td>0.472768</td>
      <td>-0.563109</td>
    </tr>
    <tr>
      <th>f</th>
      <td>0.759632</td>
      <td>0.306537</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[:, lambda df: [0, 1]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.444943</td>
      <td>-0.907930</td>
    </tr>
    <tr>
      <th>b</th>
      <td>-1.602533</td>
      <td>-1.085308</td>
    </tr>
    <tr>
      <th>c</th>
      <td>-0.705120</td>
      <td>0.563562</td>
    </tr>
    <tr>
      <th>d</th>
      <td>-1.860152</td>
      <td>-1.679263</td>
    </tr>
    <tr>
      <th>e</th>
      <td>0.472768</td>
      <td>-0.563109</td>
    </tr>
    <tr>
      <th>f</th>
      <td>0.759632</td>
      <td>0.306537</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[lambda df: df.columns[0]]
```




    a    1.444943
    b   -1.602533
    c   -0.705120
    d   -1.860152
    e    0.472768
    f    0.759632
    Name: A, dtype: float64




```python
df['A'].loc[lambda s: s > 0]
```




    a    1.444943
    e    0.472768
    f    0.759632
    Name: A, dtype: float64



## 快速访问

由于使用 `[]` 进行索引必须处理很多情况（单标签访问、切片、布尔索引等），因此它需要一些开销才能确定您的要求。如果您只想访问一个标量值，最快的方法是使用 `at` 和 `iat` 方法，它们在所有数据结构上都实现了。


```python
s = pd.Series(np.random.randint(0, 7, size=(7,)), index=list('abcdefg'))
s
```




    a    1
    b    4
    c    5
    d    6
    e    0
    f    3
    g    3
    dtype: int32




```python
s.iat[5]
```




    3




```python
s.at['a']
```




    1




```python
df = pd.DataFrame(np.random.randint(0, 7, size=(3, 4)), index=list('abc'), columns=list('ABCD'))
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>3</td>
      <td>5</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>c</th>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iat[0, 1]
```




    5




```python
df.at['b', 'A']
```




    0



## 布尔索引

Series 对象的布尔索引和 **Python** 以及 **NumPy** 类似。


```python
s = pd.Series(range(-3, 4))
s
```




    0   -3
    1   -2
    2   -1
    3    0
    4    1
    5    2
    6    3
    dtype: int64




```python
s[s > 0]
```




    4    1
    5    2
    6    3
    dtype: int64




```python
s[(s < -1) | (s > 0.5)]
```




    0   -3
    1   -2
    4    1
    5    2
    6    3
    dtype: int64




```python
s[~(s < 0)]
```




    3    0
    4    1
    5    2
    6    3
    dtype: int64




```python
df = pd.DataFrame(np.random.randn(7, 4),
                  index=pd.date_range('2022/02/22', periods=7),
                  columns=list('ABCD'))
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-02-22</th>
      <td>-1.322987</td>
      <td>1.022325</td>
      <td>0.304516</td>
      <td>-0.281856</td>
    </tr>
    <tr>
      <th>2022-02-23</th>
      <td>-0.767053</td>
      <td>0.644011</td>
      <td>2.058071</td>
      <td>-0.342653</td>
    </tr>
    <tr>
      <th>2022-02-24</th>
      <td>0.065301</td>
      <td>2.530895</td>
      <td>1.091807</td>
      <td>1.865210</td>
    </tr>
    <tr>
      <th>2022-02-25</th>
      <td>-2.094778</td>
      <td>-0.714121</td>
      <td>0.319254</td>
      <td>-1.102402</td>
    </tr>
    <tr>
      <th>2022-02-26</th>
      <td>1.543428</td>
      <td>-1.073784</td>
      <td>-0.585543</td>
      <td>-1.479911</td>
    </tr>
    <tr>
      <th>2022-02-27</th>
      <td>-0.045216</td>
      <td>-1.291289</td>
      <td>0.145565</td>
      <td>0.124343</td>
    </tr>
    <tr>
      <th>2022-02-28</th>
      <td>-1.352934</td>
      <td>-1.934588</td>
      <td>0.214902</td>
      <td>-0.942982</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df['A'] > 0]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-02-24</th>
      <td>0.065301</td>
      <td>2.530895</td>
      <td>1.091807</td>
      <td>1.865210</td>
    </tr>
    <tr>
      <th>2022-02-26</th>
      <td>1.543428</td>
      <td>-1.073784</td>
      <td>-0.585543</td>
      <td>-1.479911</td>
    </tr>
  </tbody>
</table>
</div>


