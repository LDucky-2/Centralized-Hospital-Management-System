import { Layout, Menu, Button } from "antd";
import { Link, Outlet, useNavigate } from "react-router";
import { useAuth } from "../context/AuthContext";
import type { AccountRole } from "../types/auth";
import type { ReactElement } from "react";

const menuForRole = (role: AccountRole) => {
  const base = [{ key: "dashboard", label: <Link to="/">Dashboard</Link> }];
  const menu: { key: string; label: ReactElement }[] = [...base];
  if (["PATIENT", "DOCTOR", "WARD_DOCTOR", "ASSISTANT", "IT_ADMIN"].includes(role)) {
    menu.push({ key: "appointments", label: <Link to="/appointments">Appointments</Link> });
  }
  if (["PATIENT", "DOCTOR", "WARD_DOCTOR", "WARD_NURSE", "PHARMACY_STAFF", "IT_ADMIN"].includes(role)) {
    menu.push({ key: "prescriptions", label: <Link to="/prescriptions">Prescriptions</Link> });
  }
  if (["PATIENT", "ACCOUNTANT", "PHARMACY_STAFF", "IT_ADMIN"].includes(role)) {
    menu.push({ key: "billing", label: <Link to="/billing">Billing</Link> });
  }
  if (["PATIENT", "DOCTOR", "WARD_NURSE", "WARD_DOCTOR", "IT_ADMIN"].includes(role)) {
    menu.push({ key: "reports", label: <Link to="/reports">Reports</Link> });
  }
  if (["WARD_NURSE", "IT_ADMIN"].includes(role)) {
    menu.push({ key: "wards", label: <Link to="/wards">Wards</Link> });
  }
  if (["PHARMACY_STAFF", "IT_ADMIN"].includes(role)) {
    menu.push({ key: "pharmacy", label: <Link to="/pharmacy">Pharmacy</Link> });
  }
  if (["PATHOLOGIST", "ACCOUNTANT", "IT_ADMIN"].includes(role)) {
    menu.push({ key: "pathology", label: <Link to="/pathology">Pathology</Link> });
  }
  if (role === "IT_ADMIN") {
    menu.push({ key: "staff", label: <Link to="/staff">Staff</Link> });
    menu.push({ key: "audit", label: <Link to="/audit">Audit</Link> });
  }
  return menu;
};

export function AppLayout() {
  const { account, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = async () => {
    await logout();
    navigate("/login");
  };

  const items = account
    ? menuForRole(account.role)
    : [
        { key: "login", label: <Link to="/login">Log in</Link> },
        { key: "register", label: <Link to="/register">Patient registration</Link> },
      ];

  return (
    <Layout style={{ minHeight: "100vh" }}>
      <Layout.Header style={{ display: "flex", alignItems: "center", background: "#20242a", borderBottom: "1px solid #343941" }}>
        <Link to="/" style={{ color: "#fff", fontWeight: 700, marginRight: 24 }}>CHMS</Link>
        <Menu mode="horizontal" theme="dark" items={items} style={{ flex: 1, background: "transparent" }} />
        {account && <Button onClick={handleLogout}>Log out</Button>}
      </Layout.Header>
      <Layout.Content style={{ maxWidth: 1100, width: "100%", margin: "0 auto", padding: 32 }}>
        <Outlet />
      </Layout.Content>
    </Layout>
  );
}
