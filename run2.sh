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


# Allows us to quit entire process with ctrl-c
#trap 'kill 0' SIGINT;
# Get script directory
scriptDir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")

for f in `seq 1 5`; do
    vehicleNum=$(($f + $vehicleIncrement))
    tmux split-window -d -t "$vehicleNum" -p20 -v "watch -n1 tail -n5 file_${f}";
    tmux select-layout -t "$vehicleNum" even-vertical
    tmux attach-session -t "$vehicleNum"
done

for f in `seq 1 5`; do
    vehicleNum=$(($f + $vehicleIncrement))
    tmux split-window -d -t "$vehicleNum" -p20 -v "watch -n1 tail -n5 file_${f}";
    tmux select-layout -t "$vehicleNum" even-vertical
    tmux attach-session -t "$vehicleNum"
    python3 $scriptDir/Sensors/vehicle.py "$network" "$vehicleNum" &     # Vehicle controller
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleNum" 1 &     # Front proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleNum" 2 &     # Right proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleNum" 3 &     # Back proximity sensor
    python3 $scriptDir/Sensors/proximity_sensor.py "$network" "$vehicleNum" 4 &     # Left proximity sensor
    python3 $scriptDir/Sensors/location_sensor.py "$network" "$vehicleNum" 5 &      # Location sensor
    python3 $scriptDir/Sensors/speed_sensor.py "$network" "$vehicleNum" 6 &         # Speed sensor
    python3 $scriptDir/Sensors/fuel_sensor.py "$network" "$vehicleNum" 7 &          # Fuel sensor
    python3 $scriptDir/Sensors/voltage_sensor.py "$network" "$vehicleNum" 8 &       # Voltage sensor
done
