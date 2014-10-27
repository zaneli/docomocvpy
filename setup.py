from setuptools import setup, find_packages


setup(
    name='docomocvpy',
    version='0.0.1',
    description="docomo computer vision API Python wrapper library",
    author='Shunsuke Ohtani',
    author_email='shun.otani@gmail.com',
    url='https://github.com/zaneli/docomocvpy',
    install_requires=[
      'requests'
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
)
