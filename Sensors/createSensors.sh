(
    # Allows us to quit entire process with ctrl-c
    trap 'kill 0' SIGINT;

    # Get script directory
    scriptDir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")

    # Front proximity sensor
    python $scriptDir/proximity.py 1 1 &

    # Right proximity sensor
    python $scriptDir/proximity.py 1 2 &

    # Back proximity sensor
    python $scriptDir/proximity.py 1 3 &

    # Left proximity sensor
    python $scriptDir/proximity.py 1 4 &

    # Location sensor
    python $scriptDir/location.py 1 5

)