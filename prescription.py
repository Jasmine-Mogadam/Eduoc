from taipy import Gui
from taipy import Config
from taipy import Core
from taipy.gui import Markdown

page = """
<h3 class="h5">ManagMed</h3>
# Prescriptions

## Medication Name
*Insert Medication Name Here*

## Description
Provide a brief description of the medication, including its purpose and primary use.

## Dosage Instructions
### General Guidelines
- **Dosage Form:** *Insert form (tablet, capsule, liquid, etc.)*
- **Dosage Strength:** *Insert strength (e.g., 250mg, 500mg, etc.)*

### Standard Dosage
- Adults: *Insert recommended dosage for adults*
- Children: *Insert recommended dosage for children*
  
## Administration
- *Insert instructions on how to take the medication (with or without food, at specific times of the day, etc.)*

## Special Instructions
- *Include any special instructions or precautions, such as avoiding certain foods or activities while taking the medication.*

## Side Effects
- *List potential side effects or reactions that may occur. Include when to seek medical attention.*

## Storage
- *Provide information on how and where to store the medication (e.g., room temperature, away from sunlight, etc.).*

## Missed Dose
- *Include instructions on what to do if a dose is missed and when the next dose should be taken.*

## Overdose
- *Provide information on the signs of overdose and what steps to take in case of an overdose.*

## Interactions
- *List known drug interactions and any substances to avoid while taking the medication.*

## Consultation
- *Advise users to consult with a healthcare professional for personalized advice and guidance.*

**Note:** This is a placeholder text. Please replace the generic information with specific details about the medication you are referring to.

"""
