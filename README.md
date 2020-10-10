`imreadeval` is a package to evaluate the performance of various python `imread` functions from different packages.

## Install

`pip install imreadeval`

PS. If you use `anaconda`, please install dependencies before `pip install`. The default dependency install is `pip` based.

## Packages Evaluated

- Pillow https://github.com/python-pillow/Pillow
- OpenCV https://github.com/opencv/opencv
- Matplotlib https://github.com/matplotlib/matplotlib
- imageio (descendent of `scipy.io.imread`, which is deprecated) https://github.com/imageio/imageio
- SciKit-Image (depend on SciPy) https://github.com/scikit-image/scikit-image
- imread https://github.com/luispedro/imread

## Usage

Just evaluate `import imreadeval`, then all imread packages installed will be tested, and the fastest one shows.

> In [1]: import imreadeval
> INFO:root:      `imread` performance test:
> INFO:root:              Pillow time: 0.8008584999999995.
> INFO:root:              OpenCV is not installed.
> INFO:root:              Matplotlib time: 0.8844109000000007.
> INFO:root:              imageio time: 0.9442649999999997.
> INFO:root:              SciKit-Image time: 0.9424957000000003.
> INFO:root:              imread is not installed.
> INFO:root:                      Pillow is the fastest.

Or just import a fastest `imread` function by `from imreadeval import imread`.

> In [1]: import imreadeval
> INFO:root:      `imread` performance test:
> INFO:root:              Pillow time: 0.8008584999999995.
> INFO:root:              OpenCV is not installed.
> INFO:root:              Matplotlib time: 0.8844109000000007.
> INFO:root:              imageio time: 0.9442649999999997.
> INFO:root:              SciKit-Image time: 0.9424957000000003.
> INFO:root:              imread is not installed.
> INFO:root:                      Pillow is the fastest.
> 
> In [2]: x = imread('imreadeval/images/clouds.png')
> 

or try to evaluate different `imread` functions using YOUR OWN IMAGES by

`from imreadeval import imread_eval`

`optimum_package_name = imread_eval(filenames = ['filename1.jpg', 'filename2.png'], times = 1000)`

## Develop

1. `git clone` the repo `git@github.com:quxiaofeng/imreadeval.git`
2. `pip install -e .`
3. `python -c "import imreadeval"`

## Acknowledgement

This package is done during my work hours in both [LUMI United](https://www.aqara.com/en/home.html) and [Tsinghua University, Graduate School at Shenzhen](http://www.sz.tsinghua.edu.cn/enhtml/index.html). Thanks for the kind arrangement.
