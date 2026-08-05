registered=input()
examination_fee=input()
identity_verification=input()
system_check=input()

if registered=="yes":
    if examination_fee=="yes" or identity_verification=="yes":
        if system_check=="pass":
            print("Access Granted")

        else:
            print("system check failed")

    else:
        print("Verification Pending")

else:
    print("Registration Incomplete")

