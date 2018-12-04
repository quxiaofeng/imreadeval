rm build -rf
rm dist -rf
rm *.egg-info -rf
python2 setup.py sdist bdist_wheel && python3 setup.py sdist bdist_wheel && sudo twine upload dist/*