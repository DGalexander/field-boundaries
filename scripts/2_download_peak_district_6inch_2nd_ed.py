import geopandas as gpd

parks = gpd.read_file("../National_Parks_England_4829975525583709119.geojson")
peak_district = parks[parks["NAME"]=="PEAK DISTRICT"]

from mapreader import SheetDownloader

my_ts = SheetDownloader(
    metadata_path="../MapReader/worked_examples/geospatial/NLS_metadata/metadata_OS_Six_Inch_GB_WFS_light.json",
    download_url="https://api.maptiler.com/tiles/uk-osgb1888/{z}/{x}/{y}?key=5f6FYax2HhTa0Z9RfXsp",
)

my_ts.get_grid_bb(17)
my_ts.query_map_sheets_by_polygon(peak_district.iloc[0].geometry, mode="intersects")

my_ts.download_map_sheets_by_queries(force=True, download_in_parallel=False, path_save="maps_peak_district")
