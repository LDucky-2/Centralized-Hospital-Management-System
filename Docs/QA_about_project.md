
---
### 1. Core Documentation & Architecture - First Clarification Pass

*These sections establish what your system is, how it is structured, and the rules your team followed to build it.*

* **1. Software Requirements Specification (SRS):** Functional/non-functional requirements following your course guidelines.
* **2. Software Design Specification (SDS):** UML Use Case diagrams + narratives, UML State diagrams, and Level 0 DFD.
* **4. Architectural Pattern:** Your chosen pattern (e.g., MVC, MVVM, Layered, Microservices), why you chose it, and how your folder/code structure implements it.
* **5. Coding Standards and Guidelines:** Naming conventions, formatting rules, and best practices, backed by actual snippets from your codebase.

### 2. Implementation & UI Design

*These sections showcase the actual product you built and prove it meets usability standards.*

* **7. UI Design:** High-resolution screenshots of your main screens/pages with brief explanations of what each screen does.
* **8. Nielsen's Usability Heuristics:** The evaluation tools/plugins you used (e.g., Lighthouse, WAVE, Axe, or heuristic checklist tools) and how they helped improve your UI.

### 3. Code Quality, Tooling & Testing

*These sections prove your code is maintainable, documented, and bug-free.*

* **6. Source Code Documentation Tool:** Setup instructions, comment conventions (e.g., JSDoc, Javadoc, Doxygen, Sphinx), sample commented code, and screenshots of the generated docs.
* **9. Code Review Tools and Findings:** Static analysis tools (e.g., SonarQube, ESLint, Pylint, CodeClimate) plus screenshots and explanations of **at least 5 bugs/code smells** found and how you fixed them.
* **11. Unit Testing (Test Coverage and Quality):** Representative test cases showing normal inputs, boundary conditions, invalid inputs, and edge cases/exceptions.

### 4. Project Management & Workflow Evidence

*These sections prove your team collaborated properly and used version control throughout the semester.*

* **3. Evidence of Trello and Discord Usage:** Screenshots of boards, task cards, Sprint movement, and Discord channels/discussions with brief captions.
* **10. Evidence of Usage of Git:** Screenshots of your GitHub repository showing branches, pull requests, commit history, and version tags.

### 5. Team Accountability & Final Packaging

*These items wrap up the submission requirements across both platforms.*

* **12. Individual Team Member Contributions:** A clear breakdown (a table works great here) mapping each member to their assigned roles and actual deliverables across coding, docs, UI, and testing.
* **Dual-Platform Formatting (N.B.):**
* **Google Classroom:** Compiled into one cohesive, well-formatted PDF/DOCX report.
* **GitHub Wiki:** Broken out into **12 separate Wiki pages** (one per section).

---

# Project Understanding and Clarification Questions

Please answer each numbered question directly below it by replacing `[Answer: ]` with your decision.

## 1. Project scope and boundaries

1. Should CHMS be submitted as a complete hospital replacement or explicitly as a digital aid operating alongside paper/manual workflows?
   - [Answer: ]
2. How many hospital locations or branches should the centralized database support in this semester's implementation?
   - [Answer: ]
3. Should the project support outpatient doctors, ward doctors, wards, pharmacy, laboratory, accounts, assistants, nurses, and IT in the final implementation?
   - [Answer: ]
4. Should emergency department, operating theatre, inpatient admission/discharge, inventory, staff scheduling, and ambulance services remain outside the scope?
   - [Answer: ]
5. Is the system intended to support real medical use or only a simulated academic prototype?
   - [Answer: ]
6. Should all features described in the SRS and use-case narratives be implemented, or may some remain documented-only demonstrations?
   - [Answer: ]

Answer: This is only a academic project

## 2. General product and architecture decisions

7. Confirm the implementation stack: React, TypeScript, Vite, FastAPI, SQLModel, PostgreSQL/Supabase, SQLite, Alembic, PyJWT, Argon2, and Vercel.
   - [Answer: yes]
8. Should the backend use the example project's feature-folder architecture: router, schema, service, repository, and dependencies?
   - [Answer: yes]
9. Should the frontend use the example project's page/component/context/API-service structure?
   - [Answer: yes]
10. Do you want full source code, an implementation report, a video demo, screenshots, and the report PDF/DOCX in the final submission?
    - [Answer: i will take of this later, you dont have to worry now]
11. Will CHMS be deployed to a live Vercel URL for testing and evidence screenshots?
    - [Answer: yes it will be deployed to a live vercel]
12. Should the project use PostgreSQL in production and SQLite only for local development and testing?
    - [Answer: yes but i will also connect it to supabase]

## 3. Users and roles

13. Confirm all staff roles: Doctor, Ward Doctor, Assistant, Pathologist, Accountant, Ward Nurse, Pharmacy Staff, and IT Management/System Administrator.
    - [Answer: yes]
14. Should there be separate user accounts for Patient and each staff role, or can some roles share an account type?
    - [Answer: separate]
15. Can one staff member hold more than one role, or is exactly one role assigned per account?
    - [Answer: no]
16. If exactly one role, should Ward Doctor be a separate role from Doctor?
    - [Answer: yes, they are in fact separate]
17. Should IT administrators be able to view patient data for maintenance, or should they only manage accounts and infrastructure?
    - [Answer: they can access everything]
18. Is IT allowed to change staff roles after account creation?
    - [Answer: yes]
19. Should IT be able to ban, deactivate, lock, or reset staff and patient accounts?
    - [Answer: yes, even delete account]
20. Should roles and permissions be stored server-side and read on every request rather than only trusted from the JWT?
    - [Answer: just do it as the example project did]

## 4. Patient registration and login

21. What mandatory fields are required for patient registration: name, phone number, address, date of birth, blood group, emergency contact, password, or others?
    - [Answer: no more needed]
22. Should patient login use a unique patient ID, registered phone number, email, or a combination?
    - [Answer: patient id only]
23. Are phone numbers and patient IDs unique, and is email supported or not?
    - [Answer: email is not supported, patient_id is unique]
24. Should patient sign-up be public, require verification, or require staff approval?
    - [Answer: public]
25. Is an OTP or email verification required for registration or password recovery?
    - [Answer: yes, but will not be implemented]
26. Should staff receive manually assigned usernames and passwords created by IT?
    - [Answer: yes]
27. Should passwords require a minimum length or character complexity?
    - [Answer: not really just 4 digits is enough]
28. How many failed login attempts should trigger the 15-minute lockout, and should the patient and staff lockout rules be identical?
    - [Answer: will not be implemented]
29. Should access tokens expire after 15 minutes, 5 minutes, or another duration?
    - [Answer: 15 min]
30. Should refresh tokens expire after 7 days or another duration?
    - [Answer: 7]
31. Should patients and staff be able to log out of one device, all devices, or everywhere?
    - [Answer: they can log out of the device being used. the other options will be there but not implemented]
32. Should users be able to change their own profile details or password?
    - [Answer: yes]

## 5. Patient profile and search

33. Is the unique patient ID an internally generated UUID, a human-readable hospital number, or a number following a specific format?
    - [Answer: just an 8 digit number]
34. What patient information may each role view: name, age, sex, phone, address, emergency contact, insurance, and ward?
    - [Answer: ]
35. Should staff be allowed to search by partial name, exact ID, phone number, or a combination?
    - [Answer: ]
36. Should staff search results distinguish authorized and unauthorized patients, or should unauthorized matches not be revealed?
    - [Answer: ]
37. Should patients have to confirm or select identity details before accessing a record?
    - [Answer: ]
-  go through the srs.tex, user stories and use case, then re iterate the role based views and then ask questions  - use this context to make the questions again after this conversation

## 6. Appointments

38. Which doctors are eligible for outpatient online appointment booking: only Doctor or also Ward Doctor?
    - [Answer:only doctors ]
39. Should appointments use fixed time-slot durations, and if so, what duration should one slot have?
    - [Answer: 15mins]
40. Should a doctor have configurable working dates, working hours, break times, and consultation capacity?
    - [Answer: the view for slots is a place where he can disable slots and days]
41. Can one doctor accept more than one patient in a slot, or must every slot be exclusive?
    - [Answer:no, must be exclusive ]
42. Should patients be allowed to book, reschedule, and cancel appointments?
    - [Answer: yes]
43. If rescheduling is included, when and how many times can it occur?
    - [Answer: howevermanytimes but also follows cancelation rules of 24 hours]
44. Confirm the cancellation rule: at least 24 hours before the appointment for patients and assistants.
    - [Answer: yes]
45. Confirm whether doctors can cancel with or without a reason. The SRS and use cases currently differ.
    - [Answer: without reason]
46. Should an assistant always require a cancellation reason?
    - [Answer: no]
47. Which statuses should exist: Requested, Confirmed, Scheduled, Cancelled, Completed, Missed, or others?
    - [Answer: scheduled, cancelled,completed,missed]
48. When should Confirmed become Scheduled or Completed, and who changes it?
    - [Answer: q49 and q47 explains]
49. Can a doctor or assistant mark a patient as Missed or Completed?
    - [Answer:yes ]
50. Should blocked slots be reusable after the blocked period ends?
    - [Answer: there is no period, they are indefinitly blocked until re opened]
51. Can an assistant block a single slot, day, week, or each option?
    - [Answer: all options given, both doctor and assistant can block]
52. Should concurrent appointment booking use database locking or a conditional database update?
    - [Answer:just pick one first and then the next ]
53. What should happen to a patient's appointment if the doctor blocks it after booking?
    - [Answer: cant block a schelduled one, have to cancel, which can be done by both asistant and doctor]
54. What dashboard notification, SMS, email, or phone fallback should occur for booking and cancellation?
    - [Answer:sms but will not be implemented, but after cancellation the staff should be reminded to phone the patient with a call(only if done by staff) ]
55. Should a cancelled appointment immediately disappear from the patient list or remain visible as a cancelled record?
    - [Answer: remain visible as a cancelled record, but assistant and doctor can remove it afterwards]

## 7. Prescriptions and medical reports

56. Which fields are mandatory in a medical report: diagnosis, clinical notes, prescription details, or just diagnosis?
    - [Answer: so report generation will not be implemented]
57. Should diagnosis, notes, and prescription be separate records or parts of one medical report?
    - [Answer: yes]
58. What medicine fields are required: name, dosage, frequency, duration, route, instructions, quantity, or repeats?
    - [Answer: will not be implemented]
59. Should doctors be able to add prescriptions independently of a medical report?
    - [Answer: yes  and ward doctors too]
60. Confirm the exact permissions: the SRS says Ward Doctor can add medical reports and prescriptions, while the use case narrows Ward Doctor to prescriptions only.
    - [Answer: ward doctors can only add prescriptions]
61. Should ward prescriptions be visible immediately to the ward nurse, pharmacy staff, and patient?
    - [Answer: should be visible to all]
62. Should an outpatient prescription be visible to pharmacy staff before a paid bill exists?
    - [Answer: i didnt undeeerstand what you asked, what is outpatient]
63. Should saved medical reports and prescriptions be completely immutable, or should addenda be the only permitted correction?
    - [Answer: immutable]
64. Should external patient uploads be visible to doctors before physical verification?
    - [Answer: yes]
65. What file formats are supported for external reports and medical attachments?
    - [Answer: pdf or img but this feature will not be implemented]
66. Confirm the maximum file size: 10 MB for both external and pathology files.
    - [Answer: yes]
67. Should files be stored in Supabase Storage or directly in the database?
    - [Answer: supabase]
68. Should prescriptions appear newest first, and should all past prescriptions remain viewable?
    - [Answer:newest first ]
69. Should patients be able to print or download the original file and a system-generated prescription PDF?
    - [Answer: yes, but this feature will not be implemented]

## 8. Pathology workflow

70. Which test types and parameter definitions should the demo include?
    - [Answer: ]
71. Who creates a test request: Doctor, Ward Doctor, Assistant, or another actor?
    - [Answer: doctor, not really initiates, but the report contains the tests to be done]
72. Should Ward Doctors be able to request tests for admitted patients?
    - [Answer: yes]
73. What test-request statuses are required: Requested, Awaiting Payment, Sample Collected, In Progress, Completed, Rejected, or others?
    - [Answer: this things is not important so remove this]
74. Should urgent requests always sort before normal requests?
    - [Answer: there will be no request system]
75. Should an unpaid test request remain in Awaiting Payment until the patient pays?
    - [Answer: there is no awaiting system too]
76. Should pathologists be allowed to collect and record a sample only after Paid status is confirmed?
    - [Answer: ]
77. What sample types should the system offer or validate?
    - [Answer: ]
78. Should a rejected sample return the request to Requested, preserve the rejection reason, and require re-collection?
    - [Answer: ]
79. Is report verification by the same pathologist who entered the draft acceptable, or should a separate verifier release it?
    - [Answer: ]
80. Should final clinical/laboratory comments be mandatory before release?
    - [Answer: ]
81. Should a verification rejection require a mandatory reason and return the report to Draft?
    - [Answer: ]
82. What happens to a report after it is Released: no edit, no delete, no superseding file, or addendum only?
    - [Answer: ]
83. Should released reports be visible to the requesting doctor, all authorized doctors, ward doctors, and the patient?
    - [Answer: ]
84. Should patients see test reports before the requesting doctor sees them?
    - [Answer: ]
85. Should report parameter reference ranges be predefined by test type, configurable, or manually entered?
    - [Answer: ]
86. Should numeric values with units, normal ranges, and visible out-of-range flags be included?
    - [Answer: ]
87. Should draft reports be hidden from all doctors and patients?
    - [Answer: ]
- so how it will work is doctor will mention some tests in report, the patient will go to accountant and get bills made for tests which the patient can then pay(either manually or over the internet) after that the patient will go to the pathology deparment and just show em that the ppayment was done and then the tests will be done and then published to the patient portal     - use this context to make the questions again after this conversation



## 9. Billing and payments

88. Which hospital services can be added to a bill: consultation, diagnostic tests, medicines, admission fees, "stay fee"?
    - [Answer: good enough, the "stay fee" is basically the payment for being in the hospital - change the name to smth more relevent]
89. Can account staff edit a bill after generation?
    - [Answer: yes]
90. Should the bill table support partial payments or only fully Paid/Unpaid statuses?
    - [Answer: fully paid]
91. How is a partial payment applied to a bill, and what outstanding amount rules apply?
    - [Answer: partial payments not allowed]
92. Should bills support discounts, refunds, tax, insurance, or waived charges?
    - [Answer: it would, but wont be implemented]
93. Should accountants be able to view and confirm manual counter payments?
    - [Answer: yes, they can manually check the online bill to be complete if the patient has paid manually.(has to upload the reciept - but wont be implemented)]
94. Is any real payment gateway integrated, or is it only simulated as in the SRS?
    - [Answer: wont be implemented]
95. If simulated, should it mimic bKash, cards, bank transfer, or a generic successful/failed payment flow?
    - [Answer: it would but wont be implemented]
96. Should a failed or cancelled online payment create no receipt and leave the bill Unpaid?
    - [Answer: yes]
97. Should every successful payment create a unique receipt ID and a downloadable/printable digital receipt?
    - [Answer: yes, but download able part will not be implemented]
98. Should receipts include the patient, bill, payment method, amount, date, transaction ID, and accountant/gateway reference?
    - [Answer: yes, but wont be implemented]
99. Should all staff who are allowed to verify receipts see previous and current receipts?
    - [Answer:yes ]
100. Is a manual payment marked Paid immediately, or must it be approved/reconciled?
    - [Answer: the accountant  can mark the bill paid after recieving manual payment]

## 10. Ward and support staff workflows

101. How is a patient assigned to a ward and to a ward nurse?
    - [Answer: patient are assigned to a ward, ward nurses are also assigned to wards]
102. Should ward doctors be permitted to create reports and prescriptions but not outpatient schedules?
    - [Answer: only prescriptions]
