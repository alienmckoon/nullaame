def write_done(data_, filename):
    """
    Write the data to a file.

    Args:
        data_ (str): The data to write to the file.
        filename (str): The name of the file to write to.
    """

    with open(filename, "w") as f:
        f.write(data_)

