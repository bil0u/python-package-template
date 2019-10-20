import setuptools


def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(
    author='Ugo Popée',
    author_email='ugo.popee@me.com',
    name='package-name',
    version='0.1',
    url='http://github.com/bil0u/package-name',
    description='package-name description',
    long_description=readme(),
    long_description_content_type='text/markdown',
    keywords='package-name',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing :: Linguistic',
    ],
    license='MIT',
    packages=[
        'package_name'
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'package-name=package_name.app:main'
        ],
    },
    python_requires='>=3.6',
    install_requires=[
        'pytest'
    ]
)
