class Television:
    """
    A class describing the functions of a tv remote
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL:int = 3

    def __init__(self) -> None:
        """
        Method that creates the objects and their initial values for the Television class
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        "Method that changes the power statues/boolean value when the function is called"
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        "Method that changes the mute status/boolean value everytime the function is called"
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self) -> None:
        """
        Method that raises the channel number
        """
        if self.__status == True:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method that lowers the channel number
        """
        if self.__status == True:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method that increases the tv volume.
        """
        if self.__status == True:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Method that decreases the tv volume.
        """
        if self.__status == True:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        Method that shows the tv status.
        :return: tv status.
        """
        if self.__muted == True:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
