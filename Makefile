PROJECT_NAME = ticfortoe_dash
install:
	virtualenv ve_ticfortoe_dash
	ve_ticfortoe_dash/bin/pip install IPython
	ve_ticfortoe_dash/bin/pip install -e .
upload_test_pypi:
	rm -rf dist || True
	python setup.py sdist
	twine -r testpypi dist/* 
upload_pypi:
	rm -rf dist || True
	python setup.py sdist
	twine upload dist/*
py:
	ve_ticfortoe_dash/bin/ipython
run:
	ve_ticfortoe_dash/bin/python bin/run.py
