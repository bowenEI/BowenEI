---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "pandas 基本运算"
linktitle: "pandas 基本运算"
date: 2022-03-04T11:07:16+08:00
type: book
summary: ""
weight: 35
---

<!--more-->


```python
import pandas as pd
import numpy as np
```

## 算术运算


```python
df1 = pd.DataFrame(np.random.randn(10, 4), columns=["A", "B", "C", "D"])
df1
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
      <th>0</th>
      <td>-0.039197</td>
      <td>-1.345397</td>
      <td>1.231152</td>
      <td>-1.209577</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.146425</td>
      <td>-0.126034</td>
      <td>0.049097</td>
      <td>-0.239117</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.736525</td>
      <td>0.855204</td>
      <td>1.039200</td>
      <td>-1.544436</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.644882</td>
      <td>-0.139244</td>
      <td>-1.548867</td>
      <td>-1.893190</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.763529</td>
      <td>0.350332</td>
      <td>-1.290519</td>
      <td>-0.030608</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.523727</td>
      <td>1.005206</td>
      <td>-0.268476</td>
      <td>-0.352177</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.667456</td>
      <td>-0.197137</td>
      <td>1.710659</td>
      <td>0.412051</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-1.872084</td>
      <td>-1.234837</td>
      <td>1.196401</td>
      <td>-0.333764</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.390396</td>
      <td>2.459068</td>
      <td>-0.255654</td>
      <td>-2.184972</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2.191920</td>
      <td>0.195064</td>
      <td>-0.233379</td>
      <td>1.106590</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame(np.random.randn(7, 3), columns=["A", "B", "C"])
df2
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
      <th>0</th>
      <td>-0.879968</td>
      <td>-0.381367</td>
      <td>1.288975</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.088425</td>
      <td>0.211976</td>
      <td>0.194757</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.980227</td>
      <td>-0.040865</td>
      <td>0.656159</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.987874</td>
      <td>-0.978989</td>
      <td>-0.742291</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.859827</td>
      <td>-0.987786</td>
      <td>2.217203</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-1.377002</td>
      <td>-0.866408</td>
      <td>-0.615638</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.754354</td>
      <td>0.127508</td>
      <td>-0.240242</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 * 5 + 2
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
      <th>0</th>
      <td>1.804017</td>
      <td>-4.726986</td>
      <td>8.155758</td>
      <td>-4.047884</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.267876</td>
      <td>1.369828</td>
      <td>2.245483</td>
      <td>0.804413</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.682623</td>
      <td>6.276020</td>
      <td>7.195998</td>
      <td>-5.722179</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1.224408</td>
      <td>1.303778</td>
      <td>-5.744335</td>
      <td>-7.465951</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.817644</td>
      <td>3.751659</td>
      <td>-4.452595</td>
      <td>1.846959</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4.618635</td>
      <td>7.026031</td>
      <td>0.657621</td>
      <td>0.239117</td>
    </tr>
    <tr>
      <th>6</th>
      <td>10.337280</td>
      <td>1.014315</td>
      <td>10.553293</td>
      <td>4.060255</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-7.360419</td>
      <td>-4.174187</td>
      <td>7.982006</td>
      <td>0.331182</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3.951981</td>
      <td>14.295340</td>
      <td>0.721729</td>
      <td>-8.924858</td>
    </tr>
    <tr>
      <th>9</th>
      <td>12.959601</td>
      <td>2.975322</td>
      <td>0.833105</td>
      <td>7.532952</td>
    </tr>
  </tbody>
</table>
</div>




```python
1 / df1
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
      <th>0</th>
      <td>-25.512380</td>
      <td>-0.743275</td>
      <td>0.812248</td>
      <td>-0.826735</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-6.829445</td>
      <td>-7.934342</td>
      <td>20.368024</td>
      <td>-4.182045</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.357728</td>
      <td>1.169312</td>
      <td>0.962279</td>
      <td>-0.647486</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1.550672</td>
      <td>-7.181613</td>
      <td>-0.645633</td>
      <td>-0.528209</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.309708</td>
      <td>2.854436</td>
      <td>-0.774882</td>
      <td>-32.671034</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1.909392</td>
      <td>0.994821</td>
      <td>-3.724730</td>
      <td>-2.839484</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.599716</td>
      <td>-5.072613</td>
      <td>0.584570</td>
      <td>2.426885</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-0.534164</td>
      <td>-0.809823</td>
      <td>0.835840</td>
      <td>-2.996133</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2.561500</td>
      <td>0.406658</td>
      <td>-3.911533</td>
      <td>-0.457672</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.456221</td>
      <td>5.126510</td>
      <td>-4.284876</td>
      <td>0.903677</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 ** 4
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
      <th>0</th>
      <td>0.000002</td>
      <td>3.276439</td>
      <td>2.297451</td>
      <td>2.140591e+00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.000460</td>
      <td>0.000252</td>
      <td>0.000006</td>
      <td>3.269227e-03</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.294272</td>
      <td>0.534908</td>
      <td>1.166261</td>
      <td>5.689568e+00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.172950</td>
      <td>0.000376</td>
      <td>5.755149</td>
      <td>1.284627e+01</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.339861</td>
      <td>0.015063</td>
      <td>2.773688</td>
      <td>8.777048e-07</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.075235</td>
      <td>1.020988</td>
      <td>0.005195</td>
      <td>1.538303e-02</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7.730677</td>
      <td>0.001510</td>
      <td>8.563543</td>
      <td>2.882727e-02</td>
    </tr>
    <tr>
      <th>7</th>
      <td>12.282908</td>
      <td>2.325086</td>
      <td>2.048836</td>
      <td>1.240955e-02</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.023229</td>
      <td>36.566391</td>
      <td>0.004272</td>
      <td>2.279204e+01</td>
    </tr>
    <tr>
      <th>9</th>
      <td>23.083358</td>
      <td>0.001448</td>
      <td>0.002967</td>
      <td>1.499503e+00</td>
    </tr>
  </tbody>
</table>
</div>



## 布尔运算


```python
df1 = pd.DataFrame({"a": [1, 0, 1], "b": [0, 1, 1]}, dtype=bool)
df1
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
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame({"a": [0, 1, 1], "b": [1, 1, 0]}, dtype=bool)
df2
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
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 & df2
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
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 | df2
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
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 ^ df2
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
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
-df1
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
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>

