def ask(a):
    return input(a+"\n").strip().lower()

def positive(response):
    return any(word in response for word in ["haan", "yes", "batao", "kya hai", "tell me", "sure", "please"])

def negative(response):
    return any(word in response for word in ["nahi", "no", "nahi chahiye", "not now"])

def fees():
    print("\nFee Structure:")
    print("Tuition Fee: ₹60,000")
    print("Bus Fee: ₹10,000")
    print("Total Annual Fees: ₹70,000")
    print("Installments:")
    print(" 1st Installment: ₹30,000 (due at admission)")
    print(" 2nd Installment: ₹20,000 (due after 1st semester)")
    print(" 3rd Installment: ₹20,000 (due after 2nd semester)")

def hostel():
    print("\nHostel Facilities:")
    print("1. 24x7 water and electricity")
    print("2. CCTV surveillance")
    print("3. Warden on-site")
    print("4. Hospital training: student works with real patients")

def tl():
    print("\nClinical Training Locations:")
    print("- District Hospital, Backundpur")
    print("- Community Health Centers")
    print("- Regional Hospital, Chartha")
    print("- Ranchi Neurosurgery and Allied Science Hospital, Ranchi")

def scholarship():
    print("\nScholarships Available:")
    print("- Govt Post-Matric: ₹18,000 - ₹23,000")
    print("- Labour Ministry: ₹40,000 - ₹48,000 (For Labour registration)")

def eligible():
    print("\nAdmission Eligibility: Mandatory")
    print("- 12th Biology")
    print("- PNT Exam qualified")
    print("- Age: 17-35 year")

def admission():
    while True:
        print("\nHi there, Would you like to join a Nursing College?")
        a=ask("")
        if negative(a):
            print("Okay, If you need any help in future, let me know.")
            return
        bio = ask("Are you a medical student(Biology in 12th)")
        if negative(bio):
            print("B.Sc Nursing is necessary to take admission....")
            return

        print("\nB.Sc Nursing is a full-time program which helps in clinical aur theoretical training.")
        while True:
            topic = ask("\nDo you want to know more about it?")

            if positive(topic):
                fees()
                hostel()
                tl()
                scholarship()
                eligible()
                print("\nTotal Seats Available: 60")
                print("\nCollege is located in Delhi.")
                print("\nRecognised College from Indian Nursing Council (INC), Delhi.")
            elif negative(topic):
                print("\nok, I am happy to help you. Let me know if you need any help again.")
                return
            else:
                return
admission()