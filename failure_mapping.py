import openai
import os

# Set up OpenAI API credentials
openai.api_key = "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"

# Define lists
failure_events = [
    "REMOVE AND REPLACE CYRUS OIL METERING PUMP P01101A",
    "Investigate high temperature in Kinnoull Metering mag drive pump",
    "Sand Jet Mechanical Seal Leaking - investigate and replace seal.",
    "P-04101B MOL Booster Pump Seal Oil Pipework Removal and Replacement to Remove Restriction",
    "TAHH-33122 'W' winding temp in trip with Pump offline.",
    "LP Flare pump internal investigation",
    "LP flare pump replacement (check new pump arrived)",
    "Remove failed LP flare pump and return to beach for overhaul",
    "Repair/Replace Leaking Mechanical seals on Mol Pump A",
    "2019 OUTAGE EMERGEN - Removal of sand jetting pump for repair",
    "Re-instate sand jetting pump P-16102",
    "MOL pump B DE seal replacement",
    "MOL Pump A Preservation until DE/NDE Seal changes (week 6)",
    "Remove pump and send onshore for overhaul"
]

failure_modes = [
    "shaft bent resulting in misalignment",
    "shaft cracked|sheared resulting in cracked shaft",
    "mechanical seal worn|damaged|contaminated|overheated resulting in seal fault",
    "bearing seal wear, rub resulting in seal rub",
    "bearing increased friction from lack of lubrication resulting in lack of lubrication",
    "piston seal piston contact with plunger resulting in seal fault",
    "bleed valve Valve faulty or incorrectly set so piston makes contact with plunger resulting in bleed valve failure",
    "diaphragm ruptured resulting in diaphragm failure",
    "hydrodynamic bearing end of life resulting in hydrodynamic bearing fault",
    "hydrodynamic bearing overload resulting in hydrodynamic bearing fault",
    "impellor eccentric on shaft resulting in impellor fault",
    "impellor eccentric in housing resulting in impellor fault",
    "process fluid cavitation resulting in cavitation",
    "strainer blocked resulting in poor flow",
    "wear ring excessive clearance resulting in flow loss",
    "discharge check valve blocked resulting in poor flow",
    "bearing end of life resulting in antifriction bearing defect",
    "SFL bearing lack of sold film lubrication resulting in lack of lubrication",
    "bearing Bearing failure due to other failures (binding, scoring, false brinneling, fretting).  resulting in antifriction bearing defect",
    "impellor imbalance resulting in impellor fault"
]

# Set up the prompt to send to the API
prompt = "There are two lists: failure events and failure modes. Look at each failure event and identify failure modes from the failure modes list that could be the cause of the failure event. Then provide the likelihood of matching as percentages. If there are no apparent matches, do not show a match. Then return the results in a table with the following two columns: [failure event], [possible failure modes and likelihood of matching]. Do not change the wording of either the failure events or failure modes. Here is the failure events list: {}. Here is the failure modes list: {}".format(failure_events,failure_modes)

# Set up the API parameters
model_engine = "text-davinci-002"
temperature = 0.1
max_tokens = 1024

# Send the prompt to the API and get the response
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
)

# Print the response text
print(response.choices[0].text.strip())

