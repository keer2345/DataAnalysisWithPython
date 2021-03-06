# Data Analysis with Python



# Environment Configuration

[My Emacs's Configuration](https://github.com/keer2345/keer-emacs/blob/master/lisp/lang-python.el)

- [Python environment with Pipenv, Jupyter, and EIN](https://matthewbilyeu.com/blog/python-environment-with-pipenv-jupyter-and-ein/)
- [emacs-ipython-notebook](https://github.com/millejoh/emacs-ipython-notebook)
- [Turning emacs into a Python IDE](https://gist.github.com/widdowquinn/987164746810f4e8b88402628b387d39#turning-emacs-into-a-python-ide)

## Jupyter Usage
[如何优雅地使用 Jupyter](https://www.zhihu.com/question/59392251)

Jupyter NBExtensions 的安装配置：
```
pip install jupyter_nbextensions_configurator jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
jupyter nbextensions_configurator enable --user
```

## EIN Usage
确保在 `python-mode` 模式下：
- `ein:jupyter-server-start` 启动之后在浏览器访问 http://localhost:8888/tree ，就可以看到 Jupyter 页面
- `ein:jupyter-server-stop`
- `ein:notebooklist-login` 登陆授权，以便后续操作
- `ein:notebook-open`

# Official Documentation
- [pandas](https://github.com/keer2345/DataAnalysisWithPython/tree/master/official-documentation/pandas)
- [Statsmodels](https://github.com/keer2345/DataAnalysisWithPython/tree/master/official-documentation/pandas)
- [Scikit-learn](https://scikit-learn.org/stable/index.html)


# 莫凡学Python系列
### [Morvan numpy & pandas](https://github.com/keer2345/DataAnalysisWithPython/tree/master/morvan-numpy-and-pandas)

# Deep Learning
- [_Scipy Lecture Notes_](https://github.com/keer2345/DataAnalysisWithPython/tree/master/ScipyLectureNotes)
    - [book](http://www.scipy-lectures.org/)
- [_Artificial Intelligence:Foundations-of-Computational-Agents_](https://github.com/keer2345/DataAnalysisWithPython/tree/master/Foundations-of-Computational-Agents)
- [_100-Days-Of-ML-Code_](https://github.com/keer2345/DataAnalysisWithPython/tree/master/100-Days-Of-ML-Code)
- [_Grokkng Deep Learning_](https://github.com/keer2345/DataAnalysisWithPython/tree/master/grokking-deep-learning)
    - [book](https://livebook.manning.com/#!/book/grokking-deep-learning/welcome/v-12/)


- [_Programming-Collective-Intelligence_](https://github.com/keer2345/DataAnalysisWithPython/tree/master/Programming-Collective-Intelligence)
- [_Data Science with Python and Dask_](https://github.com/keer2345/DataAnalysisWithPython/tree/master/Data-Science-with-Python-and-Dask)
- _Deep Learning_
- _Python for Data Analysis_
- _Hands-on Machine Learning with Scikit-Learn & TensorFlow_
- _The Hunderd-page Machine Learning Book_


# Github and Others
- [ujjwalkarn/DataSciencePython](https://github.com/keer2345/DataAnalysisWithPython/tree/master/ujjwalkarn-DataSciencePython)