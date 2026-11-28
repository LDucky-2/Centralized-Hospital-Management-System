import type { Account, LoginInput, TokenResponse } from "../types/auth";

const AUTH = "/api/v1/auth";
const USERS = "/api/v1/users";
const PATIENTS = "/api/v1/patients";
const STAFF = "/api/v1/staff";
const AUDIT = "/api/v1/audit";
const APPOINTMENTS = "/api/v1/appointments";
const WARDS = "/api/v1/wards";
const PRESCRIPTIONS = "/api/v1/prescriptions";
const REPORTS = "/api/v1/reports";
const BILLING = "/api/v1/billing";
const PHARMACY = "/api/v1/pharmacy";
const PATHOLOGY = "/api/v1/pathology";

const TOKEN_KEY = "chms_access_token";
let accessToken: string | null = null;
let accessExpiresAt = 0;
let sessionExpiredHandler: (() => void) | null = null;

const readStoredToken = (): string | null => {
  try {
    const saved = JSON.parse(localStorage.getItem(TOKEN_KEY) ?? "null") as { token: string; expiresAt: number } | null;
    if (saved && typeof saved.token === "string" && saved.expiresAt > Date.now()) {
      accessExpiresAt = saved.expiresAt;
      return saved.token;
    }
  } catch {
    // Ignore unreadable storage.
  }
  localStorage.removeItem(TOKEN_KEY);
  accessExpiresAt = 0;
  return null;
};

const storeToken = (token: TokenResponse | null) => {
  accessToken = token?.access_token ?? null;
  accessExpiresAt = token ? Date.now() + token.expires_in * 1000 : 0;
  if (token) {
    localStorage.setItem(TOKEN_KEY, JSON.stringify({ token: token.access_token, expiresAt: accessExpiresAt }));
  } else {
    localStorage.removeItem(TOKEN_KEY);
  }
};

accessToken = readStoredToken();

const errorMessage = async (response: Response): Promise<string> => {
  try {
    const body = await response.json();
    if (typeof body.detail === "string") return body.detail;
  } catch {
    // Use the fallback status message.
  }
  return `Request failed (${response.status})`;
};

const send = (url: string, options: RequestInit = {}) =>
  fetch(url, {
    ...options,
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
      ...(accessToken ? { Authorization: `Bearer ${accessToken}` } : {}),
      ...options.headers,
    },
  });

let refreshing: Promise<boolean> | null = null;

const refreshAccessToken = (): Promise<boolean> => {
  refreshing ??= (async () => {
    try {
      const response = await send(`${AUTH}/refresh`, { method: "POST" });
      if (!response.ok) return false;
      storeToken(await response.json() as TokenResponse);
      return true;
    } catch {
      return false;
    } finally {
      refreshing = null;
    }
  })();
  return refreshing;
};

const sendWithRefresh = async (url: string, options: RequestInit = {}): Promise<Response> => {
  let response = await send(url, options);
  if (response.status === 401 && !url.startsWith(AUTH)) {
    if (await refreshAccessToken()) response = await send(url, options);
    else {
      storeToken(null);
      sessionExpiredHandler?.();
    }
  }
  if (!response.ok) throw new Error(await errorMessage(response));
  return response;
};

const request = async <T>(url: string, options: RequestInit = {}): Promise<T> => {
  const response = await sendWithRefresh(url, options);
  return response.status === 204 ? (undefined as T) : await response.json();
};

const post = <T>(url: string, data?: unknown) =>
  request<T>(url, { method: "POST", body: data === undefined ? undefined : JSON.stringify(data) });

const patch = <T>(url: string, data: unknown) =>
  request<T>(url, { method: "PATCH", body: JSON.stringify(data) });

