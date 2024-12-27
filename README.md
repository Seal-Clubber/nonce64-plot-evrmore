nonce64-plot-evrmore
==========

This will plot block nonce against blockheight.

Dependency
-----
Make sure you have gnuplot installed:
```
sudo apt install gnuplot
```
Python 3 and the ravenrpc with:
```
pip install ravenrpc
```

Usage
-----

First of all, you should set RPC username and password in evrmore.conf:
```
rpcuser=username
rpcpassword=password
```
After that launch `./evrmored -daemon` or `./evrmore-qt` with server=1 in conf.

And finaly to run the data gathering and plotter:
```
python3 nonce.py
make
```
