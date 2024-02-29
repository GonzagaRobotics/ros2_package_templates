import os
from glob import glob

from setuptools import setup

package_name = 'python_pubsub_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share", package_name, "launch"), glob("launch/*.launch.py")),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jmsuchor',
    maintainer_email='jamesmsuchor@gmail.com',
    description='For learning python ROS2 package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = python_pubsub_pkg.publisher_member_function:main',
            'listener = python_pubsub_pkg.subscriber_member_function:main',
        ],
    },
)
