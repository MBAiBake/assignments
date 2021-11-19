class Profile:
    """
        A "Linked-in like" profile.
        Attributes:
            name - a string
            title - a string
            company - a string
            connections - a list of profiles
            employment_history - a list of tuples of the form
                                 (title, company, start year, finish year)
                                 e.g. ("VP of Engineering", "Ford", 1998, 2010)
            optionally, you could also add an education attribute....
            education - a list of tuples of the form
                        (degree, school, start year, finish year)
                        e.g. ("Bachelors of Science, Computer Science",
                              "Northwestern University",
                              2004,
                              2008)
        Methods:
            self.__init__
                takes 3 strings as input (n, t, c) with default values of ""
                    representing a name, title and company
                creates an instance of a profile with the name title and
                    company that were given as input. Connections and
                    employment_history should be initialized to an empty list
            self.__str__
                returns a string representation of the object including
                    information from all attributes
            self.add_connection
                takes another profile instance as input and adds that
                    profile to the connections attribute. However, only
                    add the profile if its not already included in the
                    connections attribute. That is, we don't want duplicates
                    in the list.
    """

    def __init__(self, n="", t="", c=""):
        """ Creates an instance of a profile. """
        self.name = n
        self.title = t
        self.company = c
        self.connections = []
        self.employment_history = []
        self.education = []

    def __str__(self):
        return self.name + " " + self.title + " " + self.company
        """ Returns a string representation of the profile."""

    def add_connection(self, a_profile):
        """if the input profile is not already connected to self,
        connect them."""
        if a_profile not in self.connections:
            self.connections.append(a_profile)


def connect(p1, p2):
    """
    connect takes two profile objects and connects them. That is, adds
    each to the other's list of connections.
    Inputs: Two profile instances.
    Returns: None
    """
    p1.add_connection(p2)
    p2.add_connection(p1)
    return None


def where_did_they_work_together(p1, p2):
    """
    where_did_they_work_together determines whether and where p1 and p2 overlapped
    in their employment history. That is, were they at the same company in
    overlapping years.
    Inputs: Two profile instances.
    Returns: The company name if they worked together. False if they did not.
    """
    for title1, employer1, start_year1, finish_year1 in p1.employment_history:
        for title2, employer2, start_year2, finish_year2 in p2.employment_history:
            if employer1 == employer2 and finish_year2 >= start_year1 and finish_year1 >= start_year2:
                return employer1
    return False


def shortest_path(p1, p2):
    """
    shortest_path determines the distance (and associated path) between two
    profiles. For example, if p2 appears in p1.connections, the distance is
    1 and the path simply contains p1.name and p2.name. See asserts for more
    examples.

    Inputs: Two profile instances.
    Returns: The distance and path between the two input profiles.
             None if no path is found
    """

    visited = []
    q = [(p1, 0, [p1.name])]
    i = 1
    while len(q) > 0:
        curr, dist, path = q.pop(0)
        visited.append(curr)

        if curr.name == p2.name:
            return (dist, path)
        else:
            for connection in curr.connections:
                if connection not in visited:
                    q.append((connection, dist + 1, path + [connection.name]))
    return None

    #   else
    #      for each of curr's connections
    #          if the connection is not already in visited
    #              append a new triple to q
    #                  (the node itself,
    #                  the distance from p1 to that node - computed from dist,
    #                  the path from p1 to that node - computed from path)
    # If we hit this point, we never returned an answer. This means that we should
    #    return None because there is no path between p1 and p2.
    # pass


# EXTENSION #1 - this function would be an extension, but not extra credit
def shortest_path_to_someone_who(p1, predicate):
    """
    shortest_path determines the distance (and associated path) between p1
    and someone who meets the criteria expressed in the predicate.

    Inputs: A profile instance and a predicate (that takes a profile and returns
    a boolean).
    Returns: The distance and path between the two input profiles.
             None if no path is found
    """
    pass