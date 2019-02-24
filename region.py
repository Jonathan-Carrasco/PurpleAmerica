class Region:
    """
    A region (represented by a list of long/lat coordinates) along with
    republican, democrat, and other vote counts.
    """

    def __init__(self, coords, r_votes, d_votes, o_votes):
        self.coords = coords
        self.r_votes = r_votes
        self.d_votes = d_votes
        self.o_votes = o_votes

    def lats(self):
        "Return a list of the latitudes of all the coordinates in the region"
        return [y for x,y in self.coords]

    def longs(self):
        "Return a list of the longitudes of all the coordinates in the region"
        return [x for x,y in self.coords]

    def min_lat(self):
        "Return the minimum latitude of the region"
        return min(y for x,y in self.coords)

    def min_long(self):
        "Return the minimum longitude of the region"
        return min(x for x,y in self.coords)

    def max_lat(self):
        "Return the maximum latitude of the region"
        return max(y for x,y in self.coords)

    def max_long(self):
        "Return the maximum longitude of the region"
        return max(x for x,y in self.coords)

    def plurality(self):
        """return 'REPUBLICAN','DEMOCRAT', or 'OTHER'
        depending on plurality of votes"""
        if self.d_votes > self.r_votes and self.d_votes > self.o_votes:
            return "DEMOCRAT"
        elif self.r_votes > self.d_votes and self.r_votes > self.o_votes:
            return "REPUBLICAN"
        else:
            return "OTHER"

    def total_votes(self):
        "The total number of votes cast in this region"
        return self.o_votes + self.d_votes + self.r_votes

    def republican_percentage(self):
        "The precentage of republication votes cast in this region"
        return (self.r_votes/self.total_votes())

    def democrat_percentage(self):
        "The precentage of democrat votes cast in this region"
        return (self.d_votes/self.total_votes())

    def other_percentage(self):
        "The precentage of other votes cast in this region"
        return (self.o_votes/self.total_votes())
