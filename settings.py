# read and write to settings files
# 
import sublime

def preferences_filename():
  """
  :return: The appropriate settings filename based on the version of Sublime Text
  """
  return 'Preferences.sublime-settings'

def conemu_open_settings_filename():
    """
    :return: The settings file for ConEmu
    """

    return 'ConEmuOpen.sublime-settings'