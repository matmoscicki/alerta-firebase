
from setuptools import setup, find_packages

version = '1.0.0'

setup(
    name="alerta-firebase",
    version=version,
    description='Alerta plugin to send alerts by Firebase Cloud messaging',
    url='https://github.com/matmoscicki/alerta-firebase',
    license='MIT',
    author='Mateusz Moscicki',
    author_email='mat.moscicki@gmail.com',
    packages=find_packages(),
    py_modules=['alerta_firebase'],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.plugins': [
            'firebase = alerta_firebase:FirebaseNotify'
        ]
    }
)
