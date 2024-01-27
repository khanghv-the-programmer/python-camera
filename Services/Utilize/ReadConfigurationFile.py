import configparser
import os


class ReadConfigurationFile(object):

    def __init__(self, *file_names):
        config = configparser.ConfigParser()
        config_conf_path = os.path.normpath(
            os.path.join(os.path.dirname(__file__), './settings.properties'))
        found = config.read(config_conf_path)
        if not found:
            raise ValueError('No config file found!')

        for section in config.sections():
            self.__dict__.__setitem__(section, {})
            for item in config.items(section):
                self.__getattribute__(section)[item[0]] = item[1]


read_config_from_file = ReadConfigurationFile('')
