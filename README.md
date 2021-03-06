# Wildebeest

[![cicd](https://github.com/ShopRunner/wildebeest/workflows/Python%20package/badge.svg
)](https://github.com/ShopRunner/wildebeest/actions?query=workflow%3A%22Python+package%22+branch%3Amaster)
[![codecov](https://codecov.io/gh/ShopRunner/wildebeest/branch/master/graph/badge.svg)](https://codecov.io/gh/ShopRunner/wildebeest)

![wildebeest stampede](https://github.com/ShopRunner/wildebeest/raw/master/docs/images/wildebeest_stampede.jpg)

Wildebeest is a file processing framework. It is designed for IO-bound workflows that involve reading files into memory, processing their contents, and writing out the results. It makes running those workflows faster and more reliable by parallelizing across files, handling errors, making it easy to skip files that have already been processed, and keeping organized records of what was done.

Wildebeest was developed for deep learning computer vision projects, so in addition to the general framework it also provides predefined components for image processing. However, it can be used for any project that involves processing data from many sources.

See [the docs](https://wildebeest-library.readthedocs.io/en/latest/) for more details.

Wildebeest was known as Creevey until version 3.0.0.
