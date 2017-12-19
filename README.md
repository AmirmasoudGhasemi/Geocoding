
## Installation

1. Install python3.
2. Clone the repo.
3. Set up an account with [Here] and add your app id and app code to `secrets.json`
4. Done!



# Usage
There are two ways for requesting the geocode for an address.
Frist:

Start the server:
```
=> python server
Server is running at http://localhost:3500
```
Make a request:
The request address should come after "http://localhost:3500?address=" and in the url-http format.
One can use browser or use 'curl' command in command line like the example below:
```
=> curl http://localhost:3500/?address=415%westview%st,%Coquitlam,%BC
{"lat": 49.2467554, "lng": -122.8890922}
```

Seccond:
Use command line api for requesting the geodoce for an address in a meaningful way.
```
=> python command_line_api
do you want to continue?[y/n]
```
if you press "n" it terminates

if you press something other "y" and "n" it asks you to retype again:
```
please just answer with y or n. do you want to continue?[y/n]
```
and if you press "y" it asks the address.
```
=> y
What is the address?
```
in this case, you can simply right the address in meaningful way like:
```
=> 415 Westview st, Coquitlam, BC
{'lat': 49.2467794, 'lng': -122.8890869}
```
This will work in a loop until you press "n" in new request.
