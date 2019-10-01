#6500VSSstandaloneELAMSUP720
import netmiko
import os
from getpass import getpass

class IntermittentDropCapture():
    
    def main(self):
        
        print("="*60)
        #input data
        destip = input("Enter the IP of the destination: ")
        
        #devicelogindata
        devicedata = {}
        inputmethod = input("Do you want to use telnet or SSH to log into the device : ")
        devicedata['device_type'] = 'cisco_ios' if inputmethod.lower() == "ssh" else 'cisco_ios_telnet'
        devicedata['ip'] = input("Enter the IP of the switch: ")
        devicedata['username'] = input("Enter the username: ")
        devicedata['password'] = getpass("Enter the login password: ")
        devicedata['secret'] = getpass("Enter the enable secret (press return of non is configured): ")
        
        #programe data
        commands = []
        precheckoutput = ""
        postcheckoutput = ""
        
        #elamdata
        trigger = input("Enter the trigger :")
        slot = input("Enter the slot: ")
        swno = input("Enter the switch number: ") if input("Is the switch a VSS [yes, no] ? ") == "yes" else ""

        #show commands
        print("Enter the commands you want to collect pre and post packet drop(Enter 'OK' when done): ")
        while True:
            command = input("> ")
            if command != 'OK': commands.append(command)
            else: break 
        print("="*60)
        
        #device login
        print("logging into the device now.")
        device = netmiko.ConnectHandler(**devicedata)
        if devicedata["secret"]: device.enable()
        print("Device has be logged into.")
        print("="*60)
        
        device.send_config_set(['service internal'])
        
        #checking reachability of destination
        print("Checking reachability of destination")
        drop = True
        while drop:
            #taking predrop outputs
            precheckoutput = self.precheck(device, commands, trigger, slot, swno)
            #chechking if the packet drop, if the packet drops the while loop breaks
            drop = False if os.system("ping -n 1 "+ destip) == 1 else True
        
        print("="*60)
        #taking post drop outputs
        postcheckoutput = self.postcheck(device, commands, slot, swno)

        #printing outputs on the prompt
        print("="*60)
        print("Precheck Output are:", precheckoutput , end = "\n" + "="*60 )
        print("="*60)
        print("Postcheck Output are:", postcheckoutput, end = "\n" + "="*60 + "\n")
            
        #saving outputs to a file    
        with open("outputs", "w") as f:
            
            f.write("\n" + "="*60 + "\nPrecheck Outputs are: \n" + precheckoutput + "\n" + "="*60)
            f.write("\n" + "="*60 + "\nPostcheck Outputs are: \n" + postcheckoutput + "\n" + "="*60)

        device.disconnect()
        input("Press enter to exit")
        
    def precheck(self, device, commands, trigger, slot, swno):

        response = ""
        #taking outputs of show commands
        if commands: response += "\n".join(map(lambda x: "\n#{}\n{}".format(x, device.send_command(x, expect_string = r"#")), commands))
        
        #if device is a VSS swno will have a value otherwise it would be empty
        if swno:
            elamcommandset = [f"attach switch {swno} module {slot}", "terminal length 0", "show platform capture elam release", 
			f"show platform capture elam asic superman slot {slot}", trigger, "show platform capture elam start", "show platform capture elam status", "exit"]
            
            #configuring ELAM
            response += "\n".join(map(lambda x: "\n#{}\n{}".format(x, device.send_command(x, expect_string = r"#")), elamcommandset))
            
        #for standable        
        else:
            elamcommandset = ["show platform capture elam release", f"show platform capture elam asic superman slot {slot}", trigger, 
			"show platform capture elam start", "show platform capture elam status"]

            response += "\n".join(map(lambda x: "\n#{}\n{}".format(x, device.send_command(x, expect_string = r"#")), elamcommandset))

        return response
        
            
    def postcheck(self, device, commands, slot, swno):
        
        response = ""

        #taking outputs of show commands
        if commands: response += "\n".join(map(lambda x: "\n#{}\n{}".format(x, device.send_command(x, expect_string = r"#")), commands))

        if swno:
            elamcommandset = [f"attach switch {swno} module {slot}", "terminal length 0", 
			"show platform capture elam status", "show platform capture elam data", "show platform capture elam release", "exit"]

            response += "\n".join(map(lambda x: "\n#{}\n{}".format(x, device.send_command(x, expect_string = r"#")), elamcommandset))
            
        else:
            elamcommandset = ["show platform capture elam status", "show platform capture elam data", "show platform capture elam release"]
            
            #configuring ELAM
            response += "\n".join(map(lambda x: "\n#{}\n{}".format(x, device.send_command(x, expect_string = r"#")), elamcommandset))
                    
        return response


test = IntermittentDropCapture()
test.main()