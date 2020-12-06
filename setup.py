from setuptools import setup

with open("requirements.txt") as f:
    install_requires = f.read().split("\n")

setup(
    name='Generic Topology',
    version='1.0',
    url='https://github.com/SergioFdezRc/MUII_G2_FamilyLock_generic_topo',
    license='Creative Commons',
    author='Gonzalo Jiménez Hinchado',
    author_email='gojimenez@alumnos.unex.es',
    description='Librería que genera una topología de red con mininet dado ciertos parámetros específicos documentados '
                'en el código',
    packages=[
        'mininet_topo',
    ],
    install_requires=install_requires
)
