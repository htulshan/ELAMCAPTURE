Read me


Motivation :

It is not possible to take ELAM captures for intermittent packet drops on Cisco switch.
Since ELAM captures only the first interesting packet that hits the hardware no matter if the packet dropped in its path to the destination or not.

Objective :

To take ELAM capture for intermittent packet drops on cisco switch.


Script logic to achieve the objective:
1) The script take predrop output from the switch and configure a ELAM.
2) The script then send an ICMP packet through the box to the destination.
3) If the ICMP reply is received back from the destination the script starts over from step one.
4) If no reply is received the script extracts ELAM data.
5) Along with ELAM the script will also take show commands outputs as specifed by the user.
6) All the outputs are saved in a txt file.
7) The script can to used for to the box traffic or through the box traffic.

Assumptios :
1) Script is hosted on windows 10 laptop.
2) ELAM is taken on SUP720 6500.
3) ICMP is allowed from source to destination.
4) The platform hosting the script is used as the ICMP source.
If any of the above assuptions is not satisfied appropriate changes in the script would be required.

Note : Please consider the fact that the script reconfigures the ELAM after every successful ping.

Test Outputs :

The test was done for to the box traffic.

PS C:\Users\xyz\Desktop\python test scripts> python .\6500VSSStandaloneELAM_U1.py
============================================================
Enter the IP of the destination: 10.1.1.1                                  <------- IP on the switch for to the box traffic, can be a different IP for through the box traffic
Do you want to use telnet or SSH to log into the device : SSH
Enter the IP of the switch: 10.1.1.1
Enter the username: cisco
Enter the login password:
Enter the enable secret (press return of non is configured):
Enter the trigger :show platform capture elam trigger dbus ipv4 if L3_PT=ICMP IP_SA=10.1.1.2 IP_DA=10.1.1.1 ICMP_TYPE=0x8
Enter the slot: 2
Is the switch a VSS [yes, no] ? yes
Enter the switch number: 2
Enter the commands you want to collect pre and post packet drop(Enter 'OK' when done):
> show clock
> OK
============================================================
logging into the device now.
Device has be logged into.
============================================================
Checking reachability of destination

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time=6ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 6ms, Maximum = 6ms, Average = 6ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time<1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time<1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time=1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 1ms, Average = 1ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time<1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time=1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 1ms, Average = 1ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time<1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time<1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time<1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time<1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time=1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 1ms, Average = 1ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time<1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time<1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time<1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time<1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time<1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time<1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time<1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time=1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 1ms, Average = 1ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time<1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time<1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Pinging 10.1.1.1 with 32 bytes of data:
Reply from 10.1.1.1: bytes=32 time<1ms TTL=251

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Pinging 10.1.1.1 with 32 bytes of data:                                  <----------- Here is configured an ACL on the switch to drop the traffic
Request timed out.

Ping statistics for 10.1.1.1:
    Packets: Sent = 1, Received = 0, Lost = 1 (100% loss),
============================================================
============================================================
Precheck Output are:
#show clock
*21:50:46.963 UTC Mon Sep 30 2019
#attach switch 2 module 2
Trying Switch ...
Entering CONSOLE for Switch
Type "^C^C^C" to end this session


#terminal length 0


#show platform capture elam release


#show platform capture elam asic superman slot 2


#show platform capture elam trigger dbus ipv4 if L3_PT=ICMP IP_SA=10.1.1.2 IP_DA=10.1.1.1 ICMP_TYPE=0x8


#show platform capture elam start


#show platform capture elam status
Active ELAM info:
Slot Cpu   Asic   Inst Ver PB Elam
---- --- -------- ---- --- -- ----
2    0   ST_SUPER 0    2.2    Y
DBUS trigger: FORMAT=IP L3_PROTOCOL=IPV4 L3_PT=ICMP IP_SA=10.1.1.2 IP_DA=10.1.1.1 ICMP_TYPE=0X8
ELAM capture in progress

#exit

[Connection to Switch closed by foreign host]
========================================================================================================================
Postcheck Output are:
#show clock
*21:50:54.191 UTC Mon Sep 30 2019
#attach switch 2 module 2
Trying Switch ...
Entering CONSOLE for Switch
Type "^C^C^C" to end this session


#terminal length 0


#show platform capture elam status
Active ELAM info:
Slot Cpu   Asic   Inst Ver PB Elam
---- --- -------- ---- --- -- ----
2    0   ST_SUPER 0    2.2    Y
DBUS trigger: FORMAT=IP L3_PROTOCOL=IPV4 L3_PT=ICMP IP_SA=10.1.1.2 IP_DA=10.1.1.1 ICMP_TYPE=0X8
ELAM capture completed

