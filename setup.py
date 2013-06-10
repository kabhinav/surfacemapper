
try:
    from setuptools import setup, find_packages
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

depends_upon = [
    'nose',
    'nosexcover',
    'coverage',
    'mock',
    'yanc',
]

setup(
    name = 'surfacemapper',
    version = '1.0',
    packages = find_packages(exclude=["tests"]),
    setup_requires = depends_upon,
    install_requires = depends_upon,
    test_suite = "nose.collector",
    entry_points = {
        'console_scripts': [
            'surfacemapper = surfacemapper.mapper:main',
            ],
        },
    description = 'Rovers squad for mapping Martian surface.',
)
