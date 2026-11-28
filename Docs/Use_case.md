---

# Centralized Hospital Management System - Use Case Narratives

## Scope and conventions

CHMS is an academic, single-hospital web prototype that operates alongside paper/manual hospital workflows. It is not intended for real clinical use or to replace a hospital.

The final implementation uses:

- React, TypeScript, and Vite;
- FastAPI and SQLModel;
- SQLite locally and PostgreSQL/Supabase in production;
- Alembic;
- PyJWT and Argon2;
- Vercel deployment.

If an older use case conflicts with this document, this document contains the final behavior.

All use cases begin from a shared login page unless stated otherwise. “Scheduled” is the active appointment status. The appointment statuses are only Scheduled, Cancelled, Completed, and Missed.

### Global placeholder convention

When a feature is explicitly marked as not implemented:

1. the UI control remains visible;
2. selecting or opening the control displays a popup/page saying “will be implemented in the near future”;
3. confirming Create persists a placeholder object with creator ID and timestamp;
4. opening the object shows read-only placeholder details and the near-future message.

This convention applies to full medical report content, external upload/report files, prescription PDF/print/detail functionality, pathology reporting, payment gateways, receipts, and password recovery.

---

## 1. Authentication and accounts

### UC-AUTH-01: Patient self-registration

- **Primary actor:** Unregistered patient
- **Preconditions:** The public registration page is available.

**Main flow**

1. The patient opens the shared sign-up page.
2. The patient enters name, phone number, address, date of birth, emergency contact, password, and optionally blood group.
3. The system validates mandatory fields and generates a unique 8-digit patient ID.
4. The system stores the Argon2 password hash and creates the Patient account.
5. The system logs account creation and opens or redirects to the login page.

**Alternative flows**

- Missing or invalid required fields: validation feedback is shown and account creation stops.
- A duplicate phone or invalid 8-digit-ID collision: the system rejects the duplicate/collision and prompts the user again.

### UC-AUTH-02: Patient login

- **Primary actor:** Patient
- **Preconditions:** A patient account exists and is active.

**Main flow**

1. The patient enters 8-digit patient ID and password on the shared login page.
2. The system verifies the Argon2 password and account state.
3. The system issues a 15-minute access token and 7-day refresh session.
4. The patient dashboard opens.

**Alternative flows**

- Wrong ID/password: a clear login error is shown and no session is created.
- Soft-deactivated account: login is denied and the account is identified as inactive.

### UC-AUTH-03: Staff login

- **Primary actor:** Staff account
- **Preconditions:** IT created the 4-digit staff ID and assigned exactly one role.

**Main flow**

1. The staff member enters 4-digit staff ID and password.
2. The system verifies credentials and account state.
3. The system issues session tokens and opens only that role's dashboard.
4. The server re-reads account role and account state for every protected request.

**Alternative flows**

- Wrong credentials or inactive account: login is denied with a clear error.
- Blocked, banned, deactivated, or soft-deleted staff account: active sessions are invalidated and login is denied.

### UC-AUTH-04: Refresh and logout

- **Primary actor:** Patient or staff

**Main flow**

1. When the access token expires, the refresh endpoint validates the secure HttpOnly/SameSite=Strict refresh cookie.
2. A valid refresh rotates the refresh token and issues a new access token.
3. Logout invalidates the current refresh session and clears the current session.

**Out of scope**

Revoke-other-device and revoke-all-device controls may be represented but are not implemented. Failed-login lockout and OTP/password recovery are also placeholder-only.

### UC-AUTH-05: Change profile or password

- **Primary actor:** Patient or staff

**Patient profile**

- Patients may edit name, phone, address, date of birth, and emergency contact.
- Blood group and patient ID are not editable after registration.
- Phone number remains searchable by staff but does not affect login.

**Password behavior**

- Profile changes use normal profile validation.
- The password-change control follows the near-future placeholder convention and does not perform a real password change.
- Password recovery and reset are also placeholder-only.

---

## 2. Patient use cases

### UC-PAT-01: Search doctor and book an appointment

- **Primary actor:** Patient
- **Preconditions:** The patient is logged in and active.

**Main flow**

1. The patient opens outpatient appointment booking.
2. The system lists regular/outpatient Doctors only.
3. The patient selects a Doctor, date, and an available 15-minute slot.
4. The system atomically verifies availability and creates a unique appointment in Scheduled status.
5. The system stores patient, Doctor, date, time, and timestamp, logs the create action, and shows confirmation.

**Alternative flows**

- No available slots: the system shows an empty-state message.
- Concurrent booking: the losing request is rejected and the patient chooses another slot.
- Ward Doctor: it is not shown for outpatient booking.

### UC-PAT-02: Cancel or reschedule an appointment

- **Primary actor:** Patient
- **Preconditions:** The appointment is Scheduled.

**Main flow**

1. The patient opens their appointment.
2. The system calculates whether at least 24 hours remain.
3. The patient confirms cancellation or opens a rescheduling selection.
4. The system changes status to Cancelled or creates the replacement schedule atomically.
5. The optional reason is recorded and the cancellation actor/timestamp are retained.

**Alternative flows**

