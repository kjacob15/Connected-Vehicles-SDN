# SC_Project3
Using SDN and Network Function Virtualisation principles to create a network on Raspberry Pis

## Usage
### Create Vehicle Network
To create a network of vehicles, enter:
```
bash create_vehicle_network.sh <network_number>
```
where `<network_number>` is either `1` or `2`, corresponding to the Raspberry Pi number that the network is running on. Running this script spins up 5 vehicles with 8 sensors each on the specified Pi.