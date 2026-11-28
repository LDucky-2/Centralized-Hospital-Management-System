# 2431059 - User stories : IT and Staff

## 1. IT Management User Stories

### User Story 1: Maintaining the System and Database

- As IT Management personnel, I want to maintain the system and database, so that CHMS remains available as an academic digital aid.
  - Supabase PostgreSQL is used in production and SQLite is used locally.
  - Alembic manages production schema changes.
  - Supabase is expected to provide backups.
  - Maintenance is performed during low usage or maintenance state, and system downtime relies on paper/manual fallback.
  - Live-compatible changes are preferred, while disruptive changes may show a maintenance state.

### User Story 2: Managing Access Levels

- As IT Management personnel, I want to configure role and account access, so that users can only reach authorized information.
  - IT manually assigns each staff account a 4-digit ID and exactly one role.
  - IT can change staff roles and manage Active, Blocked, Banned, Deactivated, and Soft-deleted states.
  - Blocking or soft-deleting a staff account invalidates active sessions immediately.
  - IT can access all patient data and view append-only audit logs.
  - Patients can self-register and receive an automatically generated 8-digit patient ID.
  - Staff cannot change their own role or self-delete their account.
  - Patient account deletion is soft deactivation and historical records remain available.

### User Story 3: Assigning Ward Nurses

- As IT Management personnel, I want to assign or reassign Ward Nurses to wards, so that ward access follows the hospital ward structure.
  - Only IT can assign or change the Ward Nurse-to-ward relationship.
  - Ward Nurse access is restricted to patients with an active assignment in that ward.

---

# 2420947 - User stories : Patient and Accountant

## 1. Patient User Stories

### User Story 1: Registering and Logging In

- As a Patient, I want to register and log in using my patient ID, so that I can access my own CHMS account.
  - Registration requires name, phone number, address, date of birth, emergency contact, and password.
  - Blood group is optional.
  - Patient login uses only the generated 8-digit patient ID and password.
  - Staff may search for a patient by ID, partial/full name, or phone number.

### User Story 2: Updating My Profile

- As a Patient, I want to update allowed profile fields, so that my contact information stays current.
  - Patients may edit name, phone number, address, date of birth, and emergency contact.
  - Patient ID and blood group are not editable.
  - IT/staff cannot edit patient identity/profile fields.

### User Story 3: Booking an Appointment

- As a Patient, I want to book an outpatient Doctor appointment, so that I can reserve a 15-minute visit.
  - Only regular/outpatient Doctors are shown.
  - Booking requires Doctor, date, and time slot.
  - No reason or appointment type is required.
  - One patient is allowed per slot.
  - Concurrent bookings cannot double-book a slot.
  - Successful booking sets status to "Scheduled".

### User Story 4: Cancelling or Rescheduling an Appointment

- As a Patient, I want to cancel or reschedule an appointment, so that I can update my visit.
  - Cancellation or rescheduling is blocked within 24 hours of the appointment.
  - Cancelling may omit a reason.
  - The cancelled record retains actor, timestamp, and optional reason.
  - Cancelled appointments remain visible until removed.
  - Patients may remove their own cancelled records.

### User Story 5: Viewing Prescription Placeholders

- As a Patient, I want to view my prescription placeholders newest first, so that I can locate historical prescription objects.
  - Prescription creation and viewing are placeholder-only.
  - Real medicine dosage, route, quantity, and duration fields are not implemented.
  - PDF/print controls show "will be implemented in the near future".
  - Patients cannot edit or delete prescription objects.

### User Story 6: Viewing Bills

- As a Patient, I want to view my bills, so that I can see charges and payment status.
  - Bills show a unique ID, date, itemized details, demo total, and Paid/Unpaid status.
  - Partial payments are not supported.
  - Manual payment is confirmed by the Accountant.
  - Online payment and receipt download/print are placeholder/demonstration features.

### User Story 7: Soft-deactivating an Account

- As a Patient, I want to deactivate my account, so that I stop using the current account.
  - Existing active ward, bill, and appointment relationships close.
  - Historical records remain linked to the old patient ID.
  - The patient may re-register and receive a new patient ID.
  - The old ID may remain visible for audit and historical staff lookup only.

## 2. Accountant User Stories

### User Story 1: Generating Patient Bills

- As an Accountant, I want to generate itemized patient bills, so that I can record hospital charges.
  - Accountants search patients by ID, name, or phone.
  - Bills may contain consultation, diagnostic test, medicine, and Service Charge lines.
  - A test bill may contain several fixed Placeholder Test entries.
  - Each bill receives a unique ID and an initial Unpaid status.
  - Pharmacy Staff may create medicine bills from fixed demo medicine lines.

### User Story 2: Editing Unpaid Bills

- As an Accountant, I want to edit Unpaid bills, so that I can correct bill line items before payment.
  - Unpaid bills are editable.
  - Paid bills are immutable.
  - Partial payments are not supported.

### User Story 3: Marking Payments Paid

- As an Accountant, I want to mark a bill Paid after manual or demonstrated payment, so that payment history is current.
  - Manual counter payments are marked Paid by the Accountant.
  - Demonstrated online payment may also mark the bill Paid.
  - No real gateway is integrated.
  - Receipt download/print is placeholder-only.

### User Story 4: Viewing Bill History

- As an Accountant, I want to view Paid and Unpaid bills, so that I can support account and patient records.
  - Search is available by patient ID, name, or bill ID.
  - Paid bills remain in all-bill and patient-bill history.
  - Paid bills cannot be edited or deleted.

