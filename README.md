# SC_Project3
Using SDN and Network Function Virtualisation principles to create a network on Raspberry Pis

## Usage
### Create Vehicle Network
To create a network of vehicles, enter:
```
bash create_vehicle_network.sh <network_number>
```
where `<network_number>` is either `1` or `2`, corresponding to the Raspberry Pi number that the network is running on. Running this script spins up 5 vehicles with 8 sensors each on the specified Pi.

### Setup Central and Filover Controllers
To spin up the central controller, run:
```
python3 Controllers/Central_controller.py
```
To spin up the Failover controller, run:
```
python3 Controllers/Failover_controller.py
```
To simulate a vehicle, create a new terminal or window and run:
```
python3 Testing/TestP2P/Secure/clientpi.py
```

The client represents the vehicle, while the 2 controllers act as primary and failover servers.

Commands from the failover controller
```
- PING
- KILL
```
