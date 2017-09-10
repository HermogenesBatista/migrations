# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from setuptools import setup

setup(
    name='migrations',
    version='0.1',
    packages=['migrations', 'migrations.connection'],
    entry_points={
          'console_scripts': [
              'migrations = migrations.main.__main__:execute_command_line'
          ]
      },
    install_requires=[
        'PyMySQL==0.7.11'],
    license='Hermogenes Batista All rights reserved',
    long_description='Hermogenes Batista All rights reserved',
)