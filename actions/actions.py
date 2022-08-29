# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
       
  
# class ActionCoronaCases(Action):
#     try:
#         def name(self) -> Text:
#          return "actions_corona_state_stat"

#         def run(self, dispatcher: CollectingDispatcher,

#              tracker: Tracker,
#              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#          response=requests.get("https://data.covid19india.org/data.json").json()
#          entities=tracker.latest_message['entities']
#          print("Last message Now",entities)
#          state=None
#          for e in entities:
#              if e["entity"]=="state":
#                 state=e["value"]
#          message="please enter valid state in india "
#          ct=0
#          max1=''
#          for data in response["statewise"]:
#              str1=state.title()
#              str2=data['state']
#              c=0
#              j=0
#              for i in str1:    
#                  if str2.find(i)>= 0 and j == str1.find(i): 
#                      c += 1
#                  j += 1

#              if c>ct:
#                  ct=c
#                  max1=data
#          message="Active: "+ max1["active"]+"  Conformed: "+ max1["confirmed"]+"  Recovered: "+ max1["deltarecovered"] +" On: " + max1["lastupdatedtime"]
                   
#          dispatcher.utter_message(message)
#          return []
#     except:
#         pass


prev=[]  

class ActionCoronaCases(Action):
    try:
        def name(self) -> Text:
         return "actions_corona_state_stat"

        def run(self, dispatcher: CollectingDispatcher,

             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         response=requests.get("https://data.covid19india.org/data.json").json()
         entities=tracker.latest_message['entities']
         prev.append(entities)
         print("Last message Now",entities)
         state=None
         for e in entities:
             if e["entity"]=="state":
                state=e["value"]
         message="please enter valid state in india "
         ct=0
         max1=''
         for data in response["statewise"]:
             str1=state.title()
             str2=data['state']
             c=0
             j=0
             for i in str1:    
                 if str2.find(i)>= 0 and j == str1.find(i): 
                     c += 1
                 j += 1

             if c>ct:
                 ct=c
                 max1=data
                 message=[{"title": "active", "payload": "/Active"}, {"title": "Recovered", "payload": "/Recovered"}, {"title": "Conformed", "payload": "/Conformed"}]
             continue
         dispatcher.utter_button_message("which type of cases you want", message)
         return []
    except:
        pass

class ActionCoronaCases(Action):
    try:
        def name(self) -> Text:
         return "actions_corona_state_stat_active"

        def run(self, dispatcher: CollectingDispatcher,

             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         response=requests.get("https://data.covid19india.org/data.json").json()
         entities=prev[-1]
         prev.append(entities)
         print("Last message Now",entities)
         state=None
         for e in entities:
             if e["entity"]=="state":
                state=e["value"]
         message="please enter valid state in india "
         ct=0
         max1=''
         for data in response["statewise"]:
             str1=state.title()
             str2=data['state']
             c=0
             j=0
             for i in str1:    
                 if str2.find(i)>= 0 and j == str1.find(i): 
                     c += 1
                 j += 1

             if c>ct:
                 ct=c
                 max1=data
         message="Active: "+ max1["active"] +" On: " + max1["lastupdatedtime"]
                   
         dispatcher.utter_message(message)
         return []
    except:
        pass

class ActionCoronaCases(Action):
    try:
        def name(self) -> Text:
         return "actions_corona_state_stat_recover"

        def run(self, dispatcher: CollectingDispatcher,

             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         response=requests.get("https://data.covid19india.org/data.json").json()
         entities=prev[-1]
         prev.append(entities)
         print("Last message Now",entities)
         state=None
         for e in entities:
             if e["entity"]=="state":
                state=e["value"]
         message="please enter valid state in india "
         ct=0
         max1=''
         for data in response["statewise"]:
             str1=state.title()
             str2=data['state']
             c=0
             j=0
             for i in str1:    
                 if str2.find(i)>= 0 and j == str1.find(i): 
                     c += 1
                 j += 1

             if c>ct:
                 ct=c
                 max1=data
         message="  Recovered: "+ max1["deltarecovered"] +" On: " + max1["lastupdatedtime"]
                   
         dispatcher.utter_message(message)
         return []
    except:
        pass

class ActionCoronaCases(Action):
    try:
        def name(self) -> Text:
         return "actions_corona_state_stat_conform"

        def run(self, dispatcher: CollectingDispatcher,

             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         response=requests.get("https://data.covid19india.org/data.json").json()
         entities=prev[-1]
         prev.append(entities)
         print("Last message Now",entities)
         state=None
         for e in entities:
             if e["entity"]=="state":
                state=e["value"]
         message="please enter valid state in india "
         ct=0
         max1=''
         for data in response["statewise"]:
             str1=state.title()
             str2=data['state']
             c=0
             j=0
             for i in str1:    
                 if str2.find(i)>= 0 and j == str1.find(i): 
                     c += 1
                 j += 1

             if c>ct:
                 ct=c
                 max1=data
         message="  Conformed: "+ max1["confirmed"]+" On: " + max1["lastupdatedtime"]
                   
         dispatcher.utter_message(message)
         return []
    except:
        pass


class ActionCoronaCases(Action):
    
    try:
        def name(self) -> Text:
         return "actions_name_entry"

        def run(self, dispatcher: CollectingDispatcher,

             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         entitie=tracker.latest_message['entities']
        
         message="Hello"+ str(entitie[0]['value'])
        
         dispatcher.utter_message(message)
         return []
    except:
        pass