- Less than 24 hours remain: cancellation/rescheduling is rejected.
- The selected replacement slot is unavailable: the patient chooses another slot.

### UC-PAT-03: View prescription placeholders

- **Primary actor:** Patient

**Main flow**

1. The patient opens Prescriptions.
2. The system lists prescription placeholder objects belonging to the patient, newest first.
3. The patient opens an object.
4. The detail page shows the near-future message and read-only context rather than real medicine details.

Prescription PDF/print is placeholder-only.

### UC-PAT-04: View bills and demonstrated payment

- **Primary actor:** Patient

**Main flow**

1. The patient opens Billing.
2. The system lists the patient's bills with ID, date, line items, total, and Paid/Unpaid status.
3. An Unpaid bill may open a payment placeholder.
4. Manual payment is not completed by the patient online. The Accountant confirms a counter payment and changes the bill to Paid.
5. A demonstrated online payment may update status to Paid, but no real gateway is integrated.

Paid receipt download/print is placeholder-only.

### UC-PAT-05: External report upload placeholder

- **Primary actor:** Patient

**Main flow**

1. The patient opens External Reports.
2. The system shows the near-future popup/page.
3. Confirming Create persists an external-report placeholder object for the patient.
4. Opening the object shows the near-future message and read-only metadata.

Real file validation, file storage, and report download are outside the implemented scope.

---

## 3. Doctor use cases

### UC-DOC-01: View the Doctor schedule

- **Primary actor:** Doctor

**Main flow**

1. The Doctor selects a date.
2. The system retrieves only that Doctor's Scheduled/Cancelled/Completed/Missed appointments.
3. Each row shows patient name/ID, time slot, and status.
4. An empty date shows a clear empty state.

### UC-DOC-02: Cancel an appointment and block availability

- **Primary actor:** Doctor

**Main flow**

1. The Doctor opens a Scheduled appointment.
2. If at least 24 hours remain, the Doctor confirms cancellation.
3. The system requires no reason.
4. The cancellation actor/timestamp and optional reason are stored.
5. The system opens a reminder that the Doctor should call the patient.
6. The Doctor may block the slot, day, or week indefinitely until reopened.

**Alternative flows**

- Late or terminal status: cancellation is rejected.
- An already scheduled slot: the Doctor must cancel it before blocking.

### UC-DOC-03: Search and review a patient

- **Primary actor:** Doctor

**Main flow**

1. The Doctor searches by exact patient ID, partial/full name, or phone number.
2. The system returns authorized matching patients.
3. The Doctor opens a patient and sees appointment, prescription, ward, billing summary, and released conceptual history permitted by role.
4. Reads are not audit-logged.

Unauthorized direct URL access returns Access Denied.

### UC-DOC-04: Create prescription placeholder

- **Primary actor:** Doctor

**Main flow**

1. The Doctor opens New Prescription for an authorized patient.
2. The system shows the near-future popup/page.
3. Confirming Create persists a prescription placeholder with Doctor ID and timestamp.
4. The object is newest-first and visible to authorized patient, Ward Nurse, Pharmacy, and Ward Doctor/Doctor views.

No real medicine/dosage/duration/route fields are implemented.

### UC-DOC-05: Create medical report placeholder

- **Primary actor:** Doctor

**Main flow**

1. The Doctor opens New Medical Report.
2. The system shows the near-future popup.
3. Confirming Create persists a report placeholder.
4. Opening it shows read-only near-future details.

Ward Doctors cannot create full reports.

---

## 4. Ward Doctor use cases

### UC-WDOC-01: Review ward patients

- **Primary actor:** Ward Doctor

**Main flow**

1. The Ward Doctor opens ward patient records.
2. The system shows only patients and records authorized for the Ward Doctor role.
3. The Ward Doctor can view report/prescription context and prescription history.

Ward Doctors cannot use outpatient appointment scheduling.

### UC-WDOC-02: Create prescription placeholder

- **Primary actor:** Ward Doctor

**Main flow**

1. The Ward Doctor opens a ward patient.
2. The system shows the prescription near-future popup.
3. Confirming Create persists a prescription placeholder stamped by the Ward Doctor.
4. The object becomes visible to the patient, Ward Nurses for that ward, and Pharmacy Staff.

---

## 5. Assistant use cases

### UC-ASST-01: Manage assigned Doctor's appointments

- **Primary actor:** Doctor's Assistant

**Preconditions:** An Assistant is assigned to an outpatient Doctor.

**Main flow**

1. The Assistant views appointments for the assigned Doctor.
2. The Assistant may book for a patient, cancel, reschedule, block a slot/day/week, and mark Scheduled Completed or Missed.
3. All 24-hour and slot-availability rules apply.
4. The Assistant may remove cancelled records.
5. Cancellation opens a reminder popup to call the patient.

The Assistant cannot manage another Doctor's schedule.

### UC-ASST-02: Search assigned patients

- **Primary actor:** Assistant

**Main flow**

1. The Assistant searches by patient ID, name, or phone.
2. The system returns only patients associated with the assigned Doctor.
3. The Assistant may view permitted general/appointment information.

---

## 6. Ward and discharge use cases

