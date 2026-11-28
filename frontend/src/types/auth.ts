export type AccountRole =
  | "PATIENT"
  | "DOCTOR"
  | "WARD_DOCTOR"
  | "ASSISTANT"
  | "PATHOLOGIST"
  | "ACCOUNTANT"
  | "WARD_NURSE"
  | "PHARMACY_STAFF"
  | "IT_ADMIN";

export type Account = {
  id: string;
  login_id: string;
  role: AccountRole;
  state: string;
};

export type LoginInput = {
  login_id: string;
  password: string;
};

export type TokenResponse = {
  access_token: string;
  token_type: string;
  expires_in: number;
};