#show platform capture elam data
DBUS data:
SEQ_NUM ......................... [5] = 0x7
QOS ............................. [3] = 0
QOS_TYPE ........................ [1] = 0
TYPE ............................ [4] = 0 [ETHERNET]
STATUS_BPDU ..................... [1] = 0
IPO ............................. [1] = 1
NO_ESTBLS ....................... [1] = 0
RBH ............................. [3] = b000
CR .............................. [1] = 0
TRUSTED ......................... [1] = 1
NOTIFY_IL ....................... [1] = 0
NOTIFY_NL ....................... [1] = 0
DISABLE_NL ...................... [1] = 0
DISABLE_IL ...................... [1] = 0
DONT_FWD ........................ [1] = 0
INDEX_DIRECT .................... [1] = 0
DONT_LEARN ...................... [1] = 0
COND_LEARN ...................... [1] = 0
BUNDLE_BYPASS ................... [1] = 0
QOS_TIC ......................... [1] = 1
INBAND .......................... [1] = 0
IGNORE_QOSO ..................... [1] = 0
IGNORE_QOSI ..................... [1] = 0
IGNORE_ACLO ..................... [1] = 0
IGNORE_ACLI ..................... [1] = 0
PORT_QOS ........................ [1] = 0
CACHE_CNTRL ..................... [2] = 0 [NORMAL]
VLAN ............................ [12] = 1033
SRC_FLOOD ....................... [1] = 0
SRC_INDEX ....................... [19] = 0x8AF
LEN ............................. [16] = 78
FORMAT .......................... [2] = 0 [IP]
MPLS_EXP ........................ [3] = 0x0
REC ............................. [1] = 0
NO_STATS ........................ [1] = 0
VPN_INDEX ....................... [10] = 0x0
PACKET_TYPE ..................... [3] = 0 [ETHERNET]
L3_PROTOCOL ..................... [4] = 0 [IPV4]
L3_PT ........................... [8] = 1 [ICMP]
MPLS_TTL ........................ [8] = 0
SRC_XTAG ........................ [4] = 0x2
DEST_XTAG ....................... [4] = 0xF
FF .............................. [1] = 0
MN .............................. [1] = 0
RF .............................. [1] = 0
SC .............................. [1] = 0
CARD_TYPE ....................... [4] = 0x0
DMAC ............................ = aaaa.aaaa.aaaa
SMAC ............................ = bbbb.bbbb.bbbb
IPVER ........................... [1] = 0 [IPV4]
IP_DF ........................... [1] = 0
IP_MF ........................... [1] = 0
IP_HDR_LEN ...................... [4] = 5
IP_TOS .......................... [8] = 0x0
IP_LEN .......................... [16] = 60
IP_HDR_VALID .................... [1] = 1
IP_CHKSUM_VALID ................. [1] = 1
IP_L4HDR_VALID .................. [1] = 1
IP_OFFSET ....................... [13] = 0
IP_TTL .......................... [8] = 124
IP_CHKSUM ....................... [16] = 0x5B8B
IP_SA ........................... = 10.1.1.2
IP_DA ........................... = 10.1.1.1
ICMP_TYPE ....................... [8] = 0x8
ICMP_CODE ....................... [8] = 0x0
ICMP_DATA [104]
0000:  4B E7 00 01 01 74 61 62 63 64 66 69 6A            "K....tabcdfij"
CRC ............................. [16] = 0xA0A1

RBUS data:
SEQ_NUM ......................... [5] = 0x7
CCC ............................. [3] = b101 [L2_POLICE]
CAP1 ............................ [1] = 0
CAP2 ............................ [1] = 0
QOS ............................. [3] = 0
EGRESS .......................... [1] = 0
DT .............................. [1] = 1 [GENERIC]
TL .............................. [1] = 0 [B32]
FLOOD ........................... [1] = 0
DEST_INDEX ...................... [19] = 0x7F0A
VLAN ............................ [12] = 1033
RBH ............................. [3] = b110
RDT ............................. [1] = 1
GENERIC ......................... [1] = 0
EXTRA_CICLE ..................... [1] = 0
FABRIC_PRIO ..................... [1] = 0
L2 .............................. [1] = 0
FCS1 ............................ [8] = 0x1
DELTA_LEN ....................... [8] = 0
REWRITE_INFO
 i0  - no rewrite.
FCS2 ............................ [8] = 0x0

Control signals:
rb_stat                          [3] = 0x7

#show platform capture elam release


#exit

[Connection to Switch closed by foreign host]
============================================================
Press enter to exit
PS C:\Users\xyz\Desktop\python test scripts># ELAMCAPTURE
