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

Assumptions :
1) Script is hosted on windows 10 laptop.
2) ELAM is taken on SUP720 6500.
3) ICMP is allowed from source to destination.
4) The platform hosting the script is used as the ICMP source.
If any of the above assuptions is not satisfied appropriate changes in the script would be required.

Note : Please consider the fact that the script reconfigures the ELAM after every successful ping.

Test Outputs : in output file

