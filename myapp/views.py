from django.shortcuts import render
import pickle
from django.http import HttpResponse
def google_verify(request):
    return HttpResponse("google-site-verification:google90a4278fbf104ff4.html")
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
import os
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
@csrf_exempt
def chatbot(request):
    if request.method != "POST":
        return JsonResponse({"reply": "Only POST allowed"}, status=405)

    if not GROQ_API_KEY:
        return JsonResponse({"reply": "Server error: API key not set"}, status=500)

    try:
        data = json.loads(request.body.decode("utf-8"))
        user_msg = data.get("message", "").strip()

        if not user_msg:
            return JsonResponse({"reply": "Please enter a message."})

        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a helpful career counselor for Indian students. "
                        "Give concise, practical guidance for choices after class 10 and 12. "
                        "Ask a clarifying question if needed."
                    ),
                },
                {
                    "role": "user",
                    "content": user_msg,
                },
            ],
            "temperature": 0.5,
        }

        response = requests.post(url, headers=headers, json=payload, timeout=30)

        # Handle HTTP-level errors cleanly
        if response.status_code != 200:
            return JsonResponse(
                {"reply": f"API error ({response.status_code}): {response.text[:300]}"},
                status=502,
            )

        result = response.json()

        # Safe extraction (prevents KeyError if API changes or errors)
        choices = result.get("choices", [])
        if not choices:
            return JsonResponse({"reply": f"API returned no choices: {result}"}, status=502)

        reply = choices[0].get("message", {}).get("content", "").strip()
        if not reply:
            reply = "I couldn't generate a response. Please try again."

        return JsonResponse({"reply": reply})

    except json.JSONDecodeError:
        return JsonResponse({"reply": "Invalid JSON request"}, status=400)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"reply": f"Network error: {str(e)}"}, status=502)
    except Exception as e:
        return JsonResponse({"reply": f"Server error: {str(e)}"}, status=500)


