from setuptools import setup, find_packages

setup(name='adform',
      version='0.1dev',
      description='Unofficial AdForm.com REST API client.',
      url='https://github.com/dutkiewicz/adform-api/',
      author='Dawid Dutkiewicz',
      author_email='dawid.dutkiewicz@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'requests==2.20.0'
      ],
      python_requires='>=3')
