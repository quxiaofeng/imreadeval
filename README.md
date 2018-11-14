`imreadeval` is a package to evaluate the performance of various python `imread` functions from different packages.

## Install

`pip install imreadeval`

PS. If you use `anaconda`, please install dependencies before `pip install`. The default dependency install is `pip` based.

## Packages Evaluated

- Pillow
- OpenCV
- Matplotlib
- imageio (descendent of `scipy.io.imread`, which is deprecated)
- SciKit-Image (depend on SciPy)

## Usage

Just evaluate 

`import imreadeval`

or just import a fastest `imread` function by

`from imreadeval import imread`

or try to evaluate different `imread` functions using YOUR OWN IMAGES

`from imreadeval import imread_eval`

`optimum_package_name = imread_eval(filenames = ['filename1.jpg', 'filename2.png'], times = 1000)`

## Develop

1. `git clone` the repo `git@github.com:quxiaofeng/imreadeval.git`
2. `pip install -e .`
3. `python -c "import imreadeval"`
