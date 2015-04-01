.. code::

  # Import the FileChooser object
  from filechooser import FileChooser

  # Define a method which returns a FileChooser, with a certain ID field (this must
  # be the same as the one defined in the template) and root directory for the file
  # browsing and finally a callback method to process the selected file
  def filechooser():
      return FileChooser("identifier", settings.FILEBROWSER_DIRECTORY, process)

  # Define a method to handle selected files.
  def process(filename):
    # do something with filename received from the filechooser
