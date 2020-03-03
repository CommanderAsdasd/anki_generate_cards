Hi, which exact way we are should use to connect? : )
just tried to connect in all the ways that I described above, got still the same - ssh connection to 89.22.2.11 is completely prohibited, as well as use this address as proxy to connect to 10.186.18.205 (this host seems to be down according to google console, so I’ve also tried another host in ‘kohls-iaas-ads-lle’ project - 10.186.18.221) - it all gives `nc: connect to 89.22.2.11 port 3128 (tcp) failed: Operation timed out`
Connection to 10.186.18.205 (and 10.186.18.221) through 10.4.7.10:3128 and 10.9.7.10:3128 gives `Proxy error: "HTTP/1.0 504 Gateway Timeout”`,
Connection to 89.22.2.11 though proxies 10.4.7.10 and 10.9.7.10 gives `403 Proxy Unacknowledged` and `407 Proxy Authentication Required`
Connection directly to 10.9.7.10 (and 10.4.7.10) on port 3128 lasts very long and eventually gives
```
ssh -vvv TKMA32V@10.9.7.10 -p 3128
OpenSSH_7.6p1, LibreSSL 2.6.2
debug1: Reading configuration data /Users/atankovskii/.ssh/config
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 48: Applying options for *
debug1: /etc/ssh/ssh_config line 52: Applying options for *
debug2: ssh_connect_direct: needpriv 0
debug1: Connecting to 10.9.7.10 port 3128.
debug1: Connection established.
debug1: identity file /Users/atankovskii/.ssh/id_rsa type 0
ssh_exchange_identification: Connection closed by remote host
```§