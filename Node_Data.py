class Node_Data:
    """
    this class represents a node in directed weighted graph:
    contains:
    key, tag, info, weight. location
    """

    def __init__(self, key, tag=0, info=0, weight=0, geo=None):
        self._key = key
        self._tag = tag
        self._info = info
        self._weight = weight
        self._location = geo
        self._NodeSize = 0

    def get_key(self) -> int:
        """
        this method return the key of the node
        :return: key:int
        """
        return self._key

    def get_tag(self):
        """
        this method return the tag of the node
        :return: tag
        """
        return self._tag

    def get_info(self):
        """
        this method return the info of the node
        :return: info
        """
        return self._info

    def get_weight(self):
        """
        this method return the weight of the node
        :return: weight
        """
        return self._weight

    def get_location(self: tuple):
        """
        this method return the location of the node
        :return: location
        """
        return self._location

    def set_key(self, key: int):
        """
         this method set the key of the node
        :param key:
        :return:
        """
        self._key = key

    def set_tag(self, tag):
        """
        this method set the tag of the node
        :param tag:
        :return:
        """
        self._tag = tag

    def set_info(self, info):
        """
        this method set the info of the node
        :param info:
        :return:
        """
        self._info = info

    def set_weight(self, weight):
        """
        this method set the weight of the node
        :param weight:
        :return:
        """
        self._weight = weight

    def set_location(self, p: tuple):
        """
        this method set the location of the node
        :param p:
        :return:
        """
        self._location = p

    def __str__(self):
        return self._key, self._location

    def __repr__(self):
        return str(self.__str__())
