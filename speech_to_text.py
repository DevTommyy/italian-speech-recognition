import speech_recognition as sr
import math

addWords = ['aggiungi', 'addiziona', 'piu', 'più', 'somma', '+', 'addizione']
subWords = ['sottrai', 'togli', 'meno', '-', 'sottrazione', 'differenza']
divWords = ['dividi', 'diviso', 'divisone', 'fratto']
mulWords = ['moltiplica', 'moltiplicazione', 'per', 'x', 'X', '*']

def sub(list):
    result = list[0]
    for x in range(1, len(list)):
        result -= list[x]
    return result

def div(list):
    result = list[0]
    for x in range(1, len(list)):
        result /= list[x]
    return result

def recognize(said):
    try:
        # said = r.recognize_google(audio, language="it-IT")
        final_result = 0
        placeholder = False

        #use this if you need to see the output from what you said
        # print(said.split()) 
        
        for x in said.split(): 
            while not placeholder:

                numbers = [int(s) for s in said.split() if s.isdigit()]
                if numbers == []:
                    print("Nessun numero riconosciuto")
                    break

                elif x.lower() in addWords:   
                    final_result += float(sum(numbers))
                    placeholder = True

                elif x.lower() in subWords:
                    final_result += float(sub(numbers))
                    placeholder = True

                elif x.lower() in divWords:
                    final_result += div(numbers)
                    placeholder = True

                elif x.lower() in mulWords:
                    final_result += float(math.prod(numbers))
                    placeholder = True
                break

        if placeholder:
            print("Il risultato è: ", final_result)
        else:
            print("Nessun operazione compresa")

    except sr.UnknownValueError:
        print("Non ho capito")



def main():
    r = sr.Recognizer()

    with sr.Microphone(device_index=0) as source:
        print("Dimmi un operazione da fare!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Va bene")

    said = r.recognize_google(audio, language="it-IT")

    recognize(said)



if __name__ == "__main__":
    main()