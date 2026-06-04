age : int
name : str
height : float
is_human : bool

def police_check(age:int) -> bool: # yha pe arrow bata rhi hai ki iss function ka return type bool hona
    # chahiye aur agar uske alawa aur kuch hoga to ye error show kr dega
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(19):
    print("You can drive")
else:
    print("Pay a fine")

