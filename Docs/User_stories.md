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
  - Assistants can update appointment scheduling details(can cancel or make appointments.

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