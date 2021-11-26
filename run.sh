(
    # Allows us to quit entire process with ctrl-c
    trap 'kill 0' SIGINT;

    # Get script directory
    scriptDir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")

    python $scriptDir/Sensors/proximity_sensor.py 1 1 &     # Front proximity sensor
    python $scriptDir/Sensors/proximity_sensor.py 1 2 &     # Right proximity sensor
    python $scriptDir/Sensors/proximity_sensor.py 1 3 &     # Back proximity sensor
    python $scriptDir/Sensors/proximity_sensor.py 1 4 &     # Left proximity sensor
    python $scriptDir/Sensors/location_sensor.py 1 5 &      # Location sensor
    python $scriptDir/Sensors/speed_sensor.py 1 6 &         # Speed sensor
    python $scriptDir/Sensors/fuel_sensor.py 1 7            # Fuel sensor

)