# Censorship Dispenser

# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read() 

# text needed to be censored first email
txtt = "learning algorithms"
# list of words to censor from second and third email
propietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
# list of words to censor from third email
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
# censor_one 
censored_one = "sandwich"
# censor_list
censored_list = "farenheit 101"
# censor_negative
censored_negative = "very nice"
# censor_before_after
censored_before_after = "uhh"
# censor used to replace censored_list in censor_before_after
new_censor_list = "kirbo"
# censor used to replace censored_negative in censor_before_after
new_censor_negative = "comfortable"

# function to replace a single string from text
def censor_one(txt1, censor, censored):
    txt = txt1.lower()
    while txt.find(censor) > 0:
        firstidx = txt.find(censor)
        lastidx = firstidx + len(censor)

        new_string = txt[:firstidx] + censored + txt[lastidx:]
        txt = new_string
        
    return txt

# function to replace a list of words from text
def censor_list(txt1, lst, censored):
    txt = txt1.lower()
    for i in lst:
        while txt.find(i) > 0:
            firstidx = txt.find(i)
            lastidx = firstidx + len(i)

            new_string = txt[:firstidx] + censored + txt[lastidx:]
            txt = new_string
    return txt

# function to replace words after more than 2 words from list appear in a text
def censor_negative(txt1, lst, censored):
    txt = txt1.lower()
    score = 0
    for i in lst:
        if i in txt:
            score = score + 1
            if score > 2:
                while txt.find(i) > 0:  
                    firstidx = txt.find(i)
                    lastidx = firstidx + len(i)

                    new_string = txt[:firstidx] + censored + txt[lastidx:]
                    txt = new_string       
    return txt

# function to replace words tthat appear before and after certain words from selected lists
def censor_before_after(txt1, censored):
    txt_propietary = censor_list(txt1, propietary_terms, censored_list)
    txt = censor_negative(txt_propietary, negative_words, censored_negative)
    while txt.count(censored_negative) > 0:

        firstidx = txt.find(censored_negative)
        lastidx = firstidx + len(censored_negative)
        
        first_half = txt[:firstidx - 1]
        second_half = txt[lastidx + 1:]

        # after
        space_after = second_half.find(" ")
        # before
        space_before = first_half.rfind(" ")
        
        new_string = first_half[:space_before] + " " +  censored + " " + new_censor_negative + " " + censored + second_half[space_after:]
        txt = new_string
        
    while txt.count(censored_list) > 0:
        firstidx = txt.find(censored_list)
        lastidx = firstidx + len(censored_list)
        
        first_half = txt[:firstidx - 1]
        second_half = txt[lastidx + 1:]

        # after
        space_after = second_half.find(" ")
        # before
        space_before = first_half.rfind(" ")
        
        complete = first_half[:space_before] + " " +  censored + " " + new_censor_list + " " + censored + second_half[space_after:]
        txt = complete
    
    return txt

# censored emails

f = open("email_one_censored.txt", "w")
f.write(censor_one(email_one, txtt, censored_one))
f.close()

f = open("email_two_censored.txt", "w")
f.write(censor_list(email_two, propietary_terms, censored_list))
f.close()

f = open("email_three_censored.txt", "w")
f.write(censor_list(censor_negative(email_three, negative_words, censored_negative), propietary_terms, censored_list))
f.close()

f = open("email_four_censored.txt", "w")
f.write(censor_before_after(email_four, censored_before_after))
f.close()



    