export const apiService = {
  onSessionExpired: (handler: (() => void) | null) => {
    sessionExpiredHandler = handler;
  },
  login: async (data: LoginInput) => {
    storeToken(await post<TokenResponse>(`${AUTH}/login`, data));
  },
  logout: async () => {
    try {
      await post<void>(`${AUTH}/logout`);
    } finally {
      storeToken(null);
    }
  },
  restoreSession: async (): Promise<Account | null> => {
    if (accessToken) {
      try {
        return await request<Account>(`${USERS}/me`);
      } catch {
        return null;
      }
    }
    if (!(await refreshAccessToken())) return null;
    return request<Account>(`${USERS}/me`);
  },
  getMe: () => request<Account>(`${USERS}/me`),
  registerPatient: (data: unknown) => post<unknown>(`${PATIENTS}/register`, data),
  getStaff: () => request<unknown[]>(STAFF),
  createStaff: (data: unknown) => post<unknown>(STAFF, data),
  updateStaff: (id: string, data: unknown) => patch<unknown>(`${STAFF}/${id}`, data),
  getAudit: () => request<unknown[]>(AUDIT),
  getAppointments: (doctorId: string, date: string) =>
    request<unknown[]>(`${APPOINTMENTS}/doctor/${doctorId}?appointment_date=${date}`),
  getMyAppointments: () => request<unknown[]>(`${APPOINTMENTS}/my`),
  getDoctors: () => request<unknown[]>(`${APPOINTMENTS}/doctors`),
  getAssignedDoctor: () => request<{ id: string; login_id: string }>(`${APPOINTMENTS}/assigned-doctor`),
  getAvailableSlots: (doctorId: string, date: string) =>
    request<string[]>(`${APPOINTMENTS}/available/${doctorId}?appointment_date=${date}`),
  createAppointment: (data: unknown) => post<unknown>(APPOINTMENTS, data),
  cancelAppointment: (id: string, reason?: string) =>
    post<unknown>(`${APPOINTMENTS}/${id}/cancel${reason ? `?reason=${encodeURIComponent(reason)}` : ""}`),
  rescheduleAppointment: (id: string, date: string, startTime: string) =>
    post<unknown>(`${APPOINTMENTS}/${id}/reschedule?appointment_date=${date}&start_time=${startTime}`),
  updateAppointmentStatus: (id: string, status: string) =>
    patch<unknown>(`${APPOINTMENTS}/${id}/status`, { status }),
  blockSchedule: (doctorId: string, data: unknown) =>
    post<unknown>(`${APPOINTMENTS}/doctor/${doctorId}/block`, data),
  removeAppointment: (id: string) =>
    request<void>(`${APPOINTMENTS}/${id}`, { method: "DELETE" }),
  getWards: () => request<unknown[]>(WARDS),
  createWard: (name: string) => post<unknown>(WARDS, { name }),
  assignNurse: (nurseId: string, wardId: string) =>
    post<unknown>(`${WARDS}/nurses`, { nurse_id: nurseId, ward_id: wardId }),
  assignPatientWard: (patientId: string, wardId: string, bedRoom: string) =>
    post<unknown>(`${WARDS}/assignments`, { patient_id: patientId, ward_id: wardId, bed_room: bedRoom }),
  dischargePatient: (assignmentId: string, note?: string) =>
    post<unknown>(`${WARDS}/assignments/${assignmentId}/discharge`, { note }),
  getPrescriptions: () => request<unknown[]>(PRESCRIPTIONS),
  createPrescription: (patientId: string) => post<unknown>(PRESCRIPTIONS, { patient_id: patientId }),
  getMedicalReports: () => request<unknown[]>(`${REPORTS}/medical`),
  createMedicalReport: (patientId: string) => post<unknown>(`${REPORTS}/medical`, { patient_id: patientId }),
  createExternalReport: (patientId: string) => post<unknown>(
    `${REPORTS}/external`,
    patientId ? { patient_id: patientId } : {},
  ),
  getTestItems: () => request<unknown[]>(`${BILLING}/test-items`),
  getBills: () => request<unknown[]>(`${BILLING}/bills`),
  createBill: (patientId: string, lineItems: unknown[]) =>
    post<unknown>(`${BILLING}/bills`, { patient_id: patientId, line_items: lineItems }),
  editBill: (billId: string, lineItems: unknown[]) =>
    patch<unknown>(`${BILLING}/bills/${billId}`, { line_items: lineItems }),
  markBillPaid: (billId: string) => post<unknown>(`${BILLING}/bills/${billId}/pay`),
  getMedicineItems: () => request<unknown[]>(`${PHARMACY}/medicine-items`),
  createMedicineBill: (prescriptionId: string, selected: unknown[]) =>
    post<unknown>(`${PHARMACY}/prescriptions/${prescriptionId}/bill`, selected),
  getPathology: () => request<unknown[]>(PATHOLOGY),
  createPathology: (patientId: string, testName: string, billingStatus: string) =>
    post<unknown>(PATHOLOGY, { patient_id: patientId, test_name: testName, billing_status: billingStatus }),
};
