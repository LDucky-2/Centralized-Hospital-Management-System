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
 2420961(Nawrin) - User stories : Doctor and Pathologist


## 1. Common (Both Roles) User Stories


### User Story 1: Secure Login


- User Story: As a Doctor or Pathologist, I want to log in with my user ID and password, so that only I can use my account.
  - Given a valid user ID and password, the role dashboard opens.
  - Given a wrong password, the message "Invalid user ID or password" appears and no session starts.
  - No function or patient data is reachable without login.


### User Story 2: Role-Based Access


- User Story: As a user, I want to see only the functions of my role, so that I cannot reach data I am not allowed to use.
  - A Doctor's menu shows no Pathologist functions, and a Pathologist's menu shows no Doctor functions.
  - Opening a Pathologist function's address while logged in as a Doctor returns "Access denied", and the reverse also holds.


### User Story 3: Access Logging


- User Story: As the hospital, I want every view or change of patient data recorded, so that misuse can be traced.
  - After a Doctor opens a patient's history, the access log holds a row with user ID, patient ID, action and date-time.


## 2. Doctor User Stories


### User Story 1: Viewing Appointment Schedule


- User Story: As a Doctor, I want to see my appointments for a chosen date, so that I can plan my clinic session.
  - The list shows only the logged-in Doctor's appointments for that date, each with time, patient name, patient ID and status.
  - A date with no appointments shows "No appointments".


### User Story 2: Canceling Appointment


- User Story: As a Doctor, I want to cancel an appointment when necessary, so that the patient's slot is not wasted.
  - For a Scheduled appointment, entering a reason and confirming sets the status to Cancelled and stores reason, Doctor ID and time.
  - Confirming without a reason is not allowed.


### User Story 3: Blocking Invalid Cancellation


- User Story: As a Doctor, I want the system to stop me cancelling an appointment that is already finished, so that records stay correct.
  - Cancelling an appointment in Completed, Cancelled or Missed status is rejected and the current status is shown.


### User Story 4: Searching Patient


- User Story: As a Doctor, I want to find a patient by ID or name, so that I open the right record.
  - Searching by exact patient ID returns that patient only.
  - Searching by part of a name returns every matching patient the Doctor may access (SEC-06) and no others.


### User Story 5: Viewing Medical History


- User Story: As a Doctor, I want to see all of a patient's previous medical and test reports, so that I can diagnose using the full history.
  - The history lists every medical report and every Released test report of the patient, newest first, each with date, type and author.
  - A patient with no records shows "No previous records".


### User Story 6: Viewing Released Test Report


- User Story: As a Doctor, I want to open a released test report with its file, so that I can read the exact results.
  - Opening a Released report shows result values, out-of-range flags, verifying Pathologist, release date and the attached file.


### User Story 7: Hiding Unverified Reports


- User Story: As a Doctor, I want to see only verified reports, so that I never act on unchecked results.
  - A report in Draft or Pending Verification status does not appear in the history, and opening it directly shows "Report not yet available".


### User Story 8: Adding Medical Report


- User Story: As a Doctor, I want to add a medical report with diagnosis, notes and prescription, so that the next Doctor can see what I found.
  - Saving a report with a diagnosis stores it in the patient's record and it appears at the top of the history.
  - Saving with an empty diagnosis is rejected; an attached file outside is rejected.


### User Story 9: Protecting Saved Reports


- User Story: As a Doctor, I want saved medical reports to be unchangeable, so that the record is trustworthy.
  - A saved report carries the Doctor's ID and date-time and offers no edit or delete option.
  - A correction is saved as a new report linked to the original, and both remain visible.


## 3. Pathologist User Stories


### User Story 1: Viewing Test Requests


- User Story: As a Pathologist, I want to see all open test requests with urgent ones first, so that I work in the right order.
  - The list contains every request in Requested, Awaiting Payment, Sample Collected or In Progress status, Urgent first, then oldest first.
  - Each row shows request ID, patient ID, patient name, test type, priority, requesting Doctor and request date-time.


### User Story 2: Checking Payment Receipt


- User Story: As a Pathologist, I want to see whether the patient has paid for a test, so that I do not have to send them to billing to ask.
  - The request shows Paid (with receipt number and date) or Not Paid.


### User Story 3: Recording Sample Collection


- User Story: As a Pathologist, I want to record that a sample was taken, so that the request moves to testing.
  - With receipt status Paid, entering sample type and collection time sets the request to Sample Collected.


### User Story 4: Holding Unpaid Requests


- User Story: As a Pathologist, I want unpaid requests held, so that tests are not processed before payment.
  - With receipt status Not Paid, the sample is not recorded and the request status becomes Awaiting Payment.


### User Story 5: Rejecting Sample


- User Story: As a Pathologist, I want to reject an unsuitable sample with a reason, so that a new sample is collected.
  - Rejecting a Sample Collected request with a reason returns it to Requested and stores the reason.


### User Story 6: Entering Test Results


- User Story: As a Pathologist, I want to enter the result of each test parameter, so that results are stored centrally.
  - Saving valid values creates a Draft Test Report and sets the request to In Progress.
  - A Draft can be reopened and edited before submission.


### User Story 7: Validating Results


- User Story: As a Pathologist, I want the system to check my entries, so that typing errors are caught before release.
  - An empty mandatory field or text in a numeric field blocks the save and highlights the field.
  - A value outside a defined reference range is saved with a visible flag.


### User Story 8: Uploading Test Report


- User Story: As a Pathologist, I want to attach the formal report file and submit it, so that it can be verified.
  - Attaching a valid file and selecting "Submit for verification" sets the report to Pending Verification.
  - A file of the wrong type or over 10 MB is rejected and the report stays Draft.


### User Story 9: Releasing Verified Report


- User Story: As a Pathologist, I want to approve a checked report, so that the Doctor can see it.
  - Approving a Pending Verification report sets it to Released, sets its request to Completed, and the report becomes visible to the requesting Doctor.


### User Story 10: Rejecting Report at Verification


- User Story: As a Pathologist, I want to send a report back with a reason when I find an error, so that it is corrected before release.
  - Rejecting with a reason returns the report to Draft; the Doctor still cannot see it.


### User Story 11: Locking Released Report


- User Story: As the hospital, I want released reports to record who verified them and to be locked, so that results cannot be changed silently.
  - A Released report shows verifier ID and time, and no user is offered an edit option.
