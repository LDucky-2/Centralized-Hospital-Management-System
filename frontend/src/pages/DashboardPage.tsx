import { Card, Typography } from "antd";
import { useAuth } from "../context/AuthContext";

export default function DashboardPage() {
  const { account } = useAuth();
  const roleLabels: Record<string, string> = {
    PATIENT: "Patient",
    DOCTOR: "Doctor",
    WARD_DOCTOR: "Ward Doctor",
    ASSISTANT: "Assistant",
    PATHOLOGIST: "Pathologist",
    ACCOUNTANT: "Accountant",
    WARD_NURSE: "Ward Nurse",
    PHARMACY_STAFF: "Pharmacy Staff",
    IT_ADMIN: "IT Administrator",
  };
  return (
    <Card>
      <Typography.Title level={2}>{roleLabels[account?.role ?? ""] ?? "CHMS"} dashboard</Typography.Title>
      <Typography.Paragraph>Use the role-specific navigation above. Unauthorized modules are hidden and protected by server-side RBAC.</Typography.Paragraph>
    </Card>
  );
}