---

# 2420961 (Nawrin) - User stories : Doctor and Pathologist

## 1. Common User Stories

### User Story 1: Secure Login

- As a Doctor or Pathologist, I want to log in with my staff ID and password, so that only I can use my account.
  - Valid credentials open the role-specific dashboard.
  - Invalid credentials show a clear error.
  - No clinical or patient function is reachable without authentication.

### User Story 2: Role-Based Access

- As a clinical user, I want to see only functions authorized for my role.
  - Ward Doctors cannot open outpatient scheduling or full report creation.
  - Assistants cannot open another Doctor's schedule.
  - Ward Nurses cannot open another ward's patients.
  - Direct URL/API access returns "Access denied".

### User Story 3: Access Logging

- As the hospital, I want create/update/delete and security events recorded.
  - Audit entries are append-only and IT-only.
  - Ordinary patient-record views are not logged.
  - Passwords and tokens never appear in audit records.

## 2. Doctor User Stories

### User Story 1: Viewing an Appointment Schedule

- As an outpatient Doctor, I want to view my appointments for a chosen date.
  - The list shows only the logged-in Doctor's appointments.
  - Each row shows patient name/ID, time slot, and status.
  - Empty dates show "No appointments".

### User Story 2: Cancelling an Appointment

- As an outpatient Doctor, I want to cancel a Scheduled appointment at least 24 hours before it.
  - A reason is optional.
  - The record keeps Doctor ID, optional reason, and timestamp.
  - The Doctor receives a reminder popup to call the patient.
  - Cancellation is blocked if less than 24 hours remains.

### User Story 3: Blocking Invalid Actions

- As an outpatient Doctor, I want terminal and late appointments protected.
  - Cancelled, Completed, or Missed appointments cannot be cancelled again.
  - Scheduled slots cannot be blocked directly; they must be cancelled first.

### User Story 4: Blocking Schedule Time

- As an outpatient Doctor, I want to block a slot, day, or week.
  - Blocks remain until reopened.
  - Assistants can manage the assigned Doctor's schedule.

### User Story 5: Searching Patient Records

- As an outpatient Doctor, I want to search for a patient by ID, name, or phone.
  - Exact ID, partial/full name, and phone searches are supported.
  - Unauthorized matches are not returned.

### User Story 6: Creating a Prescription Placeholder

- As an outpatient or Ward Doctor, I want to create a prescription placeholder.
  - The object is persisted with creator ID and timestamp.
  - No real medicine fields are required.
  - It is visible to authorized Patient, Ward Nurse, and Pharmacy views.
  - PDF/print controls show the near-future message.

### User Story 7: Creating a Medical Report Placeholder

- As an outpatient Doctor, I want to open the medical-report creation placeholder.
  - Confirmation creates a persisted placeholder object.
  - Opening it shows read-only near-future information.
  - It cannot be edited or deleted by a normal clinical user.

### User Story 8: Marking Appointment Outcomes

- As an outpatient Doctor, I want to mark Scheduled appointments Completed or Missed.
  - Terminal statuses cannot be cancelled.

## 3. Pathologist User Stories

### User Story 1: Creating a Pathology Placeholder

- As a Pathologist, I want to search for a patient and create a pathology placeholder.
  - No test request or sample-collection queue is implemented.
  - The object contains test name, billing status, Pathologist identity, publish date, and near-future message.
  - It is visible in the patient portal.

### User Story 2: Viewing Bill Status for a Test

- As a Pathologist, I want to see the demonstrated Paid/Unpaid bill status, so that I understand the simplified billing context.
  - Real paid-before-sample enforcement is not implemented.
  - The Pathologist directly creates/publishes the placeholder object.

## 4. Ward Doctor User Stories

### User Story 1: Viewing Ward Patients

- As a Ward Doctor, I want to review patients in my ward context.
  - Outpatient schedule access is hidden.
  - Full medical-report creation is hidden.
  - Prescription placeholders may be created.

---

# 2420961 (Nawrin) - Additional Support Staff User Stories

## 1. Ward Nurse User Stories

### User Story 1: Assigning and Transferring Patients

- As a Ward Nurse, I want to assign or transfer a patient to a ward/bed.
  - Ward, bed/room, and admission date are stored.
  - A patient has only one active ward assignment.
  - Transfer history is retained.

### User Story 2: Discharging a Patient

- As a Ward Nurse, I want to discharge a patient.
  - Discharge status, date/time, Ward Nurse ID, and optional note are stored.
  - Active ward/bed assignment is cleared.
  - Historical discharge information remains.

### User Story 3: Viewing Ward Records

- As a Ward Nurse, I want to view all report/prescription objects for patients in my ward.
  - The view is read-only.
  - Patients in another ward are denied.

## 2. Pharmacy User Stories

### User Story 1: Viewing Prescription Placeholders

- As Pharmacy Staff, I want to search patients and open prescription placeholders.
  - Search supports patient ID, name, and phone.

### User Story 2: Creating a Medicine Bill

- As Pharmacy Staff, I want to create an Unpaid medicine bill from fixed demo medicine lines.
  - Medicine 1 and Medicine 2 lines are available with fixed quantity and demo price choices.
  - The bill has a demo total.
  - Pharmacy Staff may edit it until it becomes Paid.
  - Paid bills are immutable.
