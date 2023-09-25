from setuptools import setup, Distribution

class BinaryDistribution(Distribution):
    def is_pure(self):
        return False
    
setup(
    name='tpcaccess',
    version='0.2.2',
    description='TPC Access library',
    author='Elsys',
    package_data={'tpcaccess': ['TpcAccess.lib', '_TpcAccess.pyd']},
    data_files=[('', ['G:\\Limit\\TIvas\\Elsys\\tpcaccess2\\src\\TpcAccessPy\\x64\Release\\_TpcAccess.lib', 'G:\\Limit\\TIvas\\Elsys\\tpcaccess2\\src\\TpcAccessPy\\_TpcAccess.pyd'])],
    distclass=BinaryDistribution,
)