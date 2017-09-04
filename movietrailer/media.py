# ===============================================================================
#
# media.py
#
# This module defines the class Movie to create instance
# of movie objects
#
# @author: Nirosh Gunaratne
# @since: 28/08/2017
# @version: 1.0
#
# ===============================================================================


class Movie(object):
    # ===========================================================================
    # This class holds attributes related to instance of a movie
    # ===========================================================================

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        # ===========================================================================
        # create movie instance using specified parameters
        # you tube of the movie trailer
        #
        # Parameters
        # ----------
        # movie_title : String
        #     title of the movie
        # movie_storyline : String
        #     story line of the movie
        # poster_image : String
        #     poster image of the movie
        # trailer_youtube : String
        #     you tube of the movie trailer
        # =============================================================
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
