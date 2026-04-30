from django.shortcuts import render
import pickle

def show(request):
    return render(request,'index.html')

def counselling(request):
    return render(request,'counselling.html')

def class10(request):
    return render(request,'class10.html')

def class12(request):
    return render(request,'class12.html')

def Arts(request):
    return render(request,'Arts.html')

def Commerce(request):
    return render(request,'Commerce.html')

def PCB(request):
    return render(request,'PCB.html')

def PCM(request):
    return render(request,'PCM.html')

######################################################################################################

def getpredictions_10(Math,Science,English,Social_Science):

    model = pickle.load(open("student_stream_10th_knn_model.sav","rb"))

    input_data = [[Math, Science, English, Social_Science]]

    prediction=model.predict(input_data)

    return prediction

def output_10(request):
    
    Math=int(request.GET['maths'])
    Science=int(request.GET['science'])
    English=int(request.GET['english'])
    Social_Science=int(request.GET['social_science'])

    result= getpredictions_10(Math,Science,English,Social_Science)

    return render(request, 'output.html',{'result':result})

######################################################################################################

def getpredictions_PCB(Physics,Chemistry,Biology):

    model = pickle.load(open("student_stream_PCB_model.sav","rb"))
    le = pickle.load(open("label_encoder_PCB.sav", "rb"))

    input_data = [[Physics,Chemistry,Biology]]

    pre_prediction=model.predict(input_data)
    final_prediction = le.inverse_transform(pre_prediction)

    return final_prediction[0]

def output_PCB(request):

    Physics=int(request.GET['physics'])
    Chemistry=int(request.GET['chemistry'])
    Biology=int(request.GET['biology'])

    result= getpredictions_PCB(Physics,Chemistry,Biology)

    return render(request, 'output.html',{'result':result})

#######################################################################################################

def getpredictions_PCM(Physics,Chemistry,Mathematics):

    model = pickle.load(open("student_stream_PCM_model.sav","rb"))
    le = pickle.load(open("label_encoder_PCM.sav", "rb"))

    input_data = [[Physics,Chemistry,Mathematics]]

    pre_prediction=model.predict(input_data)

    final_prediction = le.inverse_transform(pre_prediction)

    return final_prediction[0]

def output_PCM(request):
    Physics=int(request.GET['physics'])
    Chemistry=int(request.GET['chemistry'])
    Math=int(request.GET['mathematics'])

    result= getpredictions_PCM(Physics,Chemistry,Math)

    return render(request, 'output.html',{'result':result})

#######################################################################################################

def getpredictions_COM(Account,Business_Studies,Economics):
    import pickle
    model = pickle.load(open("student_stream_COM_model.sav","rb"))
    le = pickle.load(open("label_encoder_COM.sav", "rb"))

    input_data = [[Account,Business_Studies,Economics]]

    pre_prediction=model.predict(input_data)
    final_prediction = le.inverse_transform(pre_prediction)

    return final_prediction[0]

def output_COM(request):
    Account=int(request.GET['accounts'])
    Business_Studies=int(request.GET['business_studies'])
    Economics=int(request.GET['economics'])

    result= getpredictions_COM(Account,Business_Studies,Economics)

    return render(request, 'output.html',{'result':result})

#######################################################################################################

def getpredictions_ARTS(History,Political_Science,English):

    model = pickle.load(open("student_stream_Arts_model.sav","rb"))

    le = pickle.load(open("label_encoder_Arts.sav", "rb"))

    input_data = [[History,Political_Science,English]]

    pre_prediction=model.predict(input_data)
    
    final_prediction = le.inverse_transform(pre_prediction)

    return final_prediction[0]

def output_ARTS(request):
    History=int(request.GET['history'])
    Political_Science=int(request.GET['political_science'])
    English=int(request.GET['english'])

    result= getpredictions_ARTS(History,Political_Science,English)

    return render(request, 'output.html',{'result':result})

# Chatbot integration from here
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_msg = data.get("message", "")

            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "tinyllama:latest",
                    "prompt": f"""
You are an intelligent career counselor for Indian students.

Your job:
- Guide students after class 10 and 12
- Suggest streams: Science, Commerce, Arts
- Give practical advice
- Ask questions if needed

Student question: {user_msg}

Give a helpful, simple and real answer.
""",
                    "stream": False   # 🔥 VERY IMPORTANT
                }
            )

            result = response.json()
            print("FULL RESPONSE:", result)  # DEBUG

            reply = result.get("response")


            if not reply:
                reply = result.get("error", "No response from AI")  # fallback

        except Exception as e:
            reply = f"Error: {str(e)}"

        return JsonResponse({"reply": reply})