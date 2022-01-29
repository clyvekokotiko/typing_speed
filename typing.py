from datetime import datetime

def main():
    """Lets do main stuff here like calling other functions"""
    print("\nWELCOME TO THE GAME. ENJOY TYPING!!!!\n")

    filename = input("\nPlease enter file name: ")

    original_list = read(filename)

    print_text(filename)

    start_typing = input("\nPress enter to start typing!!!")

    start = datetime.now() #initial time
    new_list = recieve()    #This is where the person will be typing 
    finish = datetime.now() # final time

    print()
    

    time_minutes = time(start, finish)

    word_count = count_words(new_list)

    speed_wpm = speed(word_count, time_minutes)

    accuracy = word_accuracy(original_list, new_list)
    print(f"Speed: {speed_wpm:.2f}wpm | accuracy: {accuracy:.2f}%\n")




def read(filename):
    """this function reads characters from a text file and returns a
    list
    Args:
        filename: This is the name of the file. given example is "text.txt"
    """
    
    original_list = []

    try:
        
        with open(filename, "rt") as f:

            for i in f:
                i = i.split()

                for j in i:
                    original_list.append(j)

    except:
        print("File Not Found")
    
    return original_list

def print_text(filename):
    """This function prints the text to be copied"""
    try:
        with open(filename, "rt") as ff:
            for i in ff:

                print(i)
        
    except:
        print("File Not Found")

def recieve():
    """this function recieves input from a user and stores in a list.
    returns the list"""
    
    words = input("Start typing (press Enter when done): \n")

    new_list = words.split()
    
    return new_list

def count_words(file_list):
    """This function counts words from a list and returns the number"""
    word_count = 0

    for i in file_list:
        word_count += 1
    
    return word_count

def time(start, finish):
    """This function stores and returns time differerence in minutes"""
    time = finish - start 
    strp_time = str(time).split(":") # time comes in this fomat 0:00:05.130034 hence the split and focusing on the last part
    time = strp_time[2]
    time = float(time) + float(strp_time[1]) * 60 + float(strp_time[0]) * 60 * 60 # accounting for if the person takes more than a minute
    # then converting everything to seconds
    time = float(time / 60) #these will be seconds
    # print(time) # for testing

    return time

def speed(word_count, time):
    """this function calculates speed"""
    speed = 0

    #the following loop takes care when user doesnt write anything 
    if word_count > 0:
        speed = float(word_count / time)
    
    return speed

def word_accuracy(original_list, new_list):
    """This function checks accuracy of your typing and returns in percentage"""
    
    penalty = 0
    accuracy = 0

    for i in range(len(new_list)):
        if new_list[i] == original_list[i]:
            pass
        else:
            penalty += 1
    
    if len(new_list) > 0:
        accuracy = float(100 - ((penalty) / len(new_list)) * 100)

    return accuracy


if __name__ == "__main__":
    main()