# HkCrsTransformer
simple conversion between HK1980 and WGS84

HK1980 又名 EPSG 2326, 而 WGS84 (通用 GPS 坐標) 又名 EPSG 4326

Examples
```sh
'''
install dependency first
'''
# conda install pyproj -y
pip install pyproj -y
```
```py
import CrsTransformer as ct

print(ct.GPS2HK(114.00030255843123,22.485771225062955))
# (818097.5296817721, 838477.9470580409)

print(ct.HK2GPS(838477.970,818097.267))
# (114.19832156976544, 22.301818498702563)
```
