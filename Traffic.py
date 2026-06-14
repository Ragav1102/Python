print('.....Traffic signals.....')
signal=input('Enter the Signal colour red/yellow/green : ').lower()
if signal=="red":
    print("Stop")
elif signal=="yellow":
    print("Wait")
elif signal=='green':
    print("Go")
else:
    print("Invalid colour")
    
