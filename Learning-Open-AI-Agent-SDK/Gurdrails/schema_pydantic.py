# Import Pydantic for data validation and structure
from pydantic import BaseModel

# Data structure for input guardrail responses
# This ensures consistent output format from the guardrail agent


class Input_guardrail_schema(BaseModel):
    is_hotel_Hezzi_query: bool  # True = hotel-related query, False = not hotel-related
    reason: str                 # Explanation for the decision

# This is our data structure for output guardrail.


class Output_guardrail_schema(BaseModel):
    is_hotel_Hezzi_answer: bool
    is_hotel_Hezzi_account_tax_details: bool
    reason: str
