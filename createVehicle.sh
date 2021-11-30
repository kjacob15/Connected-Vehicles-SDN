network=$1
vehicleNum=$2
scriptDir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")

python3 $scriptDir/Sensors/vehicle.py "$network" "$vehicleNum" &     # Vehicle controller
python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleNum" 1 &     # Front proximity sensor
python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleNum" 2 &     # Right proximity sensor
python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleNum" 3 &     # Back proximity sensor
python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleNum" 4 &     # Left proximity sensor
python3 $scriptDir/Sensors/location_sensor.py "$network" "$vehicleNum" 5 &      # Location sensor
python3 $scriptDir/Sensors/speed_sensor.py "$network" "$vehicleNum" 6 &         # Speed sensor
python3 $scriptDir/Sensors/fuel_sensor.py "$network" "$vehicleNum" 7 &          # Fuel sensor
python3 $scriptDir/Sensors/voltage_sensor.py "$network" "$vehicleNum" 8 &       # Voltage sensor