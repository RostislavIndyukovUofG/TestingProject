class LogFileReader:

    @classmethod
    def readFromLogFile(cls, file_path):
        with open(file_path, "r") as log:
            file_data = log.read().splitlines()
        return file_data