### UC-WARD-01: Assign or transfer a patient

- **Primary actor:** Ward Nurse

**Main flow**

1. The Ward Nurse searches or selects a patient.
2. The Ward Nurse chooses ward and bed/room.
3. The system records the active assignment and admission date.
4. Any existing active ward assignment is closed and history is retained.
5. A patient has only one active ward assignment.

### UC-WARD-02: Discharge a patient

- **Primary actor:** Ward Nurse

**Main flow**

1. The Ward Nurse opens the patient's active ward record.
2. The Ward Nurse confirms discharge and may enter a general note.
3. The system stores discharge status, date/time, Ward Nurse ID, and optional note.
4. The active ward/bed assignment is cleared.
5. Historical assignment/discharge records remain visible.

### UC-WARD-03: View ward clinical records

- **Primary actor:** Ward Nurse

**Main flow**

1. The Ward Nurse opens a patient assigned to the same ward.
2. The system displays all report/prescription objects assigned to that ward patient.
3. The view is read-only.

Direct access to a patient in another ward is denied.

---

## 7. Pharmacy use cases

### UC-PHAR-01: Search prescriptions and create medicine bill

- **Primary actor:** Pharmacy Staff

**Main flow**

1. Pharmacy Staff searches for a patient and opens a prescription placeholder.
2. The system displays fixed demo medicine choices and quantities.
3. Pharmacy Staff selects Medicine 1 or Medicine 2 lines and quantities.
4. The system creates an Unpaid medicine bill for the patient with demo prices and total.
5. Pharmacy Staff may edit the Unpaid bill until it becomes Paid.

There is no real inventory or dispensing-completed status.

---

## 8. Billing and payment use cases

### UC-ACC-01: Create and edit a bill

- **Primary actor:** Accountant

**Preconditions:** The Accountant is logged in.

**Main flow**

1. The Accountant searches a patient by ID, name, or phone.
2. The Accountant selects consultation, diagnostic-test, medicine, or service lines.
3. For tests, the Accountant may add multiple fixed placeholder test lines.
4. The system calculates a demo total and saves an Unpaid bill.
5. The Accountant may edit an Unpaid bill.

Paid bills become immutable.

### UC-ACC-02: Mark counter or demonstrated online payment Paid

- **Primary actor:** Accountant

**Main flow**

1. The Accountant receives and verifies manual counter payment by hospital process.
2. The Accountant marks the bill Paid.
3. The system logs the update and retains the bill as Paid history.

A demonstrated online-payment control may also update status to Paid. No real payment gateway is integrated.

Receipt PDF/print is placeholder-only.

### UC-ACC-03: View unpaid and paid bills

- **Primary actor:** Accountant

**Main flow**

1. The Accountant opens unpaid or all-bill views.
2. The system shows patient, bill ID, date, line items, total, and status.
3. Search/filter may use patient ID, name, or bill ID.
4. Paid bills are read-only.

---

## 9. Simplified pathology use cases

### UC-PATH-01: Create and publish pathology placeholder

- **Primary actor:** Pathologist

**Main flow**

1. The Pathologist searches for a patient.
2. The Pathologist chooses or enters a demo test name and creates a pathology placeholder.
3. The system stamps the object with Pathologist ID and publish date.
4. The patient and authorized roles see test name, billing status, Pathologist identity, publish date, and the near-future message.

There is no test request queue, sample collection, verification state, or real report file.

---

## 10. IT use cases

### UC-IT-01: Provision staff account

- **Primary actor:** IT/System Administrator

**Main flow**

1. IT opens Account Management.
2. IT enters staff details and assigns a unique 4-digit staff ID.
3. IT assigns exactly one role.
4. The system creates the Argon2 password record and logs the action.

Staff cannot self-register.

### UC-IT-02: Change role or account state

- **Primary actor:** IT/System Administrator

**Main flow**

1. IT selects a staff or patient account.
2. IT may change staff role or set Active, Blocked, Banned, Deactivated, or Soft-deleted state.
3. The system confirms the action.
4. The account state is server-enforced.
5. Blocking/banning/deactivating or soft-deleting a staff account invalidates active sessions.

Patients may soft-delete their own account.

### UC-IT-03: Assign Ward Nurses

- **Primary actor:** IT/System Administrator

**Main flow**

1. IT opens Ward Staff assignments.
2. IT assigns or reassigns a Ward Nurse to a ward.
3. The system updates the Ward Nurse's permitted ward scope.

### UC-IT-04: View audit logs

- **Primary actor:** IT/System Administrator

**Main flow**

1. IT opens Audit Logs.
2. The system shows append-only create/update/delete, login/security, role-change, account, ward, appointment, billing, and placeholder-object events.
3. Ordinary read operations are not logged.
4. Passwords and tokens are never displayed.

---

## 11. Cross-role audit use case

### UC-AUD-01: Record a security or CRUD event

- **Primary actor:** System security/audit service

**Main flow**

1. A protected write or security event occurs.
2. The system stores actor ID, role, patient/entity ID where applicable, action, entity, timestamp, IP/user-agent context, and old/new status.
3. The record is append-only.
4. Only IT can view it.
