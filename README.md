# geo-heatmap

_wifi_disperse_map.py_ helps to visualize the heatmap of points within a map. The script generates wifi_disperse_map.html which uses openstreet map and two kml files to generate the heat map.

The two KML files are generated as follows:

1 (optional) Border of the city/country: This can be downloaded from sites like https://data.gov.uk/dataset/local-authority-districts-december-2016-full-clipped-boundaries-in-great-britain2 

2 Points to plot in form of json structured as: [{"lat": 52.2015, "lng": 0.09625, "density": 1}, {"lat": 52.20075, "lng": 0.095, "density": 5}]. There can be multiple such json files. These files are used as input to generate heatmap.kml (wifi_disperse_map.py - https://github.com/arvyram/geo-heatmap/blob/4631e49ff00fab00794cae97c695de4f0f96c2e0/wifi_disperse_map.py#L8)

