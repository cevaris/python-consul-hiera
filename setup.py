import consul_hiera
version = consul_hiera.__version__
readme = open('README.md').read()

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='consul_hiera',
    version=version,
    description="""Environment Variable and Settings Management via Consul""",
    long_description="""TODO""",
    author='Adam Cardenas',
    author_email='cevaris@gmail.com',
    url='https://github.com/cevaris/python-consul-hiera',
    packages=['consul_hiera',],
    include_package_data=True,
    install_requires=[
    ],
    license="MIT",
    zip_safe=False,
    keywords='consul_hiera',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        ],

)
