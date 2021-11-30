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
tmux new

for f in `seq 1 5`; do
    vehicleNum=$(($f + $vehicleIncrement))
    tmux new-session -d -s "$vehicleNum" "bash $scriptDir/createVehicle.sh $network $vehicleNum"
  #  tmux split-window -d -t "$vehicleNum" -p20 -v "bash $scriptDir/createVehicle.sh $network $vehicleNum";
    tmux select-layout -t "$vehicleNum" even-vertical
    tmux attach-session -t "$vehicleNum"
done