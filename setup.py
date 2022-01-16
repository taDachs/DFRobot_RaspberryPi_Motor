#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='DFRobot_RaspberryPi_Motor',
    license='MIT',
    packages=['DFRobotDCMotorDriverHAT'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=['smbus'],
    python_requires='>=3.6',
)
