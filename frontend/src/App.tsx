import { App as AntApp, ConfigProvider, theme } from "antd";
import { Route, Routes } from "react-router";
import { AuthProvider } from "./context/AuthContext";
import { ITRoute } from "./components/ITRoute";
import { RoleRoute } from "./components/RoleRoute";
import { ProtectedRoute } from "./components/ProtectedRoute";
import { AppLayout } from "./layouts/AppLayout";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import StaffPage from "./pages/StaffPage";
import DashboardPage from "./pages/DashboardPage";
import AppointmentsPage from "./pages/AppointmentsPage";
import WardsPage from "./pages/WardsPage";
import PrescriptionsPage from "./pages/PrescriptionsPage";
import ReportsPage from "./pages/ReportsPage";
import BillingPage from "./pages/BillingPage";
import PharmacyPage from "./pages/PharmacyPage";
import PathologyPage from "./pages/PathologyPage";
import AuditPage from "./pages/AuditPage";

function AppRoutes() {
  return (
    <Routes>
      <Route element={<AppLayout />}>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route element={<ProtectedRoute />}>
          <Route index element={<DashboardPage />} />
          <Route element={<RoleRoute allowed={["PATIENT", "DOCTOR", "WARD_DOCTOR", "ASSISTANT", "IT_ADMIN"]} />}>
            <Route path="/appointments" element={<AppointmentsPage />} />
          </Route>
          <Route element={<RoleRoute allowed={["WARD_NURSE", "IT_ADMIN"]} />}>
            <Route path="/wards" element={<WardsPage />} />
          </Route>
          <Route element={<RoleRoute allowed={["PATIENT", "DOCTOR", "WARD_DOCTOR", "WARD_NURSE", "PHARMACY_STAFF", "IT_ADMIN"]} />}>
            <Route path="/prescriptions" element={<PrescriptionsPage />} />
          </Route>
          <Route element={<RoleRoute allowed={["PATIENT", "DOCTOR", "WARD_NURSE", "WARD_DOCTOR", "IT_ADMIN"]} />}>
            <Route path="/reports" element={<ReportsPage />} />
          </Route>
          <Route element={<RoleRoute allowed={["PATIENT", "ACCOUNTANT", "PHARMACY_STAFF", "IT_ADMIN"]} />}>
            <Route path="/billing" element={<BillingPage />} />
          </Route>
          <Route element={<RoleRoute allowed={["PHARMACY_STAFF", "IT_ADMIN"]} />}>
            <Route path="/pharmacy" element={<PharmacyPage />} />
          </Route>
          <Route element={<RoleRoute allowed={["PATHOLOGIST", "ACCOUNTANT", "IT_ADMIN"]} />}>
            <Route path="/pathology" element={<PathologyPage />} />
          </Route>
          <Route element={<ITRoute />}>
            <Route path="/staff" element={<StaffPage />} />
            <Route path="/audit" element={<AuditPage />} />
          </Route>
        </Route>
      </Route>
    </Routes>
  );
}

export default function App() {
  return (
    <ConfigProvider theme={{ algorithm: theme.darkAlgorithm, token: { colorPrimary: "#475569", borderRadius: 8 } }}>
      <AntApp>
        <AuthProvider>
          <AppRoutes />
        </AuthProvider>
      </AntApp>
    </ConfigProvider>
  );
}
