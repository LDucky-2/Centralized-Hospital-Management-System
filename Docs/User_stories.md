# 2431059 - User stories : IT and Staff

## 1. IT Management User Stories

### User Story 1: Maintaining the System and Database

- As IT Management personnel, I want to maintain the system and database, so that the hospital's central data remains secure and operational.
  - Cloud databases are to be used, and backed up daily.
  - Maintenance/change/updates should be done late at night when system usage is at its lowest, unless in case of critical failure that can harm the users of the patients.
  - if a change or update can be done live then should be done live, otherwise the system has to be shut off.

### User Story 2: Managing Access Levels

- As IT Management personnel, I want to configure different access levels for different users, so that users can only view the information they are authorized/need to know.
  - IT Management manually assigns new user roles (e.g., Doctor, Assistant, Pathologist, Accounts) during account creation (not patients).
  - Patients can only view their own reports, bills, and appointments and upload test reports if done from another hospital(but must not forget to bring the physical copy of the results).
  - Pathologists can check previous test reports, and tests that the doctor has given to the patient and upload new test reports.
  - Ward nurses can see prescribed medication, doctor’s comments.
  - Pharmacy staff can check prescribed medication.
  - Assistants and accounts staff can see payment receipts(includes anyone that normally has to check bill receipts)
  - Doctors have full access to medical and test histories of the patients and can upload new reports.
  - Access permissions are to be managed by IT administrators.

## 2. Other Staff (Assistants, Pharmacy Staff, Ward Nurses, Ward doctor etc.) User Stories

### User Story 1: Checking Patient Information

- User Story: As staff, I want to check patient information, so that I can assist with hospital tasks according to my needs.
  - Ward nurses can check the prescriptions and reports of the patients that are assigned to the ward same as them.
  - Assistants can view appointments, payment receipts and general information of the patient assigned to their doctor
  - Pharmacy staff can view patient prescriptions.
  - Ward doctors have the same authority as doctors.
  - Staff can search using the patient's unique ID number or registered phone number in the central database.
  - Staff views are generally read-only.
  - Ward doctors can update and add prescriptions.
  - Assistants can update appointment scheduling details can cancel or make appointments.

### User Story 2: Verifying Bill Receipts

- User Story: As staff, I want to see the receipts of bills to see if a patient has paid, so that I can confirm payment status.
  - Receipts show a status tag(paid or unpaid), all payment receipts(previous or current) will show up without exception.
  - Staff can view and print digital receipts directly from the central database.
  - The status remains marked as "Unpaid," requiring the patient to retry or pay through the manual accounts counter.

### User Story 3: Managing and Canceling Appointments

- User Story: As a doctor's assistant, I want to be able to cancel or block appointments if necessary, so that the patients do not come for nothing.
  - Appointments can be cancelled by assistants at most a day before the scheduled slot takes place.
  - A cancellation notification is sent to the patient via the online interface or system dashboard.(the assistant should also call the person)
  - A cancelled appointment frees up the slot instantly in the system schedule.
  - A simple text field allows assistants to optionally note the reason for cancellation if needed.
  - Can block appointments for a (week/day/slot) so that no more appointments can be made.

---
# 2420947 - User stories : Patient and Accountant


## 1. Patient User Stories


### User Story 1: Booking an Appointment


- User Story: As a Patient, I want to book an appointment, so that I can consult a doctor at a suitable date and time.
  - Patients must log in to their accounts before booking an appointment.
  - Patients can select a doctor from the available doctors list.
  - The system displays the selected doctor's available dates and time slots.
  - Patients can choose a suitable appointment date and time.
  - The system must prevent multiple patients from booking the same doctor's appointment slot.
  - The system checks the availability of the selected slot before confirming the appointment.
  - Patients must provide the necessary appointment information before submitting a booking request.
  - After successful booking, the system generates a unique appointment ID.
  - The appointment status is automatically marked as "Confirmed" after successful booking.
  - Patients can view their appointment details, including doctor name, appointment date, time, and appointment ID.
  - The system sends an appointment confirmation notification to the patient through the system dashboard.
  - If the selected slot is unavailable, the system displays a message asking the patient to choose another slot.


