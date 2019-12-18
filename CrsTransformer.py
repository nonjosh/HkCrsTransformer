from pyproj import Transformer

#  HK1980 又名 EPSG 2326, 而 WGS84 (通用 GPS 坐標) 又名 EPSG 4326

def HK2GPS(northing, easting):
    """convert HK1980 northing/easting to GPS long/lat
    
    Args:
        northing {float}: HK1980 northing
        easting {float}: HK1980 easting

    Returns:
        {float, float}: GPS longitude, GPS latitude
    """
    transformer = Transformer.from_crs("EPSG:2326", "EPSG:4326", always_xy=True)
    long_, lat_ = transformer.transform(northing, easting)
    return long_, lat_

def GPS2HK(long_, lat_):
    """GPS long/lat to HK1980 northing/easting
    
    Args:
        long_ {float}: GPS longitude
        lat_ {float}: GPS latitude

    Returns:
        {float, float}: HK1980 northing, HK1980 easting
    """
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:2326", always_xy=True)
    northing, easting = transformer.transform(long_, lat_)
    return northing, easting

# main function
if __name__ == "__main__":
    
    # Usage Examples
    
    print(GPS2HK(114.00030255843123,22.485771225062955))
    # (818097.5296817721, 838477.9470580409)

    print(HK2GPS(838477.970,818097.267))
    # (114.19832156976544, 22.301818498702563)