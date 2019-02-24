from PIL import Image, ImageDraw
from PIL.ImageColor import getrgb


class Plot:

    """
    Provides the ability to map, draw and color regions in a long/lat
    bounding box onto a proportionally scaled image.
    """
    @staticmethod
    def interpolate(x_1, x_2, x_3, newlength):
        """
        linearly interpolates x_2 <= x_1 <= x_3 into newlength
        x_2 and x_3 define a line segment, and x2 falls somewhere between them
        scale the width of the line segment to newlength, and return where
        x_1 falls on the scaled line.
        """

    @staticmethod
    def proportional_height(new_width, width, height):
        """
        return a height for new_width that is
        proportional to height with respect to width
        Yields:
            int: a new height
        """

    @staticmethod
    def fill(region, style):
        """return the fill color for region according to the given 'style'"""
        if style == "GRAD":
            return Plot.gradient(region)
        else:
            return Plot.solid(region)

    @staticmethod
    def solid(region):
        """
        a solid color based on a region's plurality of votes
        Args:
            region (Region): a region object
        Yields:
            (int, int, int): a triple (RGB values between 0 and 255)
        """

    @staticmethod
    def gradient(region):
        """
        a gradient color based on percentages of votes in a region
        Args:
            region (Region): a region object
        Yields:
            (int, int, int): a triple (RGB values between 0 and 255)
        """

    def __init__(self, width, min_long, min_lat, max_long, max_lat):
        """
        Create a width x height image where height is proportional to width
        with respect to the long/lat coordinates.
        """

    def save(self, filename):
        """save the current image to 'filename'"""

    def draw(self, region, style):
        """
        Draws 'region' in the given 'style' at the correct position on the
        current image
        Args:
            region (Region): a Region object with a set of coordinates
            style (str): 'GRAD' or 'SOLID' to determine the polygon's fill
        """
from PIL import Image, ImageDraw
from PIL.ImageColor import getrgb


class Plot:

    """
    Provides the ability to map, draw and color regions in a long/lat
    bounding box onto a proportionally scaled image.
    """
    @staticmethod
    def interpolate(x_1, x_2, x_3, newlength):
        """
        linearly interpolates x_2 <= x_1 <= x_3 into newlength
        x_2 and x_3 define a line segment, and x2 falls somewhere between them
        scale the width of the line segment to newlength, and return where
        x_1 falls on the scaled line.
        """
        return (((x_1 - x_2)/(x_3 - x_2))* newlength)

    @staticmethod
    def proportional_height(new_width, width, height):
        """
        return a height for new_width that is
        proportional to height with respect to width
        Yields:
            int: a new height
        """
        return ((height * new_width)/width)

    @staticmethod
    def fill(region, style):
        """return the fill color for region according to the given 'style'"""
        if style == "GRAD":
            return Plot.gradient(region)
        else:
            return Plot.solid(region)

    @staticmethod
    def solid(region):
        """
        a solid color based on a region's plurality of votes
        Args:
            region (Region): a region object
        Yields:
            (int, int, int): a triple (RGB values between 0 and 255)
        """
        if region.plurality() == "REPUBLICAN":
            return (255,0,0)
        elif region.plurality() == "DEMOCRAT":
            return (0,0,255)
        else:
            return(0,255,0)

    @staticmethod
    def gradient(region):
        """
        a gradient color based on percentages of votes in a region
        Args:
            region (Region): a region object
        Yields:
            (int, int, int): a triple (RGB values between 0 and 255)
        """
        return (int(255*(region.republican_percentage())),int(255*(region.other_percentage())),int(255*(region.democrat_percentage())))

    def __init__(self, width, min_long, min_lat, max_long, max_lat):
        """
        Create a width x height image where height is proportional to width
        with respect to the long/lat coordinates.
        """
        self.width = width
        self.min_long = min_long
        self.min_lat = min_lat
        self.max_long = max_long
        self.max_lat = max_lat
        self.height = self.proportional_height(width,(max_long - min_long),(max_lat - min_lat))
        self.image = Image.new("RGB",(int(self.width),int(self.height)),(255,255,255))

    def save(self, filename):
        """save the current image to 'filename'"""
        self.image.save(filename, "PNG")

    def draw(self, region, style):
        """
        Draws 'region' in the given 'style' at the correct position on the
        current image
        Args:
            region (Region): a Region object with a set of coordinates
            style (str): 'GRAD' or 'SOLID' to determine the polygon's fill
        """
        def trans_lat(region):
            """
            A function that interpolates the latitudinal values given by region
            using its respective latitudinal coordinates and height.
            """
            return [Plot.interpolate(lats,self.max_lat,self.min_lat,self.height) for lats in region.lats()]

        def trans_long(region):
            """
            A function that interpolates the longitudinal values given by region
            using its respective longitudinal coordinates and width.
            """
            return [Plot.interpolate(longs,self.min_long,self.max_long,self.width) for longs in region.longs()]

        lats = trans_lat(region)
        longs = trans_long(region)
        coordinate = [(int(longi),int(lati)) for (longi,lati) in zip(longs,lats)]
        ImageDraw.Draw(self.image).polygon(coordinate, fill=Plot.fill(region,style))
