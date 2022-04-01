import email
from msilib.schema import Class
import re
from tokenize import String
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    def validate_first_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        print(f"First name  = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"Họ của bạn đang không chính xác")
            return {"first_name": None}
        else:
            return {"first_name": slot_value}

    def validate_last_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        print(f"Last name = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"Tên của bạn đang không chính xác.")
            return {"last_name": None}
        else:
            return {"last_name": slot_value}

class ValidatePhoneForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_phone_form"

    def validate_phone_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `phone_number` value."""  

        print(f"Phone number = {slot_value} length = {len(slot_value)}")
        if len(slot_value) > 10 or len (slot_value) <10:
            dispatcher.utter_message(text=f"SDT không đúng")
            return {"phone_number": None}
        else:
            if slot_value[0] == '3' or slot_value[0] == '7' or slot_value[0] == '8' or slot_value[0] == '9':
                try:
                    slot_value = int(slot_value)
                    dispatcher.utter_message(text=f"SDT cua ban da chinh xac!")
                except:
                    dispatcher.utter_message(text=f"SDT cua ban hien tai dang sai!!")
                    return {"phone_number": None}
            else:
                print("ES")         
        return {"phone_number": slot_value} 


class ValidateEmailForm(FormValidationAction):
    def name(selt) ->Text:
        return "validate_email_form"

    def validate_email_address(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `email_address` value.""" 
        # nhungnguyen899@gmail.com
        value = tracker.get_slot("email_address")
        if re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)",value):
            if len(value) <6 or len(value) >255:
                print("print id")
                dispatcher.utter_message(text="valid")
                return{"email_address": value}
            else:
                print("nfhhf")
        else:
            print("inside")
            dispatcher.utter_message(text="invaild")
            return {"email_address": None}