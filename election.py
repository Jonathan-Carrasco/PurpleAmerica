import sys
import csv
import math
from region import Region
from plot import Plot

def mercator(lat):
    """project latitude 'lat' according to Mercator"""
    lat_rad = (lat * math.pi) / 180
    projection = math.log(math.tan((math.pi / 4) + (lat_rad / 2)))
    return (180 * projection) / math.pi

def main(results, boundaries, output, width, style):
    """
    Draws an image.
    This function creates an image object, constructs Region objects by reading
    in data from csv files, and draws polygons on the image based on those Regions
    Args:
        results (str): name of a csv file of election results
        boundaries (str): name of a csv file of geographic information
        output (str): name of a file to save the image
        width (int): width of the image
        style (str): either 'GRAD' or 'SOLID'
    """

if __name__ == '__main__':
    results = sys.argv[1]
    boundaries = sys.argv[2]
    output = sys.argv[3]
    width = int(sys.argv[4])
    style = sys.argv[5]
    main(results, boundaries, output, width, style)
import sys
import csv
import math
from region import Region
from plot import Plot

def mercator(lat):
    """project latitude 'lat' according to Mercator"""
    lat_rad = (lat * math.pi) / 180
    projection = math.log(math.tan((math.pi / 4) + (lat_rad / 2)))
    return (180 * projection) / math.pi

def main(results, boundaries, output, width, style):
    """
    Draws an image.
    This function creates an image object, constructs Region objects by reading
    in data from csv files, and draws polygons on the image based on those Regions
    Args:
        results (str): name of a csv file of election results
        boundaries (str): name of a csv file of geographic information
        output (str): name of a file to save the image
        width (int): width of the image
        style (str): either 'GRAD' or 'SOLID'
    """
    def to_point(lst):
        """
        A function that transforms a list of longitudes and a seperate list of
        latitude coordinates and zips them into a pair of coordinates.
        """
        longs = [float(x) for x in lst[::2]]
        lats = [mercator(float(x)) for x in lst[1::2]]
        return [x for x in zip(longs,lats)]

    with open(results,'r') as result:
        lst_results = list(csv.reader(result))
    with open(boundaries,'r') as bounds:
        lst_boundaries = list(csv.reader(bounds))

    coordinates = [to_point(line[2:]) for line in lst_boundaries]
    regions = [Region(c,int(r[2]),int(r[3]),int(r[4])) for c,r in zip(coordinates,lst_results)]

    min_long = min([region.min_long() for region in regions])
    max_long = max([region.max_long() for region in regions])
    min_lat = min([region.min_lat() for region in regions])
    max_lat = max([region.max_lat() for region in regions])
    plot = Plot(width,min_long,min_lat,max_long,max_lat)
    for region in regions:
        plot.draw(region,style)
        plot.save(output)

if __name__ == '__main__':
    results = sys.argv[1]
    boundaries = sys.argv[2]
    output = sys.argv[3]
    width = int(sys.argv[4])
    style = sys.argv[5]
    main(results, boundaries, output, width, style)
