import { Layout, Menu, Button } from "antd";
import { Link, Outlet, useNavigate } from "react-router";
import { useAuth } from "../context/AuthContext";

export function AppLayout() {
  const { account, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = async () => {
    await logout();
    navigate("/login");
  };

  const items = account
    ? [
        { key: "dashboard", label: <Link to="/">Dashboard</Link> },
        ...(account.role !== "IT_ADMIN" ? [
          { key: "appointments", label: <Link to="/appointments">Appointments</Link> },
          { key: "prescriptions", label: <Link to="/prescriptions">Prescriptions</Link> },
          { key: "billing", label: <Link to="/billing">Billing</Link> },
        ] : []),
        ...(["WARD_NURSE", "WARD_DOCTOR", "IT_ADMIN"].includes(account.role) ? [{ key: "wards", label: <Link to="/wards">Wards</Link> }] : []),
        ...(["DOCTOR", "WARD_DOCTOR", "PATIENT", "WARD_NURSE", "IT_ADMIN"].includes(account.role) ? [{ key: "reports", label: <Link to="/reports">Reports</Link> }] : []),
        ...(["PHARMACY_STAFF", "IT_ADMIN"].includes(account.role) ? [{ key: "pharmacy", label: <Link to="/pharmacy">Pharmacy</Link> }] : []),
        ...(["PATHOLOGIST", "ACCOUNTANT", "IT_ADMIN"].includes(account.role) ? [{ key: "pathology", label: <Link to="/pathology">Pathology</Link> }] : []),
        ...(account.role === "IT_ADMIN" ? [{ key: "staff", label: <Link to="/staff">Staff</Link> }] : []),
        ...(account.role === "IT_ADMIN" ? [{ key: "audit", label: <Link to="/audit">Audit</Link> }] : []),
      ]
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
