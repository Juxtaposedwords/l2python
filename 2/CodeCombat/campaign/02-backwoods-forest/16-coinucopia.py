# Press Submit when you are ready to place flags.
# Flag buttons appear in the lower left after pressing Submit.
loop:
    flag = self.findFlag()
    if flag:
        self.pickUpFlag(flag)
    else:
        self.say("Place a flag for me to go to.")

