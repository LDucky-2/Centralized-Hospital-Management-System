import { Card, Typography } from "antd";
import { useAuth } from "../context/AuthContext";

export default function DashboardPage() {
  const { account } = useAuth();
  return (
    <Card>
      <Typography.Title level={2}>{account?.role === "PATIENT" ? "Patient dashboard" : "Staff dashboard"}</Typography.Title>
      <Typography.Paragraph>Welcome to CHMS. The implementation continues through the feature modules.</Typography.Paragraph>
    </Card>
  );
}
