network_pattern='[12]'
if ! [[ $1 =~ $network_pattern ]]; then
    echo "error: first argument to script must be pi number" &2; exit 1
fi
network=$1

vehicleIncrement=0
network_1='[1]'
if ! [[ $1 =~ $network_1 ]]; then
    vehicleIncrement=5
fi

(
    # Allows us to quit entire process with ctrl-c
    trap 'kill 0' SIGINT;
    # Get script directory
    scriptDir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")

    vehicleANum=$((1 + $vehicleIncrement))
    python3 $scriptDir/Sensors/vehicle.py "$network" "$vehicleANum" &     # Vehicle controller
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleANum" 1 &     # Front proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleANum" 2 &     # Right proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleANum" 3 &     # Back proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleANum" 4 &     # Left proximity sensor
    python3 $scriptDir/Sensors/location_sensor.py "$network" "$vehicleANum" 5 &      # Location sensor
    python3 $scriptDir/Sensors/speed_sensor.py "$network" "$vehicleANum" 6 &         # Speed sensor
    python3 $scriptDir/Sensors/fuel_sensor.py "$network" "$vehicleANum" 7 &          # Fuel sensor
    python3 $scriptDir/Sensors/voltage_sensor.py "$network" "$vehicleANum" 8 &       # Voltage sensor

    vehicleBNum=$((2 + $vehicleIncrement))
    python3 $scriptDir/Sensors/vehicle.py "$network" "$vehicleBNum" &     # Vehicle controller
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleBNum" 1 &     # Front proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleBNum" 2 &     # Right proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleBNum" 3 &     # Back proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleBNum" 4 &     # Left proximity sensor
    python3 $scriptDir/Sensors/location_sensor.py "$network" "$vehicleBNum" 5 &      # Location sensor
    python3 $scriptDir/Sensors/speed_sensor.py "$network" "$vehicleBNum" 6 &         # Speed sensor
    python3 $scriptDir/Sensors/fuel_sensor.py "$network" "$vehicleBNum" 7 &          # Fuel sensor
    python3 $scriptDir/Sensors/voltage_sensor.py "$network" "$vehicleBNum" 8 &       # Voltage sensor

    vehicleCNum=$((3 + $vehicleIncrement))
    python3 $scriptDir/Sensors/vehicle.py "$network" "$vehicleCNum" &     # Vehicle controller
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleCNum" 1 &     # Front proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleCNum" 2 &     # Right proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleCNum" 3 &     # Back proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleCNum" 4 &     # Left proximity sensor
    python3 $scriptDir/Sensors/location_sensor.py "$network" "$vehicleCNum" 5 &      # Location sensor
    python3 $scriptDir/Sensors/speed_sensor.py "$network" "$vehicleCNum" 6 &         # Speed sensor
    python3 $scriptDir/Sensors/fuel_sensor.py "$network" "$vehicleCNum" 7 &          # Fuel sensor
    python3 $scriptDir/Sensors/voltage_sensor.py "$network" "$vehicleCNum" 8 &        # Voltage sensor

    vehicleDNum=$((4 + $vehicleIncrement))
    python3 $scriptDir/Sensors/vehicle.py "$network" "$vehicleDNum" &     # Vehicle controller
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleDNum" 1 &     # Front proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleDNum" 2 &     # Right proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleDNum" 3 &     # Back proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleDNum" 4 &     # Left proximity sensor
    python3 $scriptDir/Sensors/location_sensor.py "$network" "$vehicleDNum" 5 &      # Location sensor
    python3 $scriptDir/Sensors/speed_sensor.py "$network" "$vehicleDNum" 6 &         # Speed sensor
    python3 $scriptDir/Sensors/fuel_sensor.py "$network" "$vehicleDNum" 7 &          # Fuel sensor
    python3 $scriptDir/Sensors/voltage_sensor.py "$network" "$vehicleDNum" 8 &       # Voltage sensor

    vehicleENum=$((5 + $vehicleIncrement))
    python3 $scriptDir/Sensors/vehicle.py "$network" "$vehicleENum" &     # Vehicle controller
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleENum" 1 &     # Front proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleENum" 2 &     # Right proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleENum" 3 &     # Back proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleENum" 4 &     # Left proximity sensor
    python3 $scriptDir/Sensors/location_sensor.py "$network" "$vehicleENum" 5 &      # Location sensor
    python3 $scriptDir/Sensors/speed_sensor.py "$network" "$vehicleENum" 6 &         # Speed sensor
    python3 $scriptDir/Sensors/fuel_sensor.py "$network" "$vehicleENum" 7 &          # Fuel sensor
    python3 $scriptDir/Sensors/voltage_sensor.py "$network" "$vehicleENum" 8         # Voltage sensor
)