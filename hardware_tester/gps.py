"""
GPS module: Handles GPS data parsing and communication.
"""

def get_gps_data() -> dict:
    """
    Retrieve GPS data from serial and parse NMEA sentences.

    Returns:
        dict: Dictionary with keys 'mph', 'gyro', 'compass', 'location'.
    """
    # TODO: Implement serial reading and NMEA parsing
    return {
        "mph": None,
        "gyro": None,
        "compass": None,
        "location": None
    }