103. Should ward nurses see all prescriptions and reports for their ward or only active, assigned, or recent records?
    - [Answer: they can see patients assinged to the same ward as them, and see their reports and prescriptions]
104. Should ward nurses have read-only access to the complete ward patient record or only medication and doctor notes?
    - [Answer: read only access to reports and prescriptions of patient assigned to the same ward as the ward nurse]
105. Should ward assignments change as patients are transferred or discharged?
    - [Answer:yes ]
106. How is an assistant assigned to a specific doctor?
    - [Answer: just assinged like dropdown choose doctors available, can be changed too, by IT*]
107. Should assistants see only their doctor's patients and schedules or all general patient information?
    - [Answer: only their doctors]
108. Should assistants be able to create appointments as well as cancel, block, and update them?
    - [Answer: can do all]
109. Should pharmacy staff see a prescription only after it is issued or only after it is paid and ready for dispensing?
    - [Answer: - so how this works, the prescriptions have medicine written that the pharmacy staff can search to see, and create a bill for the patient if the patiennt choses to buy the medicine form pharmacy]
110. Should pharmacy staff mark medicines as dispensed or keep the workflow read-only?
    - [Answer:read Q109 - use this context to make the questions again after this conversation]

## 11. Security and audit logging

111. Should every patient data view be logged, or only create, update, and delete actions? The SRS and use cases conflict.
    - [Answer: only crud actions]
112. If read logging is included, should the history be append-only and visible only to IT or administrators?
    - [Answer: append-only, yes visible to only IT Admins]
113. Which fields must be in each audit entry: user ID, role, patient ID, action, entity, IP address, user agent, and timestamp?
    - [Answer: good enough]
114. Should audit logs be immutable and protected from all normal user roles?
    - [Answer: immutable, nobody else can see other than IT]
115. Should login success and failure be included in the audit/security log?
    - [Answer: yes]
116. Should refresh-token reuse, forged tokens, denied access, and security events be logged?
    - [Answer: yes]
117. Should passwords and tokens ever appear in logs or database records?
    - [Answer: no]
118. What log retention period should apply?
    - [Answer: indefinitly since this is only an academic project]
119. Should refresh and access tokens use the exact security design from the example project?
    - [Answer: yes]
120. Should secure cookies and refresh-token rotation be implemented for both patients and staff?
    - [Answer: yes]
121. Should the system show the same generic login error for an unknown user and wrong password?
    - [Answer: no mention the problem in the message]
122. Should session/device management allow revoke-one, revoke-others, and revoke-all?
    - [Answer: will have all but only revoke one will be implemented]
123. How should account bans, deactivation, or lockout states affect active access tokens?
    - [Answer: how it should, blocked,banned,deactivated]

## 12. Performance, reliability, and availability

124. Are 2 seconds for standard reads and 10 seconds for 10 MB uploads realistic acceptance targets for the local and hosted demo?
    - [Answer: these wont be implemented so no need to worry]
125. How should the system behave during a network outage or server downtime?
    - [Answer: system is down, what can it do]
126. Should the system store offline drafts or rely only on paper fallback?
    - [Answer: rely on paper fallback]
127. How will routine maintenance and database migrations be demonstrated in the report?
    - [Answer: what?]
128. Should live deployment allow maintenance with no downtime, or will a maintenance page be shown?
    - [Answer: depends on the problem]
129. What database backup frequency and retention period should be documented and demonstrated?
    - [Answer: what?]
130. Should database backups be automatic, manual, or both?
    - [Answer: automaic but this aint getting implemented, since supabase will take of that]

## 13. Privacy and file storage

131. What user-consent or privacy notice should appear during registration or external report upload?
    - [Answer: nothing really]
132. Should uploaded reports and attachments be encrypted at rest?
    - [Answer: they will be treated the same as created reports]
133. Should deleted patients or records be hard-deleted, soft-deleted, or retained by legal policy?
    - [Answer: whichever is best]
134. How long should patient records, bills, prescriptions, and audit logs be retained?
    - [Answer: indefinitly]
135. Can a patient view another person's report through direct URL access, and what denial response should appear?
    - [Answer: they cant, and response(whatever suits the best)]

## 14. UI and usability

136. Should the application have a single shared login page or separate role dashboards with one login form?
    - [Answer: shared login form]
137. Which pages should the submitted UI contain at minimum:
    - Patient dashboard, Doctor dashboard, Ward Doctor dashboard, Pathologist dashboard, Accountant dashboard, Assistant dashboard, Ward Nurse dashboard, Pharmacy dashboard, IT admin dashboard.
    - [Answer: yes]
