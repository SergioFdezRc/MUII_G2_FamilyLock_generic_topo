# MUII_G2_FamilyLock_generic_topo

Librería que genera de forma genérica una topología de red de mininet

# Instalación

Mediante pip:

`pip install git+https://github.com/SergioFdezRc/MUII_G2_FamilyLock_generic_topo.git@main`

Añadiéndolo al requirements.txt

`git+https://github.com/SergioFdezRc/MUII_G2_FamilyLock_generic_topo.git@main`

# Uso

```
from mininet_topo import generic_topo as gt

gt.create_generic_topo(RemoteController, 127.0.0.1, 2345)

```

