print("                                                               **Welcome user**")
print("*------------------------------------------------------------------------"
      "-------------------------------------------------------------------------------*")
print("This detector is made from a detailed study of symptom and informations from famous websites like webmd.com , \
  heatline.com , cdc.gov, and many more. ")
print("Your response in the questions for every yes will always be '1' and for no will be '0' ")
print("*------------------------------------------------------------------------"
      "-------------------------------------------------------------------------------*")

total = 0
total_1 = 0
total_2 = 0

def basic_symptoms():
    global total
    age = int(input("What is your age ? "))
    if age < 18 :
        total += 2
    elif age > 18 and age < 64:
        total += 5
    elif age > 64 :
        total += 9
    fever = int(input("Have you been having fever recently ? (yes=1 or no = 0) : "))
    if fever == 1 :
        fever_1 = int(input("low or high fever ? (high = 1 or low = 0) :"))
        if fever_1 == 0:
            total += 2
        elif fever_1 == 1:
            total += 4
    elif fever == 0:
        pass
    cough = int(input("Have you been coughing recently ? "))
    if cough == 1 :
        cough_1 = int(input("Normal cough or dry cough (normal cough == 0 and dry cough == 1 ) :"))
        if cough_1 == 0 :
            total += 1
        elif cough_1 == 1 :
            total += 6
    else :
        pass
    fatigue = int(input("Having you been feeling tired these days ? : "))
    if fatigue == 1:
        total += 7
    else :
        pass
    appetite = int(input("have you lost your appetite to eat ? : "))
    if appetite == 1:
        total += 7
    else:
        pass
    body_pain = int(input("Having you been having body pain these days ? : "))
    if body_pain == 1:
        total += 8
    else :
        pass
    print(total)

basic_symptoms()

def mid_symptoms() :
    global total_1
    runny_nose = int(input("Have you been having a runny nose ? (yes=1 or no = 0) : "))
    if runny_nose == 1:
        total_1 += 5
    elif runny_nose == 0:
        total_1 += 2
    nausea  = int(input("Have you been having nausea ? (yes=1 or no = 0) : "))
    if nausea == 1 :
        total_1+= 4
    else :
        total_1 += 1
    loss_smell = int(input("Have you been experiencing lose of smell ? (yes=1 or no = 0) : "))
    if loss_smell == 1:
        total_1 += 4
    else :
        pass



def danger_symptoms():
    global total_2
    chest_pain = int(input("Have you been experiencing chest pain ? (yes=1 or no = 0) : "))
    if chest_pain == 1 :
        total_2 += 9
    breathing = int(input( "Have you been experiencing breathing issues ? (yes=1 or no = 0) : "))
    if breathing == 1 :
        total_2 += 9
    if total_2 >9 :
            print("Your answers predict that you at a very high risk for COVID-19 ,you must ensure that you must get \
yourself tested within this hour. Please take this issue very seriously ! ")
    elif total_2 < 9:
        print("Your answers predict that you at a medium to high risk for COVID-19 ,you must ensure that you must get \
yourself tested. There are chances that you could be asymtomatic , so we prefer you to visit a doctor or  health-care \
             center ")



def detector_1():
    print("*------------------------------------------------------------------------"
          "-------------------------------------------------------------------------------*")
    if total < 30 :
        print("Your answers predict that you are at a low-risk for COVID-19 ,you must ensure you protect yourself and\
 ensure you are following social distancing norms. ")
    elif total > 31 :
        mid_symptoms()
        if total_1 < 6:
            print("Your answers predict that you're at medium to high risk for COVID-19 ,you must ensure that you must get \
        yourself tested. There are chances that you could be asymtomatic , so we prefer you to visit a doctor or health-care \
         center ")
        elif total_1 > 6:
            danger_symptoms()

detector_1()