### User Story 2: Viewing Prescriptions


- User Story: As a Patient, I want to view my prescriptions, so that I can follow the doctor's instructions and understand my prescribed medications.
  - Patients must log in to their accounts to access their prescriptions.
  - Patients can view prescriptions issued by their doctors.
  - Each prescription should contain the doctor's name, prescription date, and patient information.
  - The system displays prescribed medicine names, dosage, frequency, and duration.
  - Patients can view the doctor's instructions and additional medical advice.
  - Patients can access their previous prescriptions for future reference.
  - Prescriptions should be arranged according to their issue dates, with the latest prescription appearing first.
  - Patients can download or print their prescriptions for personal use.
  - Patients can only access their own prescriptions.
  - Patients cannot modify or delete prescriptions uploaded by doctors.
  - If no prescription is available, the system displays an appropriate message.


### User Story 3: Paying Hospital Bills


- User Story: As a Patient, I want to pay my hospital bills, so that I can complete my payments.
  - Patients must log in to their accounts to access their billing information.
  - Patients can view all their previous and current hospital bills.
  - Each bill should contain a unique bill ID, bill date, patient information, service details, and total payable amount.
  - Bills should include relevant charges such as consultation fees, diagnostic test fees, medicine charges, and other hospital service charges.
  - Patients can check the payment status of each bill.
  - The system displays payment statuses such as "Paid", "Unpaid".
  - Patients can select an unpaid bill to proceed with payment.
  - The system provides available payment methods.
  - After successful online payment, the system automatically updates the bill status to "Paid".
  - If a payment fails, the system keeps the bill status as "Unpaid".
  - The system generates a digital payment receipt after successful payment.
  - Patients can view, download, or print their payment receipts.


## 2. Accountant User Stories


### User Story 1: Generating Patient Bills


- User Story: As an Accountant, I want to generate patient bills, so that patients can view their hospital charges and complete their payments.
  - Accountants must log in using their authorized accounts to access the billing management system.
  - Accountants can search for patients using their unique patient ID or registered phone number.
  - The system displays the patient's basic information and relevant hospital service records.
  - Accountants can generate bills based on services received by patients.
  - Bills may include consultation fees, diagnostic test charges, medicine costs, admission fees, and other hospital service charges.
  - Each bill must contain a unique bill ID.
  - The bill should include the patient's name, patient ID, bill date, service descriptions, individual charges, and total payable amount.
  - The system automatically calculates the total bill amount based on the entered charges.
  - Accountants can review the bill before generating it.
  - After successful generation, the bill is saved in the central database.
  - The generated bill becomes available in the patient's account.
  - The initial payment status of a newly generated bill is marked as "Unpaid".
  - Accountants can view previously generated bills for reference.


### User Story 2: Viewing Unpaid Bills


- User Story: As an Accountant, I want to view unpaid bills, so that I can identify outstanding payments and monitor the hospital's pending revenue.
  - Accountants must log in to access the unpaid bills section.
  - The system displays all patient bills with an "Unpaid" status.
  - Accountants can search for unpaid bills using the patient ID, patient name, or bill ID.
  - Each unpaid bill should display the patient's name, bill ID, bill date, total amount, and outstanding amount.
  - Accountants can filter unpaid bills according to bill date or patient information.
  - The system should display partially paid bills separately from fully unpaid bills.
  - Accountants can view the payment history of each bill.
  - The system automatically removes a bill from the unpaid list when its full payment is completed.
  - Accountants can identify patients who have outstanding balances.
  - Accountants can print or download unpaid bill information for record-keeping purposes.
  - The system should display an appropriate message if there are no unpaid bills.


---
