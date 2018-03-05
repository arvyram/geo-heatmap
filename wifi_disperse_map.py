import json
import glob
from string import Template


POINT_FOLD = 'points/'
kml_template =  Template('<Placemark><magnitude>$density</magnitude> <Point> <coordinates>$lng, $lat, 0</coordinates> </Point> </Placemark>\n')
op_file ='heatmap.kml'
    
class Build_KML:
    def sub_latlon(self, cell_file):
        disp_pts = json.loads( open(cell_file,'r').read())
        kml_str = ''
        if disp_pts:
            for pt in disp_pts:
                kml_str += kml_template.substitute( density = pt['density'], lng = pt['lng'], lat = pt['lat']  )
        return kml_str
    def add_head_footer( self, body ):
        header = '<?xml version="1.0" encoding="UTF-8"?> <kml xmlns="http://earth.google.com/kml/2.0" xmlns:atom="http://www.w3.org/2005/Atom"> <Document> <name>BT WiFi</name><Folder> \n'
        footer = '</Folder>  </Document> </kml>'
        return header + body + footer

bk = Build_KML()

map_content = ''

locations = ['Cambridge']

files = [l for loc in locations for l in glob.glob( POINT_FOLD + '/'+loc+'/*.json' )]

for f in files:    
    map_content += bk.sub_latlon( f )
kml_content = bk.add_head_footer(map_content)

with open( op_file, 'w' ) as f:
    f.write(kml_content)