138. Should there be a dark mode, responsive mobile layout, and the example project's polished home/dashboard style?
    - [Answer: example project's polished home/dashboard, color scheme is dark grey and white]
139. What browsers and minimum responsive screen sizes must be supported?
    - [Answer: general pc size, chrome and firefox]
140. What loading, empty, validation, confirmation, success, and denial states should be demonstrated?
    - [Answer: what?]
141. Which usability tool should be used for evaluation: Lighthouse, WAVE, Axe, a heuristic checklist, or several?
    - [Answer: i will take care of that later]
142. Should the UI include print-ready views for prescriptions and receipts?
    - [Answer: a lot of things wont be implemented - see the above]

## 15. Testing and reporting 

143. What testing framework should be used for the backend and frontend?
    - [Answer: ]
144. Should the backend include automated unit and integration tests for authentication, RBAC, appointments, billing, reports, and audit logging?
    - [Answer: ]
145. Should the frontend include component or end-to-end tests?
    - [Answer: ]
146. What normal, boundary, invalid, and exception cases must be shown in the report?
    - [Answer: ]
147. Are 5 confirmed code-smell findings and fixes enough for the static analysis section?
    - [Answer: ]
148. Which code-review/static-analysis tools should be used: SonarQube, ESLint, Pylint, or another tool?
    - [Answer: ]
149. Which documentation tool should generate source-code documentation: JSDoc, Sphinx, Doxygen, or TypeDoc?
    - [Answer: ]
150. Which team roles and actual contributions should appear in the individual contribution table?
    - [Answer: ]
- These i will take of them later
## 16. Repository and project management

151. Confirm the team size and each member's name and role.
    - [Answer: ]
152. Should the project follow issue-based branches and conventional commits from the example repository?
    - [Answer: ]
153. Should evidence include Trello board screenshots, Discord discussions, GitHub branches, pull requests, commit history, and version tags?
    - [Answer: ]
154. Should the final report include GitHub Wiki links for all 12 required sections?
    - [Answer: ]
155. Should a PDF/DOCX and the GitHub Wiki be submitted as two different deliverable formats?
    - [Answer: ]
- These i will take of them later
## 17. Requirements that need your immediate correction

156. In the SRS, canceling without a reason is mandatory for the Doctor; in the use case, it is optional. Which behavior is correct?
    - [Answer: optional]
157. The SRS says audit every view or modification, but the use case says only create/update/delete actions are logged. Which behavior is correct?
    - [Answer: only create/update/delete actions are logged]
158. The SRS says Ward Doctor has the same authority as Doctor and can add medical reports/prescriptions; the use case section says a Ward Doctor cannot use full report creation forms. Which behavior is correct?
    - [Answer: can only add prescriptions]
159. The SRS says doctors can cancel appointments but the use case adds a 24-hour restriction. Which cancellation rule should be implemented?
    - [Answer: 24 hour constraint]
160. Should a patient cancel appointments, because the use case includes this but some earlier user stories do not?
    - [Answer: yes can cancel appointments]
161. Confirm whether the final implementation must include patient appointment cancellation.
    - [Answer: yes]
162. Confirm whether external report upload is in scope for patients and should accept 10 MB files.
    - [Answer: yes, but wont be implemented]
163. Confirm whether partial bill payments must be supported, or only Paid and Unpaid.
    - [Answer: only paid or unpaid, partial will not be implemented]




- will not be implemented means that the service is there but will give a popup saying will be implmented in the near future instead of the actual feature its supposed to be

- but this has certain rules( lets say a doctor wants to add a report but report making will not be implmented, so when doctor click the button to create a report, the creation popup or whatever its supposed to be will apear but will say "will be implmented in the near future" and the doctor can then press create which will create a report object) when the patient click on the report it will open the page it would have if there was an actual report but the page will contain the message "will be implmented in the near future"

now go through this again and ask any more questions to furthur understnd the project its, features and whatnot and any confusion you have about my answers

# Updated Project Understanding - Second Clarification Pass

## Project type and purpose

CHMS is a **centralized academic web application prototype** for a hospital environment. It is not intended for real medical use and will not replace paper/manual hospital workflows. The system will operate alongside existing manual processes as a digital aid. The submitted result should include source code, a polished live deployment, UI screenshots, documentation, and evidence, although the final reporting and team-management evidence will be completed later.

The project demonstrates an integrated hospital portal for:

- patient registration and login;
- outpatient appointments;
- role-specific staff dashboards;
- basic patient, prescription, report, pathology, billing, pharmacy, and ward information views;
- staff account and role management;
- audit/security events; and
- a digital interface that mirrors the intended future system while explicitly marking unimplemented services as future work.

## Implementation stack and architecture

The agreed implementation stack is:

- React
- TypeScript
- Vite
- FastAPI
- SQLModel
- SQLite for local development and testing
- PostgreSQL through Supabase in production
- Alembic
- PyJWT
- Argon2
- Supabase Storage
- Vercel deployment

The backend should follow a feature-folder structure containing routers, schemas, services, repositories, dependencies, and model-related code. The frontend should use pages, reusable components, contexts, and API service modules. The UI should use a dark-grey-and-white color scheme and a polished, responsive PC-oriented design usable in Chrome and Firefox.

There is one shared login form for patients and staff. Successful login routes the user to a role-specific dashboard.

## Roles and account model

Exactly one role is assigned to each account. The roles are:

- Patient
- Doctor
- Ward Doctor
- Assistant
- Pathologist
- Accountant
- Ward Nurse
- Pharmacy Staff
- IT Management/System Administrator

Staff accounts are created by IT. IT chooses the assigned staff role, creates credentials, and may later change the role, block/ban/deactivate or delete the account, and reset access. IT is allowed to access all patient data for system management and maintenance.

Patients self-register publicly. Patient login is by 8-digit patient ID and password. Staff login is by manually assigned username/user ID and password. The password requirement is intentionally simple for the academic demo; a 4-digit password is sufficient. Email is not supported.

Refresh/access tokens are based on the example project's security design:

- 15-minute access tokens;
- 7-day refresh tokens;
- refresh-token rotation;
- HttpOnly, Secure, SameSite=Strict refresh cookies;
- server-side role and permission verification on protected requests;
- token reuse, invalid tokens, denied access, and security events logged;
- logout only for the current session/device in the implemented demo.

Failed-login lockout, OTP verification, password recovery, and revoke-all/revoke-other session features are not implemented. Generic login errors are not required; a clear message may explain that the user ID or password is incorrect.

- not implemented- by this i mean there will be buttons for recovery and things the user can do but will show popup saying "will be immplemented in the near future"

## Patient and staff information

The patient has a unique, internally generated 8-digit patient ID. Phone number is stored for hospital contact, but patient login must use only the patient ID. Patients can change their own profile details and password.

Staff account identity and the final staff ID format remain simple/academic choices rather than real hospital standards. Ward and doctor assignments are relational and changeable.

Patients can view their own records. Doctors are allowed to search and review authorized patient histories. Ward Doctors are restricted to their ward/patient scope and prescriptions. Ward Nurses see reports and prescriptions only for patients assigned to their ward. Assistants see only the assigned doctor's appointments and patient scheduling information. Pharmacy Staff can search patient prescriptions. Accountants handle patient billing. Pathologists publish laboratory/report results in the simplified demo. IT can access everything.

The role-based answers in the earlier SRS, use cases, and user stories are not always consistent. The most recent answers are authoritative:

- Ward Doctor is a separate role and can add **prescriptions only**, not full medical reports or outpatient appointments.
- Audit logging includes CRUD actions, login success/failure, token/security events, and denied access, but excludes ordinary view/read operations.
- IT is the only role that can view audit logs.
- The 24-hour cancellation rule applies to doctors, assistants, and patients.
- Partial payments and partial-bill statuses are outside the final model.
- The detailed pathology request/sample/verification state machine is outside the final model.

## Appointments

Appointments are only for regular/outpatient Doctors. Ward Doctors cannot book or manage outpatient appointments.

The scheduling rules are:

- 15-minute slots;
- one patient per slot;
- patients can book, reschedule, and cancel;
- rescheduling is effectively unlimited but follows the 24-hour rule;
- patients, doctors, and assistants can cancel qualifying appointments;
- doctors and assistants can cancel without a mandatory reason;
- assistants do not require a cancellation reason;
- valid statuses are Scheduled, Cancelled, Completed, and Missed;
- doctors and assistants can mark appointments Completed or Missed;
- booking must atomically prevent double booking;
- a doctor or assistant can block a slot, day, or week;
- blocks are permanent until reopened, not date-limited;
- an already scheduled slot cannot be blocked; staff must cancel the appointment first;
- cancelling a scheduled visit frees the slot unless it remains blocked;
- a cancelled appointment remains visible as a cancelled record;
- doctors and assistants may remove cancelled records afterwards;
- cancellation by staff(Assistants and doctors) adds a dashboard reminder and manual-call reminder for staff;
- SMS and email notifications are not implemented.

The final implementation may use database locking or a conditional availability update for slot integrity.

## Prescriptions and medical reports

The project is conceptually required to store prescriptions and medical-report objects. However, reports and the detailed prescription workflow are subject to the user's global “not implemented” placeholder behavior.

The intended placeholder behavior is:

1. The user clicks a not-implemented feature.
2. A popup or creation screen explains that the feature will be implemented in the near future.
3. The user presses Create/Confirm.
4. The system creates a placeholder or domain object so navigation and audit behavior remain demonstrable.
5. When that object is opened, the detail page contains or visually represents the near-future message instead of real medical content.

The project must preserve a clear distinction between UI services that are intentionally placeholder-only and services that are actual working features.

The prescription decisions are:

- both regular Doctors and Ward Doctors can add prescriptions;
- Ward Doctors cannot create full reports;
- Ward prescriptions are visible to Ward Nurses, Pharmacy Staff, and the patient;
- outpatient prescriptions are visible to the patient and authorized doctor/pharmacy views;
- prescriptions are newest-first and previous prescriptions remain viewable;
- saved prescription/report objects are intended to be immutable rather than editable/deleted;
- PDF download/print of prescriptions is placeholder-only;
- external report upload is placeholder-only;
- file upload/print/report download features should use the near-future message rather than actual processing.

The earlier use cases describe detailed medicine fields and full report structure, but these detailed clinical fields do not need to be implemented if the service is placeholder-only. The remaining ambiguity is whether a prescription itself is real or only an object demonstrating the placeholder workflow.

- whether a prescription itself is real or only an object demonstrating the placeholder workflow.(an object demonstrating the placeholder workflow.)

## Laboratory and pathology

The original detailed pathology request system is not a target implementation. Remove formal requests, request statuses, Awaiting Payment state, unpaid blocking, and the Draft/Pending Verification/Released state machine from the final scope.

The simplified intended flow is:

1. A Doctor or Ward Doctor mentions the tests needed, conceptually in a report/prescription object.
2. The patient goes to the Accountant for a bill.
3. The patient pays manually or conceptually online.
4. The patient presents proof of payment to the Pathology department.
5. The Pathologist performs or records the test.
6. The result/report is published to the patient portal.

The exact representation of “tests mentioned,” the link from tests to bills and patients, and the fields in the published pathology object remain to be confirmed.
- Basically different tests have different bills,( the accountant would have made a bill for each test type the patient takes), but bill payment itself will not be implemented just like in (line 121- the intended workflow)

The earlier detailed reference-range/out-of-range verification workflow is not necessary unless added back explicitly(since test reports will also not be implmented). Supabase Storage may store pathology files conceptually, but complete file upload workflow is not a required implementation.

## Billing and pharmacy

Bills support:

- consultation charges;
- diagnostic test charges;
- medicine charges;
- hospital stay/service charges;

Bills have unique IDs and initial Unpaid status. Accountants can generate and edit them. There are no partial payments: a bill is either Paid or Unpaid. When a patient pays manually, the Accountant marks the bill Paid. If online payment existed, it would not be implemented; it should show placeholder behavior instead.

Receipts and payment records are described conceptually:

- each successful or manually confirmed payment has a paid receipt;
- failed payment leaves the bill Unpaid;
- accountant/manual and staff receipt views should show current and previous bills;
- downloadable/printable receipts are placeholder-only;
- receipt/gateway data is not a core data requirement unless needed for the demo.

Pharmacy Staff do not follow a separate paid-before-dispensing state. They search prescriptions to see the medicine list and may then create a bill for medicines the patient chooses to buy. They do not need a marked-dispensed workflow.

## Ward and support workflows

A patient is assigned to a ward and a Ward Nurse is assigned to a ward. Ward Nurses are restricted to their assigned ward. Ward Doctors can review/admit? ward patients and create prescriptions. The patient and ward assignment details remain to be confirmed, especially which actor can change ward assignments and whether transfer/discharge is part of the demo.
- IT manages ward assignments(Ward nurses), and charged discharged is managed by ward nurses
An Assistant is assigned to one Doctor and can be reassigned by IT. An Assistant can view only that Doctor's patients/appointments, manage that Doctor's slots and scheduled visits, and verify bill receipts for operational purposes.

## Audit, privacy, and retention

CHMS logs CRUD actions on patient/clinical/appointment/billing records, login success/failure, and security events. Ordinary patient-data view/read operations are not logged. Audit entries are append-only, permanent in the academic project, and visible only to IT. Audit entries should identify user ID, role, patient ID where applicable, action, entity, IP/time data, and relevant security context.

Passwords and tokens must never be written to logs or database audit data.

Patient data and uploaded reports should follow the application's normal access control. Direct URL access must not expose another patient's report. Deleted patient/account behavior is to use the safest and most appropriate database behavior, but the exact hard-delete versus soft-delete policy remains unresolved.

No privacy notice or patient consent screen is required. Supabase Storage is intended for uploaded files; normal and external reports should follow the same storage/access treatment. The implementation is not to promise clinical security beyond the academic prototype.

Retention is effectively indefinite for the academic system. Supabase is expected to handle production backup responsibility.

## UI and reliability

Minimum UI pages/dashboards:

- Patient dashboard;
- Doctor dashboard;
- Ward Doctor dashboard;
- Pathologist dashboard;
- Accountant dashboard;
- Assistant dashboard;
- Ward Nurse dashboard;
- Pharmacy dashboard;
- IT Admin dashboard.

The UI should include shared login, dashboard navigation, loading/empty/error states, success confirmations, validation messages, and access-denied states. The general desktop layout should work in Chrome and Firefox.
- Patients also have sign up(remember) which staff dont
If the system is offline or the server is unavailable, the app is unavailable and hospital staff are expected to rely on the parallel paper workflow. Maintenance behavior depends on the failure, and backups/reliability are not implementation priorities beyond the Supabase platform.

Testing frameworks, automated test depth, static analysis tools, source documentation tools, usability testing tools, team roles, Git workflow evidence, and final report deliverables are deferred until later.

## Known conflicts between documents and final answers

- The SRS/Use Case may show “Confirmed” as a booking status, but the final answer specifies only Scheduled, Cancelled, Completed, and Missed.
- The original user stories say a Doctor may require a cancellation reason, but the latest decision says cancellation is allowed without one.
- The original SRS gives Ward Doctor broader report and scheduling authority, but the latest decision restricts Ward Doctors to prescriptions and excludes outpatient schedule management.
- The original SRS says all views and changes are audited, but the latest decision audits CRUD/security events only.
- The original billing stories permit partial payments; the latest decision permits Paid and Unpaid only.
- The original laboratory stories include request queues, payment-gated sample collection, and verification states; the latest decision removes these from the actual workflow and uses a simplified bill-to-pathology flow.
- The original SRS and use cases describe real report/upload/payment features, but the latest decision says these features should demonstrate placeholder behavior through the near-future popup and placeholder object rule.

---

# 18. New questions after reviewing the complete project again

Please answer each question directly below it.

163. How many hospital locations or branches must the final demo support?
   - [Answer: only 1 , its just a simple web based system no need for branches and hospitals]

164. What mandatory fields should patient self-registration collect in the final UI?
   - [Answer: all the details(other than blood group i guess)]

165. Is patient phone number stored for contact purposes only, or may staff use it for patient search even though patient login is patient-ID-only?
   - [Answer: can use in search]

166. What format should manually assigned staff IDs use, and is there a hospital number, username prefix, or free text chosen by IT?
   - [Answer: a 4 digit number]

167. Which patient profile fields should each staff role be allowed to see: name, age, sex, phone, address, emergency contact, blood group, insurance, or ward?
   - [Answer: you can decide]

168. Should staff search by exact patient ID and/or partial name and/or phone number in the final implementation?
   - [Answer: all of above ]

169. For the placeholder rule, does “Create” always create a real persisted placeholder object with the created-by ID and timestamp, or should it be an in-memory/demo object that disappears on refresh?
   - [Answer: always create a real persisted placeholder object with the created-by ID and timestamp,]

170. The report and prescription sections need clarification: are Doctors supposed to enter real medicine/details and save real prescription objects, or should even prescription creation and viewing be placeholder-only because medicine implementation was described as not implemented?
   - [Answer: prescription creation and viewing be placeholder-only]

171. If prescription creation is placeholder-only, should pharmacy staff still be able to open the prescription object and create a bill from a future/placeholder medicine list, or does pharmacy remain a simple search-only placeholder too?
   - [Answer:  be able to open the prescription object and create a bill]

172. If real prescription objects are wanted, what medicine fields should be mandatory: medicine name, dosage, frequency, duration, route, quantity, instructions, and/or repeats?
   - [Answer: ]

173. If real prescriptions are wanted, should a prescription be created as an independent record or as part of a medical report object?
   - [Answer: ]

174. Should Ward Nurses see all reports and prescriptions for assigned ward patients, or should prescription/report visibility be limited to active/recent records?
   - [Answer: all]

175. Who is authorized to assign, transfer, or discharge a patient from a ward in the final demo: IT, Ward Doctor, Ward Nurse, Assistant, or a combination?
   - [Answer: ward nurse]

176. Which ward assignment information should be stored: ward only, ward plus bed/room, and/or admission date?
   - [Answer: all]

177. Should IT assign Ward Nurses to wards and change those assignments, or should another role manage it?
   - [Answer: only IT]

178. How should the simplified pathology flow identify a test: free-text test names entered in a report/prescription, a dedicated test table, or direct patient-ID selection on a form?
   - [Answer: what you mean?]

179. When a Doctor or Ward Doctor specifies tests, should the patient automatically receive a pending test bill or should the Accountant create the bill separately after looking up the patient?
   - [Answer: Accountant create the bill separately after looking up the patient]

180. Should the published pathology report be a real database object with patient ID, test names, result text/file, and published date, or should it always use the near-future placeholder page?
   - [Answer: placeholder-object wwill be created]

181. If a pathology result is placeholder-only, who presses Publish, and what object should the patient see in the patient portal?
   - [Answer: pathology report object]

182. Should the “hospital stay/service charge” be named Room/Bed Stay Charge, Ward Stay Charge, or another label in the UI?
   - [Answer: just service charge]

183. When pharmacy staff find medicines in a prescription, should they create a bill immediately, create a draft for Accountant approval, or only display a medicine list for the patient to take to Accounts?
   - [Answer: create a bill immediatly]

184. Can an Accountant edit an already Paid bill, or should Paid bills become immutable while only Unpaid bills are editable?
   - [Answer: Paid bills become immutable while only Unpaid bills are editable]

185. Should a manual counter payment create a receipt object immediately, and what minimum fields should that receipt show?
   - [Answer:In case of manual payment, the accountant still creates the bill object but also sets status to paid, "Also,if a patient pays online the status becomes paid"]

186. Should a patient be able to reschedule within 24 hours if the UI treats rescheduling as a cancellation plus rebooking, or must the same 24-hour rule always block it?
   - [Answer: 24 hour rule mean , that the appointment cannot be cancelled or changed when only 24 hours is left till the appointment]

187. Are appointment reasons/appointment type fields required at booking, or is doctor, date, and slot sufficient?
   - [Answer:  doctor, date, and slot is sufficient]

188. Can assistants book appointments for patients, or are assistants allowed only to view, cancel, block, reschedule, and mark statuses?
   - [Answer: they can book appointments for patients]

189. Can a Doctor block their own schedule directly, or only cancel appointments and let the Assistant block dates/slots?
   - [Answer: doctors can block schedule directly]

190. Can doctors remove a cancelled appointment record, and can patients remove their own cancelled appointments from the patient view?
   - [Answer: yes]

191. After a patient, doctor, or assistant cancels an appointment, should the cancelled record keep the reason and cancellation actor/timestamp even though reasons are optional?
   - [Answer: yes]

192. For placeholder objects and medical records, may they be soft-deleted or removed after creation, or should all clinical placeholder objects remain permanently visible?
   - [Answer: all clinical placeholder objects remain permanently visible]

193. Should account deletion for patients and staff be a hard delete or a soft deactivation that retains audit and medical records?
   - [Answer: ]soft deactivation

194. What fields must be shown in the audit log for normal CRUD and security events: user ID, role, patient ID, action, entity, IP address, user agent, and timestamp?
   - [Answer:you can choose ]

195. Should role-change and account-deletion actions be logged as admin audit entries even when they do not involve a patient?
   - [Answer: yes]

196. Should an IT user have to confirm a role change or account deletion, and should there be a distinction between deactivated/banned/deleted states?
   - [Answer: staff cannot delete their account, nor can they change role, only IT can, patients can delete whenever]

197. Does “8-digit patient ID only” mean the 8-digit number replaces the username completely, while staff use an assigned username? No email/phone login is allowed for patients.
   - [Answer: patient id is 8 digit, staff will have 4 digit id]

198. How should patient and staff profile changes interact with account login? In particular, can changing/clearing a phone number affect staff/patient access?
   - [Answer: changing/clearing a phone number affect staff/patient access- no]

199. Should the UI retain draft form values when a near-future popup is cancelled, or should opening the placeholder popup leave the form unchanged?
   - [Answer: draft i suppose ]
---

# Updated Project Understanding - Third Clarification Pass

## Confirmed project scope

CHMS is an academic, browser-based hospital aid with one hospital location and no branch/multi-hospital requirement. It is expected to operate alongside paper/manual hospital processes, not replace them or serve real clinical use. The live demo is deployed on Vercel and uses React, TypeScript, Vite, FastAPI, SQLModel, SQLite for local development/testing, PostgreSQL through Supabase for production, Alembic, PyJWT, Argon2, and Supabase Storage.

The architecture is a feature-folder implementation:

- frontend: pages, reusable components, contexts, and API-service modules;
- backend: routers, schemas, services, repositories, models, and dependencies;
- shared login page and separate role dashboards;
- server-side role and permission checks in addition to token-provided role information;
- dark-grey-and-white desktop UI targeted generally at Chrome and Firefox.

The minimum role dashboards are for Patient, Doctor, Ward Doctor, Assistant, Pathologist, Accountant, Ward Nurse, Pharmacy Staff, and IT/System Administrator.

## Accounts and identity

Exactly one role is assigned to an account. Patient accounts can self-register and are identified by an automatically generated 8-digit patient ID. Staff accounts are manually created by IT and use an assigned 4-digit staff ID.

Patient login uses only patient ID plus password. Staff login uses the assigned staff ID plus password. Patient phone number may be used for staff search, but does not change login identity. Passwords only need the simple academic 4-digit style.

IT may:

- create staff accounts;
- assign/change staff roles;
- ban, block, deactivate, delete, and reset staff accounts;
- view every patient record;
- manage ward-nurse assignments;
- view the audit log.

Only IT can change a staff role or delete/block a staff account. A patient may delete their own account. Account deletion is soft deactivation rather than hard deletion. Deactivated/banned/deleted states and a confirmation step for IT account actions are not fully distinguished in the existing answers.

The authentication implementation follows 15-minute access tokens, 7-day refresh tokens, rotation, secure HttpOnly refresh cookies, logout for the current device, and server-side account/role checks. Lockout, OTP, email verification, password recovery, revoke-other-device, and revoke-all-device operations are not real workflows. They may appear as UI controls that display the near-future placeholder popup.

## Patient and role views

Staff may search patients by exact patient ID, partial or full name, and phone number. Patient profile fields should provide enough general and emergency information for a hospital demo, with blood group being optional. The exact role-by-role visibility of every patient field can be chosen consistently with least-privilege RBAC, while IT retains access to everything.

The final role boundaries are:

- Doctors manage their own outpatient appointments and patient history and add prescription objects.
- Ward Doctors cannot manage outpatient appointments or full reports and can add prescription objects only.
- Assistants are assigned to one Doctor, can be reassigned by IT, can book/cancel/reschedule/block appointments and mark visit outcomes, and see only their assigned Doctor's patients/appointments.
- Ward Nurses see all report and prescription objects for patients currently assigned to their ward.
- Pharmacy Staff search patient prescription objects and can immediately create a bill from selected medicine content.
- Accountants search for patients, create/edit Unpaid bills, mark manual payments Paid, and view bills/receipts.
- Pathologists publish pathology placeholder objects.
- IT manages accounts, roles, ward-nurse assignments, system records, and audit logs.

## Ward behavior

One ward system is required, but only one hospital location exists. Ward assignment records include ward, bed/room, and admission date.

Ward Nurse assignment to wards is managed by IT. Ward Nurses manage patient ward discharge. The latest answer does not yet clarify whether Ward Nurses can assign/transfer a patient between wards or only discharge patients.

Ward Nurses have read-only access to report/prescription objects for patients in their ward. Ward Doctors have ward-patient and prescription access.

## Appointment behavior

Outpatient appointments are available only with regular Doctors, not Ward Doctors. Slots are 15 minutes and exclusive. Patients and assistants can book appointments. Doctors and assistants can manage their respective schedules directly.

An appointment requires the patient, Doctor, date, and 15-minute slot. It does not require a booking reason or appointment type.

Final statuses are:

- Scheduled
- Cancelled
- Completed
- Missed

No Confirmed status is used. A scheduled visit can be marked Completed or Missed. Cancellation or rescheduling is prohibited when fewer than 24 hours remain until the appointment. The rule is also described as applying across patient, Doctor, and Assistant cancellation/rescheduling.

Doctors, assistants, and patients may cancel. Reasons are optional but, if a cancellation occurs, the cancellation record should retain the optional reason and cancellation actor/timestamp. Doctors and assistants may remove cancelled appointment records. Patient removal is also permitted. The existing answer does not explicitly confirm whether assistants may remove cancelled records.

Doctors and assistants can block their own/assigned schedule by slot, day, or week. Blocks remain until reopened. An already scheduled slot cannot be blocked; cancellation is required first.

Booking/cancellation/rescheduling must behave atomically so one slot cannot be double-booked. Cancelled appointments remain visible as cancelled records and staff calls/reminders apply when staff cancel.

## Placeholder/domain-object behavior

The near-future rule applies to intentionally unimplemented features:

1. Clicking the feature opens a popup or form that says the feature will be implemented in the near future.
2. Confirming/Create creates a persisted placeholder object.
3. The object has creator ID and timestamp.
4. Opening the object shows the near-future message/page instead of real clinical functionality.

This applies to medical report and external report workflows, prescription file/detail workflows, PDF/print workflows, external uploads, test-report workflows, online payment UI, and other explicitly unimplemented features. It is not a complete guarantee that every older use case button should perform real storage or clinical processing.

Prescription creation/viewing is placeholder-only. The placeholder prescription object may be visible to the patient, Ward Nurses, pharmacy staff, ward/outpatient doctors, and the correct role-based views. Pharmacy Staff can open it and immediately create a bill, despite no real medicine data or dispensing workflow being implemented.

Medical-report objects and pathology objects are persisted placeholder objects. They remain permanently visible and are not to be edited or removed by ordinary clinical roles. The system should not pretend that these objects contain real diagnosis or test results.

## Prescription and pathology representation

The detailed medicine fields are not implemented in the final prescription placeholder workflow. The system does not need to make dosage, route, duration, quantity, or similar fields real unless a later decision adds a real implementation.

The simplified pathology flow does not use test requests or status queues. The Accountant creates separate bills for test types after patient lookup. The patient pays manually or, in the future model, online. The Pathologist creates/publishes a pathology report placeholder object for the patient.

The exact link among a test bill, requested test list, patient, and pathology placeholder remains one of the clearest remaining design questions.

## Billing and payment

Bills contain the service category, itemized details, amount, bill ID, patient, accountant, date, and Paid/Unpaid status. Supported charge categories are:

- consultation;
- diagnostic tests;
- medicines;
- service charges.

Bills do not support partial payments. Accountants may create and edit Unpaid bills. Paid bills become immutable. Manual payment is recorded by the Accountant by changing the bill to Paid. Online payment, if eventually simulated, changes the bill to Paid but the real payment gateway is not implemented.

A manual payment or a successful online payment creates a Paid receipt conceptually. Receipt download/print and detailed gateway evidence are placeholders. Pharmacy Staff may create an immediate medicine bill from a prescription placeholder.

## Audit and security

The system logs:

- create/update/delete operations;
- login successes and failures;
- token reuse/invalid token/security events;
- denied access;
- role change and account administration;
- IT account deletion/ban/deactivation actions.

Ordinary read-only views are not logged. Audit entries are append-only and permanent for the academic project. Only IT should see the audit log. Passwords and tokens must never appear in audit data or logs.

Account and role events are included even when no patient is involved. The exact audit fields can be selected as needed.

Soft account deactivation preserves patient/clinical records and audit history. Patient account deletion is allowed and implemented as deactivation rather than irreversible destruction.

## Data, files, and privacy

Supabase Storage is the intended file location for any real or future external uploads, but external report upload is currently placeholder-only. The user has not asked for real file encryption or retention policy implementation beyond academic prototype controls.

Patient records and audit records should remain indefinitely. Supabase manages backups conceptually. The app should use normal paper fallback during downtime rather than offline drafts.

Direct access to another person's report must be denied. The exact denial message can follow existing role-denied UI conventions.

## Reporting and deferred tasks

Testing tools, test coverage, static-analysis findings, source documentation tools, usability evaluation, team names/contributions, Trello/Discord evidence, Git branching/commit evidence, report PDF/DOCX packaging, Wiki structure, and the final deployment/report checklist are deferred. They should not block implementation scope decisions.

## Known remaining ambiguities

- Old SRS/use-case text remains broader than the final decisions and may be overwritten by this understanding.
- The simplified pathology relationship among Doctor test mention, Accountant bill, patient, and Pathologist publication is not fully specified.
- Ward transfer/discharge authority is partly defined: IT assigns Ward Nurse-to-ward, Ward Nurses manage discharge, but transfer authority is unclear.
- The placeholder prescription has no medicine detail, yet Pharmacy Staff must create a bill from it. The exact bill line items need a default.
- Assistant ability to remove cancelled appointments remains unclear even though Doctor and Patient removal are confirmed.
- Deactivated/banned/deleted account states need an implementation distinction.
- Patient account deletion and soft deactivation should preserve records, but it is unclear whether the user should be able to recreate the same 8-digit ID or begin a new account.
- The near-future popup should preserve form draft values, but no exact behavior is known for cancelling versus confirming the placeholder.

---

# 19. Final clarification questions

Please answer each question directly below it.

200. Where will a Doctor or Ward Doctor enter the tests needed for a patient: in a prescription/report placeholder, in a free-text “tests” field, or nowhere; the Accountant searches for the patient and chooses tests themselves?
   - [Answer: prescription/report placeholder, the accountant can see the report and then create bills based on the ..]

201. How will the Accountant know which test bill to create for a patient: the Doctor provides/mentions tests on the placeholder object, the patient selects a test, or the Accountant chooses from a predefined test list?
   - [Answer: there would be a predefined test list, but fow now just add add placeholder test list items(like placeholdertest 1, placeholder test 2...)]

202. Should there be a simple predefined list of test names and prices, or may the Accountant freely type test name and charge for each bill line?
   - [Answer: a simple predefined list of test names and prices ]

203. When the Pathologist sees a paid test bill, should they open it and click Publish to create a pathology placeholder object, or simply search the patient and create the object directly?
   - [Answer: simply search the patient and create the object directly]

204. Should the patient pathology placeholder show only “will be implemented in the near future,” or also read-only details such as test name, billing status, pathologist name, and publish date?
   - [Answer: read-only details such as test name, billing status, pathologist name, and publish date, sure]

205. Can Ward Nurses assign or transfer patients to another ward, or may they only discharge patients while IT manages all ward assignment changes?
   - [Answer: can assign or transfer patients]

206. If a Ward Nurse discharges a patient, what fields should be saved: discharge status, discharge date/time, ward nurse ID, and/or a general discharge note?
   - [Answer: sure]

207. Since prescription placeholders contain no real medicine details, what medicine list should Pharmacy Staff create a bill from: a fixed demo medicine list, free-text medicine names entered by Pharmacy Staff, or the selected prescription placeholder with no medicine line details?
   - [Answer: the selected prescription placeholder with no medicine line details ]

208. If Pharmacy Staff create a medicine bill, should that bill belong directly to the patient and become editable only by an Accountant, or may Pharmacy Staff continue editing it before it is marked Paid?
   - [Answer: Pharmacy Staff continue editing it before it is marked Paid]

209. May the Assistant remove a cancelled appointment record, or is removal limited to Doctors and Patients?
   - [Answer: assistant can also remove appointment record]

210. When an account is banned, deactivated, or deleted, how should it differ in the UI and login behavior: banned cannot log in, deactivated is restored only by IT, deleted is hidden, or one generic blocked state?
   - [Answer: you choose]

211. If IT deletes or blocks a staff account, should active sessions stop immediately or remain valid until the access token expires?
   - [Answer: active sessions stop immediately]

212. If a patient soft-deactivates/deletes their account, may they register again and receive a new 8-digit patient ID, or must they contact IT and restore the same account?
   - [Answer: register again and recieve new id]

213. Can an inactive/deactivated patient still have their existing bills, wards, appointments, and clinical objects visible to authorized staff and IT?
   - [Answer: you choose]

214. When a placeholder form is cancelled, should all draft fields remain in the form while showing a browser confirmation; when Create is confirmed, should the form clear and the list open to the new placeholder object?
   - [Answer: i dont understand you choose best]

- when a doctor or assistant cancels an appointment there should be a popup to remind them to call the patient to notify about the cancellation

---

# Updated Project Understanding - Fourth Clarification Pass

## Finalized project scope

CHMS remains a single-hospital, academic web prototype designed to work alongside existing paper/manual hospital processes. It is not intended for real medical use or as a complete replacement for hospital operations.

The implementation uses React, TypeScript, Vite, FastAPI, SQLModel, SQLite locally, PostgreSQL/Supabase in production, Alembic, PyJWT, Argon2, Supabase Storage, and Vercel deployment. The frontend uses pages, components, contexts, and API services. The backend uses feature-folder routers, schemas, services, repositories, dependencies, and database models.

The UI is a polished desktop application in a dark-grey-and-white color scheme, with a shared login form and role-specific dashboards for:

- Patient
- Doctor
- Ward Doctor
- Assistant
- Pathologist
- Accountant
- Ward Nurse
- Pharmacy Staff
- IT/System Administrator

Chrome and Firefox are the primary demo browsers.

## Accounts and authentication

Each account has exactly one role. Patients publicly self-register using an automatically generated 8-digit ID and password. Staff accounts use 4-digit IDs, are manually created by IT, and do not self-register.

Patient login uses patient ID only. Staff login uses staff ID. Phone number is profile/search data, not an authentication identifier. The final profile fields include general patient details, with blood group optional. Staff and patient passwords may use the simple 4-digit academic format.

IT can:

- create, block, deactivate, and restore staff accounts;
- delete patient accounts;
- change staff roles;
- reset or manage staff access;
- assign Ward Nurses to wards;
- access all patient data;
- view append-only audit logs.

Staff cannot change their own role or delete their own account. Patients may delete/deactivate their own account. Existing records are retained through soft deactivation. Patient deletion allows the patient to register again and receive a new 8-digit ID.

Authentication uses 15-minute access tokens and 7-day refresh tokens, with the example project's secure refresh-cookie and rotation behavior. Logging out affects the current session/device. Lockout, OTP recovery, email verification, revoke-all, and revoke-other sessions may be represented with the near-future popup rather than implemented.

When IT blocks or deletes a staff account, active sessions stop immediately. The final distinction among blocked/banned/deactivated/deleted states is to be chosen consistently.

## Role-based workflows

Doctors can manage their own outpatient schedule, review/search authorized patient history, mark appointments Completed or Missed, and create prescription placeholder objects.

Ward Doctors are a separate role. They cannot manage outpatient appointments or create full medical reports. They can review their ward patients and create prescription placeholders.

Assistants are assigned to one Doctor and can be reassigned by IT. They can book, reschedule, cancel, block, and mark appointments, and remove cancelled appointment records. Assistant access is limited to their assigned doctor's patients and schedules.

Ward Nurses are assigned to a ward by IT and can:

- assign or transfer patients;
- discharge patients;
- view all reports and prescription objects for assigned patients.

Ward Doctor and Ward Nurse ward assignment details should include ward, bed/room, and admission date.

Pharmacy Staff can search prescription placeholders and immediately create a medicine bill. They do not have a real medicine inventory or dispensing workflow.

Accountants can search patients, create and edit Unpaid bills, mark bills Paid after counter or online confirmation, view records, and generate receipt concepts. Paid bills are immutable.

Pathologists search for a patient directly and create/publish a pathology placeholder object. The placeholder detail includes read-only test name, payment/billing status, pathologist name, and published date.

## Appointments

Only regular/outpatient Doctors accept appointments. Slots are 15 minutes and exclusive. There is no booking reason or appointment type field.

Patients, Doctors, and Assistants can book appointments. Patients can reschedule or cancel. Doctors and Assistants can cancel, block, and update appointments.

Valid statuses are Scheduled, Cancelled, Completed, and Missed. Cancelled records remain visible unless removed. Patients, Doctors, and Assistants can remove cancelled appointment records.

The 24-hour rule means an appointment cannot be changed or cancelled within 24 hours of the appointment start. Rescheduling counts as a change and follows the same rule.

Doctors and Assistants can block slots, days, or weeks indefinitely until reopened. They cannot block an already scheduled slot; they must cancel it first. Booking and scheduling changes must be atomic to prevent double booking.

Cancellation may omit a reason. When cancelled, the record should retain the cancellation actor, timestamp, and optional reason if entered. Doctor and Assistant cancellations should display a popup reminding staff to call the patient.

## Placeholder and unimplemented behavior

“Will not be implemented” means the UI is retained but the real operation is replaced by an explicit near-future state.

For not-yet-implemented actions:

1. the button opens a popup/form saying the feature will be implemented in the near future;
2. confirmation/Create creates a persisted placeholder/domain object;
3. the object is stamped with creator ID and timestamp;
4. opening the object shows read-only placeholder information and the near-future message.

This behavior applies to report creation, external uploads, prescription details/PDF/print, test-report entry, online payment/gateway UI, password recovery, and other explicitly deferred services.

Prescription creation and viewing are placeholder-only. The prescription object is visible to the patient and relevant authorized clinical/pharmacy roles and remains persisted. It does not contain real dosage, duration, route, or similar medicine details.

Medical and pathology objects are persisted placeholder objects and are normally immutable/permanent. They are not real clinical reports.

## Simplified pathology and test billing

The detailed pathology status/request state machine is outside scope. There is no formal test request, sample collection, Draft/Pending Verification/Released queue, or paid-before-sample system.

The Accountant maintains a predefined demo test list with test names and prices. Placeholder test items may be used, such as Placeholder Test 1 and Placeholder Test 2. The Accountant searches for the patient and creates separate test bills. Doctor/Ward Doctor report or prescription objects provide the clinical context from which the Accountant knows which test category to create.

The Patient pays manually or conceptually online. Counter payment is confirmed by the Accountant. Online payment UI remains placeholder unless it updates the bill to Paid in a demonstration flow.

The Pathologist searches the patient and directly creates/publishes a pathology placeholder object. The patient portal shows placeholder text plus test name, billing status, pathologist identity, and publish date.

## Billing and pharmacy

Bills support consultation, diagnostic tests, medicine, and service charges. Bills have unique IDs, patient and accountant references, itemized details, date, total, and Paid/Unpaid status.

Partial payment is not allowed. Accountants may edit Unpaid bills. Paid bills become immutable.

Manual counter payments are marked Paid immediately by the Accountant. Successful online payment also marks a bill Paid in concept, although no real gateway is integrated. Receipt download/print and detailed receipt/gateway fields are placeholder-only.

Pharmacy Staff open a prescription placeholder and may create an immediate medicine bill for the patient. The bill may initially contain no detailed medicine lines. Pharmacy Staff may continue editing it before payment. After it becomes Paid, Accountant rules make it immutable.

## Audit and security

The system logs:

- create, update, and delete operations;
- login success/failure;
- denied access and security events;
- token misuse or invalid refresh attempts;
- role changes and account administration.

Ordinary read/view operations are not logged. Audit entries are append-only and permanent. Only IT can view them. Passwords and tokens are never stored in audit entries. Audit fields may include user ID, role, patient ID, action, entity, IP/device context, and timestamp.

Soft-deactivated patient accounts retain bills, ward records, appointments, clinical objects, and audit history for authorized staff and IT.

## Data and privacy

Patient records and audit logs remain retained indefinitely. Supabase is the production database and storage platform and is treated as handling backups. The application relies on paper fallback during outages.

External upload, report file download, and print features are placeholder-only. Supabase Storage is intended for future real files. Direct URL access must not reveal another patient's information.

## Deferred submission work

Testing framework and coverage, static analysis, source documentation, usability evaluation, team contributions, Trello/Discord evidence, Git evidence, report PDF/DOCX, and Wiki pages are deferred. Live deployment remains a deliverable to prepare later.

## Remaining uncertainties

- The exact predefined test list and whether it contains fixed prices remain an implementation choice.
- The exact bill object and line-item behavior for a prescription with no real medicine details remain ambiguous.
- The distinction between blocked, banned, deactivated, and deleted account states remains to be chosen.
- The behavior of a soft-deactivated patient record in staff search and billing remains to be finalized.
- The exact placeholder cancellation/draft behavior can use a conventional confirmation design.
- Ward discharge fields and ward-transfer records need exact validation.
- The final role-by-role patient profile field restrictions can use consistent UI/API authorization rules.

---

# 20. Final implementation-clarification questions

Please answer each question directly below it.

215. Should the predefined test list contain exactly a few fixed demo tests and prices, or should Accountant/Admin be able to maintain the test list for the demo?
   - [Answer: a few fixed demo tests]

216. What demo test names and prices should appear in the first test list? For example, Blood Test, X-Ray, Ultrasound, Urine Test.
   - [Answer: nah just placeholdertest1,placeholdertest2 etc]

217. Should a test bill contain one test line or permit several test lines on the same bill?
   - [Answer: several test line]

218. How should Pharmacy Staff create a medicine bill from a prescription placeholder: choose a fixed demo medicine and quantity, enter free-text medicine charges, or create the bill with a generic “Medicines” service line and total?
   - [Answer: a fixed demo medicine and quantity, always]

219. May Pharmacy Staff continue editing a bill after another role views it, or should editing stop once the bill is created and only the Accountant can edit it?
   - [Answer: can edit until paid]

220. Should a Paid bill show in the Accountant's “all bills” history and patient bill history but be unavailable for editing/deletion?
   - [Answer: yes]

221. Which account states should the IT UI distinguish: blocked, banned, deactivated, deleted/soft-deactivated, or only Active and Blocked?
   - [Answer:all ]

222. Should an inactive patient remain visible in staff patient search and be marked inactive, or should search exclude inactive accounts?
   - [Answer: remain visible in staff patient search and be marked inactive]

223. Should staff patients who re-register receive a new ID, as decided, and should the old ID remain visible in audit or ward/billing history?
   - [Answer: you decide]

224. When a Ward Nurse discharges a patient, should the patient remain assigned to the ward with a discharged flag or should ward/bed assignment be cleared and kept only in discharge history?
   - [Answer:  should ward/bed assignment be cleared and kept only in discharge history]

225. When Ward Nurses assign or transfer a patient, should their ward dashboard show the patient's current ward and assignment history, and may one patient be in only one active ward at a time?
   - [Answer: yes]

226. Should a ward discharge require a confirmation popup and an optional/general discharge note, or is only status/date/ward-nurse ID enough?
   - [Answer: an optional/general discharge note, status/date/ward-nurse ID enough]

227. What exact patient profile fields are mandatory for registration? If blood group is optional, should name, phone, address, DOB, emergency contact, and password be required?
   - [Answer: yes]

228. What patient profile fields can IT or staff edit: identity ID, name, phone, address, DOB, blood group, emergency contact, and/or password?
   - [Answer: none]

229. Should IT be able to reset a staff or patient password, and should that password reset show placeholder behavior or create a new 4-digit password directly?
   - [Answer:cant reset ]

230. Should password/profile changes invalidate existing access and refresh sessions, or only require the user to enter the new password next time?
   - [Answer: only require the user to enter the new password next time]

231. What exact success, empty, and denied messages should be shown for patient searches, ward access, account blocks, cancelled appointments, and placeholder creates?
   - [Answer: you choose]

---

# Updated Project Understanding - Fifth Clarification Pass

## Project summary

CHMS is a centralized, academic hospital management web prototype for one hospital location. It is a digital aid that operates alongside existing paper/manual workflows and is not intended for real clinical use or to replace the hospital.

The implementation uses React, TypeScript, Vite, FastAPI, SQLModel, SQLite for local development/testing, PostgreSQL through Supabase in production, Alembic, PyJWT, Argon2, Supabase Storage, and Vercel deployment.

The backend follows feature-folder architecture with routers, schemas, services, repositories, dependencies, and database models. The frontend uses pages, components, contexts, and API service modules. The UI uses a polished dark-grey-and-white desktop style and a shared login page for all roles.

The live prototype includes role dashboards for:

- Patient
- Doctor
- Ward Doctor
- Assistant
- Pathologist
- Accountant
- Ward Nurse
- Pharmacy Staff
- IT/System Administrator

## Identity and accounts

Patients self-register with an 8-digit patient ID, password, name, phone number, address, date of birth, emergency contact, and optional blood group. Phone number is searchable by staff but not a patient login identifier.

Staff accounts use 4-digit IDs and are created manually by IT. Staff passwords use a simple 4-digit academic format. Staff cannot create their own accounts or change their own role.

IT can create/block/deactivate/restore staff accounts, change staff roles, and soft-delete patient accounts. IT can access all patient data and audit records. Patients can delete/deactivate their own accounts and may register again with a new 8-digit ID. Staff cannot delete or reset their own account.

IT cannot reset staff or patient passwords. Patients and staff may change their own password/profile in the supported UI. Password or profile changes require the user to enter the new password at the next login but do not explicitly invalidate all current tokens.

Active sessions stop immediately when IT blocks/deletes a staff account. Account states are distinguished in the IT UI, with separate blocked, banned, deactivated, and soft-deleted concepts.

Inactive/deactivated patient accounts remain visible in staff search and are clearly marked inactive.

## Authentication and security

Authentication uses 15-minute access tokens, 7-day refresh tokens, secure refresh-token cookies, refresh-token rotation, Argon2 password hashing, and server-side role/permission checks.

The current session can be logged out. Failed-login lockout, OTP verification, password recovery, revoke-other, and revoke-all session management are not implemented in the real workflow. Their controls are placeholder UI elements unless explicitly changed later.

The system logs create/update/delete operations, login success/failure, denied access, security events, token misuse, role changes, and account administration. It does not log ordinary read/view actions.

Audit entries are append-only and permanent. Only IT can view them. Passwords and tokens must never appear in audit records or logs.

## Patient and role permissions

Staff can search patients by 8-digit ID, partial/full name, and phone number. IT can access everything. Other staff views are role- and relationship-restricted.

Doctors can search and review authorized patient history and manage only their own outpatient schedule.

Ward Doctors are a separate role. They cannot manage outpatient appointments or create full medical reports. They can create prescription placeholder objects and view ward patients.

Assistants are assigned to one Doctor and can be reassigned by IT. They can book, cancel, reschedule, block, and mark appointments for that Doctor and remove cancelled records.

Ward Nurses are assigned to wards by IT. They can assign or transfer patients, discharge patients, and view all report and prescription objects for patients in their current ward.

Accountants create and edit bills, mark bills Paid after manual or demonstrated online payment, and view patient payment records. Pharmacy Staff can search prescription placeholders and create medicine bills.

Pathologists search patients directly and create/publish pathology placeholder objects.

## Appointment behavior

Outpatient appointments are exclusive 15-minute slots for regular/outpatient Doctors only. Ward Doctors do not manage outpatient schedules.

Patients, Assistants, and Doctors can use appointment booking functions:

- patients and assistants can book;
- patients, Doctors, and assistants can cancel;
- Doctors and assistants can block their schedules;
- Doctors and assistants can mark Scheduled appointments Completed or Missed.

Appointment fields are Doctor, patient, date, and time slot. No reason or appointment type is required.

Statuses are Scheduled, Cancelled, Completed, and Missed. Cancelled appointments remain visible until removed. Patients, Doctors, and Assistants may remove cancelled records.

Cancellation/rescheduling is prohibited when less than 24 hours remains until the start. A cancellation by a Doctor or Assistant opens a call-reminder popup for the staff member. The cancelled record retains cancellation actor, timestamp, and optional reason.

Doctors and Assistants can block one slot, day, or week until reopened. An already scheduled slot must be cancelled before blocking. Slot booking/cancellation/rescheduling must be atomic.

## Ward behavior

Ward assignment is represented by ward, bed/room, and admission date. Ward Nurses may assign or transfer a patient to another ward and may have only one active ward assignment at a time.

IT assigns or changes Ward Nurse-to-ward assignments. Ward Nurses discharge patients and create discharge history. Discharge clears the active ward/bed assignment while preserving discharge status, date/time, Ward Nurse ID, and optional general note.

Ward Nurses have all report/prescription access needed for patients in their current ward, subject to backend access checks.

## Placeholder behavior

When a feature is not implemented, it remains visible in the UI but opens a near-future placeholder state. Confirming/Create creates a persisted placeholder object with creator ID and timestamp.

Opening the object shows read-only placeholder details and the “will be implemented in the near future” message instead of real clinical functionality.

This behavior applies to medical reports, external uploads, prescription detail/PDF/print, pathology details, online payment, password recovery, and other explicitly deferred features.

Prescription creation and viewing are placeholder-only. The object persists and is visible to authorized patient, Doctor, Ward Doctor, Ward Nurse, and Pharmacy roles. Ward Nurses see all relevant prescription objects for their assigned patients.

Medical and pathology objects remain persistent and immutable for normal clinical users. Ordinary users may not edit or remove the placeholder clinical objects.

## Simplified pathology and test billing

The detailed request/status/workflow system is removed. There are no test requests, sample-collection states, verification queues, or released/draft report workflow.

Accountants use a fixed demo test list containing Placeholder Test 1, Placeholder Test 2, and other placeholder test entries as needed. The test list is fixed rather than maintained by users. One bill may contain several test lines. Each placeholder test should have a demo price chosen consistently in implementation.

The Accountant searches for a patient and creates test bills from the fixed list. The Doctor/Ward Doctor report or prescription context supplies the reason a test is relevant, but it does not automatically generate a bill.

Manual payment is confirmed by marking the bill Paid. Online payment, if demonstrated, also updates the bill to Paid, but no real payment gateway is integrated.

The Pathologist searches for a patient and directly creates/publishes a pathology placeholder object. The object displays test name, billing status, pathologist identity, publish date, and the near-future message.

## Billing and pharmacy

Bills support consultation, diagnostic test, medicine, and service charges. Bills have an ID, patient, amount, date, line items, and Paid/Unpaid status.

Partial payment is not supported. Accountants can create and edit Unpaid bills. Paid bills are immutable and appear in all-bill and patient-bill history.

Manual counter payment creates a paid receipt conceptually. Pharmacists can create medicine bills immediately from prescription placeholders.

Pharmacy Staff use fixed demo medicine names and quantities. The exact demo medicine/quantity list and generic totals are implementation choices. Pharmacy Staff may continue editing an Unpaid bill; only the Accountant may edit the bill after it is no longer under Pharmacy Staff control, and all editing stops after the bill becomes Paid.

## Profile and data behavior

Patients may change their own profile and password, subject to the mandatory registration fields. IT and staff cannot edit patient identity/profile fields.

Patient profile changes do not affect patient ID or login identity. Phone number is contact/search data only and changing or clearing it does not block login.

Patient deletion is soft deactivation. Staff search can retain an inactive patient record marked inactive, and authorized staff/IT retain access to existing records and history.

Billing, ward, appointment, prescription, and pathology objects remain retained indefinitely for the academic prototype. Supabase is the production database and storage system and is expected to handle backups.

Supabase Storage is intended for future real report uploads, but external-upload and report-file workflows are placeholder-only. Direct URL access to another person's report must be denied.

## UI and deferred work

The UI uses standard success, empty, validation, confirmation, and access-denied states. The exact wording can follow consistent UI conventions.

When a placeholder form is cancelled, draft fields should remain; the near-future confirmation popup does not need to lose unsaved form state. Confirm/Create creates the persisted placeholder and returns to the relevant list or object view.

Testing framework and coverage, static analysis, source documentation, usability evaluation, team contributions, Trello/Discord evidence, Git evidence, report PDF/DOCX, and Wiki pages are deferred.

## Remaining ambiguities

The implementation scope is now mostly complete. The remaining questions are limited to:

- exact placeholder test prices;
- fixed demo medicine names and quantities;
- exact allowed IT account-state transitions;
- how re-registration should relate to old IDs in historical records;
- draft/cancellation behavior beyond preserving placeholder form data;
- whether pharmacy bills should contain a generic medicine line or fixed demo medicine lines;
- which profile fields a patient may edit after registration.

---

# 21. Small remaining implementation questions

232. What fixed prices should be used for Placeholder Test 1 and Placeholder Test 2? For example, should they all be 0, or should they have demo values?
   - [Answer:demo values ]

233. What fixed demo medicine names and quantities should the Pharmacy bill UI use? For example, Medicine 1, Medicine 2, and quantity 1/5/10.
   - [Answer:  Medicine 1, Medicine 2, and quantity 1/5/10.]

234. For the medicine bill, should the bill contain selected fixed medicine lines or one generic “Medicine”/“Medicines” line with a demo total?
   - [Answer: selected fixed medicine lines and a demo total]

235. Which IT account actions should be available for each state: Active, Blocked, Banned, Deactivated, and Soft-deleted? For example, restore active, ban, deactivate, and permanent delete/record-hide.
   - [Answer: you decide]

236. If a patient self-deletes and later re-registers, should the old patient ID remain referenced in old bills, wards, and appointments, or should old records be detached from the new account and only remain in IT audit history?
   - [Answer: old patient ID remain referenced in old bills, wards, and appointments]

237. May an inactive patient still retain active ward, bill, and appointment relationships, or should the account deletion/deactivation automatically remove or close those relationships?
   - [Answer: the account deletion/deactivation automatically remove or close those relationships?]

238. May patients edit any profile field after registration, or only phone, address, emergency contact, password, and/or name/date of birth?
   - [Answer: only phone, address, emergency contact, password, and/or name/date of birth]

239. If a patient changes their password, should the UI show a normal success state directly or retain the exact near-future behavior as a placeholder?
   - [Answer: retain the exact near-future behavior as a placeholde]

---

# Updated Project Understanding - Sixth and Final Consolidation Pass

## Project status

CHMS is a centralized, one-hospital, academic web-management prototype. It is a supporting digital aid alongside paper/manual hospital workflows, not a real clinical system or full hospital replacement.

The core delivery is a live, role-based Vercel web application with React, TypeScript, Vite, FastAPI, SQLModel, Alembic, Argon2, PyJWT, PostgreSQL/Supabase, SQLite, and Supabase Storage. The backend uses feature folders with routers, schemas, services, repositories, dependencies, and database models. The frontend uses pages, components, contexts, and API service modules.

The interface uses a dark-grey-and-white desktop design, Chrome/Firefox support, a shared login form, and separate dashboards for:

- Patient
- Doctor
- Ward Doctor
- Assistant
- Pathologist
- Accountant
- Ward Nurse
- Pharmacy Staff
- IT/System Administrator

Patient self-registration and staff account management are included. Testing, static analysis, source documentation, usability evidence, team contribution evidence, Git/Trello/Discord evidence, and final report packaging are deferred administrative tasks.

## Accounts and identity

Each account has exactly one role. Patient IDs are automatically generated 8-digit numbers. Staff IDs are manually assigned 4-digit numbers.

Patients register publicly with name, phone number, address, date of birth, emergency contact, password, and optional blood group. Blood group is not mandatory. Patients log in with patient ID only. Staff log in with staff ID only. Phone number is searchable by staff but is not an authentication identifier.

Staff accounts are provisioned by IT. IT may create and manage staff accounts, assign/change roles, block/banned/deactivate/soft-delete accounts, manage Ward Nurse ward assignments, access all patient data, and view audit logs.

Patients may delete/deactivate their own account. Staff cannot delete or reset their own account. IT cannot reset patient or staff passwords. Password/profile changes use normal profile behavior, while password recovery and reset controls use the near-future placeholder behavior.

After patient deletion/deactivation, the patient may re-register and receive a new 8-digit ID. Existing records continue to reference the old patient ID and remain visible through the old historical relationship.

Active staff sessions stop immediately when IT blocks or soft-deletes the account. The system may distinguish Active, Blocked, Banned, Deactivated, and Soft-deleted states. IT is responsible for consistent restore/ban/deactivate actions.

## Authentication

Passwords use Argon2. Sessions use 15-minute access tokens, 7-day refresh tokens, secure HttpOnly/SameSite=Strict refresh cookies, and refresh-token rotation.

The current-device logout is implemented. Failed-login lockout, OTP, email verification, password recovery, revoke-other, and revoke-all are placeholder-only controls.

The system logs create, update, delete, login success/failure, security, denied-access, role-change, and account-administration events. Ordinary views are not logged. Audit records are append-only and permanent, visible only to IT, and never contain passwords or tokens.

## Patient and role views

Staff search by exact patient ID, partial/full name, or phone number. IT can access all records. Other roles are restricted by role and/or relationship:

- Doctors manage their own outpatient schedules and search/review authorized patient history.
- Ward Doctors review ward patients and create prescription placeholders only.
- Assistants belong to one Doctor, can be reassigned by IT, and manage only that Doctor's patients/appointments.
- Ward Nurses belong to a ward, view all report/prescription objects for current ward patients, and manage ward assignments/discharge.
- Accountants create/edit bills and mark payments.
- Pharmacy Staff open prescription placeholders and create medicine bills.
- Pathologists search patients and create/publish pathology placeholders.

Patient profile changes are limited to editable personal/contact fields and password. The system does not allow IT/staff to edit patient identity/profile fields.

## Appointment behavior

Only regular/outpatient Doctors accept appointments. Ward Doctors do not use outpatient scheduling.

Appointments use 15-minute, exclusive slots and require only Doctor, patient, date, and time slot. No reason or appointment type field is required.

Patients and Assistants can book. Patients, Doctors, and Assistants can cancel. Doctors and Assistants can block/cancel/reschedule and mark visits. Patients, Doctors, and Assistants can remove cancelled records.

Statuses are Scheduled, Cancelled, Completed, and Missed. Cancellation and rescheduling are blocked within 24 hours of appointment start. Cancelled appointments remain visible until removed.

Doctors and Assistants may block a slot, day, or week until reopened. Scheduled slots cannot be blocked directly; staff must cancel first. Booking and scheduling changes use atomic database protection.

Doctor/Assistant cancellation shows a reminder popup that staff should call the patient. Cancelled records retain cancellation actor, timestamp, and optional reason.

## Ward behavior

IT assigns Ward Nurses to wards and may change those assignments. Ward Nurses may assign or transfer patients to wards and may keep only one active ward/bed assignment per patient.

A ward assignment stores ward, bed/room, and admission date. Ward discharge clears the active ward/bed assignment and saves discharge status, discharge date/time, Ward Nurse ID, and an optional general discharge note. Ward transfer and discharge history remain available.

## Placeholder behavior

Any unimplemented feature remains visible but uses a near-future placeholder. Clicking it opens a popup/form saying the feature will be implemented in the near future.

Confirm/Create creates a persisted placeholder object stamped with creator ID and timestamp. Opening the object displays the near-future message and only permitted read-only placeholder details.

This rule applies to medical reports, external uploads, prescription details/PDF/print, test-report workflows, online payments, password recovery, and other explicitly deferred features. Password changes, however, use a normal success state plus the near-future behavior as specified.

Prescription creation/viewing is placeholder-only. It persists and is visible to authorized Doctor, Ward Doctor, Ward Nurse, Pharmacy, and Patient views. It has no real dosage, duration, route, quantity, or clinical details.

Medical, prescription, external-upload, and pathology objects remain visible and permanently stored rather than edited or removed by ordinary users.

When a placeholder form is cancelled, draft fields remain in the form. Confirm/Create saves the placeholder object and navigates to the relevant list/detail view.

## Laboratory and pathology simplification

There is no test-request queue, sample state, Draft/Pending Verification/Released state, or paid-before-sample workflow.

Accountants use fixed demo test entries: Placeholder Test 1, Placeholder Test 2, and additional placeholders if needed. Each test has a demo price. A test bill may contain several test lines.

The Doctor/Ward Doctor report/prescription provides clinical context. The Accountant searches for a patient and creates a test bill. The patient pays manually or through a demonstration online-payment state.

Manual payment marks a bill Paid immediately. Online payment UI is placeholder unless it demonstrably changes a bill status to Paid. Real payment gateway integration is outside scope.

The Pathologist searches the patient and directly creates a pathology placeholder object. The patient object shows test name, billing status, pathologist identity, publish date, and the near-future message.

## Billing and pharmacy

Bills support consultation, diagnostic test, medicine, and service charges. Bills have ID, patient, accountant, date, line items, total, and Paid/Unpaid status.

Only full payment is allowed. Accountants may edit Unpaid bills. Paid bills become immutable and remain in patient/all-bill history.

Manual payment creates a paid receipt conceptually. Download/print and detailed receipt/gateway fields are placeholder-only.

Pharmacy Staff select fixed demo medicine lines and quantities, create an immediate medicine bill with a demo total, and may continue editing it until payment. After Paid, the bill is immutable. The previous answer no longer requires an actual medicine inventory or real dispensing workflow.

## Profile, retention, and privacy

Patients may edit allowed profile fields and password. Name and date of birth are included as editable fields in the latest answer, but phone, address, emergency contact, and password are the clearest intended fields. IT and regular staff cannot edit the patient's identity/profile.

Patient deletion/deactivation closes active ward, bill, and appointment relationships. It is implemented as soft deactivation. The historical old patient ID remains referenced in prior bills, ward history, appointments, audit entries, and clinical objects.

Inactive/deactivated patients remain in staff search and are clearly marked inactive. They retain old historical records for authorized staff/IT but should not retain active relationships.

Patient, bill, appointment, ward, clinical, prescription, pathology, and audit records are retained indefinitely for the academic system. Supabase handles production storage/backups conceptually.

External uploads, report file storage, print/download, and receipt download are placeholder-only. Supabase Storage is reserved for future real file implementation. Direct URL access to another patient's object must be denied.

## UI and deferred work

The UI uses standard loading, empty, validation, success, confirmation, and access-denied states. It retains draft fields when placeholder forms are cancelled and returns to the relevant list/detail view after Create.

Testing framework and coverage, static analysis, source documentation, usability evaluation, team/member contributions, Trello/Discord/Git evidence, PDF/DOCX report, and Wiki pages are deferred.

---

# 22. Remaining confirmation questions

240. Should fixed demo medicine prices be simple numbers chosen by the implementation, or should the test/medicine prices remain unvalued placeholders?
   - [Answer: fixed simple numbers ]

241. Should the patient profile's editable fields be exactly phone, address, emergency contact, name, date of birth, and password, while blood group remains non-editable after registration?
   - [Answer: yes]

242. When a patient is soft-deactivated, should their old ID remain usable for staff record lookup and audit only, or should it remain searchable as an inactive patient with no active services?
   - [Answer:old ID remain usable for staff record lookup and audit only ]

---

# Updated Project Understanding - Seventh and Current Scope Consolidation

## Scope decision

No further implementation-blocking questions are necessary at this point. The remaining points can be resolved with normal academic-demo defaults unless the project owner explicitly changes them later.

CHMS is a one-hospital academic web application that works alongside existing paper/manual workflows. It is not a real clinical system and is not a complete replacement for hospital operations.

The implementation will use React, TypeScript, Vite, FastAPI, SQLModel, SQLite for local development/testing, PostgreSQL through Supabase for production, Alembic, PyJWT, Argon2, Supabase Storage, and Vercel deployment.

The backend uses feature-folder organization with routers, schemas, services, repositories, dependencies, and database models. The frontend uses pages, reusable components, contexts, and API service modules.

The UI has a dark-grey-and-white polished desktop style, a shared login form, and these dashboards:

- Patient
- Doctor
- Ward Doctor
- Assistant
- Pathologist
- Accountant
- Ward Nurse
- Pharmacy Staff
- IT/System Administrator

## Authentication and accounts

Patients are publicly registered by 8-digit patient ID and password. Staff use 4-digit IDs and are manually provisioned by IT.

Patient login uses only patient ID. Staff login uses only staff ID. Phone number is search/contact data, not login identity.

Patient registration collects name, phone, address, date of birth, emergency contact, password, and optional blood group. Patients may edit name, phone, address, date of birth, emergency contact, and password. Blood group is not editable after registration.

Passwords use Argon2. Access tokens last 15 minutes. Refresh tokens last 7 days and use secure HttpOnly/SameSite=Strict cookies with refresh-token rotation. The current-device logout is implemented.

Lockout, OTP, email verification, password recovery, revoke-other, and revoke-all are placeholder services. Password change itself is a real profile action and should return a normal success state.

IT provisions, blocks, bans, deactivates, and soft-deletes accounts, changes staff roles, assigns Ward Nurses to wards, accesses all patient data, and views audit logs. Staff cannot change their own role or delete/reset their own account. IT cannot reset passwords.

When IT blocks or soft-deletes a staff account, active sessions stop immediately. Patient soft-deactivation closes active ward, bill, and appointment relationships. Existing history remains linked to the old patient ID for staff lookup and audit.

## Roles and relationships

Doctors manage only their own outpatient schedules and review/search authorized patient history.

Ward Doctors are separate from Doctors. They cannot manage outpatient appointments or create full medical reports. They can create prescription placeholders and view ward patients.

Assistants belong to one Doctor, can be reassigned by IT, and can book/cancel/reschedule/block appointments and mark outcomes for that Doctor. They can remove cancelled appointment records.

Ward Nurses are assigned to wards by IT. They can assign, transfer, and discharge ward patients and view all report/prescription objects for patients in their current ward.

Accountants search patients and create/edit Unpaid bills and mark bills Paid. Pharmacy Staff open prescription placeholders and create medicine bills. Pathologists directly search patients and create/publish pathology placeholders.

## Appointments

Outpatient appointments are 15-minute, exclusive Doctor slots. Ward Doctors do not participate in outpatient scheduling.

Booking requires patient, Doctor, date, and slot only. No reason or appointment type is required.

Valid statuses are Scheduled, Cancelled, Completed, and Missed. Patients and Assistants can book. Patients, Doctors, and Assistants can cancel. Doctors and Assistants can block schedules and mark completed/missed appointments.

An appointment cannot be cancelled or changed within 24 hours of the appointment start. Rescheduling follows the same 24-hour rule.

Cancelled records remain visible until removed. Patients, Doctors, and Assistants may remove cancelled records. Cancellation keeps the cancellation actor, timestamp, and optional reason.

Doctors and Assistants can block a slot, day, or week until reopened. An already scheduled slot must be cancelled first. Booking, cancellation, and rescheduling use atomic database protection.

Doctor/Assistant cancellation opens a popup reminding staff to call the patient.

## Wards

Ward assignments contain ward, bed/room, and admission date. A patient may have only one active ward assignment.

IT assigns Ward Nurse-to-ward relationships. Ward Nurses assign or transfer patients and manage discharge. Discharge clears active ward/bed assignment while retaining discharge status, date/time, Ward Nurse ID, optional note, and historical ward data.

## Placeholder behavior

Features marked as not implemented remain visible but use a near-future placeholder. Clicking Create/Confirm creates a persisted placeholder object with creator ID and timestamp.

Opening the placeholder shows the near-future message and permitted read-only details. Cancelled placeholder forms retain draft fields. Confirming creates the object and returns to the relevant list/detail view.

This applies to medical reports, external uploads, prescription detail/PDF/print, test reports, payment gateway UI, password recovery, and other explicitly deferred services.

Prescription creation/viewing is placeholder-only and persistent. It is visible to authorized Patient, Doctor, Ward Doctor, Ward Nurse, and Pharmacy roles. It has no real clinical medicine fields.

Medical, prescription, external-upload, and pathology objects remain persistent and are not normally editable or removable by ordinary roles.

## Pathology and test billing

The detailed test-request, sample, verification, and report status workflow is outside the implementation.

Accountants use fixed demo test entries, such as Placeholder Test 1 and Placeholder Test 2, with simple demo prices. A test bill may contain multiple test lines.

Accountants search for a patient and create test bills. Doctor/Ward Doctor clinical context is not required to automatically create a bill.

Manual payment is confirmed by the Accountant and changes the bill to Paid. The online-payment UI may demonstrate a Paid transition, but no real gateway is integrated.

The Pathologist searches a patient and creates/publishes a pathology placeholder object with test name, billing status, pathologist identity, publish date, and the near-future message.

## Billing and pharmacy

Bills support consultation, diagnostic test, medicine, and service charges. Each bill has a unique ID, patient, accountant, date, line items, total, and Paid/Unpaid status.

Partial payment is not supported. Accountants may edit Unpaid bills. Paid bills are immutable and remain in patient/all-bill history.

Manual and demonstrated-online payments make the bill Paid. Receipt download/print and detailed gateway/receipt implementation remain placeholders.

Pharmacy Staff choose fixed demo medicine lines and quantities and immediately create a medicine bill with a demo total. They may continue editing until the bill is Paid. Paid bills become immutable.

## Data, privacy, and retention

Patient, bill, ward, appointment, prescription, pathology, and audit records are retained indefinitely for the academic demo. Soft-deactivated patient records are visible to authorized staff and IT and remain linked to historical old IDs.

Supabase is the production database/storage platform and is expected to handle backups conceptually. External uploads and real file storage are placeholder-only.

Direct URL access must not reveal another patient's record or report.

## UI and deferred deliverables

The UI uses loading, empty, validation, success, confirmation, and denied states, with consistent system-controlled wording.

Testing framework/coverage, static analysis, source documentation, usability evidence, team contributions, Trello/Discord/Git evidence, PDF/DOCX report, and Wiki pages are deferred.

The scope is currently sufficient for implementation. If a later design decision changes a settled answer, it should be recorded here and propagated to the SRS, use cases, UI, data model, and tests.

# 23. Questions status

No further questions are necessary. The remaining unresolved implementation details are either deferred, intentionally delegated to normal demo conventions, or low-risk choices that do not change the project scope.

---

# 24. Copilot-to-Copilot Implementation Handoff

## 24.1 Purpose of this document

This section is the authoritative implementation handoff for CHMS. It is a summary of the decisions that are spread across the earlier sections of this file. If the older SRS, use cases, or user stories conflict with this section, follow this section. The repository at the start of implementation contains documentation only: `README.md`, `requirements.txt`, and files under `Docs/`. There is no existing application source code.

Do not implement old features that were explicitly removed or replace as placeholders. Do not infer that the project is a real clinical product.

## 24.2 Project identity

- Project: Centralized Hospital Management System (CHMS)
- Purpose: academic, centralized hospital-management demonstration
- Product character: digital aid intended to operate alongside paper/manual workflows
- Deployment target: Vercel frontend, FastAPI backend, PostgreSQL/Supabase production database, Supabase Storage for future files
- Local database: SQLite
- Production database: PostgreSQL through Supabase
- Primary desktop browsers: Chrome and Firefox
- UI style: polished, PC-oriented, dark-grey-and-white
- Login: one shared login form for all users
- Final product: role-based dashboards, central demo data, placeholder services, and academic reporting evidence

CHMS is not intended for real medical use and must not present placeholder reports or placeholder payment records as clinically or financially real.

## 24.3 Technology and architecture

### Frontend

- React
- TypeScript
- Vite
- Page/component/context structure
- API service modules
- Shared login
- Separate role dashboards
- Dark-grey-and-white theme
- Desktop/general responsive layout

Use clear loading, empty, validation, success, confirmation, and access-denied states.

### Backend

- FastAPI
- SQLModel
- SQLite locally
- PostgreSQL/Supabase production
- Alembic migrations
- PyJWT
- Argon2 password hashing
- Feature-folder architecture

Each feature should follow this pattern where practical:

```text
feature/
  router.py
  schema.py
  service.py
  repository.py
  dependencies.py
  models.py
```

Shared modules may contain database setup, authentication dependencies, role/permission dependencies, configuration, audit logging, and exception handling.

### Authentication

- 15-minute access tokens
- 7-day refresh tokens
- HttpOnly, Secure, SameSite=Strict refresh cookie
- refresh-token rotation
- Argon2 password hashing
- server-side role and account-state verification on every protected request
- JWT role is not the only authorization source
- logout the current session/device

Do not implement failed-login lockout unless a later decision explicitly restores it.

Do not implement OTP, email verification, password recovery, revoke-other, or revoke-all as real workflows. Their controls may show the near-future placeholder.

## 24.4 Roles

The system has exactly one role per account:

1. Patient
2. Doctor
3. Ward Doctor
4. Assistant
5. Pathologist
6. Accountant
7. Ward Nurse
8. Pharmacy Staff
9. IT/System Administrator

Patient and staff account types are separate.

### Doctor

- manage only their own outpatient schedule;
- search/review authorized patient history;
- create prescription placeholder objects;
- cancel, block, reschedule, and mark appointment outcomes.

### Ward Doctor

- separate role from Doctor;
- view ward patients;
- create prescription placeholder objects;
- cannot create full medical reports;
- cannot manage outpatient appointments.

### Assistant

- assigned to one Doctor;
- IT may reassign the assistant;
- see only the assigned Doctor's patients and schedules;
- book, cancel, reschedule, block, and mark appointments;
- remove cancelled appointment records;
- verify operational receipt/bill status where permitted.

### Ward Nurse

- assigned to one ward by IT;
- assign and transfer patients;
- discharge patients;
- view all report and prescription objects for current ward patients;
- view no other ward's patients.

### Pharmacy Staff

- search prescription placeholder objects;
- select fixed demo medicine lines;
- create medicine bills immediately;
- continue editing an unpaid bill until it becomes Paid.

### Accountant

- search patients;
- create, view, and edit unpaid bills;
- add multiple diagnostic test lines;
- mark a bill Paid after manual or demonstrated online confirmation;
- view Paid bill history;
- cannot edit a Paid bill.

### Pathologist

- search for a patient;
- create/publish a pathology placeholder object;
- no real request queue or report verification workflow.

### IT/System Administrator

- create staff accounts;
- assign and change staff roles;
- block, ban, deactivate, or soft-delete accounts;
- restore accounts according to chosen account-state transition rules;
- assign and reassign Ward Nurses to wards;
- access all patient data;
- view audit logs;
- cannot be bypassed by frontend-only role checks.

## 24.5 Account identity and lifecycle

### Patient

- public self-registration;
- automatically generated 8-digit patient ID;
- login uses patient ID and password;
- phone number is not used for login;
- staff may search by ID, partial/full name, or phone.

Mandatory registration fields:

- name
- phone number
- address
- date of birth
- emergency contact
- password

Blood group is optional.

Editable by patient after registration:

- name
- phone number
- address
- date of birth
- emergency contact
- password

Blood group is not editable after registration. Staff and IT cannot edit patient identity/profile fields.

### Staff

- 4-digit manually assigned staff ID;
- password created by IT;
- IT cannot reset a password in the implemented scope;
- each account has exactly one role.

### Deactivation and deletion

- patient deletion is soft deactivation;
- patient may re-register and receive a new 8-digit ID;
- the old ID remains referenced by historical bills, wards, appointments, audit entries, and clinical objects;
- soft-deactivated patients remain searchable as inactive by authorized staff/IT;
- active ward, bill, and appointment relationships are closed on deletion/deactivation;
- historical records remain for audit and record continuity;
- staff account blocking/deletion invalidates active sessions immediately.

Use one consistent account-state model rather than allowing contradictory UI states. Suggested technical values are `ACTIVE`, `BLOCKED`, `BANNED`, `DEACTIVATED`, and `SOFT_DELETED`. Active sessions must be invalidated for blocked/banned/deactivated/deleted staff accounts.

## 24.6 Appointment workflow

Only regular/outpatient Doctors accept appointments. Ward Doctors cannot manage outpatient appointments.

### Slot rules

- fixed 15-minute slots;
- one patient per slot;
- exclusive slot availability;
- atomically prevent double booking;
- statuses: `SCHEDULED`, `CANCELLED`, `COMPLETED`, `MISSED`;
- no `CONFIRMED` status;
- no appointment reason or appointment type field.

Use a database locking/conditional-update approach so concurrent requests cannot create duplicate appointments.

### Booking

Required booking fields:

- patient
- Doctor
- date
- time slot

Allowed actors:

- Patient
- Assistant for a patient

### Cancellation, rescheduling, and removal

- Patients, Doctors, and Assistants may cancel/reschedule qualifying appointments;
- cancellation/rescheduling is blocked when less than 24 hours remain;
- rescheduling follows the cancellation rule;
- Doctors and Assistants may cancel without a reason;
- Assistants do not require a cancellation reason;
- cancellation records retain cancellation actor, timestamp, optional reason, and old/new status;
- cancelled records remain visible;
- Patients, Doctors, and Assistants may remove cancelled records;
- Doctor/Assistant cancellation opens a reminder popup telling staff to call the patient.

### Blocking and closing slots

- Doctors and Assistants may block their own/assigned schedule;
- blocks may be slot, day, or week;
- blocks remain indefinitely until reopened;
- an already scheduled slot cannot be blocked directly;
- staff must cancel the scheduled appointment first;
- cancellation frees the slot unless it remains explicitly blocked.

## 24.7 Ward workflow

Ward assignment is part of a patient's record.

Ward assignment fields:

- ward
- bed/room
- admission date
- active/inactive assignment status

A patient may have only one active ward assignment.

Ward Nurse assignment to a ward is managed only by IT.

Ward Nurses may:

- assign a patient to their ward;
- transfer a patient to another ward;
- discharge a patient;
- view all report and prescription objects for patients in their current ward.

Ward discharge fields:

- discharge status
- discharge date/time
- Ward Nurse ID
- optional general discharge note

Discharge clears the active ward/bed assignment but preserves historical ward assignment and discharge records.

## 24.8 Prescription workflow

Prescription creation and viewing are placeholder-only.

Both:

- Doctor
- Ward Doctor

may create prescription placeholder objects.

No real medicine/dosage/duration/route/quantity data is required by the current scope. The prescription object is persisted and stamped with creator ID and timestamp.

Visible to:

- the patient;
- authorized Doctor/Ward Doctor views;
- Ward Nurses for their assigned ward patients;
- Pharmacy Staff;
- IT.

The prescription detail/PDF/print operation opens the near-future placeholder rather than a real generated prescription.

Pharmacy Staff open the prescription placeholder and create an immediate medicine bill.

Prescription placeholder objects are permanently visible and may not be edited or removed through ordinary clinical UI.

## 24.9 Medical report workflow

Full medical-report creation, diagnosis, clinical notes, external reports, and file download are placeholder-only.

Clicking Create Report opens the near-future popup. Confirming creates a persisted placeholder medical-report object. Opening the object shows read-only placeholder information and the near-future message.

Accountants may use report context to create an appropriate test bill.

Ward Doctors cannot create full medical reports.

## 24.10 Simplified pathology workflow

Do not implement the old detailed request/sample verification state machine. The final demo has no:

- test request queue
- requested/awaiting-payment/sample-collected/in-progress/rejected statuses
- paid-before-sample enforcement
- Draft/Pending Verification/Released report state
- parameter reference ranges
- verification signatures

### Test billing

- use a fixed demo test list;
- placeholder test entries may include `Placeholder Test 1`, `Placeholder Test 2`, and more;
- each test has a simple demo price;
- Accountants search the patient and create a bill containing multiple test lines;
- the Doctor/Ward Doctor report context informs the Accountant which test to add;
- there is no automatic bill creation from the report.

### Payment

- unpaid and paid are the only bill statuses;
- no partial payments;
- Accountant marks the bill Paid after manual counter payment;
- online payment UI may demonstrate status changing to Paid but is not a real gateway;
- real receipt upload/download is placeholder-only.

### Publication

- Pathologist searches the patient and creates/publishes a pathology placeholder object directly;
- no paid bill queue is required;
- patient object displays test name, billing status, pathologist identity, publish date, and near-future message.

## 24.11 Billing and pharmacy workflow

Supported service categories:

- consultation
- diagnostic tests
- medicines
- service charges

Other hospital stay/admission concepts should use the UI label `Service Charge` for the demo.

### Bill fields

- bill ID
- patient
- Accountant
- bill date
- line items
- quantity
- unit demo price
- total
- Paid/Unpaid status

### Editing

- only Unpaid bills may be edited;
- Paid bills are immutable;
- Paid bills remain in patient and Accountant history;
- partial payments are forbidden.

### Pharmacy

- use fixed demo medicines and quantities;
- `Medicine 1`, `Medicine 2`, and quantity choices should be fixed demo values;
- selected medicine lines and a demo total create an Unpaid medicine bill;
- Pharmacy Staff may edit the Unpaid bill until it becomes Paid;
- no real dispensing/completed status is required.

### Manual payment

The Accountant creates the bill and marks it Paid after manual counter payment.

### Online payment

The UI may show/act as a demonstration and mark a bill Paid. No real gateway, bKash, card, bank integration, receipt file, or transaction validation is required.

## 24.12 Audit and security

### Audit these events

- account create/update/delete/block/bann/deactivate/restore
- role change
- login success
- login failure
- invalid/expired/forged token events
- refresh-token reuse
- denied access
- appointment create/update/cancel/block
- bill create/update/mark-paid
- prescription placeholder create
- report placeholder create
- pathology placeholder create
- ward assign/transfer/discharge

Do not log ordinary patient-record views.

Audit entries should contain, where applicable:

- timestamp
- actor user ID
- actor role
- patient ID
- action
- entity type
- entity ID
- IP address
- user agent
- old/new status or result

Audit records are append-only and permanent. Only IT can view them. Never log passwords or tokens.

## 24.13 Patient privacy and direct access

- patient sees only own account records;
- staff view only records permitted by role and relationship;
- IT can access everything;
- direct URL access to another patient's record or report must return an access-denied response;
- no public direct file URL should expose a patient's record;
- no privacy notice or consent screen is required;
- external upload/report file implementation is placeholder-only;
- Supabase Storage is reserved for future real file workflows.

## 24.14 UI requirements

### General

- shared login form;
- role-specific navigation;
- no role's menu items should be visible to an unauthorized role;
- backend RBAC must independently reject direct URL/API access;
- dark-grey-and-white visual system;
- Chrome/Firefox desktop support;
- clear loading, empty, validation, confirmation, success, and denial states.

### Required dashboards

- Patient
- Doctor
- Ward Doctor
- Assistant
- Pathologist
- Accountant
- Ward Nurse
- Pharmacy Staff
- IT

### Near-future UI behavior

For every explicitly unimplemented feature:

1. Show the feature control/page.
2. Open a popup/page containing the exact user-facing message:

`Will be implemented in the near future`

3. Pressing Create/Confirm persists a placeholder/domain object.
4. Stamp it with creator ID and timestamp.
5. Opening the object shows read-only placeholder details and the near-future message.
6. Keep unsaved draft form fields if the popup is cancelled.
7. After confirmed creation, navigate to the relevant list/detail view.

## 24.15 Data behavior

- records are retained indefinitely for the academic project;
- backup responsibility is delegated conceptually to Supabase;
- no offline draft system is required;
- if the system is offline, it is down and paper fallback applies;
- account soft deletion is preferred over deleting clinical history;
- old patient IDs remain in historical relationships;
- inactive/deactivated patients may remain searchable for authorized staff but not for active services;
- active ward, bill, and appointment relationships close when a patient account is deactivated.

## 24.16 Recommended implementation order

### Task 1: Repository and environment

Create the Vite/React/TypeScript frontend and FastAPI/SQLModel backend. Add development and test configuration. Configure SQLite locally and PostgreSQL/Supabase environment variables for production. Add Alembic. Add Vercel build/deployment configuration. Do not populate clinical production data.

Deliverables:

- runnable frontend;
- runnable backend;
- `/api/docs`;
- SQLite local database;
- migration setup;
- environment examples.

### Task 2: Shared database and RBAC

Add shared SQLModel models and migration setup. Add account, role, staff assignment, patient, ward, audit, and refresh-session concepts. Add JWT authentication and server-side role dependencies.

Do not trust frontend role state. Enforce role and account state in API dependencies and service/repository methods.

Deliverables:

- register/login/logout/refresh endpoints;
- role decorators/dependencies;
- account-state checks;
- audit service;
- seed role/admin data.

### Task 3: Patient registration and staff administration

Build public patient registration and shared login. Generate unique 8-digit patient IDs. Build IT staff creation and role management.

Implement patient soft-deactivation and staff account states. Search patients by ID, name, and phone.

Deliverables:

- patient signup and profile;
- staff account provisioning;
- role assignment;
- account block/deactivate/delete UI;
- inactive patient visibility.

### Task 4: Frontend shell and dashboards

Create the shared navigation shell and nine role dashboards. Add route guards and role-specific menus.

Deliverables:

- shared login;
- role dashboards;
- sidebar/header/layout;
- loading/empty/error/denied states;
- placeholder popup component.

### Task 5: Appointment module

Implement 15-minute Doctor slots, exclusive booking, cancellation/rescheduling, status updates, Doctor/Assistant blocking, and atomic availability.

Implement:

- patient booking;
- assistant booking;
- Doctor/Assistant schedule;
- 24-hour rule;
- cancelled-record removal;
- staff call-reminder popup;
- Completed/Missed status actions.

Deliverables:

- appointment models/API;
- slot availability;
- no double-booking proof;
- doctor/assistant/patient screens;
- audit entries.

### Task 6: Ward module

Implement ward, bed/room, admission date, ward assignment, transfer, discharge, and Ward Nurse assignment.

Implement IT-only Ward Nurse-to-ward assignment and Ward Nurse assignment/transfer/discharge actions.

Deliverables:

- ward and assignment models;
- ward management pages;
- patient transfer/discharge history;
- Ward Nurse patient filtering.

### Task 7: Prescription placeholder module

Implement persisted prescription placeholder objects for Doctor and Ward Doctor. Add patient/ward nurse/pharmacy/Doctor views. Add newest-first ordering.

No real medicine data is required. Pharmacy links a prescription placeholder to a medicine bill.

Deliverables:

- create prescription placeholder;
- role-restricted detail/list pages;
- immutable placeholder objects;
- audit entries.

### Task 8: Medical and external-report placeholders

Implement persisted medical-report placeholders and external-report upload placeholders.

No real report content, file processing, PDF generation, or external storage processing is required. Preserve the near-future popup and persisted placeholder object behavior.

Deliverables:

- medical report placeholder page;
- patient external upload placeholder;
- report object list/detail;
- Supabase Storage integration left out unless later restored.

### Task 9: Billing and receipts

Implement bill line items, fixed demo test items, fixed medicine items, Unpaid/Paid statuses, immutable paid bills, manual marking of Paid, and placeholder online-payment UI.

Do not implement partial payments or real payment gateway APIs.

Deliverables:

- Accountant patient/bill screens;
- test bills with several lines;
- medicine bills;
- paid/unpaid filtering;
- receipt placeholder;
- audit entries.

### Task 10: Pharmacy module

Implement prescription search and fixed demo medicine selection. Generate an Unpaid medicine bill. Allow editing by Pharmacy Staff until Paid.

Deliverables:

- prescription lookup;
- fixed medicine list;
- bill creation;
- bill edit until paid;
- patient/Accountant visibility.

### Task 11: Pathology placeholder module

Implement patient search and pathology placeholder creation. Display test name, payment/billing status, pathologist identity, publish date, and near-future message.

Do not implement request queues or report verification states.

Deliverables:

- patient lookup;
- create/publish placeholder;
- patient-visible placeholder detail;
- audit entry.

### Task 12: Audit and security administration

Implement append-only audit repository and IT-only audit page. Add account security events and CRUD audit events.

Deliverables:

- immutable audit records;
- IT audit search/list;
- login/security event capture;
- role-change/account-event capture.

### Task 13: Testing

At minimum add backend and frontend tests for:

- authentication and role enforcement;
- account states;
- patient registration;
- 24-hour appointment rules;
- slot collision;
- cancellation reminder behavior;
- ward restrictions;
- unpaid/paid bill transitions;
- immutable Paid bills;
- prescription/pathology/report placeholder persistence;
- audit event creation;
- direct URL/endpoint denial.

Use test frameworks only after the implementation team chooses tooling. The final report may document both unit and integration coverage.

### Task 14: Deployment

Configure Supabase production database and environment variables. Run Alembic migrations. Deploy backend and frontend through a working Vercel setup. Verify role login and CRUD flows in the live deployment.

Deliverables:

- live Vercel URL;
- demo account seed data;
- screenshots;
- deployed database migration status.

### Task 15: Academic submission evidence

The following work is deferred and should not stop implementation:

- test coverage report;
- static-analysis findings;
- source documentation;
- usability evaluation;
- team roles/contributions;
- Trello/Discord/Git evidence;
- PDF/DOCX report;
- GitHub Wiki pages;
- demo video;
- final screenshots.

## 24.17 Verification matrix

Before implementation is considered complete, verify:

- each protected endpoint rejects wrong role;
- IT can access all data;
- ordinary staff cannot access IT-only audit logs;
- patient can see only own records;
- Ward Nurse can see only current-ward patients;
- Assistant sees only assigned Doctor's patients;
- Ward Doctor cannot open outpatient scheduling or full report creation;
- 24-hour cancellation/rescheduling is enforced;
- no appointment slot double booking is possible;
- Paid bills cannot be edited;
- partial payments cannot be created;
- placeholder creates are persisted;
- placeholder opens show near-future message;
- account state invalidates active staff sessions;
- soft-deactivated patient records preserve history;
- direct URL manipulation returns denied;
- passwords/tokens never appear in audit logs.

## 24.18 Recommended file structure

```text
frontend/
  src/
    components/
    contexts/
    pages/
      auth/
      patient/
      doctor/
      wardDoctor/
      assistant/
      pathologist/
      accountant/
      wardNurse/
      pharmacy/
      it/
    services/
    routes/
    types/

backend/
  app/
    core/
    auth/
    patients/
    staff/
    appointments/
    wards/
    prescriptions/
    reports/
    pathology/
    billing/
    pharmacy/
    audit/
    shared/
  migrations/
  tests/
```

The exact folder names may vary, but the feature-folder responsibility split should remain clear.

## 24.19 Agent completion instructions

Before marking each task complete:

1. read the relevant section of this QA file;
2. inspect the current diff;
3. implement the smallest complete vertical slice;
4. add focused tests for the behavior;
5. verify role and account restrictions;
6. run targeted tests first;
7. run the smallest relevant build/lint/type-check suite;
8. update this QA file only if a decision changes;
9. do not silently implement any old removed feature;
10. summarize changed files, tests, and remaining decisions.

---

# 25. Post-Implementation and Submission Tasks - Do not start these task until mentioned

These tasks begin after implementation is sufficiently stable to capture real screenshots, test reports, Git history, architecture evidence, and final source. They correspond to the 12 sections in `docs/Submission_task.md`.

The final deadline is November 28, 2026. The team should not postpone implementation evidence until the report-writing phase: evidence must be captured while features are still available in the live deployment.

The final Google Classroom report must cover all 12 sections. Every section must also become an individual GitHub Wiki page. All claims in the report must reflect actual project tools, files, decisions, tests, commits, and screenshots.

## Task 16: Finalize and validate the SRS

**When:** after the implementation scope is frozen

**Objective:** produce the final human-readable SRS in the existing `SRS.tex` format.

**Work**

1. Reconcile every requirement with the implemented behavior.
2. Keep the existing LaTeX class, package, title, section layout, and report style.
3. Add or clarify all nine roles and their permissions.
4. Document the 24-hour appointment rule, Scheduled/Cancelled/Completed/Missed statuses, and slot exclusivity.
5. Document Paid/Unpaid-only bills, no partial payment, placeholder behavior, and simplified pathology.
6. Document the implementation stack, SQLite/Supabase split, Vercel deployment, security model, and account deactivation.
7. Add no requirement that was not implemented or is intentionally placeholder-only.
8. Compile and inspect the PDF.

**Evidence**

- final `Docs/SRS.tex`;
- compiled SRS PDF;
- resolved requirement checklist;
- screenshots only when they explain a visual requirement.

**Acceptance**

- no contradictory old requirements remain;
- every requirement is traceable to a use case or implementation behavior;
- placeholder features are clearly identified;
- the PDF has no broken LaTeX, blank sections, or formatting overflow.

## Task 17: Create the Software Design Specification

**When:** after feature behavior is stable

**Objective:** create an existing-style SDS document showing UML use cases, use-case narratives, state diagrams, and Level 0 DFD.

**Work**

1. Create or finalize the SDS structure required by the course.
2. Produce a system use-case diagram covering Patient and all staff roles.
3. Split large diagrams into Patient, Clinical, Billing, Ward, and IT views if a combined diagram becomes unreadable.
4. Include final use-case narratives from `Docs/Use_case.md`.
5. Create appointment state diagrams for Scheduled, Cancelled, Completed, and Missed.
6. Create bill state diagrams for Unpaid and Paid.
7. Create patient account states for active/deactivated/soft-deleted relationships.
8. Create placeholder-object lifecycle diagrams: open, popup, confirm, persisted placeholder, detail view.
9. Create a Level 0 DFD showing the patient, all staff actors, CHMS, database, storage placeholder, and external paper fallback.
10. Add role restriction and audit relationships.

**Evidence**

- SDS document;
- source UML files or editable diagrams;
- exported PNG/PDF diagrams;
- traceability between use cases and requirements.

**Acceptance**

- every actor in the implementation appears;
- no old `Confirmed`, `Draft/Pending Verification/Released`, or partial-bill states appear;
- appointment and bill transitions match the final decisions;
- DFD Level 0 boundaries and data flows are technically coherent.

## Task 18: Capture Trello and Discord collaboration evidence

**When:** throughout implementation, but collect and organize before final report assembly

**Objective:** provide real evidence of team planning, task tracking, discussions, and collaboration.

**Work**

1. Export or capture the Trello board at several Sprint stages:
   - initial backlog;
   - in progress;
   - completed;
   - blocked/resolved item.
2. Capture card descriptions and assignees where available.
3. Capture Discord channels and relevant technical/project discussions.
4. Select only screenshots that reveal real team activity.
5. Add one-sentence explanations for every screenshot.
6. Link board/channel evidence to actual implementation tasks.

**Evidence**

- board screenshots;
- task-card screenshots;
- Discord channel/discussion screenshots;
- explanatory captions.

**Acceptance**

- no fabricated or empty activity;
- evidence demonstrates task movement and communication;
- screenshots are readable and labeled;
- Sprint movement and responsibilities are visible.

## Task 19: Document the architectural pattern

**When:** after the backend/frontend folder structure is finalized

**Objective:** explain the architectural pattern and implementation rationale.

**Work**

1. Describe the feature-folder/layered architecture.
2. Diagram frontend pages/components/context/API service boundaries.
3. Diagram backend router/schema/service/repository/dependency/model boundaries.
4. Explain server-side RBAC and audit placement.
5. Explain SQLite versus PostgreSQL/Supabase selection.
6. Explain Vercel, FastAPI, Alembic, Supabase, and storage responsibilities.
7. Explain why this pattern is appropriate for a single-hospital academic prototype.
8. Show source snippets from real files, not hypothetical code.

**Evidence**

- architecture diagram;
- folder-structure screenshots;
- real code snippets;
- deployment/data-flow explanation.

**Acceptance**

- architecture claims match actual repository structure;
- cross-layer dependencies are clear;
- no microservice or distributed architecture is claimed unless implemented.

## Task 20: Document coding standards

**When:** after core source style is established

**Objective:** document the team's coding standards with real examples.

**Work**

1. Define Python naming, formatting, import, type, model, service, and exception conventions.
2. Define TypeScript/React naming, component, hooks, API, and formatting conventions.
3. Document SQLModel/Alembic naming conventions.
4. Document API response and validation conventions.
5. Document commit/branch conventions used in the repository.
6. Use actual before/after or well-written source snippets.
7. Explain automated format/lint tools if used.

**Evidence**

- coding-standard document/page;
- representative backend and frontend code examples;
- formatter/linter configuration.

**Acceptance**

- examples come from the repository;
- standards describe repeated real practices;
- every rule can be tied to a code example or tool configuration.

## Task 21: Configure and document source-code documentation

**When:** after public APIs and major modules are stable

**Objective:** fulfill the source-code documentation tool section.

**Work**

1. Select one source-documentation tool for the implementation stack.
2. Document installation/setup steps.
3. Define comments, docstring, and TypeScript documentation conventions.
4. Add representative documentation comments to backend and frontend source.
5. Generate the documentation output.
6. Capture generated documentation screenshots or exported HTML/PDF.

**Candidate tools**

- Python: Sphinx or MkDocs
- TypeScript/React: TypeDoc
- Alternative course-appropriate tools only if actually installed and used

**Evidence**

- installation instructions;
- config file;
- sample documented code;
- generated docs output/screenshots.

**Acceptance**

- tool is installed and reproducible;
- generated output exists;
- screenshots show the actual generated project documentation.

## Task 22: Capture representative UI design evidence

**When:** after deployment and demo seed data are available

**Objective:** provide screenshots of the key implemented UI with concise explanations.

**Work**

1. Capture the shared login and patient sign-up experience.
2. Capture each of the nine role dashboards or representative dashboard states.
3. Capture booking, schedule, ward, billing, pharmacy, pathology, prescription, account, and audit screens.
4. Capture normal, empty, validation, success, denied, and placeholder states.
5. Capture at least one call-reminder cancellation popup.
6. Capture one near-future placeholder create/detail flow.
7. Include desktop Chrome and, if tested, Firefox evidence.
8. Blur or use demo data only; do not show real patient information.

**Evidence**

- high-resolution screenshots;
- screen labels and explanations;
- live deployment link;
- optional short demo video.

**Acceptance**

- screenshots show real, deployed UI;
- all key actors and placeholder behavior are represented;
- no unsupported real-medical claims are displayed.

## Task 23: Perform Nielsen heuristic and usability evaluation

**When:** after UI stabilization, before final report assembly

**Objective:** evaluate the UI against Nielsen's 10 Usability Heuristics.

**Work**

1. Select the actual tools/plugins used:
   - Lighthouse
   - WAVE
   - Axe
   - or a structured Nielsen heuristic checklist
2. Run browser-based accessibility and usability checks on representative pages.
3. Map findings to relevant heuristics.
4. Fix at least the most important findings if possible.
5. Record before/after evidence.
6. Explain remaining limitations.

**Minimum evaluation coverage**

- login/signup;
- patient dashboard;
- one staff dashboard;
- appointment booking;
- billing;
- placeholder popup/detail;
- denied/empty state.

**Evidence**

- tool report;
- checklist;
- issue descriptions;
- screenshots;
- corrective changes and final recheck.

**Acceptance**

- actual tool output is included;
- findings are tied to Nielsen heuristics;
- improvements are real and verifiable;
- a tool is not described if it was not used.

## Task 24: Run code review/static analysis

**When:** after the implementation reaches a stable build

**Objective:** use code review and static-analysis tooling and document at least five findings/fixes.

**Work**

1. Select and configure the actual tools:
   - ESLint
   - Pylint/Ruff
   - SonarQube
   - or an equivalent documented tool
2. Run static analysis on frontend and backend.
3. Select at least five genuine bugs, smells, or maintainability findings.
4. Describe exact file, rule, impact, and corrective action.
5. Fix applicable findings.
6. Re-run and capture final results.
7. Distinguish intentional findings not fixed due to demonstration scope.

**Required report examples**

- unused or unsafe code;
- unsafe role/authorization logic;
- improper error handling;
- duplicated logic;
- overlarge component/function;
- insecure logging or secret exposure;
- missing validation.

**Evidence**

- tool setup/configuration;
- findings screenshots/output;
- before/after code snippets;
- final clean or documented remaining result.

**Acceptance**

- at least five substantive findings;
- findings are genuine;
- corrective actions match source changes;
- no invented SonarQube or ESLint findings.

## Task 25: Finalize unit and integration testing evidence

**When:** after implementation and code review fixes

**Objective:** prove test coverage and test quality for normal, boundary, invalid, and exceptional cases.

**Work**

1. Select backend and frontend test frameworks.
2. Add or finalize backend unit/integration tests for:
   - authentication and account state;
   - patient ID and staff ID;
   - RBAC and direct URL/API denial;
   - 24-hour appointment changes;
   - slot collision;
   - cancelled/call-reminder behavior;
   - ward restrictions and discharge;
   - Unpaid/Paid bill transitions;
   - immutable Paid bills;
   - pharmacy medicine bill creation;
   - prescription/report/pathology placeholders;
   - audit event creation;
   - soft-deactivated patient behavior.
3. Add frontend component/end-to-end tests if feasible and report accurately.
4. Generate coverage output.
5. Capture representative passing tests.

**Report test categories**

- normal/valid input;
- boundary conditions;
- invalid input;
- unauthorized role;
- concurrent/exceptional operations;
- empty states.

**Evidence**

- test source;
- test-run output;
- coverage report;
- selected test cases table;
- screenshots.

**Acceptance**

- tests are automated and reproducible;
- representative tests cover normal, boundary, invalid, and exceptional cases;
- assertions verify behavior rather than implementation constants;
- coverage claims match actual tools.

## Task 26: Capture Git and version-control evidence

**When:** throughout project and after final merge

**Objective:** document meaningful branches, commits, pull requests, history, and version tags.

**Work**

1. Ensure commits include meaningful implementation summaries.
2. Capture branch list and branch workflow.
3. Capture representative commits and pull requests.
4. Create a version tag for the final submission if acceptable to the team.
5. Capture clean repository status and release commit.
6. Export or screenshot commit history.
7. Explain the team workflow from actual Git usage.

**Evidence**

- repository branches;
- commit history;
- pull requests;
- version tags/releases;
- clean final state;
- README/setup instructions.

**Acceptance**

- evidence reflects actual GitHub history;
- no commit or branch is invented;
- final submission commit/tag is identifiable;
- secrets and environment files are not exposed.

## Task 27: Assemble and validate the final Google Classroom report

**When:** after all evidence and screenshots are complete

**Objective:** produce one cohesive team report PDF/DOCX covering all 12 submission sections.

**Work**

1. Create a title page and team/member table.
2. Include the SRS and SDS.
3. Include all 10 other submission sections in their required order.
4. Add a table of contents and consistent heading hierarchy.
5. Add figure numbering and captions.
6. Add live deployment URL and GitHub/Wiki links.
7. Cite or reference source files and tools used.
8. Remove speculative claims and broken screenshots.
9. Proofread names, roles, requirements, and diagrams.
10. Generate PDF/DOCX and inspect both.

**Report structure**

1. SRS
2. SDS
3. Trello/Discord evidence
4. architecture
5. coding standards
6. source documentation
7. UI design
8. Nielsen heuristics
9. code review
10. Git evidence
11. testing
12. team contributions

**Acceptance**

- all 12 sections are complete;
- diagrams, screenshots, and explanations are readable;
- PDF/DOCX formatting is consistent;
- repository and live deployment remain accessible;
- final report matches actual implementation.

## Task 28: Publish all 12 GitHub Wiki pages

**When:** after report content is stable

**Objective:** publish the 12 separate GitHub Wiki pages required by the submission.

**Work**

1. Create one Wiki page per submission section.
2. Use the exact 12 section titles.
3. Include concise but complete explanations.
4. Link to source files, deployment, screenshots, tests, diagrams, and report sections.
5. Cross-link pages where useful.
6. Verify navigation and image rendering.
7. Add a Wiki home page linking all pages.

**Acceptance**

- exactly 12 complete section pages plus optional home page;
- each page corresponds to the report section;
- no secret credentials or private environment values;
- links and embedded images work.

## Task 29: Produce demo video and final release package

**When:** immediately before submission

**Objective:** create a demonstration and package source/release deliverables.

**Work**

1. Record the live deployment walkthrough.
2. Demonstrate shared login and role routing.
3. Demonstrate patient registration and appointment booking.
4. Demonstrate Doctor/Assistant appointment actions.
5. Demonstrate Ward Nurse and Ward Doctor flows.
6. Demonstrate Accountant billing and Pharmacy bill creation.
7. Demonstrate Pathology and near-future placeholder objects.
8. Demonstrate IT account management and audit log.
9. Explain that placeholder features are intentionally not real clinical/payment implementations.
10. Package source, setup instructions, report, screenshots, diagrams, and test output.

**Acceptance**

- demo reflects the live deployment;
- no unsupported real clinical/payment claims;
- setup instructions reproduce the project;
- final GitHub source and report links are correct.