network_pattern='[12]'
if ! [[ $1 =~ $network_pattern ]]; then
    echo "error: first argument to script must be pi number" &2; exit 1
fi
network=$1

(
    # Allows us to quit entire process with ctrl-c
    trap 'kill 0' SIGINT;
    # Get script directory
    scriptDir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")

    python3 $scriptDir/Sensors/vehicle.py "$network" 1 &     # Vehicle controller
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 1 1 &     # Front proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 1 2 &     # Right proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 1 3 &     # Back proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 1 4 &     # Left proximity sensor
    python3 $scriptDir/Sensors/location_sensor.py "$network" 1 5 &      # Location sensor
    python3 $scriptDir/Sensors/speed_sensor.py "$network" 1 6 &         # Speed sensor
    python3 $scriptDir/Sensors/fuel_sensor.py "$network" 1 7 &          # Fuel sensor
    python3 $scriptDir/Sensors/voltage_sensor.py "$network" 1 8 &       # Voltage sensor

    python3 $scriptDir/Sensors/vehicle.py "$network" 2 &     # Vehicle controller
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 2 1 &     # Front proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 2 2 &     # Right proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 2 3 &     # Back proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 2 4 &     # Left proximity sensor
    python3 $scriptDir/Sensors/location_sensor.py "$network" 2 5 &      # Location sensor
    python3 $scriptDir/Sensors/speed_sensor.py "$network" 2 6 &         # Speed sensor
    python3 $scriptDir/Sensors/fuel_sensor.py "$network" 2 7 &          # Fuel sensor
    python3 $scriptDir/Sensors/voltage_sensor.py "$network" 2 8 &       # Voltage sensor

    python3 $scriptDir/Sensors/vehicle.py "$network" 3 &     # Vehicle controller
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 3 1 &     # Front proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 3 2 &     # Right proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 3 3 &     # Back proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 3 4 &     # Left proximity sensor
    python3 $scriptDir/Sensors/location_sensor.py "$network" 3 5 &      # Location sensor
    python3 $scriptDir/Sensors/speed_sensor.py "$network" 3 6 &         # Speed sensor
    python3 $scriptDir/Sensors/fuel_sensor.py "$network" 3 7 &          # Fuel sensor
    python3 $scriptDir/Sensors/voltage_sensor.py "$network" 3 8 &        # Voltage sensor

    python3 $scriptDir/Sensors/vehicle.py "$network" 4 &     # Vehicle controller
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 4 1 &     # Front proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 4 2 &     # Right proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 4 3 &     # Back proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 4 4 &     # Left proximity sensor
    python3 $scriptDir/Sensors/location_sensor.py "$network" 4 5 &      # Location sensor
    python3 $scriptDir/Sensors/speed_sensor.py "$network" 4 6 &         # Speed sensor
    python3 $scriptDir/Sensors/fuel_sensor.py "$network" 4 7 &          # Fuel sensor
    python3 $scriptDir/Sensors/voltage_sensor.py "$network" 4 8 &       # Voltage sensor

    python3 $scriptDir/Sensors/vehicle.py "$network" 5 &     # Vehicle controller
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 5 1 &     # Front proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 5 2 &     # Right proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 5 3 &     # Back proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" 5 4 &     # Left proximity sensor
    python3 $scriptDir/Sensors/location_sensor.py "$network" 5 5 &      # Location sensor
    python3 $scriptDir/Sensors/speed_sensor.py "$network" 5 6 &         # Speed sensor
    python3 $scriptDir/Sensors/fuel_sensor.py "$network" 5 7 &          # Fuel sensor
    python3 $scriptDir/Sensors/voltage_sensor.py "$network" 5 8         # Voltage sensor
)